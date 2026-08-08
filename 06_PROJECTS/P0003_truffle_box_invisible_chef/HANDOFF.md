# Project Handoff — P0003

## Context snapshot
P0003 is a fresh independent 10-second Gemini food/product-video project based on the user-supplied colorful truffle photograph and invisible-chef source-template prompt.

Current stage: `STAGE_18` — Repair Decision / endpoint-controlled temporal conditioning.

## Completed gates
- Input provenance and source-template analysis complete.
- Product identity lock and reference strategy complete.
- `REF-P0003-001` passed Reference QA.
- Creative direction, scenario and 10-second timeline locked.
- Storyboard `SB-P0003-001R2` passed Storyboard QA.
- Keyframe set `KFSET-P0003-001` passed Keyframe QA.
- Gemini V01 prompt was constructed and preflighted.

## Video evidence
### P0003-R0001
Rejected for structural temporal reversal: full box at start, making beats omitted, box deconstructs, invalid empty ending.

### P0003-R0002
Returned as a second video candidate before the planned standalone-start-anchor step. Exact tool/model/prompt/reference stack are unknown and recorded as unknown.

Technical metadata:
- 1280 × 720;
- 24 fps;
- 10.0 seconds;
- 3,176,110 bytes;
- SHA-256 `df5717de4e6add5b8ea53b10bfe232a74fae6697204160a9c55d225e0d900272`.

Video QA: **FAIL / rejected — timeline incomplete and final action failure**.

What improved:
- opens correctly on 25 empty cups / zero truffles;
- broad temporal direction is now empty -> filled rather than filled -> empty;
- white top-down box/product world remains recognizable.

Blocking failures:
- glass-bowl / chocolate-center formation beat absent;
- coating-dish / sprinkle-adhesion beat absent;
- direct box filling consumes most of the runtime;
- around 7.2–7.6 s a rainbow truffle descends into the box instead of lifting out after a complete hero state;
- no valid 25 seated -> 24 seated + 1 floating transition;
- no bite ending;
- late zoom/reframe breaks the fixed-camera lock;
- final floating bitten hero is absent.

## Approved new start anchor
The exact opening frame of R0002 was extracted and approved as `START-P0003-001`.

Metadata:
- 1280 × 720 PNG;
- 444,807 bytes;
- SHA-256 `759621ae9ad4fdb09de6a8afa5437bed83d91cc95ec8a9bd8ef34ed707be740a`.

Role:
- strict frame-0 temporal authority only;
- exactly 25 empty dark cups;
- zero truffles;
- centered diamond kraft box on white studio background.

This anchor does not replace the real source or `REF-P0003-001` for truffle/coating identity.

## Current repair strategy
R0002 suggests the gross direction problem can be corrected by a strong empty opening, but endpoint control and time allocation remain weak.

The next baseline should therefore use explicit **standalone start and standalone end anchors**, not the three-panel keyframe sheet directly.

### Start authority
`START-P0003-001` — approved.

### End authority to generate
`END-P0003-001` — standalone final frame containing:
- exactly 24 seated truffles;
- exactly one empty near-center cup;
- exactly one mixed-rainbow truffle floating above the box;
- one realistic bite exposing dark chocolate interior;
- same top-down white-studio scale/composition family.

Active prompt package:
`11_PROMPT_PACKAGES/PKG_CHATGPT_VIDEO_END_ANCHOR_001/resolved_prompt.md`

## Next action
Generate `END-P0003-001` in ChatGPT using `REF-P0003-001` plus `KFSET-P0003-001` as reference support, return it for focused QA, then construct/preflight the next Gemini video package with tighter mandatory timing checkpoints.

Do **not** generate another video before the final anchor passes QA and the next video package passes preflight.
