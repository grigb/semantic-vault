# Semantic Vault: Vector Search Platform with Neo4j, Graphiti, and Embedding Proxy

---

## 🚀 Onboarding & Documentation

Welcome! If you're new (human or AI agent), start here:

- **Documentation Index:** [docs/README.md](./docs/README.md) — Central navigation for all project docs
- **Master Checklist:** [docs/planning/SEMANTIC_SYSTEM_MASTER_CHECKLIST.md](./docs/planning/SEMANTIC_SYSTEM_MASTER_CHECKLIST.md) — Project phases, status, and next steps
- **Development Guide:** [docs/onboarding/DEVELOPMENT_GUIDE.md](./docs/onboarding/DEVELOPMENT_GUIDE.md) — Workflow, standards, and best practices
- **Onboarding & System Overview:**
    - [docs/onboarding/SYSTEM_OVERVIEW.md](./docs/onboarding/SYSTEM_OVERVIEW.md)
    - [docs/onboarding/TEAM_INTRO_TO_SEMANTIC_STACK.md](./docs/onboarding/TEAM_INTRO_TO_SEMANTIC_STACK.md)
- **Design Docs:** [docs/design-docs/](./docs/design-docs/) — API and component specifications

**Always consult the master checklist and documentation index first to understand project status and where to begin.**

---

## Overview
Semantic Vault is a modern, extensible platform for knowledge graph and vector search, combining:
- **Neo4j 5.18+**: Native vector search and graph database
- **Graphiti**: API and semantic search backend
- **Embedding Proxy**: OpenAI-compatible local embedding service
- **Qdrant** (optional): High-performance vector DB
- **AnythingLLM**: RAG/LLM frontend for chat and document search

All services are orchestrated via Docker Compose for reproducibility, multi-project support, and easy integration.

---

## Quickstart

### 1. Clone & Configure
```sh
git clone <your-repo-url> semantic-vault
cd semantic-vault
cp .env.example .env
# Edit .env to set NEO4J_PASSWORD, OPENAI_API_KEY, etc.
```

### 2. Build & Launch All Services
```sh
docker compose -f docker/docker-compose.yml up --build -d
```
- This starts Neo4j, Graphiti, Embedding Proxy, AnythingLLM, and Qdrant.
- Model data is shared via the `model_data` Docker volume for efficient, multi-container use.

### 3. Create Vector Index in Neo4j (One-time)
```sh
docker compose -f docker/docker-compose.yml exec neo4j cypher-shell -u neo4j -p "$NEO4J_PASSWORD" \
  "CREATE VECTOR INDEX rel_fact_embedding_index FOR ()-[r:RELATES_TO]-() ON (r.fact_embedding) OPTIONS {indexConfig: {\`vector.dimensions\`: 1536, \`vector.similarity_function\`: 'cosine'}};"
```

### 4. Ingest Test Data
```sh
python scripts/quick_ingest_neo4j.py
```

### 5. Run a Vector Search
```sh
curl -X POST http://localhost:9003/search \
  -H 'Content-Type: application/json' \
  -d '{"query": "test fact", "group_ids": ["products"], "max_facts": 5}'
```

---

For more guides, onboarding, and design docs, see the [docs/](./docs/) directory and the documentation index above.

---

## Architecture & Components

### Services
- **Neo4j**: Graph DB, stores nodes, relationships, and vector indexes
- **Graphiti**: API backend for hybrid (vector+symbolic) search
- **Embedding Proxy**: FastAPI service, OpenAI-compatible `/v1/embeddings` endpoint
- **AnythingLLM**: UI for chat/RAG workflows
- **Qdrant**: Vector DB (optional, for advanced/large-scale vector storage)

### Docker Volumes
- `model_data`: Shared across embedding proxy and other containers for efficient model reuse
- All persistent data (Neo4j, Qdrant, Graphiti, AnythingLLM) is stored in named Docker volumes for easy migration and multi-project use

---

## Notification Automation System

Semantic Vault features a robust notification automation system for real-time and historical user feedback across all backend and frontend workflows.

