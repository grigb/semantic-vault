#!/usr/bin/env python3
"""
run_e2e_test.py

End-to-end test script for Semantic Vault vector search pipeline.
- Ingests sample data into Neo4j using the ingestion script
- Runs a search query against the Graphiti API
- Validates the output and prints results
"""
import subprocess
import requests
import os
import sys
import time

# Configurable endpoints and parameters
GRAPHITI_URL = os.getenv("GRAPHITI_URL", "http://localhost:9003/search")
INGEST_SCRIPT = os.getenv("INGEST_SCRIPT", "scripts/quick_ingest_neo4j.py")
QUERY = "test fact"
GROUP_IDS = ["products"]
MAX_FACTS = 5

# Step 1: Ingest sample data
def run_ingest():
    print("[TEST] Ingesting test data...")
    result = subprocess.run([sys.executable, INGEST_SCRIPT], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("[FAIL] Ingestion failed:", result.stderr)
        sys.exit(1)
    print("[PASS] Ingestion completed.")

# Step 2: Wait for Neo4j and Graphiti to be ready
def wait_for_graphiti(timeout=30):
    print(f"[TEST] Waiting for Graphiti API at {GRAPHITI_URL}...")
    for i in range(timeout):
        try:
            resp = requests.post(GRAPHITI_URL, json={"query": QUERY, "group_ids": GROUP_IDS, "max_facts": 1}, timeout=2)
            if resp.status_code == 200:
                print("[PASS] Graphiti API is ready.")
                return
        except Exception:
            pass
        time.sleep(1)
    print("[FAIL] Graphiti API not reachable after waiting.")
    sys.exit(1)

# Step 3: Run search and validate output
def run_search():
    print(f"[TEST] Running vector search for query: '{QUERY}'...")
    resp = requests.post(GRAPHITI_URL, json={"query": QUERY, "group_ids": GROUP_IDS, "max_facts": MAX_FACTS})
    print(f"[DEBUG] Status code: {resp.status_code}")
    if resp.status_code != 200:
        print("[FAIL] Search failed:", resp.text)
        sys.exit(1)
    data = resp.json()
    print("[RESULT] Search response:")
    print(data)
    # Validate at least one result contains the test fact
    found = any(QUERY in (item.get("fact") or "") for item in data)
    if found:
        print("[PASS] Test fact found in search results.")
    else:
        print("[FAIL] Test fact NOT found in search results!")
        sys.exit(1)

if __name__ == "__main__":
    run_ingest()
    wait_for_graphiti()
    run_search()
    print("[SUCCESS] End-to-end test completed.")
