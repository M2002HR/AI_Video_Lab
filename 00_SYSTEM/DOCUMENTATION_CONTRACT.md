# Documentation Contract

This is a system rule, not a suggestion. No knowledge that matters for reproduction, comparison, cross-chat continuation, or system improvement may remain only in conversation.

## Core rule
**If a decision, input, output, failure, feedback item, prompt, tool change, workflow change, creative selection, QA result, or learning can affect a future execution, it must be recorded in the repository.**

Chat is the working interface; the repository is durable memory.

## Mandatory records
### Project state
- brief and deliverable;
- original inputs and provenance;
- assumptions and uncertainty;
- current stage, blockers, and next action;
- approved/selected assets and rationale.

### Generation
- full prompt actually used;
- prompt ID/version/status when canonical;
- tool/model/settings when known;
- ingredient/reference list and explicit role of each reference;
- every meaningful Run;
- selected outputs and failed outputs that provide useful evidence.

### Evaluation
- rubric scores;
- failure tags;
- comparisons;
- pass/fail gate decisions;
- selection rationale.

### Learning and change
- important user feedback translated into English if necessary;
- observations;
- hypotheses;
- experiments;
- validated learnings;
- prompt/SOP/checklist/tool changes;
- evidence and rationale for changes.

## Workflow discovery must also be documented
If production reveals the need for a new stage, checklist, decision rule, naming rule, continuity rule, prompt-writing rule, or workflow branch, that need is evidence. Record it at project level and promote it to system documentation when reusable and sufficiently supported.

## Documentation self-check
Before completing meaningful work, the operator must ask:
1. What was produced or decided?
2. What still exists only in chat?
3. Is it project-local or system-reusable?
4. Must `STATUS.md` or `HANDOFF.md` change?
5. Is a Run/Prompt/Observation/Hypothesis/Decision record required?
6. Must registry/dashboard/checklists be synchronized?
7. Is required media proxy persistence complete?

If any required record is missing, the task is not complete.

## Recording levels
- **Run-level** — every meaningful generation, prompt, final decision, and approval.
- **Project-level** — feedback, creative choices, failure patterns, workarounds, and context needed to continue the project.
- **System-level** — reusable rules or methods. Begin as observation/hypothesis when evidence is limited; promote under Evidence/Change policy.

## What not to record
- social conversation with no project impact;
- exact repetition of information already authoritative in the repository;
- transient speculation that does not affect decisions;
- scratch reasoning that creates no evidence or operational output.

## Cross-chat completeness
After a milestone, a fresh ChatGPT session should be able to read `AI_START_HERE.md`, project `STATUS.md`, project `HANDOFF.md`, relevant evidence, and active-stage documents and understand the project goal, approvals, failures, active prompt/reference plan, important learnings, and exact next action without asking the user to recount prior history.

## Definition of Done for documentation
A milestone is done only when its output/decision is recorded, provenance is traceable, status/handoff are synchronized when necessary, important learning is not chat-only, system-level changes follow governance, and a new session can recover the required context.

## English-only persistence policy
All persisted repository text must be English: Markdown, text, JSON string values, YAML, CSV notes, prompts, templates, examples, comments, feedback logs, handoffs, and change history. If source material or user feedback is non-English, persist an English translation/paraphrase rather than the non-English text. User-facing chat language is independent of this repository rule.

Run `python 11_TOOLS/check_english_docs.py` before declaring repository language compliance complete. The GitHub Actions English-only audit is manual-only by design to avoid routine notification noise. When explicitly dispatched, it must pass with zero forbidden-script violations.
