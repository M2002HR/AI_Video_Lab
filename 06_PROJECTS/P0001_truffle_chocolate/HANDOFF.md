# Project Handoff — P0001

## Project
- ID: `P0001`
- Deliverable: 10s, 16:9 AI product ad
- Target: Google Flow / Gemini Omni Flash / Ingredients-to-Video
- Current stage: `STAGE_10_STORYBOARD`

## Context
The project adapts the supplied tiny-chef dessert creative template to the user's real handmade colorful chocolate truffles. Core product references and a clean recurring three-chef character reference are approved. The old cheesecake creative is now retired from downstream production use. Scenario v1 and the single-shot 10-second timing are locked; the next task is the first combined product+character scene keyframe.

## Current selected reference hierarchy
### Product
1. Original real product photograph — ultimate source authority.
2. `P0001-R0003` — TOP-CLEAN, primary visible identity (~4.8/5).
3. `P0001-R0008` — ASSORTMENT, diversity/color/coating authority (~4.5/5).
4. `P0001-R0006` — MACRO, micro material/particle scale only (~4.5/5).
5. `P0001-R0002` — optional HERO-45 inferred depth support (~4.3/5), use only if justified.

### Characters
`P0001-R0010` — selected `REF-CHAR-CHOCOLATIERS` (~4.8/5): exactly three recurring chefs with coherent red uniforms and stable facial cues. `R0009` is approved alternate (~4.7/5).

Character authority boundary: R0010 defines appearance/style only, NOT action, pose, tool, scene position or chef-to-truffle scale.

## Character QA
Both R0009 and R0010 successfully removed cheesecake/old-scene contamination. R0010 selected because Character C exposes more arm/body anatomy and the trio reads slightly better as a reusable cast. Recorded as `OBS-0006`.

## Selected scenario v1
`07_SCENARIOS/selected/scenario_v01_final_touch_reveal.md`

**Final Touch → Full Box Reveal**
- one continuous 10-second shot;
- opening macro on one multicolor hero truffle;
- exactly three tiny chefs remain near that local region;
- only one simple brush action plus minimal inspection gestures;
- camera performs one smooth pull-back along a shallow upward arc;
- assortment and kraft box are progressively revealed;
- last ~1 second becomes a stable premium product hero frame.

The scenario intentionally avoids manufacturing transformations, carrying truffles, large character travel and scene cuts to reduce morphing/duplication/continuity risk.

## Locked timing
`08_SHOT_DESIGN/timeline_v01.md`

Creative scale lock for v1: chef full-body height approximately 35–45% of one truffle diameter; keep scale constant throughout video.

## Storyboard plan
`09_STORYBOARD/storyboard_plan_v01.md`
- KF01 opening macro (~00:01)
- KF02 mid assortment reveal (~00:05)
- KF03 final hero (~00:09.2)

Generate separately, not as one production collage. QA KF01 before propagating the scene grammar.

## Exact next action
Generate **two** `SB/KF01` opening combined-scene candidates using:
`11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V01_KF01/prompt.txt`

### Preferred references
1. original real product photo;
2. R0003 TOP-CLEAN;
3. R0008 ASSORTMENT;
4. R0006 MACRO — material/particle scale only;
5. R0010 CHARACTER — appearance/style only.

Do NOT use the old cheesecake creative. Do NOT add R0002 HERO-45 during this first combined-scene test unless KF01 evidence later proves extra depth support is necessary.

Expected next Runs: `P0001-R0011`, `P0001-R0012`.

### KF01 QA priorities
- exact three-chef cast identity;
- correct chef-to-truffle scale;
- one hero multicolor truffle remains true to product family;
- tiny nonpareil scale/material;
- dark fluted paper cup;
- coherent anatomy and brush contact;
- no duplicated chef/truffle;
- no cheesecake contamination;
- dark premium studio world;
- scene can plausibly expand outward via a continuous camera pull-back.

## Planned first-pass Flow ingredient stack after KF01 approval
1. R0003 TOP-CLEAN
2. R0008 ASSORTMENT
3. R0006 MACRO
4. R0010 CHARACTERS
5. selected KF01 combined scene
6. optional R0002 HERO-45 only if needed
7. reserved

Preferred first Flow test should start with five active references rather than fill all seven automatically.

## Key evidence / docs
- `04_REFERENCE_STRATEGY/reference_plan.md` v3
- `13_EVALUATION/reports/reference_qa_character_v01.md`
- `07_SCENARIOS/selected/scenario_v01_final_touch_reveal.md`
- `08_SHOT_DESIGN/timeline_v01.md`
- `09_STORYBOARD/storyboard_plan_v01.md`
- `11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V01_KF01/prompt.txt`
- repo-global `OBS-0006`

## Media continuity
Binary media is not guaranteed to live in normal Git. Run records store filenames, attachment IDs where available and hashes. A future chat should ask only for specific missing media needed for visual QA, never for the user to re-explain the project.
