# HYP-0002 — Reduced role-clean reference stack improves combined-scene compliance

status: open  
confidence: provisional  
linked_observation: OBS-0007

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
- continuity setup failure.

## v02 test
Core inputs:
- original real product photo;
- R0003 TOP-CLEAN;
- R0010 CHARACTERS.

Optional fourth input:
- R0002 only as conservative box/cup depth support if the image tool can obey role separation.

Prompt/action changes:
- no brush or other tools;
- no loose ingredients;
- quiet inspection only;
- opening scene already physically inside the kraft box;
- all three faces visible;
- truffle diameter target approximately three times one chef's full standing height.

## Success criteria
Compared with R0012 baseline, v02 should improve:
- product fidelity;
- particle scale;
- chef-to-truffle scale;
- prop cleanliness;
- face/identity readability;
- continuity readiness for pull-back to full-box reveal.

Do not promote as a global rule until repeated on other scene-generation cases or benchmarks.
