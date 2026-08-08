# Data Model

## Primary records
- `project.json`: project state and durable metadata.
- `run.json`: provenance for each meaningful AI execution.
- Markdown analysis/evaluation/decision/handoff files: human-readable evidence and context.
- `10_REGISTRY/*.csv`: generated views, not manually edited source-of-truth files.

JSON must be valid UTF-8. Unknown values are `unknown` or `null`, never guesses.

## Project continuity records
Every active project should maintain:
- `STATUS.md` — concise current operational state;
- `HANDOFF.md` — complete continuation summary;
- `18_CONVERSATION_LOG/` — durable feedback/session summaries;
- `19_HANDOFF_ASSETS/` — optional low-resolution visual proxies and manifest under Storage Policy.

`HANDOFF.md` links authoritative detail rather than duplicating every source file.

## Derivative projects
When a new deliverable changes duration/story/sequence materially, create a new derivative project and link its parent instead of overwriting the previous project. Record parent project ID, inherited learnings, and reused asset IDs only when media is actually available and role-appropriate.

## Multi-clip model
For multi-clip deliverables record:
- `sequence_id`, e.g. `P0002-S01`;
- `clip_id`, e.g. `P0002-C01` through `P0002-C04`;
- total duration and clip durations;
- architecture mode;
- Master Sequence;
- Clip Contracts and boundary contracts;
- selected final Run per clip;
- assembled final metadata/path and sequence QA.

Run IDs remain project-global, e.g. `P0002-R0017` may include `clip_id=P0002-C02`.

## Scenario architecture records
Before scenario selection when appropriate, persist Process State Map, Scenario Capacity Assessment, Duration Viability Matrix, scenario candidates/cards, selected scenario, clip count, architecture mode, and user decision.

## Reference roles
Standard role concepts include product identity, packaging identity, macro/texture, angle/geometry, assortment, character identity, style/lighting, scene master, start state, end state, and process/tool evidence. Style-only references never redefine product identity.

## Media records
If the binary is outside Git, record as much as possible: filename/location description, role, originating Run, hash when available, dimensions/duration, proxy path if any, privacy status, and whether re-attachment is required. A chat attachment alone does not mean the media is stored in the repository.

## Selection integrity
`selected_final_run` must refer to an existing evaluated Run. Failed/obsolete Runs remain preserved. For multi-clip work, each clip has an independently selected final Run and the assembled master receives separate final QA.

## Language
Persisted text fields are English-only. Translate non-English source feedback before storing it.
