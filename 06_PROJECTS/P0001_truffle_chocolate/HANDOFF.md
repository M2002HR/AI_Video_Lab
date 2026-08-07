# Project Handoff — P0001

## Project
- ID: `P0001`
- Deliverable: 10s, 16:9 AI product ad
- Target: Google Flow / Gemini Omni Flash / Ingredients-to-Video
- Current stage: `STAGE_04_REFERENCE_ASSET_CREATION`

## Context
The project adapts the tiny-chef creative template to the user's handmade colorful chocolate truffles. Product references for clean top identity, macro texture, assortment diversity and secondary novel-angle geometry have been generated and QA'd. The next controlled task is creating a clean character-only ingredient so the old cheesecake reference never needs to enter the final video generation.

## Current selected reference hierarchy
1. **Original real product photograph** — ultimate source authority/evidence.
2. `P0001-R0003` — selected `REF-PROD-TOP-CLEAN`, primary visible product identity (~4.8/5).
3. `P0001-R0008` — selected `REF-PROD-ASSORTMENT-DETAIL`, diversity/color/coating-family authority (~4.5/5).
4. `P0001-R0006` — selected `REF-PROD-MACRO`, texture/material/particle-scale authority only (~4.5/5).
5. `P0001-R0002` — provisional `REF-PROD-HERO-45`, secondary inferred geometry/depth (~4.3/5).

Approved alternates: R0004 TOP-CLEAN, R0007 ASSORTMENT, R0005 MACRO, R0001 HERO-45.

## Latest assortment evidence
- `R0008` selected: exactly six truffles, both coating families, supported colors, dark fluted cups, dark-neutral studio background.
- `R0007` alternate: good diversity but reintroduced wooden tabletop from original source despite prompt; recorded in `OBS-0005`.
- Both generated assortment views remain somewhat more spherical/regular than the handmade source, so geometry authority stays with original/R0003.

## Exact next action
Generate exactly two `REF-CHAR-CHOCOLATIERS` candidates using:
`11_PROMPT_PACKAGES/PKG_CHARACTER_REFERENCE_V01/prompt.txt`

### Input
Use the old tiny-chef/cheesecake creative image only as CHARACTER STYLE DNA. Do not upload the truffle product references in this character-only step. The prompt must strip away cheesecake, cherries, ladders, carts, tools and all old product/scene content.

### Desired output
Exactly three recurring miniature adult chocolatiers, full-body, matching rich-red chef uniforms/hats, distinct but coherent identities, correct anatomy, clean dark-neutral background, no food/product/props.

Expected next Runs: `P0001-R0009`, `P0001-R0010`.

After attachment:
1. score character count, anatomy, uniform consistency, style match, silhouette readability, plastic/toy artifact risk and background cleanliness;
2. select one character ingredient;
3. then lock scenario/shot timeline and create the scene/keyframe ingredient.

## Planned first-pass Flow ingredient stack
- R0003 TOP-CLEAN
- R0008 ASSORTMENT
- R0006 MACRO
- R0002 HERO-45 (optional; may be omitted if redundant)
- selected character reference (pending)
- scene/keyframe reference (pending)
- one reserved slot

Operational image-reference budget: 7. Do not fill all slots automatically.

## Key evidence
- `13_EVALUATION/reports/reference_qa_hero45_v01.md`
- `13_EVALUATION/reports/reference_qa_top_clean_v01.md`
- `13_EVALUATION/reports/reference_qa_macro_v01.md`
- `13_EVALUATION/reports/reference_qa_assortment_v01.md`
- `09_LEARNING/observations/OBS-0003...OBS-0005`
- `11_PROMPT_PACKAGES/PKG_CHARACTER_REFERENCE_V01/prompt.txt`

## Media continuity
Binary media is not guaranteed to be stored in normal Git. Run metadata includes filenames/hashes. A future chat should ask only for a specific image if visual QA cannot access prior attachments; never ask the user to re-explain the project.
