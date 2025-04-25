# Semantic System Development Rules & Best Practices

## Purpose
These rules define the core development process, tools, and standards for all contributors (AI and human) working on the Semantic System project. They ensure consistent, high-quality, and maintainable development.

---

## 1. Project Structure & Documentation
- All documentation must reside in `/docs/` and be organized by:
  - `/docs/planning/` for status, checklists, strategy, vision, improvements
  - `/docs/design-docs/` for design/API/component specs
  - `/docs/onboarding/` for onboarding and high-level overviews
  - `/docs/guides/` for how-tos and technical guides
  - `/docs/<component>/` for component-specific docs (e.g., `graphiti/`)
- Always update `/docs/README.md` to reflect the latest structure and navigation.
- Major changes or new workflows must be documented and indexed.

## 2. Development Workflow
- All tasks must be tracked in `/docs/planning/SEMANTIC_SYSTEM_MASTER_CHECKLIST.md`.
- Before starting any new feature or refactor:
  - Review the master checklist, strategy, and relevant design docs.
  - Update or create a design doc in `/docs/design-docs/` if the feature is new or complex.
- After each major step:
  - Run or update the test suite (unit, integration, or E2E as appropriate).
  - Never proceed to the next step if tests fail—fix or revert first.
  - Update the checklist and link to new docs/outputs.
- Always document decisions, blockers, and integration points.

## 3. Coding Standards
- Follow Python best practices (PEP8, type hints, docstrings).
- Keep code modular, readable, and well-commented.
- Prefer explicitness and traceability (clear variable names, commit messages, and PR descriptions).
- Use Docker for all deployable services; ensure portability and reproducibility.
- All model/data storage must be via shared Docker volumes for persistence and multi-project use.

## 4. Testing & Verification
- Testing is a required subtask for each phase—always verify before moving on.
- Maintain a simple but effective test solution (scripts or automated tests) for all core features.
- End-to-end tests must cover ingestion, search, and model management flows.

## 5. Collaboration & Onboarding
- New contributors (AI or human) must:
  - Start with `/docs/README.md` and `.cursor/rules/` for project and process overview.
  - Read onboarding docs and the latest handover (if present).
  - Ask questions or document uncertainties in `/docs/planning/PROJECT_STATUS.md`.
- All onboarding and process rules are to be kept in `.cursor/rules/` and referenced in `/docs/README.md`.

## 6. Security & Privacy
- Never commit secrets, credentials, or sensitive data.
- Use environment variables and `.env.template` for all config.
- Prioritize privacy and cost transparency, especially for cloud/GPU integrations.

---

**For any new process, tool, or best practice, update this file and cross-reference in `/docs/README.md`.**
