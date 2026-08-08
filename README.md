# AI Video Ad Lab

AI Video Ad Lab is a local-first, version-controlled production and R&D system for creating AI product advertisements from inputs such as **product images + a source/template prompt**. The deliverable is not only the final media: prompts, checklists, SOPs, failure knowledge, tool knowledge, decisions, and reusable learnings must improve after every project.

## Core structure
- `06_PROJECTS/`: complete project records from intake through final selection and postmortem.
- Every meaningful AI generation is a **Run** with prompt, references, settings, outputs, evaluation, and provenance.
- `02_PROMPT_SYSTEM/`: versioned prompt assets; important prompts are production assets, not disposable chat text.
- `03_TOOL_KNOWLEDGE/`: task requirements are separated from tool choice; recommendations must be evidence-based and revisable.
- `04_CHECKLISTS/`: quality gates that prevent critical production steps from being skipped.
- `07_EXPERIMENTS/`: controlled tests and A/B experiments.
- `09_LEARNING/`: observations, hypotheses, validated learnings, changes, and decisions.
- `10_REGISTRY/`: generated views for projects, Runs, prompts, tools, and learnings.

## ChatGPT as operator
ChatGPT is the current primary workflow operator and the repository is persistent memory. A new chat must not depend on prior chat history. `AI_START_HERE.md` defines context recovery, and every active project maintains `STATUS.md` and `HANDOFF.md`.

## Production cycle
Intake -> source prompt analysis -> product identity -> reference strategy -> creative/scenario architecture -> shot/storyboard/keyframes -> video prompt -> generation -> QA -> selection/post -> postmortem -> system learning.

## Principles
1. Do not overwrite originals or historical Runs.
2. Product identity has priority over style.
3. Separate WHAT the task requires from WHICH TOOL performs it.
4. Do not record tool capabilities as permanent fact without verification/evidence.
5. Failed Runs are evidence and are not deleted merely because they failed.
6. Canonical prompts change only through versioning and evidence.
7. Chat creates decisions; the repository preserves them.
8. Repository documentation and persisted text are English-only.

## Start here
- User/operator entry: `START_HERE.md`
- New AI agent/session: `AI_START_HERE.md`
- System map: `00_SYSTEM/INDEX.md`
- Operator rules: `AGENTS.md` and `00_SYSTEM/AI_OPERATOR_MANUAL.md`

Large media is managed through `00_SYSTEM/STORAGE_POLICY.md`. Metadata, prompts, evaluations, decisions, handoffs, and approved low-resolution proxies must remain versioned so work can continue across sessions.
