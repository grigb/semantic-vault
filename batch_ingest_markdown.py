import os
import glob
import requests
import argparse

API_URL = "http://localhost:8000/episode"

def ingest_markdown_files(directory, group_id=None, source="markdown", source_description="Batch Markdown Ingest"):
    md_files = glob.glob(os.path.join(directory, "**/*.md"), recursive=True)
    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        name = os.path.basename(md_file)
        data = {
            "name": name,
            "episode_body": content,
            "group_id": group_id or "markdown-batch",
            "source": source,
            "source_description": f"{source_description}: {md_file}"
        }
        resp = requests.post(API_URL, json=data)
        if resp.status_code == 200:
            print(f"[OK] Ingested: {md_file}")
        else:
            print(f"[FAIL] {md_file}: {resp.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch-ingest markdown files to Graphiti MCP via REST API.")
    parser.add_argument("directory", help="Directory with markdown files")
    parser.add_argument("--group_id", help="Group ID for episodes", default=None)
    args = parser.parse_args()
    ingest_markdown_files(args.directory, group_id=args.group_id)
