# User Journey: Semantic Search

- **Persona/Role:** End user, researcher, or developer
- **Journey Name:** Semantic Search
- **Related Features/Docs:**
  - [Search API](../../README.md#running-searches)
  - [Graphiti API Docs](../../graphiti/README.md)
  - [Onboarding & First Run](./ONBOARDING_FIRST_RUN.md)
- **Preconditions:**
  - Platform is running and healthy (see onboarding journey)
  - Test data or real data is ingested
- **Goal/Outcome:** Successfully perform a semantic search and receive relevant results from the knowledge graph

---

## Step-by-Step Journey

1. **Access the Search Endpoint**
   - Confirm Graphiti is running at `http://localhost:8000` or appropriate endpoint
2. **Prepare a Search Query**
   - Example: `{ "query": "test fact", "group_ids": ["products"], "max_facts": 5 }`
3. **Send the Search Request**
   - Use `curl`, Postman, or a Python script to POST to `/search`
   - Example: `curl -X POST http://localhost:8000/search -H 'Content-Type: application/json' -d '{"query": "test fact", "group_ids": ["products"], "max_facts": 5}'`
4. **Review the Results**
   - Inspect the returned JSON for matching facts/edges and metadata
5. **(Optional) Adjust Search Parameters**
   - Change query text, group_ids, or max_facts to refine results
6. **(Optional) Troubleshoot**
   - If no results, verify data ingestion, service health, and query format

---

## Edge Cases & Variations
- No matching results (empty response)
- Malformed query (API returns error)
- Service not running or unhealthy
- Large result sets (pagination/limits)

---

## Expected Results
- API responds with a list of semantically relevant facts/edges
- Each result includes metadata (fact, uuid, group_id, etc.)
- User can adjust queries for different results

---

## Testing Checklist
- [ ] Platform is running and healthy
- [ ] Search endpoint responds to POST requests
- [ ] Valid queries return relevant results
- [ ] Edge cases (empty, malformed, or large queries) are handled gracefully

---

## Feedback & Improvements
- Report API or search issues via GitHub Issues or project chat
- Suggest improvements to this journey doc via pull request
