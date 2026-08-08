# OBS-0010 — Product truth reference can override scene master during wide camera derivation

status: observation  
confidence: provisional  
project: P0001  
linked_runs: P0001-R0018, P0001-R0019  
linked_scene_master: P0001-R0015

## Observation
When deriving a wider final-hero camera state from `R0015` while also supplying `R0003` as product/packaging backup, both outputs shifted strongly toward the global arrangement encoded by `R0003` instead of preserving the exact local world encoded by `R0015`.

Repeated effects across both v04 candidates:
- the traceable central multicolor hero from R0015 disappeared/reconfigured;
- the local neighboring layout was rebuilt;
- the full-box arrangement became more source-like but less spatially continuous with R0015.

Additional failure in R0019:
- the three chefs moved outside/in front of the box rather than preserving their established inside-box positions.

## Interpretation
A strong complete product reference may be beneficial for product identity but harmful to camera-only scene derivation when it conflicts with a partially established scene master. The model may optimize toward the more globally coherent reference rather than preserve local spatial continuity.

## Immediate project rule
For the next KF03 derivation test, use `R0015` alone. Keep `R0003` as product truth for later Flow prompting/ingredient selection rather than injecting it into every storyboard-camera derivation.

## Scope warning
This is not yet a global rule. It needs repetition on other scene-master derivations or a controlled benchmark before promotion.
