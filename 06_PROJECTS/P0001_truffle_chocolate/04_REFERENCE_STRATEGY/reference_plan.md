# P0001 Reference Strategy v2

## Target generation mode
Google Flow → Video → Ingredients/References → Gemini Omni Flash → 10 seconds → 16:9.

## Ingredient budget
- Operational maximum for Omni Flash: **7 image-reference slots**.
- Treat 7 as a provisional operational limit and re-verify after major Flow/model changes.
- Do not fill all seven automatically. Default production target remains 4–6 high-information, non-conflicting references with headroom reserved.

## Core authority rule
For identity-sensitive products, distinguish **source authority** from **generated supporting evidence**.

Current P0001 authority order:
1. original real product photograph — ultimate source authority;
2. `P0001-R0003` — selected primary clean top identity ingredient;
3. `P0001-R0004` — approved alternate clean top identity ingredient;
4. `P0001-R0002` — selected secondary 45-degree geometry reference;
5. `P0001-R0001` — alternate 45-degree geometry evidence.

Generated novel views must never override the real source when they disagree about handmade irregularity, box construction, assortment structure or coating identity.

## Why the authority order changed
Direct QA showed that the conservative top-clean edits (`R0003`, `R0004`) preserve the original 25-truffle layout, color/coating distribution, cups and packaging much more faithfully than the synthesized 45-degree views (`R0001`, `R0002`). The 45-degree views remain useful because they provide inferred depth, but that same inference mildly regularized the handmade product and polished the box.

Linked evidence: `OBS-0003` and `13_EVALUATION/reports/reference_qa_top_clean_v01.md`.

## Collage / contact-sheet policy
Default remains: **do not combine multiple product views into one collage as a production shortcut.** Separate single-role ingredients are easier to assign and less likely to introduce duplication/reference ambiguity. This is a working hypothesis pending `EXP-0001`, not an official Google prohibition.

If later tested, keep collage product-only, neutral, 2–4 views maximum, no style elements, and compare against the same views uploaded separately.

## Current P0001 candidate reference pack

### Ingredient A — `REF-PROD-TOP-CLEAN` — APPROVED
Role: `product_identity_primary` + `composition_only`.
Selected: `P0001-R0003`.
Alternate: `P0001-R0004`.
Purpose: highest-fidelity cleaned representation of the real assortment for Flow. Preserves the visible count/layout and removes watermark/wooden-background contamination.

### Ingredient B — `REF-PROD-HERO-45` — PASS WITH CAVEATS
Role: `geometry_view` + secondary product identity evidence.
Selected: `P0001-R0002`.
Alternate: `P0001-R0001`.
Purpose: show box depth, truffle height and cup geometry unavailable in the original overhead source. Never override the clean top/original source on product identity.

### Ingredient C — `REF-PROD-MACRO` — NEXT
Role: `texture_detail`.
Macro close-up of one representative truffle in its dark fluted cup. Must teach realistic edible particle scale, dark chocolate beneath the coating, paper-cup texture and handmade surface irregularity.

### Ingredient D — `REF-PROD-ASSORTMENT-DETAIL` — PENDING
Role: `product_identity_secondary` + diversity evidence.
Close 3/4 group of 4–6 truffles showing multiple coating/color families together.

### Ingredient E — `REF-CHAR-CHOCOLATIERS` — PENDING
Role: `character_only`.
Project-specific clean reference of recurring miniature chocolatiers; no cheesecake or old-product contamination.

### Ingredient F — `REF-SCENE-KEYFRAME` — PENDING
Role: `scene_only` / `composition_only`.
Created after scenario/shot design; combines correct truffle product, tiny chocolatiers and target dark-studio composition.

### Ingredient G — RESERVED
Do not fill until QA identifies a concrete need. Potential use: second scene keyframe, repair-specific reference, or packaging geometry evidence.

## Current first-pass Flow budget recommendation
Do not upload every approved/alternate asset simultaneously. Proposed first video ingredient set after remaining creation:
1. `R0003` clean top identity;
2. `R0002` 45-degree geometry;
3. approved macro;
4. approved assortment detail;
5. approved chocolatier character reference;
6. approved scene keyframe;
7. reserved.

This intentionally uses six active roles, not seven redundant references.

## Reference creation order from here
1. `REF-PROD-MACRO` — generate two controlled candidates and QA.
2. `REF-PROD-ASSORTMENT-DETAIL` — generate two candidates and QA.
3. Generate character reference.
4. Lock final scenario/shot timeline.
5. Generate scene keyframe.
6. Build final Flow ingredient set from approved winners only.

## Current gate
`REF-PROD-TOP-CLEAN` is approved. `REF-PROD-HERO-45` is usable as secondary geometry evidence. Stage 04 does not pass until Macro and Assortment Detail also have approved candidates.
