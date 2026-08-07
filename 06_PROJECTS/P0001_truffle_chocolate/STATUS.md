# Project status — P0001

- Current stage: `STAGE_04_REFERENCE_ASSET_CREATION`; Stage 05 QA completed for HERO-45, TOP-CLEAN and MACRO roles.
- Product identity: `product_identity.md` + active injection `identity_lock_v02.md`.
- Source prompt analysis: completed v1.
- Active reference strategy: `04_REFERENCE_STRATEGY/reference_plan.md` (v2 content).
- Creative direction: tiny chocolatiers + premium macro food-commercial; provisional hybrid Workshop/Gift Box direction.

## Approved/selected references
- `P0001-R0003` → **APPROVED / SELECTED** `REF-PROD-TOP-CLEAN`, primary clean product identity ingredient, ~4.8/5.
- `P0001-R0004` → approved alternate TOP-CLEAN, ~4.7/5.
- `P0001-R0006` → **APPROVED / SELECTED** `REF-PROD-MACRO`, texture/material authority only, ~4.5/5.
- `P0001-R0005` → approved alternate MACRO, ~4.4/5; stronger handmade silhouette but weaker/glossier cup material.
- `P0001-R0002` → PASS WITH CAVEATS / selected secondary `REF-PROD-HERO-45` geometry reference, ~4.3/5.
- `P0001-R0001` → alternate HERO-45 evidence, ~4.2/5.

## Reference-authority rule
Original real product photo > R0003 TOP-CLEAN for visible identity facts > R0006 for texture/material scale > R0002 for inferred depth/novel-angle geometry. A lower-authority reference must not override a higher-authority source outside its assigned role.

## Key learning so far
Macro generation is useful for particle/material scale but can still regularize silhouette or wrapper material. `R0006` is therefore explicitly bounded to texture/material authority. Recorded as `OBS-0004`.

## Current blocker
None.

## Next action
Generate exactly two `REF-PROD-ASSORTMENT-DETAIL` candidates using:
`11_PROMPT_PACKAGES/PKG_REFERENCE_IMAGES_V04_ASSORTMENT/prompt.txt`

Preferred inputs / authority order:
1. original real product photograph — highest assortment/product authority;
2. selected `P0001-R0003` TOP-CLEAN — supporting clean identity evidence;
3. selected `P0001-R0006` MACRO — particle/material scale only.

Do not use HERO-45 references for this pass. Generate two unchanged controlled candidates, attach them, register as `P0001-R0007` and `P0001-R0008`, then QA before character generation.

- Target video workflow: Google Flow / Gemini Omni Flash / Ingredients-to-Video / 10s / 16:9.
- Ingredient budget policy: operational hard cap 7; current planned first-pass set uses six distinct roles and keeps one slot reserved.
