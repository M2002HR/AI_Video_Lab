# Project Handoff — P0001

## Project
- ID: `P0001`
- Deliverable: 10s, 16:9 AI product ad
- Target: Google Flow / Gemini Omni Flash / Ingredients-to-Video
- Current stage: `STAGE_04_REFERENCE_ASSET_CREATION`

## Context
The project adapts a tiny-chef cheesecake template to the user's handmade colorful chocolate truffles. Product identity, source-prompt analysis and reference strategy are established. HERO-45 and TOP-CLEAN reference candidates have now been generated and directly QA'd.

## Locked / active decisions
- Ultimate identity authority: original real product photo.
- Active identity injection: `03_PRODUCT_IDENTITY/identity_lock_v02.md`.
- Active strategy: `04_REFERENCE_STRATEGY/reference_plan.md` (v2 content).
- Separate Ingredients remain preferred over collage pending `EXP-0001`.
- Operational Omni ingredient cap: 7; current first-pass design targets six distinct roles and reserves one slot.

## Current approved references
### Primary clean identity
`P0001-R0003` → `REF-PROD-TOP-CLEAN` — APPROVED / SELECTED (~4.8/5).
- visually preserves the same 25-truffle layout and source color/coating arrangement;
- watermark and wooden background removed;
- high product information density.

`P0001-R0004` → approved TOP-CLEAN alternate (~4.7/5).

### Secondary geometry
`P0001-R0002` → `REF-PROD-HERO-45` — PASS WITH CAVEATS / selected secondary geometry (~4.3/5).
`P0001-R0001` → alternate HERO-45 (~4.2/5).

45-degree generation showed mild handmade→factory regularization, so generated novel views may support depth but must not override the original/clean-top identity (`OBS-0003`).

## Exact next action
Generate **two** `REF-PROD-MACRO` candidates using:
`11_PROMPT_PACKAGES/PKG_REFERENCE_IMAGES_V03_MACRO/prompt.txt`

Preferred image inputs if multiple references are supported by the chosen image tool:
1. original real product photo — highest authority;
2. `P0001-R0003` — clean top supporting reference.

Do NOT use R0001/R0002 as macro input.

Keep prompt and inputs identical for both candidate generations. Expected future Runs: `P0001-R0005`, `P0001-R0006`.

After upload:
1. register/hash both assets;
2. score edible particle scale, handmade geometry, dark-chocolate behavior, paper cup, material realism and artifacts;
3. select macro winner or revise prompt;
4. only then proceed to `REF-PROD-ASSORTMENT-DETAIL`.

## Key evidence files
- `13_EVALUATION/reports/reference_qa_hero45_v01.md`
- `13_EVALUATION/reports/reference_qa_top_clean_v01.md`
- `12_RUNS/P0001-R0001..R0004/`
- `09_LEARNING/observations/OBS-0003_top_clean_edit_preserves_identity_better_than_novel_view.md`
- `11_PROMPT_PACKAGES/PKG_REFERENCE_IMAGES_V03_MACRO/`

## Media continuity
Generated binaries are not committed to normal Git; hashes and filenames are stored in Run metadata. A future session should ask only for any specific media required for visual QA, not for project re-explanation.
