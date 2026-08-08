# AI Video Ad Lab dashboard

- System version: 1.1.1
- Primary operator: ChatGPT / AI operator architecture
- Active projects: 1
- Project current stages: `P0001` → STAGE_10 Storyboard / KF03 master-only continuity repair

## P0001 selected references / anchors
- `R0003` TOP-CLEAN — primary visible product identity (~4.8/5)
- `R0008` ASSORTMENT — diversity/color/coating-family authority (~4.5/5)
- `R0006` MACRO — texture/material/particle-scale authority only (~4.5/5)
- `R0010` CHARACTERS — recurring three-chef appearance/style authority (~4.8/5)
- `R0016` KF01 — selected close opening camera state (~4.5/5)
- `R0015` SCENE MASTER / KF02-like mid-state (~4.3/5)
- `R0002` HERO-45 — optional secondary inferred depth/geometry (~4.3/5)
- `R0018` — retained only as a standalone final product/aesthetic target, not a sequence endpoint.

## Storyboard state
- KF01: `R0016` — approved.
- KF02/mid: `R0015` — approved scene master.
- KF03/final: not approved.

## KF03 v04 result
Inputs: `R0015 + R0003`.

- `R0018` ~3.9/5 — visually strong full-box hero, chefs remain inside, but strict continuity fails because the central hero/local arrangement from R0015 is replaced by a source-like full-box arrangement.
- `R0019` ~3.3/5 — same scene reconstruction plus chefs move outside/in front of the box.

Conclusion: the complete product-truth reference can overpower the scene master during wide camera derivation (`OBS-0010`).

## Next controlled generation
Prompt:
`06_PROJECTS/P0001_truffle_chocolate/11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V05_KF03_MASTER_ONLY/prompt.txt`

Upload ONLY:
1. `R0015` SCENE MASTER.

Expected runs: `P0001-R0020`, `P0001-R0021`.

Goal: preserve the exact central hero, local neighboring arrangement and all three inside-box chef positions while moving the camera farther and moderately higher. Additional box/world may be extrapolated outside the existing crop, but the visible R0015 region may not be rebuilt.

## Learning / experiments
- EXP-0001: separate ingredients vs contact sheet — planned/non-blocking.
- HYP-0002 received strong project-level support: minimal role-clean scene stack outperformed five-reference scene synthesis.
- OBS-0009: stable scene master → adjacent camera derivation worked for KF01.
- OBS-0010 / HYP-0003: adding a complete source-product layout to wide camera derivation may override scene continuity; test master-only derivation next.
- Validated global learnings: 0; findings remain project/provisional until promoted by evidence policy.

## Cross-chat readiness
Enabled via `AI_START_HERE.md` + project `HANDOFF.md`.

Generated/maintained dashboard; project truth lives in project metadata/status/handoff and underlying evidence.
