# API Endpoints

---

> **API Documentation Maintenance Checklist**
>
> - Update this document first when adding new endpoints; set status to `missing` until implemented.
> - When implementing or changing endpoints, update status and details immediately.
> - Regularly review for accuracy, especially before releases.
> - Ensure all endpoints (implemented or planned) are listed here with status and description.
> - Add sample requests, responses, and error responses for every endpoint.
> - Reference relevant test cases/scripts where possible.
> - Mark deprecated endpoints and provide migration guidance if needed.
> - Group endpoints logically and use consistent naming/versioning.
> - Document authentication/authorization requirements.
> - Keep code and documentation in sync through code reviews and CI checks.

---


This document lists all available API endpoints in the system, with descriptions and sample requests/responses.

---

**Status Legend:**
- `working`: Implemented and confirmed functional
- `broken`: Implemented but not working as intended
- `untested`: Implemented but not yet tested
- `missing`: Not implemented in the codebase at all; only implied or desired
- `deprecated`: Implemented but no longer intended for use (if applicable)

---

---

## Model Management

### List All Models
- **Endpoint:** `GET /v1/model_catalog`
- **Description:** Returns a paginated list of all available models (local and Hugging Face).
- **Status:** working
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
- **Sample Error Response:**
  ```json
  {"detail": "Internal Server Error: <error details>"}
  ```

### Switch Active Model
- **Endpoint:** `POST /v1/model_catalog/switch`
- **Description:** Switches the active model for a given type (llm or embedding).
- **Status:** untested
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/v1/model_catalog/switch \
    -H 'Content-Type: application/json' \
    -d '{"name": "all-MiniLM-L6-v2", "type": "embedding"}'
  ```
- **Sample Response:**
  ```json
  {"message": "Switched active model to all-MiniLM-L6-v2", "type": "embedding"}
  ```
- **Sample Error Response:**
  ```json
  {"detail": "Model not installed"}  // 404
  {"detail": "Missing required parameter: name"}  // 400
  {"detail": "Internal Server Error: <error details>"}  // 500
  ```

---

### List Loaded Models
- **Endpoint:** `GET /v1/models`
- **Description:** Lists all currently loaded models (embedding proxy).
- **Status:** working
- **Sample Response:**
  ```json
  {"models": ["all-MiniLM-L6-v2", "other-model"]}
  ```
- **Sample Error Response:**
  ```json
  {"detail": "Internal Server Error: <error details>"}
  ```

---

### Install Model (Embedding Proxy)
- **Endpoint:** `POST /v1/install_model`
- **Description:** Installs a new model via the embedding proxy.
- **Status:** working
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/v1/install_model \
    -H 'Content-Type: application/json' \
    -d '{"name": "all-MiniLM-L6-v2"}'
  ```
- **Sample Response:**
  ```json
  {"message": "Model installed", "name": "all-MiniLM-L6-v2"}
  ```
- **Sample Error Response:**
  ```json
  {"detail": "Invalid model name"}  // 400
  {"detail": "Internal Server Error: <error details>"}  // 500
  ```

---

### Add Entity Node
- **Endpoint:** `POST /entity-node`
- **Description:** Adds a new entity node to the graph.
- **Status:** working
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/entity-node \
    -H 'Content-Type: application/json' \
    -d '{"name": "Entity Name", "type": "concept"}'
  ```
- **Sample Response:**
  ```json
  {"uuid": "1234-uuid", "name": "Entity Name", "type": "concept"}
  ```
- **Sample Error Response:**
  ```json
  {"detail": "Missing required parameter: name"}  // 400
  {"detail": "Internal Server Error: <error details>"}  // 500
  ```

---

### Add Episode
- **Endpoint:** `POST /episode`
- **Description:** Adds a new episode to the graph.
- **Status:** working
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/episode \
    -H 'Content-Type: application/json' \
    -d '{"title": "Episode Title", "description": "Details here"}'
  ```
- **Sample Response:**
  ```json
  {"uuid": "5678-uuid", "title": "Episode Title"}
  ```
- **Sample Error Response:**
  ```json
  {"detail": "Missing required parameter: title"}  // 400
  {"detail": "Internal Server Error: <error details>"}  // 500
  ```

---

