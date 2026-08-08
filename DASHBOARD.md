# AI Video Ad Lab dashboard

- System version: 1.1.1
- Primary operator: ChatGPT / AI operator architecture
- Active projects: 1
- Project current stages: `P0001` → STAGE_10 Storyboard / derive true KF01 from selected scene master

## P0001 selected references
- `R0003` TOP-CLEAN — primary visible product identity (~4.8/5)
- `R0008` ASSORTMENT — diversity/color/coating-family authority (~4.5/5)
- `R0006` MACRO — texture/material/particle-scale authority only (~4.5/5)
- `R0010` CHARACTERS — recurring three-chef appearance/style authority (~4.8/5)
- `R0015` SCENE MASTER — selected coherent inside-box combined world / KF02-like anchor (~4.3/5)
- `R0002` HERO-45 — optional secondary inferred depth/geometry (~4.3/5)

## Combined-scene evidence
### v01 five-reference setup
- R0011 2.9/5 — fail
- R0012 3.4/5 — fail / best diagnostic
- R0013 3.2/5 — fail

Repeated failures: props/tools/loose ingredients, wrong scene anchoring, scale/readability issues and geometry regularization.

### v02 minimal-reference setup
Inputs: R0003 + R0010 only; no tools/actions.
- R0014 ~4.1/5 — strong scene-grammar evidence, too wide for opening.
- R0015 ~4.3/5 — selected scene master / mid-reveal anchor.

Both v02 outputs successfully place the scene inside the kraft box with exactly three recognizable chefs and zero unwanted props. `HYP-0002` receives strong project-level support; not yet a global rule.

## Current creative strategy
Do not regenerate the whole combined scene again.
Use R0015 as the stable world anchor and derive camera states from it:
- true KF01 = closer/slightly lower view;
- R0015 ≈ KF02/mid reveal;
- KF03 later = wider full-box hero derived from the same world.

## Next controlled generation
Prompt:
`06_PROJECTS/P0001_truffle_chocolate/11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V03_KF01_FROM_MASTER/prompt.txt`

Upload ONLY:
1. R0015 SCENE MASTER
2. R0003 TOP-CLEAN as product-identity backup

Expected runs: `P0001-R0016`, `P0001-R0017`.

Goal: change camera/framing only. Reveal much less assortment than R0015 while preserving exact scene/characters and same-box continuity.

## Learning / experiments
- Open experiment: EXP-0001 separate ingredients vs contact sheet (planned, non-blocking)
- Key observations include OBS-0007 five-reference scene over-conditioning and OBS-0008 minimal-stack improvement + storyboard-role reassignment.
- Validated global learnings: 0; current findings remain project/provisional unless promoted through evidence policy.

## Cross-chat readiness
Enabled via `AI_START_HERE.md` + project `HANDOFF.md`.

Generated/maintained dashboard; not source of truth. Project truth lives in project metadata/status/handoff and underlying evidence.
