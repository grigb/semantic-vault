#!/usr/bin/env python3
"""
scripts/export_notion.py: Export Notion databases to Markdown with YAML front-matter.
"""
import os
import sys
from dotenv import load_dotenv
from notion_client import Client
import frontmatter

def blocks_to_md(blocks):
    lines = []
    for b in blocks:
        btype = b.get("type")
        if btype == "paragraph":
            texts = b["paragraph"]["rich_text"]
            text = "".join([t.get("plain_text", "") for t in texts])
            lines.append(text)
        elif btype.startswith("heading_"):
            level = int(btype.split("_")[1])
            texts = b[btype]["rich_text"]
            text = "".join([t.get("plain_text", "") for t in texts])
            lines.append("#" * level + " " + text)
        elif btype == "bulleted_list_item":
            texts = b["bulleted_list_item"]["rich_text"]
            text = "".join([t.get("plain_text", "") for t in texts])
            lines.append(f"- {text}")
        elif btype == "numbered_list_item":
            texts = b["numbered_list_item"]["rich_text"]
            text = "".join([t.get("plain_text", "") for t in texts])
            lines.append(f"1. {text}")
        else:
            continue
    return "\n".join(lines)

def slugify(s: str) -> str:
    import re
    from urllib.parse import quote
    s = s.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s]+", "-", s)
    return quote(s, safe="-")

def export_databases(api_keys, db_ids, export_path):
    os.makedirs(export_path, exist_ok=True)
    for key, db_id in zip(api_keys, db_ids):
        client = Client(auth=key)
        try:
            result = client.databases.query(database_id=db_id)
        except Exception as ex:
            print(f"[export_notion] Failed to query {db_id}: {ex}", file=sys.stderr)
            continue
        for page in result.get("results", []):
            page_id = page.get("id")
            props = page.get("properties", {})
            title = None
            # extract title property
            for prop_name, prop_val in props.items():
                if prop_val.get("type") == "title":
                    title = "".join([t.get("plain_text", "") for t in prop_val.get("title", [])])
                    break
            if not title:
                title = page_id
            # fetch children blocks
            blocks = client.blocks.children.list(block_id=page_id).get("results", [])
            body_md = blocks_to_md(blocks)
            meta = {
                "title": title,
                "notion_id": page_id,
                "database_id": db_id,
                "url": page.get("url", ""),
            }
            post = frontmatter.Post(body_md, **meta)
            filename = f"{slugify(title)}-{page_id}.md"
            path = os.path.join(export_path, filename)
            with open(path, "w") as f:
                frontmatter.dump(post, f)
            print(f"[export_notion] Wrote {path}")

def main():
    load_dotenv()
    keys = os.getenv("NOTION_API_KEYS", "")
    ids = os.getenv("NOTION_DATABASE_IDS", "")
    if not keys or not ids:
        print("Please set NOTION_API_KEYS and NOTION_DATABASE_IDS in your .env or environment", file=sys.stderr)
        sys.exit(1)
    api_keys = [k.strip() for k in keys.split(",") if k.strip()]
    db_ids = [d.strip() for d in ids.split(",") if d.strip()]
    if len(api_keys) != len(db_ids):
        print("Mismatch: number of API keys and database IDs must be equal", file=sys.stderr)
        sys.exit(1)
    export_path = os.getenv("NOTION_EXPORT_PATH", "notion-export")
    export_databases(api_keys, db_ids, export_path)

if __name__ == "__main__":
    main()
