#!/bin/bash
# Script to check for required containers/services and (re)build or start them if missing.
# Intended for onboarding and as a workflow pre-step.

set -e
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DOCKER_COMPOSE_FILE="$PROJECT_ROOT/docker/docker-compose.yml"

# List of required services (update as needed)
REQUIRED_SERVICES=("whispercpp-arm64" "clip-arm64" "embedding-proxy")

# Check if docker-compose file exists
if [ ! -f "$DOCKER_COMPOSE_FILE" ]; then
  echo "[ERROR] docker-compose.yml not found at $DOCKER_COMPOSE_FILE. Please ensure it exists."
  exit 1
fi

cd "$PROJECT_ROOT/docker"

echo "[INFO] Checking status of required containers..."
MISSING_SERVICES=()
for svc in "${REQUIRED_SERVICES[@]}"; do
  if ! docker compose ps --services --filter "status=running" | grep -q "^$svc$"; then
    MISSING_SERVICES+=("$svc")
  fi
done

if [ ${#MISSING_SERVICES[@]} -eq 0 ]; then
  echo "[INFO] All required containers are running."
  exit 0
fi

echo "[INFO] The following services are missing or not running: ${MISSING_SERVICES[*]}"
echo "[INFO] (Re)building and starting missing containers..."
docker compose up -d ${MISSING_SERVICES[*]}

echo "[INFO] Container check and (re)build complete."
