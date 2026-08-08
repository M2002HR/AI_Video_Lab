# Video QA — Flow / Gemini Omni Flash V01 baseline

Runs: `P0001-R0022`, `P0001-R0023`

Input stack for both runs was identical:
1. `R0016` KF01 opening
2. `R0015` scene master / mid
3. `R0020` KF03 final
4. `R0003` product identity
5. `R0010` character identity

Prompt: `PKG_FLOW_OMNI_VIDEO_V01`
Duration: 10s
Format: 1280×720, 24 fps, 16:9

## R0022 — SELECTED baseline
Overall: ~4.6/5 — pass with caveats.

### Temporal review
- 0–2s: exactly three recurring chefs visible; central multicolor hero truffle stable; clean inside-box world; no props.
- 2–6s: camera performs a coherent continuous backward/upward reveal; additional truffles enter through framing rather than obvious scene cuts; hero remains traceable; chef count remains three.
- 6–9s: full-box readability increases smoothly; chefs shrink only in screen space; no visible character duplication or teleportation in sampled frames.
- 9–10s: stable final product hold with complete box readable.

### Strengths
- single-shot camera grammar followed well;
- exact three-character count remains stable;
- central hero remains traceable throughout;
- zero-tool / zero-bowl / zero-loose-ingredient rule respected;
- product category, colored coatings, dark cups and kraft packaging remain coherent;
- no obvious scene cut or catastrophic box morph;
- final hold is commercially usable.

### Caveats
- central hero remains smoother/more spherical than the real handmade source;
- final arrangement is not a literal pixel/spatial match to KF03, though continuity within the generated clip is strong;
- chef motion is very restrained/static, which is acceptable for the current low-risk scenario.

Decision: SELECT as current best video baseline and candidate final if no better repair run is produced.

## R0023 — REJECT
Overall: ~3.6/5 — failed hard gate.

### Temporal review
- 0–2s: begins strongly; same three intended chefs, stable hero and smooth camera.
- ~2.4s: a partial additional red-uniform chef begins to become visible at the far-right edge as new off-screen space is revealed.
- ~3.0s onward: the fourth chef is clearly present and persists through the remainder of the video.
- 6–10s: camera and product reveal remain visually coherent, but exact character-count continuity is permanently broken.

### Strengths
- smooth camera reveal;
- hero-truffle continuity remains strong;
- product/material/box language remains coherent;
- no tool or ingredient clutter.

### Hard failure
`duplicate_character` / `offscreen_population_hallucination`.

The model appears to treat newly revealed off-screen scene area as permission to instantiate an additional chef even though the visible anchors and prompt specify exactly three.

Decision: REJECT for production use.

## Baseline conclusion
Identical inputs produced one strong pass and one hard character-count failure. The core scene/camera/product architecture is therefore viable, but exact cast count is not yet fully reliable under stochastic video generation.

Recommended next experiment: keep the five-image stack and all settings unchanged; modify only the prompt with an explicit OFF-SCREEN POPULATION LOCK stating that the three chefs visible at frame 0 are the only humans/characters anywhere in the entire world and that newly revealed off-screen space may contain only box/cardboard/truffles/cups/background, never additional chefs. Generate two controlled V02 runs before changing ingredients.
