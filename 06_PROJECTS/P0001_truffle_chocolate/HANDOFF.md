# Project Handoff — P0001

## Project
- ID: `P0001`
- Deliverable: 10s, 16:9 AI product ad
- Target: Google Flow / Gemini Omni Flash / Ingredients-to-Video
- Current stage: `STAGE_10_STORYBOARD`

## Current approved reference hierarchy
### Product
1. Original real product photograph — ultimate source truth.
2. `P0001-R0003` — TOP-CLEAN, primary clean visible identity (~4.8/5).
3. `P0001-R0008` — ASSORTMENT, diversity/color/coating authority (~4.5/5).
4. `P0001-R0006` — MACRO, micro material/particle scale only (~4.5/5).
5. `P0001-R0002` — optional HERO-45 inferred depth support (~4.3/5).

### Characters
`P0001-R0010` — selected recurring three-chef character reference (~4.8/5), appearance/style authority only.

### Combined scene
`P0001-R0015` — selected `REF-SCENE-MASTER` (~4.3/5) and approximate KF02/mid-reveal anchor. It defines the coherent combined product+character world and inside-box continuity, but does not override R0003 on real product identity.

R0014 is retained as alternate scene-grammar evidence (~4.1/5).

## Scene-generation history
### KF01 v01 — failed
R0011–R0013 used five references and repeatedly showed unwanted props/tools/loose ingredients, wrong scene anchoring, scale/readability problems and geometry regularization.

Evidence: `reference_qa_kf01_v01.md`, `OBS-0007`, `HYP-0002`.

### KF01 v02 minimal-reference — strong improvement
R0014 and R0015 used only R0003 product + R0010 characters and removed tools/actions.

Both v02 outputs:
- live physically inside the kraft box;
- contain exactly three recognizable recurring chefs;
- contain no tools, bowls or loose ingredients;
- create plausible pull-back continuity.

R0015 is selected because it is the cleaner and more product-dominant combined scene.

Important: R0015 reveals too much of the assortment for the intended 00:01 opening, so it is deliberately reassigned to `SCENE MASTER / KF02-like` instead of being forced into the wrong storyboard role. See `reference_qa_kf01_v02.md` and `OBS-0008`.

## Active scenario
`07_SCENARIOS/selected/scenario_v02_quiet_inspection_reveal.md`

Core motion remains one continuous backward + shallow upward camera reveal with exactly three tiny chefs and no tool interaction.

## Exact next action — derive true KF01 from R0015
Generate exactly TWO candidates using:
`11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V03_KF01_FROM_MASTER/prompt.txt`

### Upload only
1. `R0015` — selected scene master and highest authority for the combined world.
2. `R0003` — secondary product-identity backup only.

Do not upload R0010 in this pass unless character identity later drifts; R0015 already contains the accepted cast and direct reuse reduces static-pose pressure.

Expected next runs: `P0001-R0016`, `P0001-R0017`.

### Desired result
A closer/slightly lower camera view of the SAME R0015 scene:
- hero truffle fills roughly 50–60% frame height;
- exact same three chefs remain readable;
- only limited neighboring truffle/box context visible;
- much less assortment revealed than R0015;
- no props or loose ingredients;
- later camera pull-back can naturally reach R0015.

## Scale note
The original 1:3 chef-height/truffle-diameter target was not reached, but R0015 still communicates a strong miniature-world cue. For this project, continuity/stability takes priority over forcing an arbitrary ratio that repeatedly destabilizes generation. Do not promote this as a global scale rule.

## After KF01 passes
Use the same scene-master world to derive the wider final KF03/full-box hero view. Avoid independently synthesizing unrelated keyframes.

## Cross-chat continuity
A new ChatGPT session should read `AI_START_HERE.md`, this HANDOFF, STATUS, `reference_qa_kf01_v02.md`, `OBS-0008`, and the active v03 prompt. Ask only for media that is visually unavailable; never ask the user to re-explain the project.
