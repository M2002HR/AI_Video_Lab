# Fast Start Protocol

Use this when the user wants to begin a real project with minimal friction.

Fast Start accelerates setup, documentation, and the first decision gate. It **does not** skip the production pipeline. Always combine this protocol with `00_SYSTEM/SEQUENTIAL_STAGE_GATE_PROTOCOL.md`.

## Minimum required inputs
1. at least one original product image;
2. one source/template/reference prompt.

Optional information such as project name, duration, aspect ratio, platform, audience, style references, audio, and creative constraints is useful but not automatically blocking.

## Procedure
1. Create a project ID and initialize the project template.
2. Preserve original input provenance and the source prompt as immutable records.
3. Record deliverable, known constraints, unknowns, and low-risk assumptions.
4. Reverse-engineer source/template structure with a KEEP / ADAPT / REMOVE matrix; identify product leakage, contradictions, over-complexity, and tool-specific assumptions.
5. Extract product identity: category, silhouette, geometry/proportions, materials, texture, colors, packaging/components, critical details, natural imperfections, and uncertainty.
6. Create an `identity_lock.md` for downstream prompts.
7. Build an initial reference plan: decide whether the original is sufficient, what cleanup/angles/macro/packaging/scene references are actually necessary, and separate identity references from style references.
8. Initialize/update `project.json`, `STATUS.md`, and `HANDOFF.md`.
9. Stop at the earliest real incomplete gate. Prepare only the immediate next-stage task, prompt package, or decision needed there.
10. Tell the user what was learned and exactly what to do next. If external generation is required, request only the current-stage image/reference/keyframe generation and wait for its result before advancing.

## Anti-jump rule
Do **not** create or activate a final video-generation prompt during Fast Start merely because the source/template already contains a complete video prompt.

The source/template is evidence to analyze. It may lock camera, mechanism, timing grammar, or style, but the project must still pass the relevant reference, creative/scenario, storyboard/keyframe, and preflight gates before final video prompting.

A final video prompt created before those gates pass must be marked `premature_draft` / `not_active` and must not become the project next action.

Do not begin with generic questions such as “what lighting/style/camera?” unless analysis proves the decision is genuinely required.

## Fast Start outputs
At minimum:
- registered project;
- immutable input record;
- source prompt analysis;
- product identity + identity lock;
- initial reference strategy;
- updated status/handoff;
- explicit **next immediate stage**.

Fast Start does not require a scenario, storyboard, keyframe set, final video prompt, or video baseline in the first response unless those stages had already been completed and evidenced before the current session.