### Test Embedding (OpenAI Compatible)
- **Endpoint:** `POST /v1/embeddings`
- **Description:** OpenAI-compatible endpoint for generating embeddings.
- **Status:** working
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/v1/embeddings \
    -H 'Content-Type: application/json' \
    -d '{"input": "Hello world"}'
  ```
- **Sample Response:**
  ```json
  {"data": [{"embedding": [0.1, 0.2, 0.3], "index": 0}], "object": "list"}
  ```
- **Sample Error Response:**
  ```json
  {"detail": "Invalid input"}  // 400
  {"detail": "Internal Server Error: <error details>"}  // 500
  ```

---

### Ingest Markdown Chunks
- **Endpoint:** `POST /v1/qa/markdown/ingest_chunks`
- **Description:** Ingests markdown chunks for semantic processing.
- **Status:** working
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/v1/qa/markdown/ingest_chunks \
    -H 'Content-Type: application/json' \
    -d '{"chunks": ["chunk1", "chunk2"]}'
  ```
- **Sample Response:**
  ```json
  {"message": "Chunks ingested", "count": 2}
  ```
- **Sample Error Response:**
  ```json
  {"detail": "Missing required parameter: chunks"}  // 400
  {"detail": "Internal Server Error: <error details>"}  // 500
  ```

---

### Task Routing
- **Endpoint:** `POST /v1/task/route`
- **Description:** Routes a task to the appropriate model or service.
- **Status:** working
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/v1/task/route \
    -H 'Content-Type: application/json' \
    -d '{"task": "summarize", "input": "Text here"}'
  ```
- **Sample Response:**
  ```json
  {"result": "Summary here"}
  ```
- **Sample Error Response:**
  ```json
  {"detail": "Missing required parameter: task"}  // 400
  {"detail": "Internal Server Error: <error details>"}  // 500
  ```

---

### Set Notification Preferences
- **Endpoint:** `POST /v1/notifications/prefs`
- **Description:** Sets user notification preferences.
- **Status:** working
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/v1/notifications/prefs \
    -H 'Content-Type: application/json' \
    -d '{"email": true, "sms": false}'
  ```
- **Sample Response:**
  ```json
  {"message": "Preferences updated", "prefs": {"email": true, "sms": false}}
  ```
- **Sample Error Response:**
  ```json
  {"detail": "Invalid preference format"}  // 400
  {"detail": "Internal Server Error: <error details>"}  // 500
  ```


### Model Management Web UI
- **Endpoint:** `GET /v1/model_management_ui`
- **Description:** Returns an HTML web UI for managing models.
- **Status:** working
- **Sample Request:**
  ```bash
  curl http://localhost:9083/v1/model_management_ui
  ```
- **Sample Response:**
  ```html
  <!DOCTYPE html>
  <html>...</html>
  ```
- **Sample Error Response:**
  ```html
  Internal Server Error: <error details>
  ```

---

## LLM Provider

### Get Current LLM Provider
- **Endpoint:** `GET /v1/llm/provider`
- **Description:** Returns the current LLM provider (e.g., openai, ollama, anthropic).
- **Status:** working
- **Sample Response:**
  ```json
  {"provider": "openai"}
  ```
- **Sample Error Response:**
  ```json
  {"detail": "Internal Server Error: <error details>"}
  ```

### Switch LLM Provider
- **Endpoint:** `POST /v1/llm/switch`
- **Description:** Switches the LLM provider.
- **Status:** working
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
- **Sample Error Responses:**
  ```json
  {"detail": "Missing required parameter: provider"}  // 400
  {"detail": "Internal Server Error: <error details>"}  // 500
  ```

---

## LLM Completion

### LLM Completion
- **Endpoint:** `POST /v1/llm/complete`
- **Description:** Generate a completion from the active LLM.
- **Status:** broken
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
- **Status:** working
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
- **Status:** broken
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
- **Status:** broken

---

## Analytics

### Get Metrics
- **Endpoint:** `GET /v1/analytics/metrics`
- **Description:** Returns current system/API metrics.
- **Status:** working

### Get Metrics History
- **Endpoint:** `GET /v1/analytics/metrics/history`
- **Description:** Returns historical metrics for a given key.
- **Status:** working
- **Sample Request:**
  ```bash
  curl 'http://localhost:9083/v1/analytics/metrics/history?key=llm.requests&since_seconds=3600'
  ```

### Get Entity Network
- **Endpoint:** `GET /v1/analytics/entity_network`
- **Description:** Returns a demo entity network graph for visualization.
- **Status:** working

---

## Notifications

### Send Notification
- **Endpoint:** `POST /v1/notify`
- **Description:** Sends a notification.
- **Status:** working

### Mark Notification as Read
- **Endpoint:** `POST /v1/notifications/read`
- **Status:** broken

### Mark All Notifications as Read
- **Endpoint:** `POST /v1/notifications/mark_all_read`
- **Status:** working

