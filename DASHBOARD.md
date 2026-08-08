# AI Video Ad Lab dashboard

- System version: 1.1.1
- Primary operator: ChatGPT / AI operator architecture
- Active projects: 1
- Project current stages: `P0001` → STAGE_10 Storyboard / combined-scene keyframe preparation

## P0001 selected references
- `R0003` TOP-CLEAN — primary visible product identity (~4.8/5)
- `R0008` ASSORTMENT — diversity/color/coating-family authority (~4.5/5)
- `R0006` MACRO — texture/material/particle-scale authority only (~4.5/5)
- `R0010` CHARACTERS — exact recurring three-chef appearance/style authority (~4.8/5)
- `R0002` HERO-45 — optional secondary inferred depth/geometry (~4.3/5)

Approved alternates: R0004, R0007, R0005, R0009, R0001.

## Current creative lock
- Scenario selected: `Final Touch → Full Box Reveal`
- One continuous 10-second shot
- Camera: smooth pull-back on shallow upward arc
- Exactly three recurring chefs
- Minimal finishing/inspection action
- Stable full-box hero ending
- Text storyboard: KF01 opening macro → KF02 mid assortment → KF03 final hero

## Next controlled generation
Generate two `SB/KF01` combined product+character opening keyframes using:
`06_PROJECTS/P0001_truffle_chocolate/11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V01_KF01/prompt.txt`

Preferred references: original real product + R0003 + R0008 + R0006 + R0010. Do not use old cheesecake creative. Do not add R0002 in the first KF01 test unless later evidence justifies it.

Expected next Runs: `P0001-R0011`, `P0001-R0012`.

## Learning / experiments
- Open experiment: `EXP-0001` separate ingredients vs contact sheet (planned, non-blocking)
- Observations:
  - `OBS-0001` Flow operational seven-image reference limit
  - `OBS-0002` low inter-run variance for HERO-45 baseline
  - `OBS-0003` novel-angle generation can regularize handmade geometry
  - `OBS-0004` macro refs need narrow material/scale authority
  - `OBS-0005` source environment can leak despite background instruction
  - `OBS-0006` clean character-only regeneration can remove old-creative contamination; pose must not become character-action authority
- Validated global learnings: 0; evidence is still project/provisional unless separately promoted.

## Cross-chat readiness
Enabled via `AI_START_HERE.md` + project `HANDOFF.md`.

Generated/maintained dashboard; not source of truth. Project truth lives in project metadata/status/handoff and underlying evidence.
