# OBS-0003 — Conservative top-clean editing preserved product identity better than novel-view generation

- Date: 2026-08-07
- Project: `P0001`
- Compared Runs: `P0001-R0001..R0004`
- Evidence level: provisional project observation

## Observation
For the P0001 truffle product, conservative top-down cleanup/editing (`R0003`, `R0004`) preserved the real product's arrangement, count, coating/color distribution, paper cups and packaging substantially better than generating a new 35–45 degree view (`R0001`, `R0002`) from the same top-down source.

## Likely explanation
The top-clean task stays close to geometry directly evidenced by the source, while a novel 3/4 view forces the image model to infer hidden depth and shape. That inference introduced mild regularization: more uniform spheres/sizes and a more polished box.

## Practical implication for P0001
Use a conservative cleaned source view as primary identity authority and generated novel views only as secondary geometry evidence.

## What this does NOT prove
This is not yet a universal rule for every product or every image model. Products with strong multi-view source photography may behave differently.

## Candidate general hypothesis
When only one identity-critical source angle exists, conservative source-preserving edit/segmentation is likely safer as the primary identity reference than asking a generative model to synthesize a new angle. Novel generated views may still be useful as secondary references.

## Next validation
Test this pattern across future products, especially rigid packaging, reflective products and complex asymmetrical geometry, before promoting to a global SOP rule.
