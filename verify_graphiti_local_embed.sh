#!/bin/bash

# This script checks if Graphiti is running and if search requests return a valid response (not a 429 or OpenAI error)

GRAPHITI_URL="http://localhost:9003/search"
AUTH_HEADER="Authorization: Bearer becb9982db2004657bf0403a8f0e5e9c09875c7c0c21897ef48153a7c1099eb0"
QUERY_PAYLOAD='{"query": "project"}'

set -e

echo "Checking if Graphiti search endpoint is up..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$GRAPHITI_URL" -H "Content-Type: application/json" -H "$AUTH_HEADER" -d "$QUERY_PAYLOAD")

if [ "$HTTP_CODE" != "200" ]; then
  echo "Graphiti search endpoint returned HTTP $HTTP_CODE."
  echo "Check Graphiti logs for errors: docker logs --tail 80 graphiti"
  exit 1
fi

RESPONSE=$(curl -s -X POST "$GRAPHITI_URL" -H "Content-Type: application/json" -H "$AUTH_HEADER" -d "$QUERY_PAYLOAD")

if echo "$RESPONSE" | grep -q 'openai'; then
  echo "❌ Detected OpenAI error in response. Patch may not be applied."
  exit 2
fi

if echo "$RESPONSE" | grep -q '429' || echo "$RESPONSE" | grep -q 'quota'; then
  echo "❌ Detected rate limit or quota error. Patch may not be applied."
  exit 3
fi

echo "✅ Graphiti is running and search endpoint is responding!"
echo "Response: $RESPONSE"
