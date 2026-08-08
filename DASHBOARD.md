# AI Video Ad Lab dashboard

- System version: 1.1.1
- Primary operator: ChatGPT / AI operator architecture
- Active projects: 1
- Project current stages: `P0001` → STAGE_10 Storyboard / KF01 v02 repair

## P0001 selected references
- `R0003` TOP-CLEAN — primary visible product identity (~4.8/5)
- `R0008` ASSORTMENT — diversity/color/coating-family authority (~4.5/5)
- `R0006` MACRO — texture/material/particle-scale authority only (~4.5/5)
- `R0010` CHARACTERS — exact recurring three-chef appearance/style authority (~4.8/5)
- `R0002` HERO-45 — optional secondary inferred depth/geometry (~4.3/5)

## KF01 v01 result
- `R0011` — 2.9/5 — FAIL
- `R0012` — 3.4/5 — FAIL / best diagnostic only
- `R0013` — 3.2/5 — FAIL

Repeated failures: extra props/bowls/ingredients, wrong chef scale, oversized nonpareils, over-perfect hero sphere, back-facing character identity loss, and opening scene not physically inside the final kraft box.

No scene keyframe is approved yet.

## Active creative revision
Scenario v02: `Quiet Inspection → Full Box Reveal`
- no tools or bowls;
- hands empty;
- opening already inside the same kraft box;
- truffle diameter ≈ 3× chef height;
- all three faces readable;
- same continuous pull-back + shallow rise;
- final full-box hero hold.

## Next controlled generation
Use ONLY:
1. `R0003` TOP-CLEAN
2. `R0010` CHARACTERS

Prompt:
`06_PROJECTS/P0001_truffle_chocolate/11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V02_KF01/prompt.txt`

Expected next Runs: `P0001-R0014`, `P0001-R0015`.

Do not add original wooden-background source, R0006, R0008 or R0002 in the first v02 pass. This is a deliberate minimal-reference repair test (`HYP-0002`).

## Learning / experiments
- Open experiment: `EXP-0001` separate ingredients vs contact sheet (planned, non-blocking)
- Key observations:
  - `OBS-0001` provisional Flow seven-image reference limit
  - `OBS-0003` novel-angle generation can regularize handmade geometry
  - `OBS-0004` macro refs need narrow material/scale authority
  - `OBS-0005` source environment can leak despite background instruction
  - `OBS-0006` clean character-only reference removes old-creative contamination; poses are not authority
  - `OBS-0007` combined-scene five-reference/long-prompt setup produced recurring role bleed, prop invention and continuity failure
- `HYP-0002` tests whether a two-reference, no-prop scene improves compliance.
- Validated global learnings: 0; current findings remain project/provisional unless promoted through evidence policy.

## Cross-chat readiness
Enabled via `AI_START_HERE.md` + project `HANDOFF.md`.

Generated/maintained dashboard; not source of truth. Project truth lives in project metadata/status/handoff and underlying evidence.
