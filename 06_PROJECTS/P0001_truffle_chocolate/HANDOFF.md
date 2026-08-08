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

### Combined scene / storyboard anchors
- `P0001-R0016` — SELECTED KF01 / opening camera state (~4.5/5).
- `P0001-R0015` — SELECTED SCENE MASTER / approximate KF02 mid-state (~4.3/5).
- `P0001-R0017` — KF01 alternate (~4.4/5).
- `P0001-R0014` — scene-grammar alternate (~4.1/5).

## Scene-generation history
### v01 independent combined-scene synthesis — failed
R0011–R0013 used five references and repeatedly showed role bleed, tools/bowls/loose ingredients, wrong scene anchoring, scale/readability problems and product regularization.

### v02 minimal-reference combined scene — passed scene grammar
R0014–R0015 used only R0003 product + R0010 characters, with all tools/actions removed. This created a clean inside-box world. R0015 selected as scene master / KF02-like anchor.

### v03 camera derivation from scene master — KF01 PASSED
R0016–R0017 were generated from only R0015 + R0003.

`R0016` selected because:
- camera is clearly closer than R0015;
- hero truffle dominates more strongly;
- exact same three-chef cast remains readable and better differentiated than R0017;
- no tools, bowls, loose ingredients or debris;
- same kraft-box world and lighting remain coherent;
- one continuous pull-back from R0016 to R0015 is plausible.

Caveats: some static pose language remains and more neighboring assortment is visible than ideal, but continuity stability is more valuable than forcing another independent regeneration.

Evidence: `13_EVALUATION/reports/reference_qa_kf01_v03.md`, `OBS-0009`.

## Storyboard mapping now
- KF01 (~00:01): `P0001-R0016`
- KF02 / scene master (~00:05): `P0001-R0015`
- KF03 final hero (~00:09.2): next task

## Exact next action — derive KF03 from R0015
Generate exactly TWO candidates using:
`11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V04_KF03_FROM_MASTER/prompt.txt`

### Upload only
1. `R0015` — selected scene master / combined-world authority.
2. `R0003` — product/packaging identity backup.

Do NOT upload R0010 character reference, R0006 macro, R0008 assortment, R0002 hero-45 or original wooden-background source in this first KF03 pass.

Expected runs: `P0001-R0018`, `P0001-R0019`.

### Desired KF03
A farther + moderately higher camera state of the SAME world:
- complete kraft box readable;
- colorful assortment becomes primary hero;
- same three chefs remain present but visually smaller;
- hero-truffle region remains traceable;
- no props, bowls, tools, loose ingredients or debris;
- deeper/moderate focus suitable for product reveal;
- dark studio breathing room suitable for final ~1 second hold and post-production branding;
- same path continuity: R0016 → R0015 → KF03.

## Important current learning
For this project, `stable scene master → derive adjacent camera states` is outperforming independent keyframe synthesis. This is recorded as `OBS-0009`; it remains project/provisional until repeated elsewhere.

## Cross-chat continuity
A new ChatGPT session should read `AI_START_HERE.md`, this HANDOFF, STATUS, `reference_qa_kf01_v03.md`, `OBS-0009`, and the active KF03 prompt. Ask only for media that is visually unavailable; never ask the user to re-explain the project.
