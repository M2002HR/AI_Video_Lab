# OBS-0007 — Combined-scene generation can amplify role bleed and prop invention

status: observation  
confidence: provisional  
project: P0001  
evidence: P0001-R0011, P0001-R0012, P0001-R0013

## Observation
Three KF01 combined-scene candidates generated from the same long scene prompt and five-reference stack repeatedly produced the same classes of error:
- extra tools/bowls/loose ingredients despite strict exclusions;
- chefs larger than the requested chef-to-truffle ratio;
- over-perfect hero-truffle geometry;
- oversized nonpareils;
- one recurring chef often shown from behind;
- opening scene detached from the kraft box that must later be revealed.

One candidate also reintroduced a wooden workshop/background product context.

## Interpretation
The failure pattern suggests that adding more detailed negative wording is unlikely to be the best first repair. The combined task may be over-conditioned by imperfect supporting references and by action/workshop language that encourages scene invention.

In particular, R0006 and R0008 are useful within narrow reference roles but contain generated regularization that becomes undesirable when they are used as broad scene-synthesis inputs.

## Current project action
For KF01 v02:
- reduce the image-reference stack;
- remove macro and assortment generated references from scene synthesis;
- remove tools/action props entirely;
- place the entire opening scene physically inside the same kraft box;
- keep all three character faces readable;
- simplify prompt priority hierarchy.

## Boundary
This is P0001 evidence from ChatGPT Image scene synthesis. It is not yet a universal rule for all models or products.
