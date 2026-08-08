# DEC-0002 — Sequential Stage Gates Are Mandatory

Status: active
Decision date: 2026-08-08
Scope: system-wide production workflow

## Context
A new project session received a product image plus a complete source/template video prompt. The operator correctly created a separate project and performed useful intake/source/product analysis, but then incorrectly treated the completeness of the source prompt as permission to create and activate a final Gemini video prompt in the same pass.

This skipped the reference-readiness, creative/scenario, storyboard/keyframe, and preflight gates and produced a next action that asked the user to generate the final video immediately.

The user explicitly requires the lab to work methodically and visibly, stage by stage, so each reference, creative decision, storyboard/keyframe, and final prompt is built and QA'd before downstream generation.

## Options considered
1. Keep Fast Start broad and rely on operator judgment.
2. Add a project-specific warning only for the affected project.
3. Make sequential stage gates a mandatory system rule and add anti-jump checks to all new-project entry points.

## Decision
Adopt option 3.

`00_SYSTEM/SEQUENTIAL_STAGE_GATE_PROTOCOL.md` is now mandatory for every real production project.

A source/template prompt is an analysis input, not permission to skip stages. Fast Start may accelerate initialization but must stop at the earliest real incomplete gate. Final video prompting may only become active after the relevant upstream gates pass.

When an operator needs user-generated external media, it should request only the generation belonging to the current stage, wait for the output, QA it, record it, and then advance.

## Handling previous premature artifacts
Do not delete them. Preserve exact historical artifacts, mark them `premature_draft` / inactive, clear active downstream pointers, roll the project back to the earliest incomplete gate, and continue sequentially.

## Evidence
- P0002 was initially set to `STAGE_11` with a Gemini video package as the immediate next action despite no P0002 Reference QA or storyboard/keyframe gate.
- User feedback on 2026-08-08 explicitly rejected this behavior and required complete step-by-step progression.

## Consequences
Positive:
- fewer hidden assumptions;
- fewer contaminated or under-conditioned final prompts;
- clearer user control at meaningful milestones;
- stronger provenance and QA;
- better cross-chat continuation.

Cost:
- more intermediate steps and potentially more turns before final generation.

This cost is intentional because the lab optimizes for reliable, reusable production quality rather than fastest possible prompt dumping.

## Review condition
Revisit only if repeated project evidence shows a specific class of work can safely collapse stages without harming identity, continuity, or user control. Any such exception must be explicit and evidence-backed; it must not silently weaken the default rule.
