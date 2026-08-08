# HYP-0003 — Master-only wide derivation preserves spatial continuity better than adding product truth

status: open  
confidence: provisional  
project: P0001  
linked_observation: OBS-0010

## Hypothesis
For an already-established combined product+character scene, deriving an adjacent wider camera state from the scene master alone will preserve object identity and local spatial relationships better than combining the scene master with a second complete product-layout reference.

## Evidence motivating test
KF03 v04 used:
- `R0015` scene master;
- `R0003` clean full-box product reference.

Both R0018 and R0019 snapped toward R0003's global layout and lost the traceable central hero/local arrangement from R0015. R0019 additionally moved the chefs outside the box.

## Controlled v05 test
Use ONLY:
- `R0015` scene master.

Keep task and desired camera direction comparable:
- farther backward;
- moderately higher;
- reveal more of the same box;
- preserve central hero identity/local neighborhood;
- preserve same three chefs and inside-box positions;
- zero props/loose ingredients.

Do not upload R0003 or any other reference in this pass.

## Success criteria
Compared with R0018/R0019:
- central multicolor hero remains traceable;
- local paper cup and nearby objects remain spatially coherent;
- same three chefs remain inside the box in the same broad region;
- camera path reads as outward extrapolation instead of scene reconstruction;
- no new props/debris.

## Decision rule
If master-only improves continuity sufficiently, use it as the selected KF03 derivation strategy and keep product truth references separate for final Flow ingredient prompting.

If master-only still fails, stop iterating the still-image endpoint indefinitely. Reassess whether the final full-box shot should be an aesthetic target rather than a strict interpolated endpoint, or whether the final reveal should be produced as a separate clip.
