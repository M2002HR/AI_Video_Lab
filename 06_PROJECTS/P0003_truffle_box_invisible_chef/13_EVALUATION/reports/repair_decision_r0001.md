# Repair Decision — P0003-R0001

## Decision
**REGENERATE WITH REVISED TEMPORAL CONDITIONING.**

Do not locally patch or cosmetically tune the failed video. The failure is structural: chronology is reversed, required making beats are omitted, assembly becomes depletion, and the final state is wrong.

## Root stage
Return to the video-conditioning/reference interface immediately before video prompt execution. Keep the approved product identity, creative direction, scenario, storyboard, timing and keyframe logic; do not redesign them yet.

## Evidence
`P0003-R0001` begins from the completed hero state, performs the lift/bite motif early, and then empties the box. This strongly suggests the generation interpreted the full-product reference as an initial frame and/or read the multi-panel keyframe sheet without the intended left-to-right temporal authority.

## Repair strategy
1. Do **not** use the three-panel keyframe sheet directly in the next video generation.
2. Create one dedicated standalone 16:9 **video start anchor** showing exactly the opening state: centered kraft box, 25 empty dark paper cups, zero truffles, white studio background.
3. Keep `REF-P0003-001` only as secondary product/final-identity authority.
4. In the next video prompt, make the standalone empty-box anchor the explicit first-frame / start-state authority and state that the full-product reference must never be interpreted as the opening state.
5. Preserve the existing timeline for the first repaired regeneration; do not simplify the scenario until this cleaner conditioning strategy is tested once.

## New repair asset
ID: `START-P0003-001`

Role: `VIDEO_START_FRAME_AUTHORITY`

Authority boundary:
- controls only frame-0/opening composition, box placement, 25 empty cups, white environment and camera;
- does not override real product identity or final truffle appearance;
- `REF-P0003-001` remains final-product/packaging identity authority.

## Gate
Generate and QA `START-P0003-001` before constructing/authorizing `PKG_GEMINI_VIDEO_V02`.