### Architecture
- **Backend:** FastAPI-based notification service integrated in Graphiti. Triggers notifications for ingestion, model management, routing, entity/group/episode operations, and more.
- **Persistence:** All notifications are stored in a local SQLite database (`notifications.sqlite3`), ensuring durability and historical access.
- **User Preferences:** Users can mute or filter notification types (success, error, info, etc.). Preferences are stored per user and respected in all notification queries.
- **API Endpoints:**
    - `POST /v1/notify`: Send a notification (backend use)
    - `GET /v1/notifications`: List notifications (supports filtering by type/read/user)
    - `POST /v1/notifications/read`: Mark a notification as read
    - `POST /v1/notifications/mark_all_read`: Mark all notifications as read
    - `GET/POST /v1/notifications/prefs`: Get/set user notification preferences

### Frontend Features
- **Notification Center:** Real-time toasts for new notifications.
- **Notification History:** Bell icon opens a drawer with all notifications, filterable by type and read/unread status.
- **User Preferences UI:** Users can mute notification types via a preferences panel.
- **Bulk Actions:** Mark all as read, filter, and manage notification history.

### Project Recovery & Persistent Memory
- All notification data and user preferences are stored persistently in SQLite.
- System is compliant with project recovery rules: state is recoverable after crash/restart, and onboarding is seamless.

---

## Notification Automation System

Semantic Vault features a robust notification automation system for real-time and historical user feedback across all backend and frontend workflows.

### Architecture
- **Backend:** FastAPI-based notification service integrated in Graphiti. Triggers notifications for ingestion, model management, routing, entity/group/episode operations, and more.
- **Persistence:** All notifications are stored in a local SQLite database (`notifications.sqlite3`), ensuring durability and historical access.
- **User Preferences:** Users can mute or filter notification types (success, error, info, etc.). Preferences are stored per user and respected in all notification queries.
- **API Endpoints:**
    - `POST /v1/notify`: Send a notification (backend use)
    - `GET /v1/notifications`: List notifications (supports filtering by type/read/user)
    - `POST /v1/notifications/read`: Mark a notification as read
    - `POST /v1/notifications/mark_all_read`: Mark all notifications as read
    - `GET/POST /v1/notifications/prefs`: Get/set user notification preferences

### Frontend Features
- **Notification Center:** Real-time toasts for new notifications.
- **Notification History:** Bell icon opens a drawer with all notifications, filterable by type and read/unread status.
- **User Preferences UI:** Users can mute notification types via a preferences panel.
- **Bulk Actions:** Mark all as read, filter, and manage notification history.

### Project Recovery & Persistent Memory
- All notification data and user preferences are stored persistently in SQLite.
- System is compliant with project recovery rules: state is recoverable after crash/restart, and onboarding is seamless.

---

## Usage & Testing

### Ingesting Data
- Use `scripts/quick_ingest_neo4j.py` or `scripts/example_ingest.py` to create test nodes and relationships with all required properties:
  - `fact_embedding` (1536-dim vector)
  - `created_at` (Neo4j datetime)
  - `episodes` (empty list or list of episode metadata)
  - `fact`, `name`, `uuid`, `file_path`, `group_id`

### Running Searches
- Use the `/search` endpoint on Graphiti:
  - POST `{ "query": "<text>", "group_ids": ["products"], "max_facts": 5 }`
  - Returns matching facts/edges with metadata

### Health Checks
- Neo4j: http://localhost:7474 (browser), or `docker compose logs neo4j`
- Embedding Proxy: `curl localhost:9009/v1/embeddings`
- Graphiti: `/search` endpoint, or `docker compose logs graphiti`

### Automated End-to-End Test
- Run the ingestion script, then query `/search` and assert the returned fact matches the ingested one.
- Example test script: `scripts/example_ingest.py`

---

## Integration & Extensibility

### API Endpoints
- **Graphiti**: `/search`, `/ingest`, `/api/v1/memory` (shared memory for LLMs)
- **Embedding Proxy**: `/v1/embeddings` (OpenAI-compatible)
- **Neo4j**: Bolt and HTTP (for advanced queries)
- **AnythingLLM**: UI and API for chat/RAG

### Multi-Project & Multi-Container Use
- All containers use the same `model_data` volume for model files
- You can mount your own data, fork the repo, or symlink `.env` and Docker Compose files for new projects
- Supports running multiple projects on the same host without model duplication

### Adding Your Own Data
- Modify or extend the ingestion scripts to add your own nodes, relationships, and embeddings
- Use the embedding proxy to generate vectors for any text
- Adapt Graphiti endpoints for custom search workflows

---

## Tools & Scripts

### Ingestion
- `scripts/quick_ingest_neo4j.py`: Minimal test data ingestion
- `scripts/example_ingest.py`: Template for custom ingestion

