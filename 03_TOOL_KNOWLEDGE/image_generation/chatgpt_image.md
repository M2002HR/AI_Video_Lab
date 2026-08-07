# ChatGPT Image — internal tool card

tool_id: TOOL-IMG-CHATGPT-IMAGE  
tool_name: ChatGPT Image  
category: image_generation  
verification_status: internal_observation_only  
last_verified: 2026-08-07

## Scope of this card
This card currently records **our own project evidence only**. Exact underlying model/version and vendor capability details are unknown for P0001 and must not be invented.

## Internal evidence
### P0001 — REF-PROD-HERO-45 baseline
- Runs: `P0001-R0001`, `P0001-R0002`
- Input: same original truffle product image.
- Prompt: same `PKG_REFERENCE_IMAGES_V01` → `RUN 1 — REF-PROD-HERO-45` prompt.
- User-reported result: the two candidates looked very similar to each other.
- Direct visual QA: pending because the shared ChatGPT URL was not retrievable in the current operator session.

## Current interpretation
Potentially promising repeatability / low inter-run variance for this specific prompt-reference combination. No claim yet about product-identity fidelity or comparative quality.

## Current recommendation status
`candidate_for_testing`, not preferred globally.

Before recommending ChatGPT Image over another tool for product multiview/reference generation, collect:
- direct image QA scores;
- multiple angle/task results;
- controlled comparison against another tool such as Nano Banana Pro when practical.

## Linked evidence
- `OBS-0001`
- `P0001-R0001`
- `P0001-R0002`
