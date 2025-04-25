# AI Friendly Pipeline Overview

**See also:**
- [System Overview](../onboarding/SYSTEM_OVERVIEW.md)
- [Graphiti Local Guide](README_GRAPHITI_LOCAL.md)
- [CSA Reference](../CSA.md)


This document provides a comprehensive, self-contained technical and conceptual overview of the AnythingLLM + Ollama toolset and pipeline. It is designed for AI agents, developers, and system architects who need robust persistent memory, semantic search, schema flexibility, and multi-agent project management. All details are included here—no external references required.

---

## 1. System Purpose & Philosophy

This system is a **local-first, privacy-focused, modular platform** for:
- Persistent, queryable memory for AI and human workflows
- Project and knowledge management across teams, devices, and timescales
- Semantic search, retrieval, and context-aware chat using local LLMs and embeddings
- Schema-on-demand storage for any data, supporting evolving and complex projects

It is suitable as a backend for autonomous agents, copilots, collaborative tools, or as a standalone knowledge/project management engine.

---

## 2. Architecture & Pipeline (Step-by-Step)

### **A. Data Ingestion & Storage**
- Users or agents upload documents, create tasks, or add notes via web UI, API, or CLI.
- Data is stored in a local SQLite database (optionally Neo4j for graph use cases).
- **Schema Flexibility:**
  - Tables include `workspaces`, `workspace_documents`, `chat_history`, `tasks`, and more.
  - Arbitrary metadata (JSON) can be attached to any entity (e.g., document, task, user).
  - New columns, tables, or data types can be added on demand—no rigid schema lock-in.
- **Example:**
  - A workspace might store: `{id, name, description, createdAt, metadata}`
  - A document record: `{id, workspaceId, filename, docpath, metadata, createdAt}`

### **B. Embedding & Indexing**
- All text data (documents, notes, chat, etc.) is sent to a local embedding server:
  - Default: FastAPI server running SentenceTransformer (e.g., `all-MiniLM-L6-v2`)
  - Supports Apple Silicon GPU (MPS) or CPU

---
