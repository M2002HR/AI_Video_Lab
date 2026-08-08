# Project status — P0001

- Current stage: `STAGE_16_VIDEO_GENERATION` — storyboard/keyframe gate passed; final Flow/Omni prompt package and preflight are ready.
- Product identity: `product_identity.md` + active injection `identity_lock_v02.md`.
- Source prompt analysis: completed v1.
- Active reference strategy: `04_REFERENCE_STRATEGY/reference_plan.md`.
- Active scenario: `07_SCENARIOS/selected/scenario_v02_quiet_inspection_reveal.md`.
- Active timing: `08_SHOT_DESIGN/timeline_v02.md`.
- Active video package: `11_PROMPT_PACKAGES/PKG_FLOW_OMNI_VIDEO_V01/`.

## Approved / selected references
- `P0001-R0003` → SELECTED `REF-PROD-TOP-CLEAN`, primary clean product/packaging identity, ~4.8/5.
- `P0001-R0008` → SELECTED `REF-PROD-ASSORTMENT-DETAIL`, diversity/color/coating-family authority, ~4.5/5.
- `P0001-R0006` → SELECTED `REF-PROD-MACRO`, texture/material/particle-scale authority only, ~4.5/5.
- `P0001-R0010` → SELECTED `REF-CHAR-CHOCOLATIERS`, exact recurring three-chef appearance/style authority, ~4.8/5.
- `P0001-R0015` → SELECTED `REF-SCENE-MASTER`, stable combined inside-box world / KF02-like mid-state, ~4.3/5.
- `P0001-R0016` → SELECTED `KF01`, opening camera state derived from scene master, ~4.5/5.
- `P0001-R0020` → SELECTED `KF03`, final wide camera state derived from scene master only, ~4.5/5.
- `P0001-R0002` → provisional optional `REF-PROD-HERO-45`, lower-authority inferred geometry/depth, ~4.3/5.
- `P0001-R0018` → standalone final-product/aesthetic hero candidate only; not a sequence endpoint.

## Locked storyboard anchors
- `KF01` (~00:01): `P0001-R0016` — APPROVED.
- `KF02` / scene master (~00:05): `P0001-R0015` — APPROVED.
- `KF03` / final hero (~00:09.2): `P0001-R0020` — APPROVED.

## KF03 v05 — PASSED
Input:
- `R0015` scene master only.

Results:
- `R0020` ~4.5/5 — SELECTED. Preserves the central multicolor hero, same three chefs inside the box, zero props, and a plausible farther/higher camera state while extrapolating more of the same world.
- `R0021` ~4.2/5 — approved alternate. Core continuity survives but newly extrapolated assortment/box geometry drifts more than R0020.

Evidence:
- `13_EVALUATION/reports/reference_qa_kf03_v05.md`
- `OBS-0011`

Key project-level finding: after a stable combined scene exists, adjacent camera-state derivation can be more stable when the scene master is the only image reference. A globally complete secondary product reference can otherwise act as a competing layout attractor. Keep provisional until cross-project validation.

## Final Flow ingredient stack — v01
Use exactly FIVE uploaded images, in this order:
1. `R0016` — opening KF01.
2. `R0015` — scene master / mid state.
3. `R0020` — final KF03.
4. `R0003` — product/packaging identity only.
5. `R0010` — character identity only.

Do NOT fill slots 6–7 on the first video pass.
Do NOT upload macro, assortment, hero-45, original wooden-background source or R0018 unless video QA later identifies a specific failure those images are expected to fix.

Reference rationale: `11_PROMPT_PACKAGES/PKG_FLOW_OMNI_VIDEO_V01/references.md`.

## Video preflight
`11_PROMPT_PACKAGES/PKG_FLOW_OMNI_VIDEO_V01/preflight_checklist.md` → PASS.

Primary prompt:
`11_PROMPT_PACKAGES/PKG_FLOW_OMNI_VIDEO_V01/prompt.txt`.

Recommended run setup:
`11_PROMPT_PACKAGES/PKG_FLOW_OMNI_VIDEO_V01/recommended_settings.md`.

## Exact next action — first controlled Flow baseline
Target:
- Google Flow
- Gemini Omni Flash
- Ingredients / references to video
- 10 seconds
- 16:9

Generate exactly TWO videos with IDENTICAL:
- five-image ingredient stack;
- upload order;
- prompt;
- exposed settings/defaults.

Expected next Run IDs:
- `P0001-R0022`
- `P0001-R0023`

Do not optimize between these two runs. Their purpose is baseline stability measurement.

After generation, provide/export both videos for frame-by-frame QA before changing prompt or ingredients.
