#!/usr/bin/env bash
set -euo pipefail # Exit on error, unset variable, or pipe failure
IFS=$'\n\t'      # Safer looping and splitting

# --- Configuration ---
ENV_FILE=".env"
TEMPLATE_FILE=".env.template"

# --- Helper Functions ---
log() {
  echo "[INFO] $@"
}

warn() {
  echo "[WARN] $@" >&2
}

error() {
  echo "[ERROR] $@" >&2
  exit 1
}

# Function to generate a secure random hex string (32 bytes = 64 hex chars)
generate_key() {
  openssl rand -hex 32
}

# --- Main Script ---

# 1. Check for Docker and Docker Compose
log "Checking prerequisites..."
# Ensure Docker CLI & Compose plugin are available
if ! command -v docker &>/dev/null; then
  error "'docker' command not found. Please install Docker Desktop."
fi
# Verify Docker Compose plugin
if ! docker compose version &>/dev/null; then
  error "Docker Compose plugin not found. Please install or enable 'docker-compose' CLI plugin."
fi
# After confirming Docker, clear any custom endpoints so CLI uses default context
unset DOCKER_HOST DOCKER_TLS_VERIFY DOCKER_CERT_PATH
log "Cleared DOCKER_* env vars to use default Docker context"

# Removed DOCKER_HOST override to rely on Docker context and CLI plugin

# On macOS, auto-launch Docker Desktop if not running
if [[ "$(uname)" == Darwin* ]]; then
  log "Launching Docker Desktop on macOS..."
  open -a Docker || warn "Failed to open Docker Desktop. Please start it manually."
fi

# Wait for Docker daemon to be ready
log "Waiting for Docker daemon to be ready..."
until docker info >/dev/null 2>&1; do
  sleep 2
done
log "Docker daemon is ready."

# 2. Create .env from template if it doesn't exist
if [ ! -f "$ENV_FILE" ]; then
  log "File '$ENV_FILE' not found. Generating from '$TEMPLATE_FILE'..."
  if [ ! -f "$TEMPLATE_FILE" ]; then
    error "Template file '$TEMPLATE_FILE' not found. Cannot generate '$ENV_FILE'."
  fi

  # Generate the required API keys
  GENERATED_ANYTHINGLLM_KEY=$(generate_key)
  GENERATED_GRAPHITI_KEY=$(generate_key)
  GENERATED_NEO4J_PASSWORD=$(generate_key) # Generate Neo4j password

  # Copy template and replace placeholders
  cp "$TEMPLATE_FILE" "$ENV_FILE"
  # Use sed -i for in-place editing. The '' argument handles macOS compatibility.
  sed -i'' -e "s|{{ANYTHINGLLM_INITIAL_ADMIN_KEY_PLACEHOLDER}}|$GENERATED_ANYTHINGLLM_KEY|g" "$ENV_FILE"
  sed -i'' -e "s|{{GRAPHITI_API_KEY_PLACEHOLDER}}|$GENERATED_GRAPHITI_KEY|g" "$ENV_FILE"
  sed -i'' -e "s|{{NEO4J_PASSWORD_PLACEHOLDER}}|$GENERATED_NEO4J_PASSWORD|g" "$ENV_FILE" # Replace Neo4j password placeholder

  # Prompt for OpenAI API Key if using the default
  if grep -q '^OPENAI_API_KEY="unused"' "$ENV_FILE"; then
    echo ""
    read -p "Graphiti requires an OpenAI API key for validation. Do you want to provide one now? (y/N): " -r provide_openai_key
    if [[ "$provide_openai_key" =~ ^[Yy]$ ]]; then
      read -sp "Enter your OpenAI API Key: " user_openai_key
      echo "" # Newline after secret input
      if [ -n "$user_openai_key" ]; then
        # Use a different delimiter for sed in case the key contains slashes
        sed -i'' -e "s|^OPENAI_API_KEY=\"unused\"|OPENAI_API_KEY=\"$user_openai_key\"|" "$ENV_FILE"
        log "OPENAI_API_KEY updated in 	$ENV_FILE."
      else
        warn "No key entered. Keeping default 'unused'. You may need to edit 	$ENV_FILE manually later if OpenAI features are needed."
      fi
    else
      warn "Keeping default OPENAI_API_KEY=\"unused\". You may need to edit 	$ENV_FILE manually later if OpenAI features are needed."
    fi
  fi

  log "Successfully generated '$ENV_FILE' with new API keys and Neo4j password."
  warn "IMPORTANT: Review the generated '$ENV_FILE'."
  warn "  - If using AnythingLLM authentication (AUTH_MODE=true), use the generated ANYTHINGLLM_INITIAL_ADMIN_KEY for your first login."
  warn "  - If using OpenAI features via Graphiti, replace the default OPENAI_API_KEY=\"unused\" with your actual key."
