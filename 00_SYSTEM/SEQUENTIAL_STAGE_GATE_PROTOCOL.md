# Sequential Stage-Gate Protocol

This protocol is mandatory for every real production project. It exists to prevent an AI operator from jumping from intake directly to a final video-generation prompt.

## Core rule
A source/template prompt is an input to analyze and adapt. It is **not** permission to skip production stages.

Do not move directly from product image + source/template prompt to a final video prompt or final video generation.

The project must advance through the relevant stages in order, with explicit evidence that each gate is complete. A stage may be lightweight when the task is simple, but it may not be silently skipped.

## Canonical stage order
Use the SOP sequence in `01_SOPS/INDEX.md` as the default production path:

1. Project intake.
2. Source prompt analysis.
3. Product identity extraction and identity lock.
4. Reference strategy.
5. Reference generation or cleanup when needed.
6. Reference QA and selection.
7. Creative direction.
8. Scenario generation / architecture when applicable.
9. Scenario selection.
10. Shot timing / timeline.
11. Storyboard design.
12. Storyboard QA.
13. Keyframe generation when useful for the target model/workflow.
14. Keyframe QA and continuity gate.
15. Final video-prompt construction.
16. Video preflight.
17. Video generation.
18. Video QA.
19. Repair / iteration decision.
20. Final selection.
21. Post-production when needed.
22. Final QA.
23. Postmortem and system learning.

Not every project requires heavy artifacts at every stage, but the operator must explicitly record why a stage is not applicable before advancing.

## Hard gates

### Gate A — Intake and understanding
Before any external generation, complete at least:
- immutable input/provenance record;
- source/template KEEP / ADAPT / REMOVE analysis;
- product identity extraction;
- identity lock;
- current uncertainties and contamination risks.

The first user-facing production response should report these findings and the next stage. It must not present a final video-generation prompt.

### Gate B — Reference readiness
Before creative scene synthesis, storyboard, keyframes, or final video prompting:
- define the reference roles;
- decide which references are truly needed;
- generate/clean references if needed;
- QA each candidate;
- select approved references with explicit authority boundaries.

If the original product image contains distracting background, watermark, bad angle, insufficient detail, or identity ambiguity, resolve those issues first rather than hoping the final video model will ignore them.

### Gate C — Creative and scenario lock
Before storyboard or final video prompting:
- define the creative mechanism/direction;
- adapt the source template to the actual product;
- remove source-product leakage;
- present or record meaningful scenario choices when the direction is not already truly locked;
- select/approve the scenario;
- create the shot/timing structure.

A source template can strongly constrain the direction, but it still must be analyzed and translated into a product-specific scenario before downstream prompting.

### Gate D — Visual continuity readiness
Before final video prompting, when the workflow benefits from visual anchors:
- create storyboard/keyframe plan;
- generate the minimum necessary keyframes/scene anchors;
- QA product identity, composition, character/object count, scale, props, and continuity;
- reject contaminated or drifted anchors;
- select the scene/keyframe set that will actually condition the video model.

Do not independently regenerate every frame if a stable scene master can be conservatively derived into multiple camera states.

### Gate E — Final prompt readiness
Only after prior relevant gates pass:
- construct the final model-specific video prompt;
- define reference stack and authority order;
- run preflight;
- tell the user exactly what to upload and what prompt to run.

A final video prompt created before these gates is a **premature draft**, not an active generation package.

## User interaction rule
For a new project, work in visible milestones. Do not dump the entire pipeline into one answer.

Default milestone rhythm:
1. intake + source analysis + product identity;
2. reference plan and reference-generation/cleanup task;
3. reference QA and selection;
4. creative/scenario decision;
5. storyboard/keyframe work;
6. final video prompt + preflight;
7. video QA + iteration.

After each milestone, give the user the exact next action. When an external image/video generation is required, request only that generation and wait for the result before advancing.

## Anti-jump checks
Before writing or activating any `VIDEO` prompt package, verify all of the following:
- current project stage is actually ready for video prompting;
- source prompt analysis exists;
- identity lock exists;
- approved reference strategy exists;
- required reference QA is complete;
- scenario is selected;
- timeline is selected;
- required storyboard/keyframe gate is complete or explicitly marked not applicable with rationale;
- no unresolved blocker from `STATUS.md` or `HANDOFF.md` contradicts video generation.

If any item fails, stop and continue from the earliest incomplete stage.

## Handling premature work
If an earlier agent already created downstream artifacts too early:
- do not delete historical files;
- mark them `premature_draft` / `not_active`;
- roll the active project stage back to the earliest incomplete gate;
- clear downstream pointers such as `active_video_prompt_package` until the gates are passed;
- preserve the draft only as historical material that may be reworked later.

## Fast Start interpretation
`FAST_START_PROTOCOL.md` accelerates setup and documentation. It does **not** collapse the production pipeline. Fast Start may initialize later-stage folders, but it must leave the project at the earliest real incomplete gate and only prepare the next immediate task.
