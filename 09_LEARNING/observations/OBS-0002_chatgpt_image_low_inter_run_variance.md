# OBS-0002 — Low inter-run variance in ChatGPT Image HERO-45 reference generation

- Date: 2026-08-07
- Project: `P0001`
- Runs: `P0001-R0001`, `P0001-R0002`
- Task: `product_reference_generation_hero_45`
- Tool: ChatGPT Image
- Evidence level: direct project visual QA; still only one product/task.

## Observation
Two candidates generated from the same original product reference and the same prompt are strongly similar in composition, product interpretation, color/coating families, box treatment and overall quality. Direct inspection confirms the user's initial report of low inter-run variance.

## Positive signal
For this particular prompt/reference combination, ChatGPT Image produced repeatable outputs with stable product category and clean presentation.

## Shared error tendency
The two Runs also share the same mild bias: handmade truffle geometry is regularized toward more uniform spheres/sizes and the kraft box is reconstructed somewhat more thickly/polished than the original. Repeatability therefore includes both strengths and shared reconstruction bias.

See `OBS-0003` for the artisan-regularization finding.

## What this does NOT establish
- global superiority over Nano Banana Pro or another image model;
- fidelity on unseen angles/products;
- that repeatability is always desirable;
- that two similar outputs constitute independent proof of factual geometry.

## Promotion status
Keep as project evidence. Comparative tool recommendation requires additional tasks/products or a controlled experiment.
