import os
import glob
import hashlib
import requests
from neo4j import GraphDatabase
import argparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def parse_args():
    parser = argparse.ArgumentParser(description="Ingest markdown files as semantic nodes/edges in Neo4j.")
    parser.add_argument('--md-root', default='obsidian-vault/DC-Notion-Export/Private & Shared', help='Root directory for markdown import')
    parser.add_argument('--embed-url', default='http://localhost:9009/v1/embeddings', help='Embedding server URL')
    parser.add_argument('--neo4j-uri', default=os.environ.get('NEO4J_URI', 'bolt://localhost:9007'), help='Neo4j Bolt URI')
    parser.add_argument('--neo4j-user', default=os.environ.get('NEO4J_USER', 'neo4j'), help='Neo4j user')
    parser.add_argument('--neo4j-password', default=os.environ.get('NEO4J_PASSWORD'), help='Neo4j password')
    parser.add_argument('--group-id', default='notion', help='Group ID for nodes/edges')
    parser.add_argument('--max-summary-chars', type=int, default=2000, help='Max chars for summary/fact')
    return parser.parse_args()

def get_embedding(text, embed_url):
    payload = {"model": "text-embedding-3-small", "input": [text]}
    try:
        res = requests.post(embed_url, json=payload, timeout=30)
        res.raise_for_status()
        return res.json()["data"][0]["embedding"]
    except Exception as e:
        logging.error(f"Embedding error: {e}")
        return [0.0] * 5  # fallback dummy embedding

def create_node(tx, uuid, name, summary, group_id):
    tx.run(
        "MERGE (n:Entity {uuid: $uuid}) SET n.name = $name, n.summary = $summary, n.group_id = $group_id",
        uuid=uuid, name=name, summary=summary, group_id=group_id
    )

def create_edge(tx, source_uuid, target_uuid, edge_uuid, fact, embedding, group_id):
    tx.run(
        """
        MATCH (a:Entity {uuid: $source}), (b:Entity {uuid: $target})
        MERGE (a)-[r:RELATES_TO {uuid: $edge_uuid}]->(b)
        SET r.group_id = $group_id,
            r.name = 'related',
            r.fact = $fact,
            r.fact_embedding = $embedding,
            r.episodes = [],
            r.created_at = datetime(),
            r.valid_at = datetime(),
            r.invalid_at = null,
            r.expired_at = null
        """,
        source=source_uuid, target=target_uuid, edge_uuid=edge_uuid,
        group_id=group_id, fact=fact, embedding=embedding
    )

def extract_title_and_summary(path, max_chars=2000):
    name = os.path.basename(path)
    summary = ""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # Title: first Markdown heading (line starting with #), else filename
        for line in lines:
            if line.strip().startswith('#'):
                name = line.strip('#').strip()
                break
        # Summary: first max_chars of content
        summary = ''.join(lines)[:max_chars]
    except Exception as e:
        logging.error(f"Error reading {path}: {e}")
        summary = ""
    return name, summary

def main():
    args = parse_args()
    if not args.neo4j_password:
        logging.error("NEO4J_PASSWORD not set. Use --neo4j-password or set env var.")
        return
    # Recursively find all .md files
    md_files = glob.glob(os.path.join(args.md_root, '**', '*.md'), recursive=True)
    logging.info(f"Found {len(md_files)} markdown files for ingestion.")
    driver = GraphDatabase.driver(args.neo4j_uri, auth=(args.neo4j_user, args.neo4j_password))
    with driver.session() as session:
        for path in md_files:
            # Use a hash of the path as uuid
            uuid = 'notion-' + hashlib.sha1(path.encode('utf-8')).hexdigest()
            name, summary = extract_title_and_summary(path, max_chars=args.max_summary_chars)
            if not summary:
                logging.warning(f"Skipping empty file: {path}")
                continue
            try:
                session.execute_write(create_node, uuid, name, summary, args.group_id)
                embedding = get_embedding(summary, args.embed_url)
                edge_uuid = f"edge-{uuid}"
                session.execute_write(create_edge, uuid, uuid, edge_uuid, summary, embedding, args.group_id)
                logging.info(f"Ingested {path} as node '{name}'")
            except Exception as e:
                logging.error(f"Failed for {path}: {e}")
    driver.close()
    logging.info("Done.")

if __name__ == "__main__":
    main()
def get_embedding(text, embed_url):
    payload = {"model": "text-embedding-3-small", "input": [text]}
    try:
        res = requests.post(embed_url, json=payload, timeout=30)
        res.raise_for_status()
        return res.json()["data"][0]["embedding"]
    except Exception as e:
        logging.error(f"Embedding error: {e}")
        return [0.0] * 5  # fallback dummy embedding

def create_node(tx, uuid, name, summary, group_id):
    tx.run(
        "MERGE (n:Entity {uuid: $uuid}) SET n.name = $name, n.summary = $summary, n.group_id = $group_id",
        uuid=uuid, name=name, summary=summary, group_id=group_id
    )

def create_edge(tx, source_uuid, target_uuid, edge_uuid, fact, embedding, group_id):
    tx.run(
        """
        MATCH (a:Entity {uuid: $source}), (b:Entity {uuid: $target})
        MERGE (a)-[r:RELATES_TO {uuid: $edge_uuid}]->(b)
        SET r.group_id = $group_id,
            r.name = 'related',
            r.fact = $fact,
            r.fact_embedding = $embedding,
            r.episodes = [],
            r.created_at = datetime(),
            r.valid_at = datetime(),
            r.invalid_at = null,
            r.expired_at = null
        """,
        source=source_uuid, target=target_uuid, edge_uuid=edge_uuid,
        group_id=group_id, fact=fact, embedding=embedding
    )

def main():
    args = parse_args()
    if not args.neo4j_password:
        logging.error("NEO4J_PASSWORD not set. Use --neo4j-password or set env var.")
        return
    with open(args.data, "r") as f:
        data = json.load(f)
    products = data["products"]
    driver = GraphDatabase.driver(args.neo4j_uri, auth=(args.neo4j_user, args.neo4j_password))
    with driver.session() as session:
        for i, product in enumerate(products):
            uuid = f"product-{product['id']}"
            name = product["title"]
            summary = product["body_html"]
            try:
                session.execute_write(create_node, uuid, name, summary, args.group_id)
                embedding = get_embedding(summary, args.embed_url)
                edge_uuid = f"edge-{uuid}"
                session.execute_write(create_edge, uuid, uuid, edge_uuid, summary, embedding, args.group_id)
                logging.info(f"Created node and edge for {name}")
            except Exception as e:
                logging.error(f"Failed for {name}: {e}")
    driver.close()
    logging.info("Done.")

if __name__ == "__main__":
    main()
