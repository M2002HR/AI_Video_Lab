# Project Handoff — P0001

## Project
- ID: `P0001`
- Deliverable: 10s, 16:9 AI product ad
- Target: Google Flow / Gemini Omni Flash / Ingredients-to-Video
- Current stage: `STAGE_10_STORYBOARD`

## Current approved reference hierarchy
### Product
1. Original real product photograph — ultimate source truth, but not always uploaded when its wooden environment risks contamination.
2. `P0001-R0003` — TOP-CLEAN, primary clean visible identity (~4.8/5).
3. `P0001-R0008` — ASSORTMENT, diversity/color/coating authority (~4.5/5).
4. `P0001-R0006` — MACRO, micro material/particle scale only (~4.5/5).
5. `P0001-R0002` — optional HERO-45 inferred depth support (~4.3/5).

### Characters
`P0001-R0010` — selected recurring three-chef character reference (~4.8/5). It defines character appearance/style only, not pose/action/tool/scale.

## KF01 v01 result — FAILED GATE
Three combined-scene candidates were generated with the five-reference stack and `PKG_SCENE_KEYFRAME_V01_KF01`:
- `R0011` ~2.9/5 — fail;
- `R0012` ~3.4/5 — best diagnostic only, still fail;
- `R0013` ~3.2/5 — fail.

No v01 scene candidate is approved.

### Repeated failures
- unwanted tools, bowls and/or loose ingredients;
- chef-to-truffle scale too large;
- hero truffle over-perfect and nonpareils visually oversized;
- center chef frequently shown from behind, weakening identity control;
- opening scene staged on a separate surface instead of physically inside the final kraft box;
- R0011 also leaked wooden workshop/background-product context.

Full report: `13_EVALUATION/reports/reference_qa_kf01_v01.md`.
Learning: `OBS-0007`.
Repair hypothesis: `HYP-0002`.

## Active scenario v02
`07_SCENARIOS/selected/scenario_v02_quiet_inspection_reveal.md`

**Quiet Inspection → Full Box Reveal**
- one continuous 10-second shot;
- opening is already inside the actual kraft box;
- exactly three recurring chefs with all three faces readable;
- all hands empty; no tools, bowls or loose ingredients;
- hero truffle diameter ≈ 3× one chef's full standing height;
- one smooth pull-back + shallow upward rise reveals the already-existing assortment;
- final ~1 second is a stable product hero hold.

Active timeline: `08_SHOT_DESIGN/timeline_v02.md`.

## Exact next action — KF01 v02
Generate exactly TWO candidates using:
`11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V02_KF01/prompt.txt`

### Upload ONLY these two references
1. `R0003` TOP-CLEAN.
2. `R0010` CHARACTER.

Do not upload the original wooden-background source in this pass. Do not upload R0006 MACRO, R0008 ASSORTMENT or R0002 HERO-45. This intentionally tests whether a minimal role-clean stack reduces bleed/regularization.

Expected runs: `P0001-R0014`, `P0001-R0015`.

### KF01 v02 gate
- opening scene visibly belongs inside the same kraft box;
- exactly three recurring chefs;
- all three faces identifiable in front/3-quarter views;
- zero props/tools/bowls/loose sprinkles/chocolate debris;
- truffle diameter roughly 3× chef height;
- small source-like nonpareils;
- handmade truffle, not perfect factory sphere;
- clean dark environment;
- physical continuity to full-box pull-back is plausible.

Do not generate KF02/KF03 until KF01 v02 passes.

## Cross-chat continuity
A new ChatGPT session should read `AI_START_HERE.md`, this HANDOFF, STATUS, `reference_qa_kf01_v01.md`, `OBS-0007`, `HYP-0002`, and the active KF01 v02 prompt. Ask only for visual assets not accessible in the new session; never ask the user to re-explain the project.
