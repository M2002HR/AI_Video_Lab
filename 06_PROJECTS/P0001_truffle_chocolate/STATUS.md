# Project status — P0001

- Current stage: `STAGE_10_STORYBOARD` — combined-scene KF01 v01 failed the strict gate; revised v02 scenario/prompt is active.
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
- `P0001-R0002` → provisional optional `REF-PROD-HERO-45`, secondary inferred geometry/depth, ~4.3/5.

Approved alternates: R0004 TOP-CLEAN, R0007 ASSORTMENT, R0005 MACRO, R0009 CHARACTER, R0001 HERO-45.

## KF01 v01 QA — FAILED GATE
Three combined-scene candidates were evaluated:
- `R0011` ~2.9/5 — wooden workshop/background product and multiple prop contamination.
- `R0012` ~3.4/5 — best diagnostic candidate, but extra tools/bowl, loose particles, center chef back-facing, wrong scale and no kraft-box continuity.
- `R0013` ~3.2/5 — attractive but cluttered with extra props/food debris, same scale/continuity issues.

No v01 candidate is approved as a scene ingredient. Full report: `13_EVALUATION/reports/reference_qa_kf01_v01.md`.

## What v01 taught us
Repeated cross-candidate failures indicate a strategy problem, not merely insufficient negative wording:
- five-reference scene stack over-conditioned the scene;
- R0006/R0008 generated regularization leaked into scene synthesis;
- active brush/worksite language encouraged bowls/tools/loose ingredients;
- the opening frame was not physically anchored inside the final kraft box;
- chef-to-truffle scale and all-face readability were not obeyed reliably.

Recorded as `OBS-0007`; repair hypothesis is `HYP-0002`.

## Scenario v02 — active
`Quiet Inspection → Full Box Reveal`:
- no tools or bowls at all;
- all hands empty;
- opening frame already exists inside the same kraft box;
- hero truffle diameter ≈ 3× one chef's standing height;
- all three recurring faces readable in 3/4 view;
- one continuous pull-back + shallow rise reveals the already-existing assortment and final box.

## Next action — KF01 v02 controlled generation
Use ONLY TWO reference images:
1. `R0003` TOP-CLEAN;
2. `R0010` CHARACTER.

Do not upload original wooden-background source, R0006 MACRO, R0008 ASSORTMENT or R0002 HERO-45 for the first v02 pass.

Generate exactly two candidates using:
`11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V02_KF01/prompt.txt`

Expected runs: `P0001-R0014`, `P0001-R0015`.

Gate before KF02/KF03:
- scene physically inside kraft box;
- zero props/loose ingredients;
- exactly three recognizable chefs with faces readable;
- correct ~1:3 chef-height/truffle-diameter scale;
- source-like small nonpareils and handmade truffle shape;
- clean dark environment;
- pull-back continuity plausible.

- Target video workflow: Google Flow / Gemini Omni Flash / Ingredients-to-Video / 10s / 16:9.
- Operational ingredient budget remains 7; target remains fewer high-value references rather than filling all slots automatically.
