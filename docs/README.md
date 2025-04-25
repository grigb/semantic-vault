# Documentation Index & Navigation Guide

Welcome to the documentation hub for this project. Use this index to find all planning, design, onboarding, guides, and component-specific documentation. Both humans and AI agents should follow this structure for clarity and maintainability.

---

## Directory Structure

- **/docs/planning/** — Project status, checklists, strategy, vision, improvements, and dev plans
  - `PROJECT_STATUS.md` — Operational log and current state (single source of truth)
  - `SEMANTIC_SYSTEM_MASTER_CHECKLIST.md` — Actionable, checkable master checklist
  - `SEMANTIC_SYSTEM_STRATEGY.md` — Build strategy and phases
  - `SEMANTIC_SYSTEM_FULL_VISION.md` — Long-term vision and roadmap
  - `IMPROVEMENTS.md` — System improvement ideas and backlog
  - `AI_DEV_PLAN.md` — Development and integration plan
- **/docs/design-docs/** — All system and component design docs
  - `MODEL_CATALOG_API_DESIGN.md` — Model catalog API design/spec
  - `FRIENDLY_UI_PLAN.md` — Web UI design and UX plan
- **/docs/onboarding/** — Onboarding and high-level system overviews
  - `TEAM_INTRO_TO_SEMANTIC_STACK.md` — Non-technical introduction
  - `SYSTEM_OVERVIEW.md` — System architecture and user workflow
- **/docs/guides/** — How-tos and technical guides
  - `AI_FRIENDLY_PIPELINE_OVERVIEW.md` — Pipeline and retrieval overview
  - `Obsidian Gitcrypt Guide.md` — Obsidian + git-crypt guide
  - `notion-export_ComplexProject.md` — Notion export/ingest guide
- **/docs/graphiti/** — All Graphiti-specific documentation
  - (All files related to Graphiti, e.g., `graphiti_README.md`)
- **/docs/(other-component/)/** — For future major subsystems

---

## How to Add & Maintain Documentation
- Place new design docs in `/docs/design-docs/`.
- Add new planning/status docs to `/docs/planning/`.
- Add onboarding or high-level intros to `/docs/onboarding/`.
- Place guides and how-tos in `/docs/guides/`.
- For component-specific docs, create a subdirectory (e.g., `/docs/graphiti/`).
- Always update this README to keep the index current.
- Cross-link relevant docs for context and onboarding.

## Cursor Rules & Agent Onboarding
- All active cursor rules and agent onboarding docs are in [`/.cursor/rules/`](../.cursor/rules/).
- Agents and new team members should read this index and `.cursor/rules/` first.
- When adding new docs, update both this README and `.cursor/rules/` as needed.

---

If you have suggestions or need to add new docs, please update this README and keep the navigation up to date. For any major changes, update `.cursor/rules/` to guide future agents and contributors.
