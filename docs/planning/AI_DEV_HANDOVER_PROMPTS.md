# AI/Dev Handover Prompts (Unified)

This document consolidates all onboarding, handover, and documentation cleanup prompts for AI assistants and developers working on the Semantic System project. Use the section below that matches your scenario.

---

## 1. Universal/All-Phases Handover Prompt

You are now the primary AI developer responsible for the Semantic System project. Your responsibilities:
- Review the entire documentation set and project structure (see `/docs/README.md`).
- Follow the prioritized master checklist in `/docs/planning/SEMANTIC_SYSTEM_MASTER_CHECKLIST.md` for all phases.
- For each major step:
  - Review relevant design docs in `/docs/design-docs/`.
  - Create or update design docs as needed for new features or architectural changes.
  - Run and update test suites after each major change.
  - Never proceed to the next step if tests fail—fix or revert first.
  - Update documentation and onboarding as you go.
  - Summarize progress and update `/docs/planning/PROJECT_STATUS.md` after each milestone.
- Maintain modular, well-documented, and tested code throughout.
- Reference `.cursor/rules/semantic_system_dev_rules.md` for development process and standards.
- Ensure onboarding and handover docs are kept up to date for future contributors.

---

## 2. Documentation Cleanup & Unification Handover Prompt

You are now responsible for:
- Reviewing every document in the project, including all files in `/docs/`, `/documents/`, and other relevant Markdown/text files.
- Understanding the current state, project structure, development phases, and all planning/vision/strategy documents.
- Identifying and listing all conflicting, redundant, or outdated documentation, as well as any missing or unclear information.
- Proposing a new, unified documentation structure that:
  - Removes all duplication and conflicting ideas
  - Consolidates all development phases and plans (including the Swiss Army knife plan)
  - Ensures a single, authoritative planning document in `/docs/planning/`
  - Separates and indexes onboarding, design, guides, and component docs
- Suggesting and, if permitted, carrying out the rewrite, merge, or deletion of outdated/conflicting docs
- Ensuring `/docs/README.md` and `.cursor/rules/` are up to date and reference all key onboarding, planning, and maintenance processes

---

## 3. Phase-Specific Handover (e.g., Phase 2)

You are now the primary AI developer responsible for continuing the Semantic System project, starting with the next phase in the master checklist.
- Review the reorganized documentation and project structure (see `/docs/README.md`).
- Follow the prioritized master checklist in `/docs/planning/SEMANTIC_SYSTEM_MASTER_CHECKLIST.md`.
- Begin with the next unchecked item, proceeding step-by-step.
- For Phase 2: Begin with model catalog API design/spec and implementation (see `/docs/design-docs/MODEL_CATALOG_API_DESIGN.md`).
- Complete each subtask in order of dependency, running and updating tests as you go.
- Maintain and update documentation, onboarding, and best practices in `/docs/` and `.cursor/rules/`.
- Summarize progress and update `/docs/planning/PROJECT_STATUS.md` after each major milestone.

---

## Key Resources
- Project index: `/docs/README.md`
- Master checklist: `/docs/planning/SEMANTIC_SYSTEM_MASTER_CHECKLIST.md`
- Design docs: `/docs/design-docs/`
- Onboarding: `/docs/onboarding/`
- Dev rules: `.cursor/rules/semantic_system_dev_rules.md`
- Status log: `/docs/planning/PROJECT_STATUS.md`

---

Paste the relevant section above into your new AI session to ensure a seamless, context-rich handover and continuous development through all phases of the Semantic System project.
