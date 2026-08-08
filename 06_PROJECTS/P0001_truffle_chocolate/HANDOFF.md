# Project Handoff — P0001

## Project
- ID: `P0001`
- Deliverable: 10s, 16:9 AI product ad
- Target: Google Flow / Gemini Omni Flash / Ingredients-to-Video
- Current stage: `STAGE_10_STORYBOARD`

## Current approved anchors
### Product
- `R0003` TOP-CLEAN — primary clean visible identity (~4.8/5).
- `R0008` ASSORTMENT — diversity/color/coating authority (~4.5/5).
- `R0006` MACRO — micro material/particle-scale only (~4.5/5).
- `R0002` HERO-45 — optional inferred depth support (~4.3/5).

### Characters
- `R0010` — selected exact three-chef appearance/style reference (~4.8/5).

### Combined scene / storyboard
- `R0016` — SELECTED KF01 / opening camera state (~4.5/5).
- `R0015` — SELECTED SCENE MASTER / KF02-like mid-state (~4.3/5).
- KF03 — not approved yet.

## Important history
### Independent scene synthesis v01
R0011–R0013 failed due role bleed, tools/bowls/loose ingredients, scale/readability problems and wrong physical anchoring.

### Minimal-reference scene synthesis v02
R0014–R0015 used only R0003 + R0010 and no tools/actions. This created a stable inside-box world. R0015 selected as scene master.

### Camera-derived KF01 v03
R0016–R0017 derived from R0015 + R0003. R0016 selected; camera-path continuity into R0015 is plausible.

### KF03 v04 — FAILED STRICT CONTINUITY
R0018–R0019 attempted to derive the final wide state from R0015 + R0003.

- `R0018` ~3.9/5: excellent standalone full-box product hero; complete box, exactly three chefs, no props. However it rebuilds the local arrangement and loses the traceable central hero from R0015. Keep only as a standalone final aesthetic/product target, not sequence endpoint.
- `R0019` ~3.3/5: same scene-rebuild failure plus chefs move outside/in front of the box. Reject.

Evidence: `13_EVALUATION/reports/reference_qa_kf03_v04.md`.
Learning: `OBS-0010`.
Repair hypothesis: `HYP-0003`.

## Current interpretation
Adding R0003 to a wide camera derivation appears to pull the model toward R0003's globally coherent full-box layout and away from R0015's local spatial continuity. Product truth and scene continuity are both useful, but they should not necessarily be injected into the same still-image derivation step.

## Exact next action — KF03 v05 master-only
Generate exactly TWO candidates using:
`11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V05_KF03_MASTER_ONLY/prompt.txt`

### Upload ONLY
1. `R0015` scene master.

Do not upload R0003 or any other reference in this controlled pass.

Expected runs: `P0001-R0020`, `P0001-R0021`.

### Desired result
- camera farther and moderately higher than R0015;
- same central multicolor hero remains traceable in same local region/cup;
- same three chefs remain inside the box in same broad positions;
- additional box/assortment is extrapolated around the existing scene, not substituted for it;
- zero tools, bowls, loose ingredients or debris;
- plausible continuity: R0016 → R0015 → KF03.

## Stop rule
If v05 master-only still cannot preserve the scene while revealing a coherent full box, do not keep making the prompt longer. Switch architecture: either use R0018 as a final aesthetic target without treating it as a strict end-frame, or split the final reveal into a separate controlled clip.

## Cross-chat continuity
A new ChatGPT session should read `AI_START_HERE.md`, this HANDOFF, STATUS, `reference_qa_kf03_v04.md`, `OBS-0010`, `HYP-0003`, and the active V05 prompt. Ask only for media unavailable in the new session; never ask the user to re-explain the project.
