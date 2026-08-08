# Project status — P0001

- Current stage: `STAGE_10_STORYBOARD` — KF01 has now passed using camera derivation from the stable scene master. Next task is final hero KF03 derivation.
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

Approved alternates/evidence: R0004 TOP-CLEAN, R0007 ASSORTMENT, R0005 MACRO, R0009 CHARACTER, R0001 HERO-45, R0014 scene-grammar alternate, R0017 KF01 alternate.

## Scene/keyframe history
### KF01 v01 — failed
R0011–R0013 failed due role bleed, unwanted props/tools/loose ingredients, wrong physical scene anchoring, scale/readability problems and product regularization.

### KF01 v02 — stable combined world
R0014–R0015 used only R0003 + R0010 and no tools/actions. This produced a coherent inside-box scene. R0015 was selected as `SCENE MASTER / KF02-like` rather than forcing it into an opening role because it revealed too much assortment.

### KF01 v03 — PASSED via camera derivation
R0016–R0017 were derived from R0015 + R0003 instead of rebuilding the world.

- `R0016` ~4.5/5 — SELECTED KF01.
- `R0017` ~4.4/5 — approved alternate.

R0016 passes because it is clearly closer than R0015, preserves the same three-chef cast and kraft-box world, keeps the hero truffle dominant, introduces zero props/loose ingredients and plausibly connects to R0015 via one continuous pull-back.

Remaining caveats:
- more neighboring assortment is visible than the strict opening target;
- some static pose language remains;
- hero geometry is still mildly regularized relative to the handmade source.

Evidence: `13_EVALUATION/reports/reference_qa_kf01_v03.md`, `OBS-0009`.

## Storyboard mapping now
- `KF01` (~00:01): `P0001-R0016`.
- `KF02` / mid-state (~00:05): `P0001-R0015`.
- `KF03` / final hero (~00:09.2): NEXT.

Do not independently regenerate KF02. Derive KF03 outward from R0015 to preserve the same combined world.

## Next action — KF03 final hero derivation
Generate exactly TWO candidates with:
`11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V04_KF03_FROM_MASTER/prompt.txt`

### Upload only
1. `R0015` — selected SCENE MASTER / highest authority for combined-world continuity.
2. `R0003` — product/packaging truth backup.

Do not upload character reference, macro, assortment, hero-45 or original wooden-background source unless a later controlled repair explicitly requires one of them.

Expected next runs: `P0001-R0018`, `P0001-R0019`.

### KF03 gate
- clearly farther and moderately higher camera than R0015;
- complete kraft box readable without changing box identity;
- colorful assortment dominates the final commercial frame;
- same three chefs remain present, smaller in screen space but physically consistent;
- no extra chefs, tools, bowls, loose ingredients or debris;
- hero-truffle region remains traceable;
- deeper/moderate focus keeps most of product readable;
- clean dark studio breathing room suitable for final hold / later branding;
- plausible same camera path from R0016 → R0015 → new KF03.

- Target video workflow: Google Flow / Gemini Omni Flash / Ingredients-to-Video / 10s / 16:9.
- Operational ingredient budget remains 7; final Flow stack will be chosen after KF03 QA rather than filling all available slots automatically.
