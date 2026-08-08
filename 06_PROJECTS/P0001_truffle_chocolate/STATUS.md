# Project status — P0001

- Current stage: `STAGE_10_STORYBOARD` — core reference generation is complete enough for v1; selected scenario and 10-second shot timing are now locked.
- Product identity: `product_identity.md` + active injection `identity_lock_v02.md`.
- Source prompt analysis: completed v1.
- Active reference strategy: `04_REFERENCE_STRATEGY/reference_plan.md`.
- Selected scenario: `07_SCENARIOS/selected/scenario_v01_final_touch_reveal.md`.
- Locked shot timing: `08_SHOT_DESIGN/timeline_v01.md`.
- Storyboard plan: `09_STORYBOARD/storyboard_plan_v01.md`.

## Approved / selected reference stack
- `P0001-R0003` → **SELECTED** `REF-PROD-TOP-CLEAN`, primary clean visible-product identity, ~4.8/5.
- `P0001-R0008` → **SELECTED** `REF-PROD-ASSORTMENT-DETAIL`, diversity/color/coating-family authority, ~4.5/5.
- `P0001-R0006` → **SELECTED** `REF-PROD-MACRO`, texture/material/particle-scale authority only, ~4.5/5.
- `P0001-R0010` → **SELECTED** `REF-CHAR-CHOCOLATIERS`, recurring three-character identity/style authority, ~4.8/5.
- `P0001-R0002` → provisional optional `REF-PROD-HERO-45`, secondary inferred geometry/depth, ~4.3/5.

Approved alternates: R0004 TOP-CLEAN, R0007 ASSORTMENT, R0005 MACRO, R0009 CHARACTER, R0001 HERO-45.

## Reference authority rule
Original real product photo > R0003 for visible product identity/geometry > R0008 for assortment diversity/coating-family distinction > R0006 for micro texture/material scale > R0002 for inferred novel-angle depth. R0010 independently defines character appearance/style only. No lower-authority reference may override a higher-authority source outside its role.

## Character QA result
- R0010 selected over R0009 because it gives slightly stronger full-body/arm readability while preserving the same coherent trio.
- Exactly three recurring chefs: moustached foreman, clean-shaven chocolatier, small-goatee detail specialist.
- Old cheesecake/product/prop contamination successfully removed.
- Important boundary: R0010 defines character identity and uniform, NOT pose/action. Recorded as `OBS-0006`.

## Scenario v1 — locked
`Final Touch → Full Box Reveal`: one continuous 10-second shot. Start on one multicolor hero truffle with the three tiny chefs performing minimal final-inspection actions; camera executes one smooth pull-back along a shallow upward arc; more assortment enters frame; finish on stable premium full-box hero reveal.

This low-risk scenario intentionally avoids truffle assembly, object transportation, scene cuts and large character movement.

## Current blocker
None.

## Next action — SB/KF01 opening combined-scene keyframe
Generate exactly two opening keyframe candidates using:
`11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V01_KF01/prompt.txt`

Preferred reference inputs:
1. original real product photo — ultimate product authority;
2. R0003 TOP-CLEAN — clean visible identity;
3. R0008 ASSORTMENT — diversity support;
4. R0006 MACRO — particle/material scale only;
5. R0010 CHARACTER — exact recurring trio identity/style only.

Do NOT use the old cheesecake creative. Do NOT use R0002 HERO-45 for this first combined-scene test unless the first two KF01 candidates prove that extra full-box depth support is necessary.

Generate two unchanged controlled candidates, attach them, register as `P0001-R0011` and `P0001-R0012`, then perform combined-scene QA before generating KF02/KF03.

## Planned first-pass Omni ingredient stack after scene QA
1. R0003 TOP-CLEAN
2. R0008 ASSORTMENT
3. R0006 MACRO
4. R0010 CHARACTER
5. selected combined scene keyframe
6. R0002 HERO-45 only if evidence shows it adds useful geometry without conflict
7. reserved repair-specific slot

Operational ingredient budget remains 7; target remains fewer high-value references rather than filling all slots automatically.
