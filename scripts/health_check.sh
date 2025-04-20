#!/usr/bin/env bash
# health_check.sh: Simple smoke tests for all services
set -euo pipefail
IFS=$'\n\t'

# Define endpoint names and URLs
names=("AnythingLLM UI" "Graphiti Docs" "Qdrant Collections")
urls=("http://localhost:9002" "http://localhost:9003/docs" "http://localhost:9004/collections")

# Run checks
echo "[INFO] Running health checks..."
for (( i=0; i<${#names[@]}; i++ )); do
  name="${names[$i]}"
  url="${urls[$i]}"
  echo "[INFO] Checking $name at $url"
  if ! curl -sf "$url"; then
    echo "[ERROR] $name unreachable at $url"
    exit 1
  fi
  echo "[INFO] $name is up"
done

echo "[INFO] All services are healthy"
