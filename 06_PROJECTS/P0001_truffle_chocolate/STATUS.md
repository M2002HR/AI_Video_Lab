# Project status — P0001

- Current stage: `STAGE_04_REFERENCE_ASSET_CREATION`; Stage 05 QA completed for HERO-45, TOP-CLEAN, MACRO and ASSORTMENT-DETAIL roles.
- Product identity: `product_identity.md` + active injection `identity_lock_v02.md`.
- Source prompt analysis: completed v1.
- Active reference strategy: `04_REFERENCE_STRATEGY/reference_plan.md`.
- Creative direction: tiny chocolatiers + premium macro food-commercial; provisional hybrid Workshop/Gift Box direction.

## Approved / selected product references
- `P0001-R0003` → **SELECTED** `REF-PROD-TOP-CLEAN`, primary clean visible-identity ingredient, ~4.8/5.
- `P0001-R0008` → **SELECTED** `REF-PROD-ASSORTMENT-DETAIL`, assortment/color/coating-family authority, ~4.5/5.
- `P0001-R0006` → **SELECTED** `REF-PROD-MACRO`, texture/material/particle-scale authority only, ~4.5/5.
- `P0001-R0002` → selected provisional `REF-PROD-HERO-45`, secondary inferred geometry/depth reference, ~4.3/5.

Approved alternates: R0004 TOP-CLEAN, R0007 ASSORTMENT, R0005 MACRO, R0001 HERO-45.

## Reference authority rule
Original real product photo > R0003 TOP-CLEAN for visible product identity/geometry > R0008 for assortment diversity and coating-family distinction > R0006 for micro texture/material scale > R0002 for inferred novel-angle depth. Lower-authority references cannot override higher-authority facts outside their assigned role.

## Assortment QA result
- R0008 selected because it obeys exact six-truffle count, includes both round nonpareils and elongated sprinkles, shows supported color diversity and matches the dark-neutral reference environment.
- R0007 retained as alternate/evidence; it reintroduced the original wooden tabletop despite explicit dark-background instructions (`OBS-0005`).
- Both assortment candidates still regularize handmade geometry somewhat; R0008 is NOT a geometry authority.

## Current blocker
None.

## Next action — character-only reference
Generate exactly two `REF-CHAR-CHOCOLATIERS` candidates using:
`11_PROMPT_PACKAGES/PKG_CHARACTER_REFERENCE_V01/prompt.txt`

Input reference:
- use the original tiny-chef / cheesecake creative image ONLY as character-style DNA;
- do not provide product reference images for this character-only generation;
- prompt explicitly forbids cheesecake/product/prop contamination.

Generate two unchanged controlled candidates. After attachment, register as `P0001-R0009` and `P0001-R0010`, perform anatomy/style/consistency QA and select one clean character ingredient.

## Planned first-pass Omni ingredient roles
1. R0003 TOP-CLEAN — primary product identity.
2. R0008 ASSORTMENT — color/coating diversity.
3. R0006 MACRO — texture/particle scale.
4. R0002 HERO-45 — optional secondary depth/geometry support.
5. character reference — pending.
6. scene/keyframe reference — created after scenario/shot lock.
7. reserved / repair-specific slot.

Ingredient limit remains operationally 7; final video test may omit R0002 if scene keyframe already supplies enough 3D geometry and reducing reference conflict improves results.