### Get/Set Notification Preferences
- **Endpoints:**
  - `GET /v1/notifications/prefs`
  - `POST /v1/notifications/prefs`
- **Status:** broken

---

## Markdown Q&A

### Ingest Obsidian Vault
- **Endpoint:** `POST /v1/ingest/obsidian`
- **Description:** Ingests markdown notes from an Obsidian vault.
- **Status:** working

### Q&A Over Markdown
- **Endpoint:** `POST /v1/qa/markdown`
- **Description:** Ask questions about ingested markdown content.
- **Status:** working

---

## Task Routing

### Route Task
- **Endpoint:** `POST /v1/task/route`
- **Description:** Routes a task to the correct model/service based on type (embedding/llm).
- **Status:** broken
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
- **Status:** untested
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/search \
    -H 'Content-Type: application/json' \
    -d '{"group_ids": ["default"], "query": "example", "max_facts": 5}'
  ```

### Get Episodes
- **Endpoint:** `GET /episodes/{group_id}`
- **Description:** Get episodes for a group.
- **Status:** untested
- **Sample Request:**
  ```bash
  curl http://localhost:9083/episodes/default?last_n=10
  ```
- **Sample Response:**
  ```json
  [
    {"uuid": "ep-001", "name": "Kickoff", "summary": "Initial meeting"},
    {"uuid": "ep-002", "name": "Sprint Planning", "summary": "Planning next sprint"}
  ]
  ```

### Add Episode
- **Endpoint:** `POST /episode`
- **Description:** Add a new episode.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/episode \
    -H 'Content-Type: application/json' \
    -d '{"uuid": "ep-001", "group_id": "default", "name": "Kickoff", "summary": "Initial meeting"}'
  ```
- **Sample Response:**
  ```json
  {"uuid": "ep-001", "group_id": "default", "name": "Kickoff", "summary": "Initial meeting"}
  ```

### Get Episode
- **Endpoint:** `GET /episode/{uuid}`
- **Description:** Retrieve an episode by UUID.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl http://localhost:9083/episode/ep-001
  ```
- **Sample Response:**
  ```json
  {"uuid": "ep-001", "group_id": "default", "name": "Kickoff", "summary": "Initial meeting"}
  ```

### Update Episode
- **Endpoint:** `PUT /episode/{uuid}`
- **Description:** Update an episode by UUID.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl -X PUT http://localhost:9083/episode/ep-001 \
    -H 'Content-Type: application/json' \
    -d '{"name": "Kickoff Updated", "summary": "Initial meeting updated"}'
  ```
- **Sample Response:**
  ```json
  {"uuid": "ep-001", "group_id": "default", "name": "Kickoff Updated", "summary": "Initial meeting updated"}
  ```

### Get Entity Edge
- **Endpoint:** `GET /entity-edge/{uuid}`
- **Description:** Retrieve an entity edge by UUID.
- **Status:** untested
- **Sample Request:**
  ```bash
  curl http://localhost:9083/entity-edge/1234-uuid
  ```
- **Sample Response:**
  ```json
  {"edge_id": "edge-999", "source_uuid": "1234-uuid", "target_uuid": "5678-uuid", "type": "related"}
  ```

### Add Entity Edge
- **Endpoint:** `POST /entity-edge`
- **Description:** Add a new entity edge.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/entity-edge \
    -H 'Content-Type: application/json' \
    -d '{"source_uuid": "1234-uuid", "target_uuid": "5678-uuid", "type": "related"}'
  ```
- **Sample Response:**
  ```json
  {"edge_id": "edge-999", "source_uuid": "1234-uuid", "target_uuid": "5678-uuid", "type": "related"}
  ```

### Update Entity Edge
- **Endpoint:** `PUT /entity-edge/{uuid}`
- **Description:** Update an entity edge by UUID.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl -X PUT http://localhost:9083/entity-edge/edge-999 \
    -H 'Content-Type: application/json' \
    -d '{"type": "updated-type"}'
  ```
- **Sample Response:**
  ```json
  {"edge_id": "edge-999", "type": "updated-type"}
  ```

### Delete Entity Edge
- **Endpoint:** `DELETE /entity-edge/{uuid}`
- **Description:** Delete an entity edge by UUID.
- **Status:** untested
- **Sample Request:**
  ```bash
  curl -X DELETE http://localhost:9083/entity-edge/1234-uuid
  ```
- **Sample Response:**
  ```json
  {"message": "Entity edge deleted", "edge_id": "edge-999"}
  ```

