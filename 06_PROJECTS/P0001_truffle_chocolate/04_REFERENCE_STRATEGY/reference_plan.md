# P0001 Reference Strategy v1

## Target generation mode
Google Flow → Video → Ingredients/References → Gemini Omni Flash → 10 seconds → 16:9.

## Ingredient budget
- Operational maximum for Omni Flash: **7 image-reference slots**. This is corroborated by current third-party Flow API documentation exposing `referenceImage_1..7`; the current official Google Flow Help confirms Omni Flash Ingredients/References supports 4s/6s/8s/10s but does not currently state the numeric 7-slot limit on the Help page.
- Treat 7 as a provisional operational limit that should be re-verified when Flow UI/model behavior changes.
- **Do not fill all seven automatically.** Default production target is 4–6 high-information, non-conflicting references and 1–2 spare slots for later iteration.

## Official Google best-practice constraints
Google Flow Help currently advises:
1. product/subject ingredients should use plain or segmented backgrounds;
2. location/style references should avoid extra subjects unless intentional;
3. text prompts should complement rather than contradict visual inputs;
4. prompt should explicitly reference the supplied ingredients;
5. ingredient images with a consistent look/feel blend more effectively.

Sources verified 2026-08-07:
- https://support.google.com/flow/answer/16353334?hl=en
- https://support.google.com/flow/answer/16352836?hl=en

Operational corroboration for 7 refs (not an official Google source):
- https://useapi.net/docs/articles/omni-flash-bash — documents Omni Flash `referenceImage_1..7` and a combined seven-image reference budget.

## Collage / contact-sheet policy
**Default: do not combine multiple product views into one collage to save ingredient slots.**

Reasoning:
- Google recommends clean single-subject/product references and warns against extra subjects in style/location references.
- A multi-view contact sheet contains several visual instances of the product inside one image; the model can interpret them as multiple scene objects/composition rather than independent identity evidence.
- It also makes reference-role assignment less explicit and may increase duplication or geometry ambiguity.
- Therefore a collage is not considered equivalent to several independent ingredient slots.

This is an inference from Google's published best practices, not an explicit Google prohibition. We will test it later as `EXP-0001` rather than treat it as universal fact.

If a collage must be tested:
- keep it product-only;
- neutral consistent background;
- no style reference mixed into the same sheet;
- no labels/arrows/text unless necessary;
- 2–4 orthogonal views maximum;
- use it as a secondary experimental reference, not the primary identity source;
- A/B test it against the same views uploaded separately.

## P0001 candidate reference pack

### Slot 1 — `REF-PROD-HERO-45`
Role: `product_identity_primary` + `geometry_view`.
Clean 3/4 45-degree hero view of the full open kraft box. Shows box depth, truffle height, paper cups and assortment.

### Slot 2 — `REF-PROD-TOP`
Role: `product_identity_secondary` + `composition_only`.
Cleaned top-down version of the original product photo, with watermark/table distractions removed while preserving the assortment identity.

### Slot 3 — `REF-PROD-MACRO`
Role: `texture_detail`.
Macro close-up of one representative truffle in its dark fluted cup; must clearly show chocolate beneath nonpareils/sprinkles and food-scale surface realism.

### Slot 4 — `REF-PROD-ASSORTMENT-DETAIL`
Role: `product_identity_secondary`.
Close 3/4 group of 4–6 truffles showing the main coating/color families together. Helps prevent the model from collapsing the assortment into one color/style.

### Slot 5 — `REF-CHAR-CHOCOLATIERS`
Role: `character_only`.
Clean project-specific reference of the miniature chocolatiers: same red uniforms/hats, proportions and premium miniature realism, but **no cheesecake or old dessert**.

### Slot 6 — `REF-SCENE-KEYFRAME`
Role: `scene_only` / `composition_only`.
Created later after scenario/shot design: a project-specific keyframe that already combines the correct truffle product, tiny chocolatiers and target black studio scene.

### Slot 7 — RESERVED
Do not fill during first pass. Possible later uses: a second scene keyframe, packaging geometry reference or repair-specific ingredient if evaluation shows a concrete need.

## Reference creation order
1. Generate/clean Slots 1–4 first.
2. Run Reference QA against the original product.
3. Reject identity-drifting images before they can contaminate downstream generations.
4. Generate Slot 5 character reference separately.
5. After final shot design, generate Slot 6 scene keyframe.
6. Build the final active ingredient set from approved assets only.

## Current gate
Stage 04 passes only when Slots 1–4 have at least one approved candidate each. Slot 5 is required before final video generation. Slot 6 is created after storyboard/keyframe design.
