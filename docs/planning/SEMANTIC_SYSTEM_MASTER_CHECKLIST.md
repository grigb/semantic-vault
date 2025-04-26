# Semantic System Master Checklist & Instructions

This checklist breaks down each phase into actionable, checkable steps, with acceptance criteria, subtasks, and links to design docs. Use this as your project tracker and onboarding doc for any new AI assistant or team member.

---

## How to Use This Document
- **Check off** each item as you complete it (use `[x]` for done, `[ ]` for not done)
- **Update** with notes, links, or decisions as you go
- **Reference relevant design docs** (see links in each phase below)
- **New AI assistants and team members:**
    - Read this file first to instantly get project context and current status
    - Review the development guide at `/docs/onboarding/DEVELOPMENT_GUIDE.md`
    - Follow cursor/context rules in `/.cursor/rules/rules.json`:
        - Always review this checklist, strategy, and vision docs before acting
        - After each major step, run or update the test suite (unit, integration, or end-to-end as appropriate)
        - Never proceed to the next step if tests fail—fix or revert first
        - Update checklist and link to new docs/outputs
        - Never lose context between phases
- **Best Practices:**
    - Always link to or update relevant design/vision/strategy docs (see /docs/planning/ and /docs/design-docs/) for each step
    - Break down large tasks into subtasks with clear acceptance criteria
    - Document decisions, blockers, and integration points
    - Maintain modularity, clarity, and traceability throughout
    - Integrate and maintain a simple but effective testing solution (scripts or automated tests) for all core features
    - Testing is a required subtask for each phase—always verify before moving on

---

## Phase 1: Foundation (COMPLETE)
- [x] Embedding proxy service (SentenceTransformers, OpenAI-compatible)
- [x] Vector search pipeline (Neo4j, Qdrant, Graphiti)
- [x] Ingestion, search, and end-to-end testing
- [x] Dockerized services
- [x] Documentation for setup and usage

---

## Phase 2: Unified Model Management & Web Interface (Prioritized by Dependency)
- [x] **Design/spec model catalog API (local + Hugging Face/remote)** _(see [Model Catalog API Design](../design-docs/MODEL_CATALOG_API_DESIGN.md))_
    - [x] Acceptance Criteria: Lists local and remote models with metadata (name, type, desc, size, status)
    - [x] Subtasks: Research Hugging Face API, draft OpenAPI spec, define schema, link to design doc
- [x] **Implement API endpoints for install/list/switch (embedding & LLM models)**
    - [x] Acceptance Criteria: Endpoints work for local/remote models, clear error/status reporting
    - [x] Subtasks: Implement endpoints, test with multiple model types (see `test_model_catalog.py` for coverage)
    - [x] Tests: All error/status scenarios are covered and passing
- [x] **Enable shared model storage across containers/projects**
    - [x] Acceptance Criteria: Models persist across container rebuilds, can be shared by multiple projects
    - [x] Subtasks: Docker volume config, test persistence, document setup
- [x] **Build web UI for model management, testing, and switching**
    - [x] Acceptance Criteria: Can view/install/switch models, run embedding/LLM tests from browser
    - [x] Subtasks: UI for model selection, install, status; integrate test tools; document usage
- [ ] **Integrate and test with Obsidian markdown vault**
    - [ ] Acceptance Criteria: Can ingest/test markdown from Obsidian vault
    - [ ] Subtasks: Build/test ingestion script for markdown, expose via web UI, document workflow
- [ ] **Q&A over markdown content**
    - [ ] Acceptance Criteria: User can ask questions about ingested markdown and get semantic answers
    - [ ] Subtasks: Add Q&A UI, connect to search/LLM backend, test with sample queries
- [ ] **System health dashboard in web UI**
    - [ ] Acceptance Criteria: Can view status of all core services (embedding proxy, vector DB, LLMs, etc.)
    - [ ] Subtasks: Implement health checks, display status in UI, add alerts for failures
- [ ] **Document model management features and usage**
    - [ ] Acceptance Criteria: Clear docs for all new features, with screenshots/examples
    - [ ] Subtasks: Update README, add web UI usage guide, link to design docs

---

## Phase 3: LLM Integration & Task Routing (Reordered for Dependency)
- [ ] **Design/spec LLM integration architecture**
    - [ ] Acceptance Criteria: Clear plan for local/API LLM integration, task routing logic, security
    - [ ] Subtasks: Research LLM APIs (Ollama, LM Studio, OpenAI, Anthropic), draft spec, link to design doc
- [ ] **Implement LLM integration (local and API-based)**
    - [ ] Acceptance Criteria: Can run LLMs locally or via API, switch between them, secure config
    - [ ] Subtasks: Implement adapters, test with multiple providers
