# OBS-0003 — Novel-view generation regularized handmade product geometry

- Date: 2026-08-07
- Project: `P0001`
- Runs: `P0001-R0001`, `P0001-R0002`
- Tool: ChatGPT Image
- Task: generate a 35–45° product view from one original top-down product image.
- Evidence level: project observation after direct visual QA.

## Observation
Both generated HERO-45 candidates preserved the correct truffle category, major coating/color families, dark fluted cups and kraft-box concept, but both made the assortment more regular and manufactured than the original photo. Truffles became more uniformly spherical, similarly sized and evenly presented. The kraft box was also inferred with thicker/more polished geometry than the source proves.

## Interpretation
When a new view requires substantial hidden-geometry inference from a single top-down source, a generative image model may create a plausible product reconstruction rather than a factual view. For artisan products this reconstruction can regularize natural imperfections.

## Consequence for P0001
- Keep generated HERO-45 as secondary geometry evidence.
- Promote a conservative cleaned top-down source-derived image to `product_identity_primary`.
- Add explicit artisan-variation constraints to later prompts.
- Do not let a generated novel-angle reference override original-source traits when they conflict.

## Prompt correction to test
Explicitly preserve natural variation in sphere shape, diameter, coating density, particle distribution and placement. State that the product must feel handmade by an artisan chocolatier rather than standardized by a factory.

## Generalization status
Do **not** promote this to a universal model rule yet. Test across more handmade/organic products and/or controlled tool comparisons.
