import argparse
import requests
import json

def main():
    parser = argparse.ArgumentParser(description="Search Graphiti for semantic facts.")
    parser.add_argument('--query', required=True, help='Search query string')
    parser.add_argument('--group-id', default='products', help='Group ID to search')
    parser.add_argument('--url', default='http://localhost:9003/search', help='Graphiti search endpoint URL')
    parser.add_argument('--max-facts', type=int, default=5, help='Max facts to return')
    args = parser.parse_args()

    payload = {
        "query": args.query,
        "group_ids": [args.group_id],
        "max_facts": args.max_facts
    }
    try:
        resp = requests.post(args.url, json=payload, timeout=20)
        resp.raise_for_status()
        result = resp.json()
        facts = result.get('facts', [])
        if not facts:
            print("No results found.")
            return
        print(f"Top {len(facts)} facts for query '{args.query}':\n")
        for i, fact in enumerate(facts, 1):
            print(f"{i}. {fact['fact']}")
            print(f"   (uuid: {fact['uuid']}, name: {fact['name']})\n")
    except Exception as e:
        print(f"Search error: {e}")

if __name__ == "__main__":
    main()
