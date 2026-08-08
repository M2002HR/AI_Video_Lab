# Project Handoff — P0001

## Project
- ID: `P0001`
- Deliverable: 10s, 16:9 AI product ad
- Target: Google Flow / Gemini Omni Flash / Ingredients-to-Video
- Current stage: `STAGE_18_REPAIR_DECISION`

## Locked storyboard / scene anchors
- `R0016` — SELECTED KF01 / opening close camera state (~4.5/5).
- `R0015` — SELECTED SCENE MASTER / KF02-like mid state (~4.3/5).
- `R0020` — SELECTED KF03 / final farther+higher camera state (~4.5/5).

## Identity anchors used in Flow V01
- `R0003` — TOP-CLEAN product/packaging truth (~4.8/5).
- `R0010` — exact recurring three-chef appearance/style identity (~4.8/5).

## Current video result
### `R0022` — CURRENT BEST / SELECTED BASELINE
Google Flow / Gemini Omni Flash / 10s / 16:9.
Overall ~4.6/5.

Strong points:
- exact three-chef count remains stable in sampled timeline;
- central multicolor hero remains continuously traceable;
- smooth backward + shallow upward camera reveal;
- no tools, bowls, loose ingredients or scene clutter;
- product/box world remains coherent;
- stable final commercial hold.

Caveats:
- hero/product geometry still slightly more spherical/regular than real handmade source;
- final wide arrangement does not exactly reproduce KF03, but continuity inside the video itself is strong.

### `R0023` — REJECT
Overall ~3.6/5.
Hard failure: a fourth chef is invented in newly revealed off-screen space. A partial extra red-uniform chef is already visible around ~2.4s at the far-right edge, clearly present by ~3.0s, and persists through the final reveal.

Camera/product behavior is otherwise strong, making this a clean character-count reliability failure rather than a total architecture failure.

Evidence:
- `13_EVALUATION/reports/video_qa_flow_v01_r0022_r0023.md`
- `OBS-0012`

## Active interpretation
The five-image V01 stack is viable because R0022 passes strongly. Do not change the ingredient architecture yet.

The next controlled change is prompt-only: explicitly lock the entire world's population to the three chefs already visible at frame 0 and forbid any new chef/human in off-screen space revealed by the pull-back.

## Exact next action — V02 count-lock test
Keep EVERYTHING from V01 identical:
1. `R0016`
2. `R0015`
3. `R0020`
4. `R0003`
5. `R0010`

Same upload order, model, 10s duration, 16:9, and exposed settings.

Base prompt remains `PKG_FLOW_OMNI_VIDEO_V01/prompt.txt`.
Add ONLY the block in:
`11_PROMPT_PACKAGES/PKG_FLOW_OMNI_VIDEO_V02_COUNT_LOCK/prompt_delta.md`

Generate exactly two controlled runs:
- `P0001-R0024`
- `P0001-R0025`

Success gate:
- exactly three chefs from first through final frame;
- no chef enters from left/right/rear/off-screen area;
- preserve R0022-level camera continuity and hero traceability;
- no degradation in product identity or final hero hold.

If both pass, promote count-lock language into the active project prompt. If character duplication persists, change ingredient architecture next rather than adding more prompt length.

## Cross-chat continuity
A new ChatGPT session should read:
1. `AI_START_HERE.md`
2. this `HANDOFF.md`
3. `STATUS.md`
4. `13_EVALUATION/reports/video_qa_flow_v01_r0022_r0023.md`
5. `09_LEARNING/observations/OBS-0012.md`
6. `11_PROMPT_PACKAGES/PKG_FLOW_OMNI_VIDEO_V02_COUNT_LOCK/prompt_delta.md`

Ask only for media unavailable in the new session. Do not ask the user to re-explain project history.
