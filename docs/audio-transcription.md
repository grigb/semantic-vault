# Audio Transcription Strategy

## Current Status
- The initial plan was to use Whisper.cpp built locally in a Docker container for speech-to-text (STT).
- Encountered reliability and build issues with Whisper.cpp on ARM64/Mac M1 Docker, causing unpredictable builds and missing binaries.

## Updated Plan
- **Short-term:** Use a third-party speech-to-text API (e.g., OpenAI Whisper API, Google Speech-to-Text, or AssemblyAI) for audio transcription during development and early production.
- **Long-term:** Once usage grows and API costs become significant, revisit local model deployment (e.g., Whisper.cpp or other on-prem solutions) and invest in a robust, reproducible container build process.

## Rationale
- Third-party APIs are fast to integrate, reliable, and cost-effective at low-to-moderate scale.
- Local models are preferred for privacy/cost at scale, but require more engineering investment for reproducibility and maintenance.

## Action Items
- Remove Whisper.cpp Docker build from the critical path for now.
- Integrate a third-party STT API and document usage.
- Track API usage/costs and revisit local deployment when justified.

## Notes
- If privacy or data residency is a concern, prioritize local solutions sooner.
- Document all API keys and configuration in a secure location.

---

_Last updated: 2025-04-26T19:46:09-06:00_
