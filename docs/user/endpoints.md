# API Endpoints

This document lists all available API endpoints in the system, with descriptions and sample requests/responses.

---

## Model Management

### List All Models
- **Endpoint:** `GET /v1/model_catalog`
- **Description:** Returns a paginated list of all available models (local and Hugging Face).
- **Sample Request:**
  ```bash
  curl http://localhost:9083/v1/model_catalog
  ```
- **Sample Response:**
  ```json
  {
    "models": [
      {"name": "TheBloke/phi-2-GGUF", "type": "llm", "installed": false, ...},
      ...
    ],
    "page": 1,
    "total": 20
  }
  ```

### Switch Active Model
- **Endpoint:** `POST /v1/model_catalog/switch`
- **Description:** Switches the active model for a given type (llm or embedding).
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/v1/model_catalog/switch \
    -H 'Content-Type: application/json' \
    -d '{"name": "TheBloke/phi-2-GGUF", "type": "llm"}'
  ```
- **Sample Response:**
  ```json
  {"message": "Active llm model set to TheBloke/phi-2-GGUF", "active_models": {"llm": "TheBloke/phi-2-GGUF"}}
  ```

### Model Management Web UI
- **Endpoint:** `GET /v1/model_management_ui`
- **Description:** Returns an HTML web UI for managing models.

---

## LLM Provider

### Get Current LLM Provider
- **Endpoint:** `GET /v1/llm/provider`
- **Description:** Returns the current LLM provider (e.g., openai, ollama, anthropic).
- **Sample Response:**
  ```json
  {"provider": "openai"}
  ```

### Switch LLM Provider
- **Endpoint:** `POST /v1/llm/switch`
- **Description:** Switches the LLM provider.
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/v1/llm/switch \
    -H 'Content-Type: application/json' \
    -d '{"provider": "ollama"}'
  ```
- **Sample Response:**
  ```json
  {"message": "Switched LLM provider to ollama", "provider": "ollama"}
  ```

---

## LLM Completion

### LLM Completion
- **Endpoint:** `POST /v1/llm/complete`
- **Description:** Generate a completion from the active LLM.
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/v1/llm/complete \
    -H 'Content-Type: application/json' \
    -d '{"query": "What is the capital of France?"}'
  ```
- **Sample Response:**
  ```json
  {"response": "Paris."}
  ```

---

## Embedding

### Test Embedding
- **Endpoint:** `POST /v1/embedding/test`
- **Description:** Generate an embedding for a given query.
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/v1/embedding/test \
    -H 'Content-Type: application/json' \
    -d '{"query": "Hello world"}'
  ```
- **Sample Response:**
  ```json
  {"embedding": [0.1, 0.2, 0.3], "query": "Hello world"}
  ```

---

## Ingestion

### Add Messages
- **Endpoint:** `POST /messages`
- **Description:** Ingest one or more messages for semantic processing.
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/messages \
    -H 'Content-Type: application/json' \
    -d '{"messages": [{"content": "Sample message", "role_type": "user"}], "group_id": "default"}'
  ```
- **Sample Response:**
  ```json
  {"message": "Messages added to processing queue", "success": true}
  ```

### Clear Graph
- **Endpoint:** `POST /clear`
- **Description:** Clears all data from the graph.

---

## Analytics

### Get Metrics
- **Endpoint:** `GET /v1/analytics/metrics`
- **Description:** Returns current system/API metrics.

### Get Metrics History
- **Endpoint:** `GET /v1/analytics/metrics/history`
- **Description:** Returns historical metrics for a given key.
- **Sample Request:**
  ```bash
  curl 'http://localhost:9083/v1/analytics/metrics/history?key=llm.requests&since_seconds=3600'
  ```

### Get Entity Network
- **Endpoint:** `GET /v1/analytics/entity_network`
- **Description:** Returns a demo entity network graph for visualization.

---

## Notifications

### Send Notification
- **Endpoint:** `POST /v1/notify`
- **Description:** Sends a notification.

### Mark Notification as Read
- **Endpoint:** `POST /v1/notifications/read`

### Mark All Notifications as Read
- **Endpoint:** `POST /v1/notifications/mark_all_read`

### Get/Set Notification Preferences
- **Endpoints:**
  - `GET /v1/notifications/prefs`
  - `POST /v1/notifications/prefs`

---

## Markdown Q&A

### Ingest Obsidian Vault
- **Endpoint:** `POST /v1/ingest/obsidian`
- **Description:** Ingests markdown notes from an Obsidian vault.

### Q&A Over Markdown
- **Endpoint:** `POST /v1/qa/markdown`
- **Description:** Ask questions about ingested markdown content.

---

## Task Routing

### Route Task
- **Endpoint:** `POST /v1/task/route`
- **Description:** Routes a task to the correct model/service based on type (embedding/llm).
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/v1/task/route \
    -H 'Content-Type: application/json' \
    -d '{"task_type": "llm", "query": "Hello"}'
  ```

---

## Retrieval

### Search
- **Endpoint:** `POST /search`
- **Description:** Semantic search over ingested data.

### Get Episodes
- **Endpoint:** `GET /episodes/{group_id}`

### Get Entity Edge
- **Endpoint:** `GET /entity-edge/{uuid}`

### Delete Entity Edge
- **Endpoint:** `DELETE /entity-edge/{uuid}`

### Delete Episode
- **Endpoint:** `DELETE /episode/{uuid}`

### Delete Group
- **Endpoint:** `DELETE /group/{group_id}`

---

## Miscellaneous

### Dashboard Root
- **Endpoint:** `GET /`
- **Description:** Returns the model management dashboard UI.

---

# Notes
- All endpoints are available on the port configured for your backend (default: 9083).
- For endpoints requiring authentication or special headers, see the OpenAPI docs at `/docs`.
- This document is a living reference and should be updated as new endpoints are added.