### Delete Episode
- **Endpoint:** `DELETE /episode/{uuid}`
- **Description:** Delete an episode by UUID.
- **Status:** untested
- **Sample Request:**
  ```bash
  curl -X DELETE http://localhost:9083/episode/1234-uuid
  ```
- **Sample Response:**
  ```json
  {"message": "Episode deleted", "uuid": "1234-uuid"}
  ```

### Delete Group
- **Endpoint:** `DELETE /group/{group_id}`
- **Description:** Delete a group by group_id.
- **Status:** untested
- **Sample Request:**
  ```bash
  curl -X DELETE http://localhost:9083/group/default
  ```

### Add Group
- **Endpoint:** `POST /group`
- **Description:** Add a new group.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/group \
    -H 'Content-Type: application/json' \
    -d '{"group_id": "engineering", "description": "Engineering team"}'
  ```
- **Sample Response:**
  ```json
  {"group_id": "engineering", "description": "Engineering team"}
  ```

### Get Group
- **Endpoint:** `GET /group/{group_id}`
- **Description:** Retrieve a group by group_id.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl http://localhost:9083/group/engineering
  ```
- **Sample Response:**
  ```json
  {"group_id": "engineering", "description": "Engineering team"}
  ```

### Update Group
- **Endpoint:** `PUT /group/{group_id}`
- **Description:** Update a group by group_id.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl -X PUT http://localhost:9083/group/engineering \
    -H 'Content-Type: application/json' \
    -d '{"description": "Updated description"}'
  ```
- **Sample Response:**
  ```json
  {"group_id": "engineering", "description": "Updated description"}
  ```

---

## Advanced Search

- **Endpoint:** `GET /search/filters`
- **Description:** Retrieve available search filters and formats.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl http://localhost:9083/search/filters
  ```
- **Sample Response:**
  ```json
  {
    "filters": {
      "created_after": "date",
      "group_ids": ["engineering", "marketing"],
      "max_facts": "integer"
    }
  }
  ```

## Integrations

- **Endpoint:** `POST /integrations/{tool}/sync`
- **Description:** Trigger sync/import from an external tool.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/integrations/obsidian/sync \
    -H 'Content-Type: application/json' \
    -d '{"vault_path": "/Users/me/ObsidianVault"}'
  ```
- **Sample Response:**
  ```json
  {"status": "sync_started", "tool": "obsidian"}
  ```

- **Endpoint:** `GET /integrations`
- **Description:** List configured integrations and their status.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl http://localhost:9083/integrations
  ```
- **Sample Response:**
  ```json
  [
    {"tool": "obsidian", "status": "connected"},
    {"tool": "anythingllm", "status": "disconnected"}
  ]
  ```

## Projects

- **Endpoint:** `POST /projects`
- **Description:** Create a new project/namespace.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/projects \
    -H 'Content-Type: application/json' \
    -d '{"name": "project-xyz", "description": "A new research project"}'
  ```
- **Sample Response:**
  ```json
  {"project_id": "project-xyz", "status": "created"}
  ```

- **Endpoint:** `GET /projects`
- **Description:** List all projects/namespaces.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl http://localhost:9083/projects
  ```
- **Sample Response:**
  ```json
  [
    {"project_id": "project-xyz", "description": "A new research project"},
    {"project_id": "project-abc", "description": "Legacy data"}
  ]
  ```

- **Endpoint:** `POST /projects/{project_id}/switch`
- **Description:** Switch the active project/namespace.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/projects/project-xyz/switch
  ```
- **Sample Response:**
  ```json
  {"active_project": "project-xyz", "status": "switched"}
  ```

## Analytics (Extended)

- **Endpoint:** `GET /v1/analytics/usage`
- **Description:** Retrieve system usage metrics.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl http://localhost:9083/v1/analytics/usage
  ```
- **Sample Response:**
  ```json
  {"llm_calls": 1234, "embedding_requests": 567, "active_users": 42}
  ```

- **Endpoint:** `GET /v1/analytics/ingestion`
- **Description:** Retrieve ingestion/content metrics.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl http://localhost:9083/v1/analytics/ingestion
  ```
- **Sample Response:**
  ```json
  {"docs_ingested": 100, "chunks": 500, "largest_doc": "doc1.md"}
  ```

- **Endpoint:** `GET /v1/analytics/user_behavior`
- **Description:** Retrieve user behavior analytics.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl http://localhost:9083/v1/analytics/user_behavior
  ```
- **Sample Response:**
  ```json
  {"most_common_queries": ["project update", "meeting notes"], "feature_adoption": {"search": 80, "qna": 50}}
  ```

