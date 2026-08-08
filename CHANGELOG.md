# Changelog

## Unreleased
### Added
- English-only repository documentation policy.
- `11_TOOLS/check_english_docs.py` and CI guard to reject Arabic/Persian-script or Cyrillic text in tracked documentation.

### Changed
- All persisted documentation, templates, SOPs, checklists, examples, project handoffs, feedback logs, and historical operational notes are canonicalized to English.
- Non-English user feedback is stored as English translation/paraphrase when persistence is required.

## 1.3.0
### Added
- `00_SYSTEM/MEDIA_PROXY_PIPELINE.md` for low-resolution image/video proxy persistence.
- `11_TOOLS/media_proxy.py` for WebP and H.264/MP4 proxy generation.
- Project-level `19_HANDOFF_ASSETS/git_previews/` and `proxy_manifest.json` for visual memory across chats.

### Changed
- Default storage for non-sensitive meaningful media moved from metadata-only to `git_previews`; original/full-resolution media remains outside normal Git.
- `.gitignore` re-includes only standard proxy-path WebP/MP4 while continuing to exclude normal heavy media.
- Default image proxy: long edge <=1280, WebP quality about 72, metadata stripped.
- Default video proxy: H.264 MP4, long edge <=1280, about 24fps, CRF about 30, AAC about 96kbps when retained.
- `AGENTS.md`, `AI_START_HERE.md`, project templates, and P0001 handoff rules integrate proxy generation/manifest/commit into cross-chat persistence.

### Safety
- Low-resolution media in a public repository is still public. Sensitive/client/confidential/`do_not_publish` media remains metadata-only unless a safe explicit storage mode is chosen.

## 1.2.0
### Added
- `SCENARIO_ARCHITECTURE_SYSTEM.md` for adaptive 10/20/30/40-second and 1–4-clip scenario proposals.
- `PRM-SCN-ARCH-001_v1.0.0` candidate prompt for Process State Map + duration viability + Scenario Architecture Menu.
- Multi-clip Master Sequence / Clip Contract templates and explicit 2/3/4-clip support.
- P0001 30s derivative new-chat handoff.

### Changed
- Scenario generation became Process State Map + Capacity Assessment + Duration Viability + adaptive menu rather than a fixed idea quota.
- Hybrid architecture documented as a strong candidate for many multi-clip sequences, not a mandatory default.
- Per-clip reference stacks should be minimum sufficient and role-clean; filling slots is not an objective.
- Real product process must be verified/user-confirmed or clearly labeled creative metaphor.

### Project evidence
- P0001 showed that more references do not always improve scene synthesis and that scene-master-derived adjacent camera states can improve continuity. These remain scoped/provisional learnings unless promoted by further evidence.

## 1.1.0
### Added
- First real project `P0001_truffle_chocolate` with brief, provenance, source-prompt analysis, identity, reference strategy, prompt packages, evaluations, and handoff.
- Google Flow / Gemini Omni Flash tool knowledge and operational seven-reference budget observation.
- OBS/HYP/EXP records for reference-budget and separate-vs-collage strategy.

### Changed
- Reference-image production favors one target view per Run and single-purpose clean references.
- Operational Omni ingredient budget target: up to seven, often 4–6 with reserved slots when feasible.

## 1.0.0
### Added
- Core AI Video Ad Lab architecture, 24-stage workflow, SOPs/checklists/templates, registries, learning loop, and CLI helpers.
- AI/session context recovery, handoff protocol, and repository-based durable memory.

### Architecture change
- System evolved from Codex-specific assumptions to AI-operator architecture with ChatGPT as current primary operator. This is a design decision based on the user’s operating requirements, not a benchmark claim.