- [ ] **Implement task router for embedding vs. LLM requests**
    - [ ] Acceptance Criteria: System can route requests to correct model/service based on task
    - [ ] Subtasks: Implement routing logic, add tests, document
- [ ] **Add prompt engineering and chunking for long docs**
    - [ ] Acceptance Criteria: Can handle long documents, advanced prompting
    - [ ] Subtasks: Implement chunking logic, prompt templates, test
- [ ] **Extend UI: chat with data, Q&A, rewriting, summarization**
    - [ ] Acceptance Criteria: User can interact with all LLM features via web UI
    - [ ] Subtasks: UI features, connect to backend, test
- [ ] **Document LLM integration and usage patterns**
    - [ ] Acceptance Criteria: Clear docs, usage examples, troubleshooting
    - [ ] Subtasks: Update README, add LLM usage guide, link to design docs

---

## Phase 4: Advanced Features & Multi-Modal Support (Reordered for Dependency)
- [ ] **Design/spec analytics dashboard and visualizations**
    - [ ] Acceptance Criteria: Clear plan for analytics, visualizations, data sources
    - [ ] Subtasks: Draft dashboard spec, define metrics, link to design doc
- [ ] **Build analytics dashboard (usage, resource, trends)**
    - [ ] Acceptance Criteria: Dashboard displays real-time and historical data
    - [ ] Subtasks: Implement backend, frontend, test
- [ ] **Add visualizations (character arcs, entity networks, etc.)**
    - [ ] Acceptance Criteria: Can visualize key data relationships
    - [ ] Subtasks: Implement graphing, integrate with dashboard, test
- [ ] **Implement multi-modal support (images, audio, etc.)**
    - [ ] Acceptance Criteria: Can ingest/search non-text data
    - [ ] Subtasks: Research libraries, prototype, document
- [ ] **Add notification and automation features**
    - [ ] Acceptance Criteria: System can alert users, trigger workflows
    - [ ] Subtasks: Implement notification logic, UI, test
- [ ] **Document advanced features and onboarding**
    - [ ] Acceptance Criteria: Clear docs, onboarding for new users
    - [ ] Subtasks: Update README, add onboarding guide, link to design docs

---

## Phase 5: Portability & Integration (Reordered for Dependency)
- [ ] **Design/spec single-container deployment and integration**
    - [ ] Acceptance Criteria: Plan for Dockerization, shared storage, import/export
    - [ ] Subtasks: Draft Docker spec, define volume strategy, link to design doc
- [ ] **Ensure all features run in a single Docker container**
    - [ ] Acceptance Criteria: All core features available in one container
    - [ ] Subtasks: Dockerfile update, compose config, test
- [ ] **Support volume mounts/shared model/data storage**
    - [ ] Acceptance Criteria: Model/data persists, can be shared by projects
    - [ ] Subtasks: Docker volume config, test, document
- [ ] **Build import/integration scripts for other projects**
    - [ ] Acceptance Criteria: Easy to integrate with other systems
    - [ ] Subtasks: Script dev, test, document
- [ ] **Finalize documentation and onboarding for all users**
    - [ ] Acceptance Criteria: Clear, complete docs for all user types
    - [ ] Subtasks: Update README, onboarding, link to design docs

---

## Stretch Goals

### GPU Cloud Integration (Future Enhancement)
- [ ] **Acceptance Criteria:**
    - Can offload heavy LLM/embedding tasks to a cloud GPU provider (e.g., RunPod, Lambda, AWS, GCP, Paperspace, vast.ai)
    - Secure, configurable, and cost-controlled integration
    - Seamless switching between local and cloud compute as needed
    - Clear documentation and UI for managing cloud resources
- **Subtasks:**
    - [ ] Research and compare GPU cloud providers (cost, API, security)
    - [ ] Prototype remote inference with at least one provider
    - [ ] Add config/UI for selecting local vs. cloud execution
    - [ ] Implement authentication and cost controls
    - [ ] Document setup, usage, and best practices
- **Best Practices:**
    - Always prioritize privacy and cost transparency
    - Make cloud integration optional and user-controlled
    - Monitor usage and provide alerts for unexpected costs
    - Update all relevant docs and onboarding materials

---

**NOTE:** Once all design docs and planning are complete, start a new chat/session to reset the context window for implementation.

---

## Instructions for New AI Assistants or Team Members
1. **Read this checklist and the strategy/vision docs.**
2. **Pick the first unchecked item in the current phase.**
3. **Review related files and requirements.**
4. **Propose a plan and execute the next step.**
5. **Update this checklist and add notes/links as you go.**

---

*This file is your single source of truth for project progress and onboarding. Always update it as you work!*