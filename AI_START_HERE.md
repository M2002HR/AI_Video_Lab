# AI Start Here

This is the entry point for every new ChatGPT/AI-agent session. The goal is to recover system and project context from the repository without relying on previous chat history.

## System mission
AI Video Ad Lab is a production + R&D system for creating AI advertisements from inputs such as **product images + a source/template prompt**. Final media matters, but so do prompt quality, checklists, SOPs, failure knowledge, tool knowledge, and reusable learning.

## Mandatory context-load protocol
1. Inspect the repository/default branch and current head.
2. Read `AGENTS.md`, `START_HERE.md`, `README.md`, `DASHBOARD.md`, `00_SYSTEM/INDEX.md`, `00_SYSTEM/AI_OPERATOR_MANUAL.md`, and `00_SYSTEM/SEQUENTIAL_STAGE_GATE_PROTOCOL.md`.
3. Inspect `06_PROJECTS/INDEX.md` and/or project registry.
4. If exactly one relevant active project exists, read its `project.json`, `STATUS.md`, `HANDOFF.md`, and files for the current stage without asking for a recap.
5. If several projects are active and user context does not disambiguate, ask only which project is intended.
6. If there is no active project and the user supplied product image(s) + source/template prompt, execute `00_SYSTEM/FAST_START_PROTOCOL.md` **without collapsing or skipping the production stages**.
7. Load only knowledge relevant to the current task; do not summarize the entire repository without purpose.
8. Before continuing, give a short Context Snapshot: project, stage, approved items, blockers, next action.

## Mandatory sequential production rule
A product image + source/template prompt is the **start of analysis**, not authorization to jump directly to a final video prompt.

Advance through the relevant SOP/stage gates in order. At minimum, intake/source analysis/product identity must precede reference work; reference readiness must precede downstream creative conditioning; creative/scenario/timing must precede storyboard/keyframe work; final video prompting is allowed only after the relevant upstream gates pass.

If a previous agent created a downstream artifact prematurely, preserve it as history, mark it inactive/premature, roll the active stage back to the earliest incomplete gate, and continue sequentially.

For the full rules and anti-jump checks, follow `00_SYSTEM/SEQUENTIAL_STAGE_GATE_PROTOCOL.md`.

## Scenario / multi-clip routing
For scenario choice or 10/20/30/40-second work, read `00_SYSTEM/SCENARIO_ARCHITECTURE_SYSTEM.md`, `01_SOPS/SOP_07_SCENARIO_GENERATION.md`, and `04_CHECKLISTS/CHK_SCENARIO_ARCHITECTURE_MENU.md` before storyboard/prompt production.

For 2–4 clips also read `00_SYSTEM/MULTI_CLIP_ARCHITECTURE.md`, `01_SOPS/SOP_MULTI_CLIP_SEQUENCE.md`, and `04_CHECKLISTS/CHK_MULTI_CLIP_CONTINUITY.md`.

The system must build an adaptive Scenario Architecture Menu and present only meaningful candidates. Do not recommend four clips merely because four are supported.

## Fastest new-project input
Required minimum:
- at least one original product image;
- source/template/reference prompt as text or file.

Optional but useful:
- target duration / clip count;
- aspect ratio;
- platform;
- creative constraints;
- style references;
- verified process information.

Record low-risk assumptions and ask only when a decision is genuinely blocking or could waste substantial work.

## Media persistence across chats
For meaningful, non-sensitive media that is locally accessible:
1. record provenance and hash when possible;
2. create a low-resolution proxy using `00_SYSTEM/MEDIA_PROXY_PIPELINE.md`;
3. commit it under `19_HANDOFF_ASSETS/git_previews/`;
4. update `proxy_manifest.json` and `HANDOFF.md` as needed.

Default profiles are WebP up to 1280px long edge at approximately quality 72, and MP4/H.264 up to 1280px long edge at approximately 24fps / CRF 30. Full-resolution originals stay outside normal Git by default. A proxy is not source of truth.

In a new chat, inspect available Git proxies first. Request re-attachment only when original/full-resolution detail is actually required.

## End-of-session protocol
Before leaving an active project after meaningful work:
- update `STATUS.md`;
- update `HANDOFF.md`;
- persist important feedback/decisions in `18_CONVERSATION_LOG/`;
- register new Runs/prompts/evaluations;
- sync required media proxies/manifest or document why metadata-only was used;
- persist reusable workflow discoveries through the Documentation Contract;
- commit meaningful changes.

## English-only repository rule
All persisted repository text must be English. This includes documentation, prompts, templates, examples, comments, handoffs, feedback translations, JSON string values, and operational logs. User-facing chat may use the user’s preferred language. Run `python 11_TOOLS/check_english_docs.py` manually when an English-language audit is needed; the audit workflow is intentionally manual-only to avoid routine notification noise.
