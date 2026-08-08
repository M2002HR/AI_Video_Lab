# AI Operator Rules

This repository is persistent memory and the source of truth for AI Video Ad Lab. ChatGPT is the current primary operator, but these rules apply to future AI agents as well.

## Start every new chat/session
1. Read `AI_START_HERE.md` first.
2. Then read `START_HERE.md`, `DASHBOARD.md`, and `00_SYSTEM/INDEX.md`.
3. Read `00_SYSTEM/SEQUENTIAL_STAGE_GATE_PROTOCOL.md` before starting or advancing a real production project.
4. For an active project, read its `project.json`, `STATUS.md`, and `HANDOFF.md` before doing work.
5. Load only the SOP, checklist, prompt, tool knowledge, and learnings relevant to the current stage.
6. Never treat chat history as durable memory; important decisions, feedback, outputs, and learnings belong in the repository.

## Non-negotiable rules
- Never overwrite original inputs, historical Runs, or historical prompt versions.
- Every meaningful AI generation must have traceable provenance.
- Every reference must have an explicit role; product identity has priority over style.
- A single experience is normally an observation, not a universal rule.
- Promote canonical prompts/workflows/rubrics/checklists/tool recommendations only through evidence and `CHANGE_PROMOTION_POLICY.md`.
- Unknown values are `unknown`/`null`; do not invent them.
- Separate vendor claims from internal evidence.
- After meaningful changes, sync metadata/registries/dashboard and check integrity.
- Anything needed for reproduction, comparison, cross-chat continuation, or system improvement must be persisted under `00_SYSTEM/DOCUMENTATION_CONTRACT.md`.
- Documentation itself is part of Definition of Done.
- When a new workflow branch, checklist need, naming rule, or reusable process is discovered, record project evidence first and promote it to system documentation when justified.
- **Never jump from product image + source/template prompt directly to a final video prompt.** Follow `00_SYSTEM/SEQUENTIAL_STAGE_GATE_PROTOCOL.md` and the ordered SOP stages.
- A downstream prompt/package created before its upstream gates pass is historical `premature_draft`, not an active package.
- When external generation is required, ask for only the generation belonging to the current stage, then wait for and QA the result before advancing.

## Scenario routing
If scenario/duration/clip count is not locked, run `00_SYSTEM/SCENARIO_ARCHITECTURE_SYSTEM.md` and `01_SOPS/SOP_07_SCENARIO_GENERATION.md` first. Candidate count is adaptive; no filler options.

For 2, 3, or 4 clips, read `00_SYSTEM/MULTI_CLIP_ARCHITECTURE.md` and `01_SOPS/SOP_MULTI_CLIP_SEQUENCE.md`; create the Master Sequence, Clip Contracts, and boundary contracts before per-clip heavy prompting.

## Media persistence
- Chat attachments do not automatically become repository binaries.
- Default for non-sensitive locally accessible meaningful media is `git_previews`.
- Create low-resolution proxies under `19_HANDOFF_ASSETS/git_previews/` and sync `proxy_manifest.json`.
- Full-resolution originals do not enter normal Git by default; proxies use `source_of_truth=false`.
- Sensitive, confidential, client, or `do_not_publish` media remains metadata-only unless a safe explicit storage mode is selected.
- Lower quality does not make public-repository media private.
- Never claim a proxy was committed if binary upload capability was unavailable.

## GitHub change permission
The user authorizes necessary, low-risk, documented, reversible repository changes and commits during production. Use focused readable commits. Ask explicit approval before destructive deletion, history rewriting/force push, publishing sensitive data, or other high-risk architectural changes.

## Language policy
**All persisted repository text must be English. No Persian/Arabic-script or Cyrillic prose is allowed in documentation, prompts, logs, examples, comments, or metadata.** If the user provides non-English feedback that must be preserved, store an English translation/paraphrase and mark it as translated if relevant. User-facing chat may remain in the user’s preferred language.

Run `python 11_TOOLS/check_english_docs.py` manually when an English-language audit is needed. The audit workflow is intentionally manual-only and must not be re-enabled on every push/PR without a deliberate repository-policy change.

Full operator guidance: `00_SYSTEM/AI_OPERATOR_MANUAL.md`.
