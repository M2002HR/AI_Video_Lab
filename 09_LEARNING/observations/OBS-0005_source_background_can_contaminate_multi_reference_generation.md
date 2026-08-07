# OBS-0005 — Source background can contaminate multi-reference generation

- Date: 2026-08-08
- Project: `P0001`
- Runs: `P0001-R0007`, `P0001-R0008`
- Task: `product_reference_generation_assortment_detail`
- Tool: ChatGPT Image
- Evidence level: provisional project observation

## Observation
Two assortment-detail candidates were generated with the same prompt and reference stack. Both correctly followed the requested six-truffle diversity structure. However, R0007 reintroduced the wooden tabletop visible in the original real source photograph even though the prompt explicitly required a dark-neutral studio background and the supporting cleaned references used a dark studio environment. R0008 followed the requested dark background.

## What this suggests
A visually dominant source environment can leak into a generated reference even when its role is intended to be product-identity authority only. Textual role separation and negative constraints reduce but do not eliminate this contamination risk.

## Practical implication
For future identity-critical reference generation where the original source environment is unwanted:
1. preserve the original source as evidence authority;
2. prefer a cleaned/segmented source as the active generation input when possible;
3. explicitly assign the original source authority to product facts only;
4. QA background/style contamination separately from product fidelity;
5. do not reject an otherwise useful model globally from one contaminated run—compare sibling runs and other products.

## Related observations
- `OBS-0003` — conservative source-preserving cleanup retained identity better than novel-angle reconstruction.
- `OBS-0004` — macro generation is useful for particle/material scale but may regularize silhouette/wrapper material.

## Promotion status
Do not promote to a universal rule yet. Re-test on future products with strong source backgrounds.
