# Project Handoff — P0001

## Project
- ID: `P0001`
- Title: Colorful Chocolate Truffle Miniature Commercial
- Deliverable: 10s, 16:9 AI product ad
- Target: Google Flow / Gemini Omni Flash / Ingredients-to-Video
- Current stage: `STAGE_04_REFERENCE_ASSET_CREATION`

## Context
The project adapts a supplied 10-second tiny-chef chocolate-cherry-cheesecake template to the user's real handmade colorful chocolate truffles. We preserve the template's miniature-worker, premium macro commercial and timed-storytelling DNA while removing all cheesecake/cherry/process content. Product identity, source-prompt analysis, reference strategy and the first reference prompt package are documented.

## Locked / operationally accepted
- Product category: handmade chocolate truffles.
- Identity-critical presentation: colorful nonpareils/elongated sprinkles, dark fluted paper cups, open natural kraft box, handmade near-spherical geometry.
- Source watermark is not identity and must not appear downstream.
- Old cheesecake storyboard has style/creative authority only, never product-identity authority.
- Reference-collage default: do not use as production shortcut; separate single-role ingredients are the current default pending EXP-0001.
- Omni ingredient planning limit: 7 operational slots, but target 4–6 active refs and reserve headroom.

## Latest real generation evidence
The user generated two first-pass `REF-PROD-HERO-45` candidates with **ChatGPT Image**, not Nano Banana Pro:
- `P0001-R0001`
- `P0001-R0002`

Both used the same original product reference and the same project prompt. User feedback: **the two outputs look very similar to each other**. This is recorded as `OBS-0001` as possible evidence of low inter-run variance, but does not yet prove that either output is faithful to the source product.

Shared generation URL:
https://chatgpt.com/s/m_6a76360f676c8191872d12bfe552c957

The current operator could not retrieve that shared URL, so visual QA is pending.

## Exact next action
Ask the user to attach both generated images directly in chat. Then:
1. compare each against the original product photo;
2. score product category, geometry/proportion, coating types, color diversity, paper cups, kraft-box structure, material realism, artifacts and usefulness as Flow ingredient;
3. compare R0001 vs R0002;
4. decide `PASS`, `MINOR PROMPT FIX`, `STRUCTURAL STRATEGY CHANGE`, or controlled `ChatGPT Image vs Nano Banana Pro` test;
5. only after baseline approval continue to Slots 2–4.

## Important files
1. `STATUS.md`
2. `00_BRIEF/brief.md`
3. `01_INPUTS/input_manifest.md`
4. `01_INPUTS/source_prompt/source_prompt_transcription.md`
5. `02_SOURCE_ANALYSIS/source_prompt_analysis.md`
6. `03_PRODUCT_IDENTITY/product_identity.md`
7. `04_REFERENCE_STRATEGY/reference_plan.md`
8. `11_PROMPT_PACKAGES/PKG_REFERENCE_IMAGES_V01/REFERENCE_IMAGE_PROMPT_PACKAGE.md`
9. `12_RUNS/P0001-R0001/run.json`
10. `12_RUNS/P0001-R0002/run.json`
11. `18_CONVERSATION_LOG/FEEDBACK_LOG.md`
12. `09_LEARNING/observations/OBS-0001.md` (repo-global)
13. `03_TOOL_KNOWLEDGE/image_generation/chatgpt_image.md` (repo-global)

## Media re-attach note for a future chat
Original and generated binary media are not necessarily committed to normal Git. For the immediate next step, the two ChatGPT Image candidates must be attached directly if the connector cannot access them. Do not ask the user to re-explain the project.
