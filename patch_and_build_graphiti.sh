#!/bin/bash

set -e

# Paths (update if you move files)
PATCH_SRC="/Users/grig/semantic-vault/graphiti_embedder_patch.py"
DOCKERFILE_SRC="/Users/grig/semantic-vault/Dockerfile.graphiti-local"
GRAPHITI_REPO_ROOT="$(pwd)"
EMBEDDER_TARGET="$GRAPHITI_REPO_ROOT/graphiti_core/embedder/openai.py"
DOCKERFILE_TARGET="$GRAPHITI_REPO_ROOT/Dockerfile.graphiti-local"

if [ ! -f "$PATCH_SRC" ]; then
  echo "Patch file not found: $PATCH_SRC" >&2
  exit 1
fi
if [ ! -f "$DOCKERFILE_SRC" ]; then
  echo "Dockerfile not found: $DOCKERFILE_SRC" >&2
  exit 1
fi
if [ ! -d "$GRAPHITI_REPO_ROOT/graphiti_core/embedder" ]; then
  echo "Run this script from the root of your Graphiti repo!" >&2
  exit 1
fi

echo "Copying patched embedder..."
cp "$PATCH_SRC" "$EMBEDDER_TARGET"

echo "Copying Dockerfile..."
cp "$DOCKERFILE_SRC" "$DOCKERFILE_TARGET"

echo "Building custom Graphiti Docker image..."
docker build -f Dockerfile.graphiti-local -t graphiti-local-embed:latest .

echo "If you haven't already, update your docker-compose.yml to use:\n  image: graphiti-local-embed:latest\n"
echo "Restarting Graphiti service..."
docker compose restart graphiti

echo "Done! Graphiti should now use your local embedding server."
