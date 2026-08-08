# Project status — P0001

- Current stage: `STAGE_10_STORYBOARD` — KF01 passed; KF03 v04 failed strict continuity because the complete product reference overrode the scene master during the wide derivation. Next task is a scene-master-only KF03 v05 test.
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
- `P0001-R0016` → SELECTED `KF01`, closer camera-derived opening state, ~4.5/5.
- `P0001-R0002` → provisional optional `REF-PROD-HERO-45`, secondary inferred geometry/depth, ~4.3/5.
- `P0001-R0018` → retained only as a standalone final-product/aesthetic hero candidate; NOT an approved sequence endpoint.

## Storyboard mapping
- `KF01` (~00:01): `P0001-R0016` — APPROVED.
- `KF02` / mid-state (~00:05): `P0001-R0015` — APPROVED scene master.
- `KF03` / final hero (~00:09.2): NOT YET APPROVED.

## KF03 v04 — FAILED STRICT CONTINUITY
Inputs:
- R0015 scene master;
- R0003 clean full-box product reference.

Results:
- `R0018` ~3.9/5 — visually strong standalone full-box hero, chefs remain inside, but the central hero/local arrangement from R0015 is rebuilt and no longer traceable. Retain only as aesthetic/product target.
- `R0019` ~3.3/5 — same scene-rebuild failure plus all three chefs drift outside/in front of the box.

Root-cause interpretation: during wide derivation, R0003 is a stronger globally coherent full-box layout than the partial R0015 world, so the image model snaps toward the product reference instead of performing camera-only extrapolation.

Evidence:
- `13_EVALUATION/reports/reference_qa_kf03_v04.md`
- `OBS-0010`
- `HYP-0003`

## Next action — KF03 v05 MASTER ONLY
Generate exactly TWO candidates with:
`11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V05_KF03_MASTER_ONLY/prompt.txt`

### Upload ONLY
1. `R0015` — selected scene master.

Do NOT upload R0003 or any other reference in this pass.

Expected next Runs: `P0001-R0020`, `P0001-R0021`.

### v05 success gate
- same central multicolor hero remains traceable in the same cup/local region;
- same three chefs remain inside the box in the same broad region;
- camera is simply farther and moderately higher;
- more of the same box is extrapolated around the existing scene rather than replacing it;
- no props, loose ingredients or character duplication;
- plausible path: R0016 → R0015 → new KF03.

If master-only still fails, stop repeated still-image endpoint iteration. Reassess final-flow architecture: use R0018 as a final aesthetic/product target without strict interpolation, or split the reveal into a separate controlled clip.

- Target video workflow: Google Flow / Gemini Omni Flash / Ingredients-to-Video / 10s / 16:9.
- Operational ingredient budget remains 7; use only high-value role-clean ingredients.
