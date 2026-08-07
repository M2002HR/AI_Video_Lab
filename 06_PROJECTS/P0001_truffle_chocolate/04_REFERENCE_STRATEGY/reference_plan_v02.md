# P0001 Reference Strategy v2 — after HERO-45 QA

Supersedes v1 for active production decisions while preserving `reference_plan.md` as history.

## Key change from v1
Direct QA showed that generated novel-angle images are useful but infer and regularize hidden product geometry. Therefore **source-derived identity evidence outranks generated novel-angle evidence**.

## Current active Ingredient plan (max operational budget: 7)

### Slot 1 — `REF-PROD-TOP-CLEAN` — PRIMARY
Role: `product_identity_primary` + `composition_only`.
Create a conservative edit of the real original top-down product photo. Preserve product pixels/structure as much as possible; remove watermark and replace/diminish the wooden environment. This is the highest-authority product identity ingredient.

### Slot 2 — `REF-PROD-HERO-45` — SECONDARY
Role: `geometry_view` + `product_identity_secondary`.
Selected provisional candidate: `P0001-R0002`. Useful for box depth, truffle height and cup geometry, but it must not override original-source traits. Caveat: mild factory regularization and inferred box thickness.

### Slot 3 — `REF-PROD-MACRO`
Role: `texture_detail`.
One representative handmade truffle in its dark fluted cup. Must show edible scale, chocolate, coating micro-texture and paper folds. Use identity lock v02.

### Slot 4 — `REF-PROD-ASSORTMENT-DETAIL`
Role: `product_identity_secondary` + `coating_diversity`.
4–6 truffles showing both nonpareil and elongated-sprinkle families plus major color diversity. Preserve artisan variation.

### Slot 5 — `REF-CHAR-CHOCOLATIERS`
Role: `character_only`.
Clean project-specific tiny chocolatier reference with no cheesecake/old product contamination.

### Slot 6 — `REF-SCENE-KEYFRAME`
Role: `scene_only` + `composition_only`.
Created after final shot design. Should already combine correct truffle identity, characters and target studio scene.

### Slot 7 — RESERVED
Do not fill by default. Use only if QA reveals a concrete missing constraint.

## Authority order
1. original real product image / conservative source-derived edit;
2. approved source-faithful detail references;
3. approved generated novel-angle geometry references;
4. character reference (no product authority);
5. scene/style keyframe (no authority to redesign product).

## Current generation order
1. Generate `REF-PROD-TOP-CLEAN` with a conservative edit prompt.
2. QA two candidates; prefer the candidate that changes the fewest product facts.
3. Then create Macro and Assortment Detail using `identity_lock_v02.md`.
4. Only after Slots 1–4 pass QA, create character reference.
5. Scene keyframe follows scenario/shot design.

## Contact sheet policy
No change: separate single-role Ingredients remain the default. Collage/contact-sheet use remains experimental under `EXP-0001`.

## HERO-45 evidence
See `13_EVALUATION/reports/reference_qa_hero45_v01.md`. `P0001-R0002` currently holds the provisional HERO-45 role.