### Health & Setup
- `start.sh`: Automated setup and startup
- `scripts/health_check.sh`: Health check for all services

### Testing
- Use the provided ingestion and search scripts to validate the pipeline
- Add regression tests as needed for your workflow

---

## Example: Add a New Project
1. Fork or clone the repo
2. Mount your own data directory (e.g., `-v /my/data:/app/data`)
3. Use the shared `model_data` volume
4. Start containers with Docker Compose
5. Ingest your data and use the API endpoints as described

---

## Troubleshooting
- Check logs for each service with `docker compose logs <service>`
- Confirm all environment variables are set in `.env`
- Ensure the Neo4j vector index is created and online
- Verify the embedding proxy returns 1536-dim vectors

---

## FAQ
**Q: Can I use my own embeddings or models?**
A: Yes, point the embedding proxy to your model or use any OpenAI-compatible endpoint.

**Q: How do I scale to multiple projects or users?**
A: Use Docker volumes and environment variables to isolate or share data as needed.

**Q: How do I add new endpoints or workflows?**
A: Extend Graphiti or add new scripts/services as needed—everything is modular.

---

## Credits
- Inspired by modern RAG, vector search, and knowledge graph best practices
- Contributions welcome!

---

## License
MIT License


This repository provides a simple way to set up a self-hosted AI environment using Docker Compose, featuring:

*   **AnythingLLM:** A powerful RAG (Retrieval-Augmented Generation) platform for chatting with documents, data, and more.
*   **Graphiti:** A memory system acting as a central hub, storing conversation history and context accessible by multiple AI tools.
*   **Qdrant:** A high-performance vector database used by Graphiti to store and search embeddings efficiently.

The core idea is that AnythingLLM (and potentially other tools like AI IDE extensions) write memories to Graphiti, creating a shared context layer.

## Prerequisites

