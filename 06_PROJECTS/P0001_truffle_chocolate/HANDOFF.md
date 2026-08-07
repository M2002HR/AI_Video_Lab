# Project Handoff — P0001

## Project
- ID: `P0001`
- Deliverable: 10s, 16:9 AI product ad
- Target: Google Flow / Gemini Omni Flash / Ingredients-to-Video
- Current stage: `STAGE_04_REFERENCE_ASSET_CREATION`

## Context
The project adapts a tiny-chef cheesecake template to the user's handmade colorful chocolate truffles. Product identity, source-prompt analysis and reference strategy are established. HERO-45, TOP-CLEAN and MACRO reference roles have now been generated and directly QA'd.

## Current reference hierarchy
1. **Original real product photograph** — ultimate source authority.
2. `P0001-R0003` — selected `REF-PROD-TOP-CLEAN`, primary clean identity ingredient (~4.8/5).
3. `P0001-R0006` — selected `REF-PROD-MACRO`, texture/material-scale authority only (~4.5/5).
4. `P0001-R0002` — selected provisional `REF-PROD-HERO-45`, secondary inferred geometry reference (~4.3/5).

Approved alternates: R0004 TOP-CLEAN, R0005 MACRO, R0001 HERO-45.

## Important learning
- Novel-angle generation can regularize handmade geometry and infer unsupported packaging thickness (`OBS-0003`).
- Macro generation can provide useful particle/material evidence while still introducing shape or wrapper interpretation; macro refs therefore get explicit texture/material-only authority (`OBS-0004`).
- Lower-authority references must not override visible facts from higher-authority sources.

## Exact next action
Generate exactly two `REF-PROD-ASSORTMENT-DETAIL` candidates using:
`11_PROMPT_PACKAGES/PKG_REFERENCE_IMAGES_V04_ASSORTMENT/prompt.txt`

Preferred inputs:
1. original real product photo;
2. R0003 clean top;
3. R0006 macro only as particle/material-scale support.

Do not use R0002/R0001 HERO-45 for this pass. Keep prompt and inputs identical across the two runs. After attachment, register as `P0001-R0007` and `P0001-R0008`, perform Stage 05 QA and select one assortment-diversity ingredient before character generation.

## What QA should test next
- exactly six truffles;
- both round nonpareils and elongated sprinkles;
- supported distinct color families;
- handmade variation without cloned geometry;
- correct dark fluted cups;
- realistic edible particle scale;
- no invented coating families;
- clean 3/4 group readability.

## Key evidence files
- `13_EVALUATION/reports/reference_qa_hero45_v01.md`
- `13_EVALUATION/reports/reference_qa_top_clean_v01.md`
- `13_EVALUATION/reports/reference_qa_macro_v01.md`
- `12_RUNS/P0001-R0001` ... `P0001-R0006`
- `03_PRODUCT_IDENTITY/identity_lock_v02.md`
- `04_REFERENCE_STRATEGY/reference_plan.md`
- `11_PROMPT_PACKAGES/PKG_REFERENCE_IMAGES_V04_ASSORTMENT/`
- repo-global `OBS-0002`, `OBS-0003`, `OBS-0004`.

## Media continuity
Generated binaries are not committed to normal Git; hashes and attachment IDs are stored in Run metadata where available. If a new session needs visual comparison and cannot access the attachments, ask only for the needed images, not for project re-explanation.
