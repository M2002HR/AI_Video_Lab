# Chat Continuity Protocol

Goal: any project can continue across independent chat sessions without depending on conversation memory.

## Three context layers
1. System rules: `AI_START_HERE.md`, `AGENTS.md`, system/SOP/checklist docs.
2. Project current state: `project.json`, `STATUS.md`, `HANDOFF.md`.
3. Evidence/history: Runs, prompt packages, evaluations, conversation logs, proxy media, learnings.

## `HANDOFF.md` must include
- project and deliverable;
- current stage;
- latest approved decisions/assets;
- product identity summary and authoritative spec path;
- approved references;
- selected scenario/keyframes/prompt package;
- important recent Runs/results;
- known failures;
- important translated user feedback;
- blockers;
- exact next action;
- media availability and whether any original must be re-attached.

`HANDOFF.md` is an operational summary, not a replacement for authoritative source files.

## Conversation log
`18_CONVERSATION_LOG/` stores only durable-value context such as important translated feedback, session summaries, and decisions/preferences that affect production. Do not store full transcripts unless there is a specific reason.

## End of a meaningful session
1. Register Runs/prompts/evaluations.
2. Record important feedback.
3. Sync `STATUS.md`.
4. Write `HANDOFF.md` so an uninformed AI can continue.
5. Create OBS/HYP records when reusable insight exists.
6. Sync media proxies if required.
7. Commit focused changes.

## Start of next session
Read the repository first. Never ask the user to explain everything again unless a genuine repository gap remains.

## Media limitation
Git metadata alone is not a substitute for visual inspection. Use low-resolution Git proxies for recall/planning. Request original media only when detailed inspection or generation input requires it.
