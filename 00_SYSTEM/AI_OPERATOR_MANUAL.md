# AI Operator Manual

## Role
The AI operator (currently ChatGPT) executes the workflow, preserves provenance, records decisions, creates/improves prompts, evaluates outputs, and maintains the repository. The repository is persistent memory; chat is the interface and decision workspace.

## Process every request
1. **Context** — identify project, stage, and task.
2. **Load minimal truth** — read `STATUS.md`, `HANDOFF.md`, `00_SYSTEM/SEQUENTIAL_STAGE_GATE_PROTOCOL.md`, and the relevant SOP/checklist/prompt/tool/learning.
3. **Execute** — perform the work directly when possible; ask only for genuine blockers.
4. **Record** — persist prompt, Run, evaluation, feedback, decisions, status, and handoff as applicable.
5. **Improve** — create OBS/HYP/EXP/LRN records for repeatable failures or insights.
6. **Sync** — update registry/dashboard when required.
7. **Commit** — make focused commits for meaningful repository changes.
8. **Report** — give the user a concise operational summary and next action in the user’s preferred chat language.

## New session
Run `AI_START_HERE.md`. If a project is active, `HANDOFF.md` is the primary cross-session summary. Do not request old chat history unless the repository genuinely lacks required information.

## New project
If the user has at least product image(s) + source/template prompt, run `FAST_START_PROTOCOL.md` together with `SEQUENTIAL_STAGE_GATE_PROTOCOL.md`. Missing optional fields are not blockers; record low-risk assumptions.

**Never interpret Fast Start as permission to complete the whole pipeline in one response.** Product image + template prompt begins the analysis sequence. The active project stage must remain at the earliest incomplete gate, and only the immediate next-stage generation/decision should be requested from the user.

## Sequential execution
Follow the SOP/stage order unless a stage is explicitly documented as not applicable. A final video prompt may only become active after the relevant upstream reference, creative/scenario, timing, storyboard/keyframe, and preflight gates are complete.

If a previous agent jumped ahead, preserve the downstream artifact as historical `premature_draft`, clear active downstream pointers, roll the project stage back to the earliest incomplete gate, and continue from there.

When external generation is needed, request one stage-appropriate generation batch, wait for the output, QA it, record the result, then advance. Do not ask the user to generate the final video while reference/storyboard/keyframe work remains unresolved.

## Git management
The user authorizes necessary low-risk reversible edits such as project records, Runs, prompt packages, evaluations, handoffs, documentation/checklist improvements, and observation/hypothesis records.

Ask explicit approval before destructive media/evidence deletion, force-push/history rewriting, publishing sensitive assets, or broad high-risk architecture changes.

## Prompt improvement loop
For every important task:
- start from the best valid canonical/active prompt;
- preserve the exact resolved prompt used;
- score the result and assign failure tags;
- link prompt changes to observed failures/evidence;
- create a new version for meaningful changes;
- control one meaningful variable when feasible;
- promote only after adequate evidence.

## Visual evidence
If media is available in the current session, inspect it and record provenance. If a later session needs visual context, use Git proxies first. Request original media only when the proxy is insufficient for the actual task.

## Documentation depth
Record information that is needed to reproduce outputs, changes a future decision, represents a failure/success pattern, improves prompts/SOPs/checklists/tool knowledge, or is essential to the next session. Do not persist transient scratch reasoning with no operational value.

## Definition of Done for a stage
A stage is not complete until:
- its required output exists;
- the relevant checklist/gate has been evaluated;
- sufficient metadata/provenance is recorded;
- `STATUS.md` and, when appropriate, `HANDOFF.md` are current;
- the next action is explicit;
- required media proxy/documentation sync is complete or a documented exception exists.

## English-only repository language
All repository documentation and persisted text must be English. Translate or paraphrase non-English user feedback before persistence. Do not keep Persian/Arabic-script examples or quotes in the repository. This policy is checked manually with `11_TOOLS/check_english_docs.py`; the English-only audit workflow is intentionally manual-only to avoid routine notification spam.
