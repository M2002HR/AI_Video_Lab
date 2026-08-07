# Project Handoff — P0001

## Project
- ID: `P0001`
- Deliverable: 10s, 16:9 AI product ad
- Target: Google Flow / Gemini Omni Flash / Ingredients-to-Video
- Current stage: `STAGE_04_REFERENCE_ASSET_CREATION`

## Context
The project adapts a tiny-chef cheesecake template to the user's handmade colorful chocolate truffles. Product identity, source-prompt analysis and reference strategy are established. Two real HERO-45 reference generations from ChatGPT Image have now been directly reviewed.

## Current locked / active decisions
- Highest authority remains the **original real product photo**.
- Active identity injection: `03_PRODUCT_IDENTITY/identity_lock_v02.md`.
- Active strategy: `04_REFERENCE_STRATEGY/reference_plan_v02.md`.
- Generated novel-angle references are supporting evidence, not replacements for visible source facts.
- `P0001-R0002` is provisional `REF-PROD-HERO-45` secondary geometry reference (~4.3/5).
- `P0001-R0001` is alternate evidence (~4.2/5).
- HERO QA found good category/coating repeatability but mild factory-perfect regularization and inferred box geometry (`OBS-0002`, `OBS-0003`).
- Therefore `REF-PROD-TOP-CLEAN` is promoted to the future `product_identity_primary` role.
- Separate Ingredients remain preferred over collage pending `EXP-0001`.
- Operational Omni ingredient cap: 7; default target 4–6.

## Exact next action
Generate **two** `REF-PROD-TOP-CLEAN` candidates using only the original real product photo and:
`11_PROMPT_PACKAGES/PKG_REFERENCE_IMAGES_V02/REF_PROD_TOP_CLEAN_PROMPT.md`

Preferred method order:
1. non-generative cleanup/segmentation if practical;
2. otherwise conservative image edit;
3. do not free-regenerate from text alone.

After the two outputs are attached, register them as `P0001-R0003` and `P0001-R0004`, perform Stage 05 QA, and select the primary identity reference. Do not move to Macro/Assortment until TOP-CLEAN passes.

## Key evidence files
- `13_EVALUATION/reports/reference_qa_hero45_v01.md`
- `12_RUNS/P0001-R0001/`
- `12_RUNS/P0001-R0002/`
- `03_PRODUCT_IDENTITY/identity_lock_v02.md`
- `04_REFERENCE_STRATEGY/reference_plan_v02.md`
- `11_PROMPT_PACKAGES/PKG_REFERENCE_IMAGES_V02/REF_PROD_TOP_CLEAN_PROMPT.md`
- repo-global `OBS-0002`, `OBS-0003`, and ChatGPT Image tool card.

## Media continuity
Generated binaries are not committed to normal Git; hashes are stored in Run metadata. If a new session needs direct visual comparison and cannot access the attachments, ask only for the needed candidate images, not for project re-explanation.
