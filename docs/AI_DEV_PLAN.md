# AI Starter Kit: Web App & Backend Integration – Development Plan

> **Note:** This document was originally created for the Rust frontend app, but the project has transitioned to a web app. All concepts are retained, but the target platform is now a web interface.

**See also:**
- [SYSTEM_OVERVIEW.md](SYSTEM_OVERVIEW.md)
- [AI_FRIENDLY_PIPELINE_OVERVIEW.md](AI_FRIENDLY_PIPELINE_OVERVIEW.md)
- [README_GRAPHITI_LOCAL.md](README_GRAPHITI_LOCAL.md)
- [CSA Reference](CSA.md)


## Purpose
This document tracks the autonomous development and diagnostic work on the AI Starter Kit project, specifically focused on the Rust frontend app and its integration with the backend (Graphiti or compatible). It is designed so that progress, findings, and next steps are always documented and recoverable, even if the session is interrupted or restarted.

---

## Current Focus
- Enable fully automated, headless testing of the Rust frontend app's integration with the backend, **without requiring manual UI or user intervention**.
- Diagnose and resolve backend availability or error issues that prevent successful integration tests.
- Lay groundwork for robust, repeatable development and testing workflows.

---

## Task Checklist

### 1. Project & Problem Recap
- [x] Review project structure and Rust frontend app
- [x] Identify current integration test (`integration_search.rs`) and its requirements
- [x] Attempt to run integration test headlessly
- [x] Observe backend 500 error

### 2. Backend Diagnostics & Automation
- [x] Check if backend service is running on `localhost:9003`
- [x] If not running, identify how to start backend (Docker, script, etc.)
- [x] Attempt to start backend automatically
- [x] Once running, verify `/search` endpoint health
- [x] Re-run integration test and confirm success
- [ ] Once running, verify `/search` endpoint health
- [ ] Re-run integration test and confirm success

### 3. Test Robustness
- [ ] If backend cannot be started, create a mock/dummy backend for test purposes
- [ ] Improve error output and diagnostics in integration tests

### 4. Automation & Documentation
- [ ] Propose or implement a script or CI workflow for automated integration testing
- [ ] Update this document with progress and findings as tasks are completed

---

## Progress Log
- **2025-04-20:**
    - Integration test runs but fails due to backend 500 error.
    - Next: Diagnose backend status and try to start/fix it.

---

## How to Resume Work
1. Review this document for current status and completed steps.
2. Continue with the next unchecked item in the checklist.
3. Update this document as progress is made.

---

## Notes
- This plan is meant to be living and updated as work progresses.
- If you restart or lose context, always check this file first!
