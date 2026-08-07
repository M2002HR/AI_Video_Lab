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
- Direct visual QA completed after both images were attached.
- R0001 overall reference QA: ~`4.2/5`.
- R0002 overall reference QA: ~`4.3/5`; preferred provisional HERO-45 geometry reference.

### Strengths observed
- stable correct product category;
- strong coating/color-family preservation;
- clean dark reference backgrounds;
- good depiction of nonpareils vs elongated sprinkles;
- low inter-run variance / repeatability;
- useful reconstruction of 3D depth from a top-down source.

### Weaknesses observed
- handmade forms were regularized toward more uniform spheres/sizes;
- packing became more orderly/manufactured;
- kraft-box walls were inferred somewhat thicker/more polished;
- a generated novel angle is plausible reconstruction, not proof of hidden geometry.

## Current operational recommendation
`candidate_for_testing`.

For identity-critical handmade products:
- keep the real/source-derived image as primary identity authority;
- use ChatGPT-generated novel-angle views as secondary geometry references after QA;
- add explicit artisan-imperfection constraints;
- prefer conservative editing/non-generative cleanup for the primary source view.

Do not yet recommend ChatGPT Image globally over Nano Banana Pro or other tools. More angles/products and controlled comparisons are required.

## Linked evidence
- `OBS-0002`
- `OBS-0003`
- `P0001-R0001`
- `P0001-R0002`
- `06_PROJECTS/P0001_truffle_chocolate/13_EVALUATION/reports/reference_qa_hero45_v01.md`
