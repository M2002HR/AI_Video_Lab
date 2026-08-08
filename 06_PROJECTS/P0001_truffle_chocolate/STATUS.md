# Project status — P0001

- Current stage: `STAGE_10_STORYBOARD` — minimal-reference combined-scene test passed the scene-grammar gate; R0015 is selected as scene master / KF02-like anchor. True KF01 will now be derived from that stable scene.
- Product identity: `product_identity.md` + active injection `identity_lock_v02.md`.
- Source prompt analysis: completed v1.
- Active reference strategy: `04_REFERENCE_STRATEGY/reference_plan.md`.
- Active scenario: `07_SCENARIOS/selected/scenario_v02_quiet_inspection_reveal.md`.
- Active timing: `08_SHOT_DESIGN/timeline_v02.md`.

## Approved / selected references
- `P0001-R0003` → SELECTED `REF-PROD-TOP-CLEAN`, primary clean visible-product identity, ~4.8/5.
- `P0001-R0008` → SELECTED `REF-PROD-ASSORTMENT-DETAIL`, diversity/color/coating-family authority, ~4.5/5.
- `P0001-R0006` → SELECTED `REF-PROD-MACRO`, texture/material/particle-scale authority only, ~4.5/5.
- `P0001-R0010` → SELECTED `REF-CHAR-CHOCOLATIERS`, recurring three-character identity/style authority, ~4.8/5.
- `P0001-R0015` → SELECTED `REF-SCENE-MASTER`, coherent inside-box combined world / KF02-like anchor, ~4.3/5.
- `P0001-R0002` → provisional optional `REF-PROD-HERO-45`, secondary inferred geometry/depth, ~4.3/5.

Approved alternates/evidence: R0004 TOP-CLEAN, R0007 ASSORTMENT, R0005 MACRO, R0009 CHARACTER, R0001 HERO-45, R0014 scene-grammar alternate.

## KF01 v01 — FAILED
R0011–R0013 failed strict scene gate due repeated props/tools/loose ingredients, wrong scene anchoring, scale/readability problems and geometry regularization. Evidence: `13_EVALUATION/reports/reference_qa_kf01_v01.md`, `OBS-0007`, `HYP-0002`.

## KF01 v02 minimal-reference result — MAJOR IMPROVEMENT
Inputs were reduced to only R0003 TOP-CLEAN + R0010 CHARACTER, with all tools/actions removed.

- `R0014` ~4.1/5 — strong scene-grammar evidence, but too wide for opening KF01.
- `R0015` ~4.3/5 — selected as combined `SCENE MASTER / KF02-like` anchor.

Both v02 candidates:
- are physically inside the kraft box;
- contain exactly three recognizable chefs;
- contain zero tools/bowls/loose ingredients;
- provide clean continuity for a pull-back.

Remaining mismatch:
- both reveal too much assortment to serve as the 00:01 opening;
- original 1:3 requested scale was not reached, though miniature scale is visually clear;
- some static pose leakage remains;
- hero truffle geometry remains somewhat regularized.

Full evidence: `13_EVALUATION/reports/reference_qa_kf01_v02.md`, `OBS-0008`.

## Current strategy
Do NOT synthesize the combined world again from scratch.
Use R0015 as the stable scene master and derive adjacent storyboard views from it.

R0015 now functions approximately as KF02 / mid-reveal state. The true opening KF01 should look like the same camera moved closer and slightly lower in the same physical scene.

## Next action — KF01 v03 camera derivation
Generate exactly TWO candidates with:
`11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V03_KF01_FROM_MASTER/prompt.txt`

### Upload only
1. `R0015` — selected SCENE MASTER / highest authority for the combined world;
2. `R0003` — product-identity backup only.

Do NOT upload R0010 in this pass unless character identity later drifts; R0015 already contains the accepted cast and re-uploading R0010 can reapply static-pose pressure.

Expected runs: `P0001-R0016`, `P0001-R0017`.

### v03 gate
- clearly closer camera than R0015;
- hero truffle dominates opening frame;
- substantially less box/assortment revealed than R0015;
- exact same three chefs/world remain recognizable;
- zero props/loose ingredients;
- same-box continuity preserved;
- plausible continuous pull-back from new KF01 → R0015.

Do not generate final hero KF03 until a derived KF01 passes. After that, derive KF03 outward from the same scene-master/world.

- Target video workflow: Google Flow / Gemini Omni Flash / Ingredients-to-Video / 10s / 16:9.
- Operational ingredient budget remains 7; use fewer high-value references rather than filling all slots automatically.
