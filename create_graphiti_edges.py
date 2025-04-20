import json
import requests
from neo4j import GraphDatabase
import os
import argparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def parse_args():
    parser = argparse.ArgumentParser(description="Ingest products and create semantic edges in Neo4j.")
    parser.add_argument('--data', default='mock_data.json', help='Path to product data JSON')
    parser.add_argument('--embed-url', default='http://localhost:9009/v1/embeddings', help='Embedding server URL')
    parser.add_argument('--neo4j-uri', default=os.environ.get('NEO4J_URI', 'bolt://localhost:9007'), help='Neo4j Bolt URI')
    parser.add_argument('--neo4j-user', default=os.environ.get('NEO4J_USER', 'neo4j'), help='Neo4j user')
    parser.add_argument('--neo4j-password', default=os.environ.get('NEO4J_PASSWORD'), help='Neo4j password')
    parser.add_argument('--group-id', default='products', help='Group ID for nodes/edges')
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
