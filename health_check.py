import requests
import sys

def check_endpoint(url, method="GET", payload=None, expect_json=True):
    try:
        if method == "POST":
            resp = requests.post(url, json=payload, timeout=5)
        else:
            resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        if expect_json:
            resp.json()
        print(f"[OK] {url}")
        return True
    except Exception as e:
        print(f"[FAIL] {url}: {e}")
        return False

def main():
    all_ok = True
    # Graphiti search API
    all_ok &= check_endpoint(
        "http://localhost:9003/search",
        method="POST",
        payload={"query": "test", "group_id": "notion", "max_facts": 1},
        expect_json=True
    )
    # AnythingLLM root page
    all_ok &= check_endpoint("http://localhost:9002", method="GET", expect_json=False)
    # AnythingLLM JS asset
    all_ok &= check_endpoint("http://localhost:9002/index.js", method="GET", expect_json=False)
    # Qdrant API (collections list)
    all_ok &= check_endpoint("http://localhost:9004/collections", method="GET", expect_json=True)
    # Embedding Proxy (/v1/embeddings)
    all_ok &= check_endpoint(
        "http://localhost:9009/v1/embeddings",
        method="POST",
        payload={"input": ["test sentence"], "model": "local"},
        expect_json=True
    )
    # Local Embed Server (/embeddings)
    all_ok &= check_endpoint(
        "http://localhost:9008/embeddings",
        method="POST",
        payload={"sentences": ["test sentence"]},
        expect_json=True
    )
    if all_ok:
        print("\nAll services healthy.")
        sys.exit(0)
    else:
        print("\nOne or more services failed health checks.")
        sys.exit(1)

if __name__ == "__main__":
    main()
