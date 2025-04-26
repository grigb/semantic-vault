# AnythingLLM + Ollama System Overview

**See also:**
- [AI Friendly Pipeline Overview](../guides/AI_FRIENDLY_PIPELINE_OVERVIEW.md)
- [Graphiti Local Guide](../guides/README_GRAPHITI_LOCAL.md)
- [CSA Reference](../CSA.md)


## Introduction
This document provides a comprehensive overview of the AnythingLLM system integrated with a local Ollama LLM backend. It explains the architecture, user experience, and what users should expect when interacting with the system.

---

## System Architecture

### 1. **Frontend (Rust/Egui/AnythingLLM UI)**
- Presents a web-based interface for chat, document upload, and workspace management.
- Allows users to create workspaces, upload files, and interact with the LLM.

### 2. **Backend (AnythingLLM in Docker)**
- Manages workspaces, document embedding, chat history, and LLM interactions.
- Connects to Ollama as the local LLM provider for all chat and RAG (Retrieval Augmented Generation) tasks.
- Embedding pipeline uses a native embedder or a patched OpenAI-compatible local embedding server.

### 3. **Ollama (Local LLM)**
- Serves the LLM model (e.g., `llama3.1:latest`) for chat and document-aware inference.
- Runs locally for privacy, speed, and cost-effectiveness.

### 4. **Database (SQLite)**
- Stores all metadata: workspaces, documents, chat history, vector embeddings, and configuration.

---

## User Workflow
1. **Start the System:**
   - Launch AnythingLLM (Docker) and ensure Ollama is running locally.
2. **Create a Workspace:**
   - Use the UI to create a new workspace for your project or topic.
3. **Upload Documents:**
   - Drag-and-drop or use the UI to upload files. These are embedded and indexed for search and RAG.
4. **Chat and Search:**
   - Use the chat interface to ask questions about your documents or run semantic searches.
   - The system retrieves relevant chunks and generates answers using the LLM.

---
