# ChatGPT Image — internal tool card

tool_id: TOOL-IMG-CHATGPT-IMAGE  
tool_name: ChatGPT Image  
category: image_generation  
verification_status: internal_observation_only  
last_verified: 2026-08-07

## Scope
This card records our project evidence. Exact underlying model/version/settings for P0001 are unknown and must not be invented.

## Internal evidence
### P0001 — REF-PROD-HERO-45 baseline
- Runs: `P0001-R0001`, `P0001-R0002`
- Same original truffle source image and same `PKG_REFERENCE_IMAGES_V01/RUN_1` prompt.
- Direct visual QA completed.
- R0001: ~`4.2/5`.
- R0002: ~`4.3/5`; selected secondary HERO-45 geometry reference.

Observed strengths:
- stable correct product category;
- strong coating/color-family preservation;
- clean reference backgrounds;
- good nonpareil vs elongated-sprinkle distinction;
- low inter-run variance;
- useful inferred 3D depth.

Observed weaknesses:
- handmade forms regularized toward more uniform spheres/sizes;
- packing looked more manufactured;
- kraft-box walls inferred somewhat thicker/more polished;
- novel view is plausible reconstruction, not evidence of hidden geometry.

### P0001 — REF-PROD-TOP-CLEAN conservative edit
- Runs: `P0001-R0003`, `P0001-R0004`.
- Task: preserve visible source product and arrangement while removing watermark/wooden background.
- R0003: ~`4.8/5`; selected primary clean identity ingredient.
- R0004: ~`4.7/5`; approved alternate.

Observed strengths:
- retained the visible 25-truffle count and diamond layout;
- retained source-like color/coating placement with high fidelity;
- preserved dark fluted cups and simple kraft-box concept;
- removed watermark and environmental contamination cleanly;
- much lower identity drift than novel-angle generation.

Residual weakness:
- mild generative cleanup/regularization remains; this is not a literal pixel-preserving cutout.

## Current operational recommendation
`candidate_for_testing` — useful in this workflow, but not globally preferred over other image tools yet.

For identity-critical products with only one real source angle:
1. keep the original real image as ultimate authority;
2. prefer conservative edit/cleanup for the primary clean identity ingredient;
3. use generated novel-angle views only as secondary geometry evidence after QA;
4. explicitly constrain artisan imperfection where relevant;
5. compare against other tools on future projects before global promotion.

## Linked evidence
- `OBS-0002`
- `OBS-0003`
- `P0001-R0001..R0004`
- `06_PROJECTS/P0001_truffle_chocolate/13_EVALUATION/reports/reference_qa_hero45_v01.md`
- `06_PROJECTS/P0001_truffle_chocolate/13_EVALUATION/reports/reference_qa_top_clean_v01.md`
