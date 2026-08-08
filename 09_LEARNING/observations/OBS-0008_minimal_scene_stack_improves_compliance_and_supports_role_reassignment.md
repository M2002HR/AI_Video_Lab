# OBS-0008 — Minimal scene stack improved compliance; strong off-timestamp images can be reassigned

status: provisional_observation  
project: P0001  
linked_hypothesis: HYP-0002  
linked_runs: P0001-R0011, P0001-R0012, P0001-R0013, P0001-R0014, P0001-R0015

## Observation
In P0001 combined scene generation, reducing the scene-input stack from five references to two role-clean references (R0003 product + R0010 characters) and removing all tools/active decoration language produced a large qualitative compliance improvement.

The v01 five-reference runs repeatedly invented bowls/tools/loose ingredients, regularized product geometry, failed requested scale/readability and staged the opening outside the final kraft box.

The v02 two-reference runs both:
- placed the scene physically inside the kraft box;
- kept exactly three recognizable recurring chefs;
- removed tool/bowl/loose-ingredient contamination;
- improved face readability;
- created coherent pull-back-compatible product worlds.

## Secondary observation — temporal role mismatch
Both successful v02 images showed more of the assortment than intended for the opening-macro timestamp. The stronger image (R0015) is therefore more useful as a scene master / mid-reveal anchor than as KF01.

This suggests a useful production behavior: if a generation strongly satisfies scene grammar, identity and continuity but misses only the intended camera distance/timestamp, consider reassigning it to a better-fitting storyboard role instead of discarding it. Then derive adjacent keyframes from that stable scene.

## Caveats
This is one project and one image model. Do not promote the reduced-reference-stack conclusion or role-reassignment workflow to a universal rule without additional projects/experiments.

The v02 runs still show:
- mild handmade-geometry regularization;
- character pose leakage from the identity reference;
- failure to reach the originally requested 1:3 chef-height/truffle-diameter ratio.

## Project action
- Select R0015 as combined `REF-SCENE-MASTER` / KF02-like anchor.
- Derive the true KF01 as a tighter camera view from R0015 rather than regenerating the whole combined world.
- Use R0003 only as product-identity backup in that derivation.