- **Endpoint:** `GET /v1/analytics/alerts`
- **Description:** Retrieve active alerts/anomalies.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl http://localhost:9083/v1/analytics/alerts
  ```
- **Sample Response:**
  ```json
  [
    {"alert": "High error rate on /llm/complete", "severity": "critical"},
    {"alert": "Unusual ingestion latency", "severity": "warning"}
  ]
  ```

## Platform Health & Docs

- **Endpoint:** `GET /health`
- **Description:** Health check endpoint for platform services.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl http://localhost:9083/health
  ```
- **Sample Response:**
  ```json
  {"status": "healthy", "services": {"neo4j": "ok", "qdrant": "ok", "llm": "ok"}}
  ```

- **Endpoint:** `GET /docs/index`
- **Description:** List all documentation sections and URLs.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl http://localhost:9083/docs/index
  ```
- **Sample Response:**
  ```json
  [
    {"section": "API Endpoints", "url": "/docs/user/endpoints.md"},
    {"section": "User Journeys", "url": "/docs/guides/user-journeys/"}
  ]
  ```

## Model Management (Extended)

- **Endpoint:** `POST /v1/model_catalog/install`
- **Description:** Install a new model from a remote source.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/v1/model_catalog/install \
    -H 'Content-Type: application/json' \
    -d '{"name": "sentence-transformers/all-MiniLM-L6-v2", "type": "embedding"}'
  ```
- **Sample Response:**
  ```json
  {"message": "Model installation started", "name": "sentence-transformers/all-MiniLM-L6-v2", "type": "embedding"}
  ```

- **Endpoint:** `GET /v1/model_catalog/installed`
- **Description:** List all installed models and their metadata.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl http://localhost:9083/v1/model_catalog/installed
  ```
- **Sample Response:**
  ```json
  [
    {"name": "TheBloke/phi-2-GGUF", "type": "llm", "installed": true},
    {"name": "sentence-transformers/all-MiniLM-L6-v2", "type": "embedding", "installed": true}
  ]
  ```

## Miscellaneous

### Add Entity Node
- **Endpoint:** `POST /entity-node`
- **Description:** Add a new entity node to the graph.
- **Status:** untested
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/entity-node \
    -H 'Content-Type: application/json' \
    -d '{"uuid": "1234-uuid", "group_id": "default", "name": "Entity Name", "summary": "Summary text"}'
  ```
- **Sample Response:**
  ```json
  {"uuid": "1234-uuid", "group_id": "default", "name": "Entity Name", "summary": "Summary text"}
  ```

### Get Entity Node
- **Endpoint:** `GET /entity-node/{uuid}`
- **Description:** Retrieve an entity node by UUID.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl http://localhost:9083/entity-node/1234-uuid
  ```
- **Sample Response:**
  ```json
  {"uuid": "1234-uuid", "group_id": "default", "name": "Entity Name", "summary": "Summary text"}
  ```

### Update Entity Node
- **Endpoint:** `PUT /entity-node/{uuid}`
- **Description:** Update an entity node by UUID.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl -X PUT http://localhost:9083/entity-node/1234-uuid \
    -H 'Content-Type: application/json' \
    -d '{"name": "Updated Name", "summary": "Updated summary"}'
  ```
- **Sample Response:**
  ```json
  {"uuid": "1234-uuid", "group_id": "default", "name": "Updated Name", "summary": "Updated summary"}
  ```

### Delete Entity Node
- **Endpoint:** `DELETE /entity-node/{uuid}`
- **Description:** Delete an entity node by UUID.
- **Status:** missing
- **Sample Request:**
  ```bash
  curl -X DELETE http://localhost:9083/entity-node/1234-uuid
  ```
- **Sample Response:**
  ```json
  {"message": "Entity node deleted", "uuid": "1234-uuid"}
  ```

### Ingest Markdown Chunks
- **Endpoint:** `POST /v1/qa/markdown/ingest_chunks`
- **Description:** Ingest markdown chunks for Q&A.
- **Status:** untested
- **Sample Request:**
  ```bash
  curl -X POST http://localhost:9083/v1/qa/markdown/ingest_chunks \
    -H 'Content-Type: application/json' \
    -d '{"chunks": ["Chunk 1", "Chunk 2"]}'
  ```

### Dashboard Root
- **Endpoint:** `GET /`
- **Description:** Returns the model management dashboard UI.

---

# Notes
- All endpoints are available on the port configured for your backend (default: 9083).
- For endpoints requiring authentication or special headers, see the OpenAPI docs at `/docs`.
- This document is a living reference and should be updated as new endpoints are added.
