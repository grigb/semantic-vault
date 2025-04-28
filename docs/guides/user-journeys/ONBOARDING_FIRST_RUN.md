# User Journey: Onboarding & First Run

- **Persona/Role:** New user (human or AI agent)
- **Journey Name:** Onboarding & First Run
- **Related Features/Docs:**
  - [Main README](../../README.md)
  - [Documentation Index](../README.md)
  - [Development Guide](../onboarding/DEVELOPMENT_GUIDE.md)
  - [Master Checklist](../planning/SEMANTIC_SYSTEM_MASTER_CHECKLIST.md)
- **Preconditions:**
  - Access to the repository
  - Docker and Docker Compose installed
  - .env file configured with required secrets
- **Goal/Outcome:** Successfully set up and run the Semantic Vault platform locally for the first time.

---

## Step-by-Step Journey

1. **Clone the Repository**
   - Run: `git clone <repo-url> semantic-vault && cd semantic-vault`
2. **Configure Environment**
   - Copy `.env.example` to `.env` and fill in required secrets (Neo4j password, API keys, etc.)
3. **Build & Launch Services**
   - Run: `docker compose -f docker/docker-compose.yml up --build -d`
   - Wait for all services to report healthy (Neo4j, Graphiti, Embedding Proxy, etc.)
4. **Create Vector Index in Neo4j**
   - Run the provided `cypher-shell` command (see README)
5. **Ingest Test Data**
   - Run: `python scripts/quick_ingest_neo4j.py`
6. **Run a Vector Search**
   - Use the provided `curl` command to test the `/search` endpoint
7. **Verify System Health**
   - Check Docker Compose logs and/or use health check endpoints
8. **Explore Documentation**
   - Review the documentation index and onboarding guides for next steps

---

## Edge Cases & Variations
- Missing or misconfigured `.env` file
- Docker daemon not running
- Service health checks failing (troubleshoot using logs)
- Network port conflicts

---

## Expected Results
- All services start and report healthy
- Test data is ingested successfully
- Search endpoint returns expected results
- User understands where to find further documentation and support

---

## Testing Checklist
- [ ] Repository can be cloned and accessed
- [ ] .env file is configured and present
- [ ] All containers start and are healthy
- [ ] Vector index can be created
- [ ] Data ingestion script runs without error
- [ ] Search endpoint returns valid results
- [ ] User can find documentation for further steps

---

## Feedback & Improvements
- Report onboarding issues or suggestions via GitHub Issues or the project chat
- Suggest improvements to this journey doc via pull request
