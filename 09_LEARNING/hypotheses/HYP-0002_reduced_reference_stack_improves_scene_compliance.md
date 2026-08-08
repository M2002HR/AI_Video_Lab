# HYP-0002 — Reduced role-clean reference stack improves combined-scene compliance

status: open  
confidence: provisional  
linked_observation: OBS-0007

## Hypothesis
For P0001 combined product+character scene-keyframe generation, a very small reference stack containing only role-clean inputs plus a simpler no-prop scene will produce better source fidelity and instruction compliance than the v01 five-reference stack.

## v01 baseline
Inputs:
- original real product photo;
- R0003 TOP-CLEAN;
- R0008 ASSORTMENT;
- R0006 MACRO;
- R0010 CHARACTERS.

Result across R0011–R0013:
- repeated prop invention;
- scale drift;
- geometry regularization;
- oversized particle appearance;
- continuity setup failure;
- one candidate also leaked the original wooden/workshop environment.

## v02 test — deliberately minimal
Use ONLY:
1. `R0003` TOP-CLEAN — product/packaging identity and clean environment;
2. `R0010` CHARACTERS — exact three-chef appearance/style.

Do **not** upload the original real photo in this scene-synthesis pass even though it remains the project's ultimate truth source, because `OBS-0005` shows that its wooden environment can leak into multi-reference generation. `R0003` was specifically created as the cleaned source-preserving identity surrogate.

Do not upload R0006, R0008 or R0002 for the first v02 pass. If a specific missing geometry problem appears, add only the single reference required to diagnose it in a later controlled test.

Prompt/action changes:
- no brush or other tools;
- no bowls, loose ingredients or food debris;
- quiet inspection only;
- opening scene already physically inside the same kraft box that will later be revealed;
- all three faces visible in 3/4 view;
- truffle diameter target approximately three times one chef's full standing height;
- shorter prioritized prompt with fewer competing instructions.

## Success criteria
Compared with R0012 baseline, v02 should improve:
- product fidelity;
- particle scale;
- chef-to-truffle scale;
- prop cleanliness;
- face/identity readability;
- continuity readiness for pull-back to full-box reveal.

Do not promote as a global rule until repeated on other scene-generation cases or benchmarks.
