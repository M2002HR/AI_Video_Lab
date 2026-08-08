# Fast Start Protocol

Use this when the user wants to begin a real project with minimal friction.

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
9. At the first real external-generation or creative-decision gate, prepare the relevant prompt package/preflight and tell the user exactly what to generate or choose.

Do not begin with generic questions such as “what lighting/style/camera?” unless analysis proves the decision is genuinely required.

## Fast Start outputs
At minimum: registered project, immutable input record, source prompt analysis, product identity + identity lock, initial reference strategy, updated status/handoff, and explicit next action.
