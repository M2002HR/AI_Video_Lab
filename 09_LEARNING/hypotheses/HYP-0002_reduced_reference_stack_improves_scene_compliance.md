# HYP-0002 — Reduced role-clean reference stack improves combined-scene compliance

status: project_supported / still provisional globally  
confidence: moderate_to_strong_for_P0001  
linked_observations: OBS-0007, OBS-0008

## Hypothesis
For P0001 combined product+character scene-keyframe generation, a smaller reference stack containing only high-authority/role-clean inputs plus a simpler no-prop scene will produce better source fidelity and instruction compliance than the v01 five-reference stack.

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
- character readability problems;
- opening staged outside the final kraft-box continuity;
- one candidate leaked wooden/workshop environment.

## v02 controlled repair
Inputs:
- R0003 TOP-CLEAN;
- R0010 CHARACTERS.

Deliberate removals:
- original wooden-background source;
- R0006 MACRO;
- R0008 ASSORTMENT;
- R0002 HERO-45;
- all brushes/tools/bowls/loose ingredients.

Results:
- R0014 ~4.1/5;
- R0015 ~4.3/5, selected scene master.

Both outputs:
- exist physically inside the kraft box;
- contain exactly three recognizable recurring chefs;
- have zero tool/bowl/loose-ingredient contamination;
- improve face readability and combined-scene coherence;
- provide a plausible world for a continuous pull-back.

## Interpretation
The P0001 evidence strongly supports the narrow project hypothesis that fewer role-clean references plus reduced action complexity improved scene compliance versus the v01 setup.

However, v02 still did not fully satisfy:
- the original 1:3 chef-height/truffle-diameter scale target;
- opening-macro camera distance;
- handmade-geometry fidelity;
- full removal of static pose influence.

R0015 is therefore repurposed as a scene master / KF02-like anchor, and the true opening frame will be derived from it rather than independently resynthesized.

## Global status
Do NOT promote this to a universal prompt/tool rule yet. Confirm on additional products or a controlled benchmark/experiment before global promotion.

## Next evidence step
Derive KF01 from R0015 using a camera-only edit with R0003 as product-identity backup. This tests whether stabilizing one combined scene and deriving adjacent camera states outperforms repeated independent scene generation.