else
  log "Existing '$ENV_FILE' found. Using it."
fi

# --- 2b. Ensure Neo4j password is set ---
if ! grep -q '^NEO4J_PASSWORD=' "$ENV_FILE"; then
  log "Missing NEO4J_PASSWORD in '$ENV_FILE'. Generating Neo4j password..."
  GENERATED_NEO4J_PASSWORD=$(generate_key)
  echo "NEO4J_PASSWORD=$GENERATED_NEO4J_PASSWORD" >> "$ENV_FILE"
  warn "Added generated NEO4J_PASSWORD to '$ENV_FILE'."
fi

# 3. Load environment variables from .env file
# Ensures docker-compose uses the values from the .env file
log "Loading environment variables from '$ENV_FILE'..."
set -o allexport # Export all variables defined from now on
# shellcheck source=.env
source "$ENV_FILE"
set +o allexport # Stop exporting variables

# 3b. Validate required environment variables
log "Validating required environment variables..."
required_vars=("GRAPHITI_API_KEY" "NEO4J_PASSWORD" "OPENAI_API_KEY") # Added OPENAI_API_KEY
missing_vars=()
for var in "${required_vars[@]}"; do
  # Check if the variable is unset or empty
  if [ -z "${!var+x}" ] || [ -z "${!var}" ]; then
    missing_vars+=("$var")
  fi
done

if [ ${#missing_vars[@]} -ne 0 ]; then
  error "The following required environment variables are missing or empty in 	$ENV_FILE:	 ${missing_vars[*]}
  Please set them manually."
fi
log "Required environment variables are set."

# 4. Start services using Docker Compose
log "Starting services via docker-compose..."

# Stop existing services
log "Stopping any existing services..."
docker compose -f docker/docker-compose.yml down --remove-orphans

# Launch fresh services
log "Launching fresh services..."
docker compose -f docker/docker-compose.yml up -d --remove-orphans

log "Services are starting up in the background."
echo ""
log "Access services:"
log "  AnythingLLM UI: http://localhost:9002"
log "  Graphiti API:   http://localhost:9003 (Requires API Key: ${GRAPHITI_API_KEY})"
log "  Qdrant API:     http://localhost:9004"
echo ""
log "Setup complete!"

# --- Python venv for ingestion scripts ---
if [ -f "requirements.txt" ]; then
  if [ ! -d ".venv" ]; then
    log "Setting up Python virtual environment .venv..."
    python3 -m venv .venv
  fi
  log "Activating virtual environment..."
  # shellcheck disable=SC1091
  . .venv/bin/activate
  log "Installing Python dependencies..."
  pip install --upgrade pip
  pip install -r requirements.txt
  PYTHON_CMD=".venv/bin/python"
else
  PYTHON_CMD="python3"
fi

# --- Obsidian ingestion (auto-run if vault exists) ---
if [ -n "${OBSIDIAN_VAULT_PATH:-}" ] && [ -d "${OBSIDIAN_VAULT_PATH}" ] && [ -f "scripts/ingest_obsidian.py" ]; then
  if [ -z "${OPENAI_API_KEY}" ] || [ "${OPENAI_API_KEY}" = "unused" ]; then
    warn "OPENAI_API_KEY is unset or default; skipping ingestion pipeline."
  else
    log "Running Obsidian ingestion pipeline..."
    "$PYTHON_CMD" scripts/ingest_obsidian.py
    log "Obsidian ingestion complete."
  fi
fi

exit 0
