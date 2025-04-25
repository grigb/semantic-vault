# Graphiti Local LLM Integration Workflow

[Moved from docs/README_GRAPHITI_LOCAL.md]

(Full content preserved; see project index in /docs/README.md for navigation.)

---

# Graphiti Local LLM Integration Workflow

**See also:**
- [System Overview](../onboarding/SYSTEM_OVERVIEW.md)
- [AI Friendly Pipeline Overview](AI_FRIENDLY_PIPELINE_OVERVIEW.md)
- [CSA Reference](../CSA.md)


This guide documents how to ingest data, generate embeddings with your local LLM, and enable semantic search in Graphiti—**without any external API dependencies**.

---

## 1. Prerequisites
- **Neo4j** running and accessible (default Bolt port: `9007`, HTTP: `9006`)
- **Graphiti** and **local embedding server** running (as configured in your Docker Compose)
- Python 3.8+
- Install dependencies:
  ```sh
  pip install neo4j requests
  ```

## 2. Ingesting Data with Local Embeddings

Use the provided script to ingest product data and create semantic edges:

```sh
python3 create_graphiti_edges.py \
  --data mock_data.json \
  --embed-url http://localhost:9009/v1/embeddings \
  --neo4j-uri bolt://localhost:9007 \
  --neo4j-user neo4j \
  --neo4j-password <YOUR_PASSWORD> \
  --group-id products
```

Or set environment variables in `.env`:
```
NEO4J_URI=bolt://localhost:9007
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password_here
```
Then run:
```sh
python3 create_graphiti_edges.py
```

- The script will:
  - Read your product data
  - Call your local embedding server for each product
  - Create nodes and semantic edges in Neo4j
  - Log all progress and errors

---

## 3. Running Semantic Search

Example search query (replace `TinyBirds` with your keyword):
```sh
curl -s -X POST http://localhost:9003/search \
  -H 'Content-Type: application/json' \
  -d '{"query": "TinyBirds", "group_ids": ["products"]}' | jq .
```

---

## 4. Troubleshooting
- **Neo4j connection errors:** Ensure Neo4j is running and port is correct (`9007`).
- **Embedding errors:** Ensure your local embedding server is up and accessible at the specified URL.
- **No search results:** Confirm that edges with `fact_embedding` exist in Neo4j (rerun the ingestion script if needed).
- **Logs:** Check script output for detailed error messages.

---

## 5. Customization
- You can modify the ingestion script to create edges between related products (not just self-loops).
- Adapt the script for any dataset—just provide a compatible JSON file.

---

## 6. Support
If you encounter issues or want to automate more of your workflow, contact your AI assistant for further customization!
