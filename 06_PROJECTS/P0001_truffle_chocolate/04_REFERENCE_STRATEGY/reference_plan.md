# P0001 Reference Strategy v3

## Target generation mode
Google Flow → Video → Ingredients/References → Gemini Omni Flash → 10 seconds → 16:9.

## Ingredient budget
- Operational maximum for Omni Flash: **7 image-reference slots**.
- Treat 7 as a provisional operational limit and re-verify after major Flow/model changes.
- Do not fill all seven automatically. Default production target remains 4–6 high-information, non-conflicting references with headroom reserved.

## Core authority rule
Separate source truth from generated supporting evidence. Each generated reference receives a narrow authority role so that a useful reference cannot accidentally redefine unrelated product/character facts.

### Product authority order
1. original real product photograph — ultimate source authority;
2. `P0001-R0003` — selected clean-top visible product identity;
3. `P0001-R0008` — assortment/color/coating-family authority;
4. `P0001-R0006` — micro texture/material/particle-scale authority only;
5. `P0001-R0002` — optional secondary inferred geometry/depth support only.

Generated references never override the real source when they disagree about handmade irregularity, box construction, coating family or visible arrangement.

### Character authority
`P0001-R0010` independently defines the recurring three-chef cast appearance/style:
- moustached foreman;
- clean-shaven chocolatier;
- small-goatee specialist;
- consistent deep-red jackets/hats, dark trousers/shoes;
- compact stylized premium miniature proportions.

R0010 does NOT define action, pose, tool, scene position or chef-to-truffle scale.

## Collage / contact-sheet policy
Default remains: **do not combine multiple product views into one collage as a production shortcut.** Separate single-role ingredients are easier to assign and less likely to introduce duplication/reference ambiguity. This is a working hypothesis pending `EXP-0001`, not an official Google prohibition.

A clean group image of the exact three intended recurring chefs is different: those three are real intended scene entities, not alternate views of one object. Therefore R0010 is accepted as one character-only slot.

## Approved core references

### Ingredient A — `REF-PROD-TOP-CLEAN` — APPROVED / SELECTED
Selected: `P0001-R0003` (~4.8/5).  
Alternate: `P0001-R0004`.

Role: `product_identity_primary` + visible composition evidence.

Purpose: highest-fidelity cleaned representation of the real assortment; watermark/wooden environment removed while visible product facts remain close to source.

### Ingredient B — `REF-PROD-ASSORTMENT-DETAIL` — APPROVED / SELECTED
Selected: `P0001-R0008` (~4.5/5).  
Alternate: `P0001-R0007`.

Role: assortment diversity / color-family / coating-family evidence.

Purpose: explicitly show multiple supported colors plus both round nonpareils and elongated sprinkles. Not geometry authority.

### Ingredient C — `REF-PROD-MACRO` — APPROVED / SELECTED
Selected: `P0001-R0006` (~4.5/5).  
Alternate: `P0001-R0005`.

Role: texture/material/particle-scale only.

Purpose: teach tiny edible nonpareil size/contact, dark-chocolate glimpses and matte folded-paper cup behavior. Not silhouette/assortment authority.

### Ingredient D — `REF-CHAR-CHOCOLATIERS` — APPROVED / SELECTED
Selected: `P0001-R0010` (~4.8/5).  
Alternate: `P0001-R0009`.

Role: `character_only`.

Purpose: clean exact three-character cast without cheesecake/old-scene contamination. Downstream prompts must explicitly override reference poses while preserving appearance.

### Ingredient E — `REF-SCENE-KEYFRAME` — NEXT
Role: combined scene / composition / scale anchor.

Purpose: combine the real product family and selected three-chef cast in the opening macro world, locking chef-to-truffle scale and initial composition before video generation.

Generate/QA KF01 first from the storyboard. Do not generate later keyframes until combined-scene grammar passes.

### Ingredient F — `REF-PROD-HERO-45` — OPTIONAL
Selected candidate: `P0001-R0002` (~4.3/5).  
Alternate: `P0001-R0001`.

Role: secondary inferred geometry/depth only.

Use only if scene-keyframe/video tests show that extra full-box depth support adds value without product regularization or reference conflict. Omit by default in first-pass testing if redundant.

### Ingredient G — RESERVED
Keep unused unless QA identifies a specific repair need.

## Recommended first-pass Flow ingredient stack after KF01 approval
1. `R0003` TOP-CLEAN — primary product identity.
2. `R0008` ASSORTMENT — diversity/coating families.
3. `R0006` MACRO — particle/material scale.
4. `R0010` CHARACTERS — recurring trio identity/style.
5. selected KF01 combined scene reference — composition + chef/product scale.
6. optional `R0002` HERO-45 only if preflight evidence justifies it.
7. reserved.

Preferred first experiment: start with five active references (1–5) rather than automatically adding R0002. Add R0002 only as a controlled variable if the box-depth/3D geometry is insufficient.

## Evidence notes
- `OBS-0003`: novel-angle image generation regularized handmade geometry; source-derived identity refs must outrank synthesized views.
- `OBS-0004`: macro references are useful but must receive narrow material/scale authority.
- `OBS-0005`: source environments can leak into generated references despite explicit background instructions.
- `OBS-0006`: character-only regeneration successfully removed old cheesecake contamination; selected group reference must be treated as appearance/style authority, not pose authority.

## Current gate
Core product and character reference roles are approved. Scenario/shot timing are locked. The next gate is combined-scene keyframe QA (`SB/KF01`). After one KF01 candidate is approved, proceed to later storyboard/keyframe states and then final Flow prompt synthesis/preflight.