*   **Docker:** [Install Docker](https://docs.docker.com/engine/install/)
*   **Docker Compose:** Usually included with Docker Desktop, or [install separately](https://docs.docker.com/compose/install/). (v2+ recommended)
*   **Git:** To clone this repository.
*   **OpenSSL:** Usually pre-installed on Linux/macOS. Needed by `start.sh` to generate secure keys. (On Windows, Git Bash often includes it).

## Quickstart

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url> ai-starter
    cd ai-starter
    ```

2.  **Run the setup script:**
    ```bash
    chmod +x start.sh
    ./start.sh
    ```
    *   This script will check prerequisites.
    *   If `.env` doesn't exist, it will generate it from `.env.template`, creating secure random API keys for AnythingLLM (initial admin) and Graphiti.
    *   It will then start all services using `docker-compose up -d`.

3.  **Access Services:**
    *   **AnythingLLM UI:** [http://localhost:3001](http://localhost:3001)
        *   If you left `AUTH_MODE="true"` in `docker-compose.yml` (recommended for security), your *first login* will require the `ANYTHINGLLM_INITIAL_ADMIN_KEY` found in your generated `.env` file. Use this key as the password for the default `admin` user or follow UI prompts.
    *   **Graphiti API:** [http://localhost:8080](http://localhost:8080)
        *   Requires the `GRAPHITI_API_KEY` (found in `.env`) for authentication (e.g., in the `Authorization: Bearer <key>` header or via specific client configurations).
    *   **Qdrant API:** [http://localhost:6333](http://localhost:6333)

## Configuration

*   **`.env` file:** Contains generated API keys and connection details. **Do not commit this file to Git.** Modify it if you need to change ports or use existing keys.
*   **`docker-compose.yml`:** Defines the services, ports, volumes, and environment variables. You can adjust settings like `AUTH_MODE` for AnythingLLM here.
*   **`.env.template`:** The template used to create `.env` on the first run.
*   **Sensitive files** (e.g., `.env`, `*.pem`, any credentials) are listed in `.gitignore` and must never be committed to version control.

## Notion Integration
To export your Notion databases and ingest them into this system:

1. Install Python dependencies:
   ```bash
   pip install notion-client python-frontmatter python-dotenv
   ```
2. Configure your `.env` file:
   ```bash
   NOTION_API_KEYS="<key1>,<key2>,<key3>"
   NOTION_DATABASE_IDS="<dbid1>,<dbid2>,<dbid3>"
   NOTION_EXPORT_PATH="notion-export"
   ```
3. Share each Notion database with its corresponding integration (via Notion's Share dialog).
4. Run the export script:
   ```bash
   python scripts/export_notion.py
   ```
5. The exported Markdown files will appear in `notion-export/` and can be ingested like your Obsidian vault.

_For multiple accounts/databases, supply comma-separated API keys and database IDs in matching order._

## Using Shared Memory

*   **AnythingLLM:** Is pre-configured in `docker-compose.yml` to use Graphiti as its memory backend via the Memory Connector Plugin (MCP). Chats and context managed within AnythingLLM will be stored in Graphiti.
*   **Other Tools (Cursor, Goose, Custom Scripts):** To access the shared memory:
    *   Point them to the Graphiti API endpoint: `http://localhost:8080/api/v1/memory` (or the relevant Graphiti endpoint for their integration).
    *   Provide the `GRAPHITI_API_KEY` from your `.env` file for authentication.
    *   Optionally specify a namespace if you want to segment memories (e.g., per project).

---

## ⚡️ Current State & Upgrade Roadmap

**Current Stack:**
- Neo4j: 5.13 (as pinned in docker-compose.yml; not yet on 5.18+)
- Graph Data Science (GDS): version as provided by the current Neo4j image (may not be latest)
- Qdrant: latest
- AnythingLLM, Graphiti: custom/patched images
- Embedding Proxy: OpenAI-compatible, local FastAPI service

**Known Limitations:**
- Neo4j vector similarity search (native vector indexes, metadata filtering, etc.) is only fully supported in Neo4j 5.18+ and GDS 2.16+.
- Current stack may not support all advanced vector search features (relationship vector indexes, pre-filtering, etc.).
- Helper scripts for bootstrap, migration, and health checks are **not yet included**—these will be added after the upgrade.

**Upgrade Plan:**
1. Upgrade Neo4j to 5.18+ and GDS to 2.16+ (see below for Docker example).
2. Validate new vector index features and advanced queries.
3. Update all documentation and provide full automation scripts for setup, migration, and health checks.
4. Ensure all new projects and integrations use the upgraded, reproducible stack.

*This section will be updated as the upgrade progresses. For now, follow the manual steps and version notes below.*

---

## 🔗 How to Integrate This Stack Into Other Projects

This stack is designed for easy reuse across projects needing semantic memory, LLMs, or vector search. To integrate:

1. **Reuse Graphiti as a Central Memory API:**
   - Point any app or script to the Graphiti endpoint (e.g., `http://localhost:8080/api/v1/memory` or via Docker network).
   - Use the `GRAPHITI_API_KEY` from your `.env` for authentication.
   - Optionally set a custom namespace per project for data isolation.

2. **Connect to AnythingLLM for RAG/Chat:**
   - Access via the AnythingLLM UI or API (`http://localhost:3001` or mapped port).
   - Configure the `MEMORY_BACKEND` and `MCP_API_URL` to point to your Graphiti instance.
   - Use the same `.env` variables for seamless integration.

3. **Leverage the Embedding Proxy:**
   - Use the OpenAI-compatible `/v1/embeddings` endpoint (default: `http://localhost:9009/v1/embeddings`).
   - Point any OpenAI-compatible client, script, or service to this endpoint for local, fast embeddings.

4. **Share the Vector Store (Qdrant/Neo4j):**
   - Use the same Qdrant or Neo4j DB for multiple projects by sharing host/port and credentials from `.env`.
   - Ensure vector schema consistency across projects.

5. **Copy or Symlink the `.env` and Docker Compose Files:**
   - For new projects, copy `.env.template` and customize as needed.
   - You can symlink or import the Docker Compose and service configs for rapid setup.

6. **Extend or Swap Components:**
   - Add new LLMs, memory backends, or vector DBs by updating the compose file and `.env`.
   - All components are modular and can be replaced or extended as needed.

---

## 🚀 Upgrade Strategy: Neo4j & GDS

To unlock advanced vector search features, follow this upgrade plan:

### 1. Upgrade Neo4j to 5.18+ and GDS to 2.16+
- **Docker:**
  ```bash
  docker run \
    --name neo4j-vector \
    -p7474:7474 -p7687:7687 \
    -e NEO4J_AUTH=neo4j/test \
    -e NEO4J_PLUGINS='["graph-data-science"]' \
    -e NEO4J_dbms_security_procedures_unrestricted=gds.* \
    neo4j:5.18
  ```
- **Neo4j Desktop:**
  - Download the latest Neo4j Desktop and create a new DBMS with version 5.18 or higher.
  - Add the Graph Data Science (GDS) plugin (version 2.16+).

### 2. Update docker-compose.yml
- Change the Neo4j image tag to `neo4j:5.18` (or higher) in your compose file.
- Ensure `NEO4J_PLUGINS` includes `graph-data-science`.
- Rebuild/restart your stack after making changes.

### 3. Post-Upgrade Checklist
- Confirm Neo4j is running 5.18+ and GDS is 2.16+ (`CALL gds.version()` in Cypher shell).
- Test creating a vector index and running a vector query (see below).
- Check that all services (Graphiti, AnythingLLM, embedding proxy) connect successfully.
- Update documentation and scripts as needed.

### 4. Next Steps
- After confirming the upgrade, create or update helper scripts for bootstrap, migration, and health checks.
- Announce the new baseline for all future projects and integrations.

---

## 🔗 How to Integrate This Stack Into Other Projects

### 🚀 Latest Features (Neo4j 5.18+ & GDS 2.16+)
- **High-dimensional vector indexes** (up to 4096 dims; e.g., OpenAI `text-embedding-3-large`)
- **Relationship vector indexes** for semantic search over relationship embeddings
- **Enhanced similarity functions:** `vector.similarity.cosine`, `vector.similarity.euclidean`
- **Metadata pre-filtering** for efficient, targeted vector search
- **GDS library** with advanced similarity algorithms and performance improvements

### 🛠️ Upgrade & Implementation Steps
1. **Upgrade Neo4j** to 5.18+ for latest vector features.
2. **Install GDS 2.16+** (Graph Data Science plugin) for advanced similarity and vector support.
   - Docker example:
     ```bash
     docker run \
       --name neo4j-vector \
       -p7474:7474 -p7687:7687 \
       -e NEO4J_AUTH=neo4j/test \
       -e NEO4J_PLUGINS='["graph-data-science"]' \
       -e NEO4J_dbms_security_procedures_unrestricted=gds.* \
       neo4j:5.18
     ```
   - Or add GDS via Neo4j Desktop plugin manager.
3. **Store embeddings as `FloatArray`** properties on relationships (e.g., `r.embedding`).
   - Normalize vectors before storage for cosine similarity.
   - Use consistent vector length.
   - Example:
     ```cypher
     MATCH (a)-[r:SIMILAR_TO]->(b)
     SET r.embedding = [0.12, -0.45, ..., 0.91]
     ```
4. **Create a vector index:**
   ```cypher
   CREATE VECTOR INDEX rel_embedding_index IF NOT EXISTS
   FOR ()-[r:SIMILAR_TO]-()
   ON (r.embedding)
   OPTIONS {
     indexConfig: {
       `vector.dimensions`: 1536,
       `vector.similarity_function`: "cosine"
     }
   }
   ```
5. **Query with vector similarity:**
   ```cypher
   CALL db.index.vector.queryRelationships('rel_embedding_index', 5, [0.12, -0.45, ..., 0.91])
   YIELD relationship, score
   RETURN relationship, score
   ORDER BY score DESC
   ```
   Or with GDS:
   ```cypher
   WITH [0.12, -0.45, ..., 0.91] AS queryEmbedding
   MATCH ()-[r:SIMILAR_TO]->()
   RETURN r, gds.similarity.cosine(r.embedding, queryEmbedding) AS score
   ORDER BY score DESC LIMIT 10
   ```
6. **Migration tip:**
   ```cypher
   MATCH ()-[r:SIMILAR_TO]->()
   WHERE NOT exists(r.embedding)
   SET r.embedding = apoc.convert.toFloatList(r.raw_embedding_string)
   ```

### ⚠️ Production Considerations
- **Index Maintenance:** Monitor and rebuild after bulk imports/model changes.
- **Security:** Restrict unused procedures; use authentication.
- **Performance:** Use metadata pre-filtering and proper indexing; normalize vectors for best results.
- **Consistent Schema:** Ensure all embeddings are same length and type.

### 📚 References
- [Neo4j Vector Search Docs](https://neo4j.com/docs/operations-manual/current/indexes/vector-index/)
- [GDS Similarity Functions](https://neo4j.com/docs/graph-data-science/current/algorithms/vector-similarity/)
- [Cypher Manual - Vector Indexes](https://neo4j.com/docs/cypher-manual/current/indexes-for-vector-search/)
- [APOC Procedures](https://neo4j.com/labs/apoc/)

---

```bash
docker-compose down

```
