# Semantic System Development Guide

## Introduction

This guide outlines the development process, documentation standards, and best practices for all contributors working on the Semantic System project. It's designed to help maintain consistency, quality, and clear documentation throughout development.

## Single Source of Truth

The project maintains these authoritative documents:

1. **Master Checklist** (`/docs/planning/SEMANTIC_SYSTEM_MASTER_CHECKLIST.md`):
   - Contains all project phases with detailed acceptance criteria
   - Tracks progress with checkboxes
   - Lists next steps and implementation details
   - **Always consult this document first to understand project status**

2. **Documentation Index** (`/docs/README.md`):
   - Central navigation for all project documentation
   - Organized by documentation category

3. **Project Status** (`/docs/planning/PROJECT_STATUS.md`):
   - Running operational log of project state
   - Documents decisions, blockers, and their resolutions

## Getting Started

If you're new to the project:

1. Start with the master checklist to understand project status and phases
2. Review the documentation index to find relevant documentation
3. Identify the current phase (first phase with unchecked items)
4. Begin with the first unchecked item in the current phase

## Documentation Structure

```
/docs/
  ├── README.md (central index)
  ├── planning/
  │   ├── SEMANTIC_SYSTEM_MASTER_CHECKLIST.md
  │   ├── SEMANTIC_SYSTEM_STRATEGY.md
  │   ├── SEMANTIC_SYSTEM_FULL_VISION.md
  │   └── PROJECT_STATUS.md
  ├── design-docs/
  │   └── (API designs, component specs)
  ├── onboarding/
  │   └── (system overviews, introductions)
  ├── guides/
  │   └── (how-tos, technical guides)
  └── graphiti/
      └── (component-specific docs)
```

## Development Workflow

### Before Starting
- Review the master checklist to identify current phase and next steps
- Check acceptance criteria for your task
- Review/create design docs if needed

### During Implementation
- Follow subtasks in order of dependency
- Document decisions and integration points
- Write tests for all features

### After Each Step
- Run appropriate tests
- Fix failing tests before proceeding
- Update the master checklist with progress

## Testing Requirements

- Unit tests for all components
- Integration tests for API endpoints
- End-to-end tests for user-facing features
- Never proceed if tests are failing

## Maintaining Documentation

- Add design docs to `/docs/design-docs/`
- Add guides to `/docs/guides/`
- Add overviews to `/docs/onboarding/`
- Always update the central README.md
- Cross-link related documents

## Handover Process

When handing over to another contributor:
- Update all documentation
- Summarize progress in PROJECT_STATUS.md
- Clearly mark next steps in the master checklist

---

**Remember**: Always refer to the master checklist first to understand project status and next steps.