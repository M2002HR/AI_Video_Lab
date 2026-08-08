# P0003 Keyframe Plan v01

Status: **ready for generation**.

Storyboard `SB-P0003-001R2` passed Storyboard QA. Generate only the minimum controlling visual anchors that materially improve continuity for the later Gemini video prompt.

## Authority stack
1. Original real product photograph — highest product-identity authority.
2. `REF-P0003-001` — clean white-studio box/composition/environment authority.
3. `SB-P0003-001R2` — approved sequence and state-transition authority.

## Required keyframes

### KF-P0003-01 — Opening cups state
Approximate timeline anchor: 00:00.4.

Purpose:
- lock box geometry, diamond orientation, camera and 25-cup starting state;
- prevent early extra truffles or packaging drift.

Visual state:
- centered shallow kraft box;
- exactly 25 empty dark fluted paper cups;
- pure white matte tabletop;
- exact 90-degree top-down camera;
- no truffles, utensils, hands or unrelated props.

### KF-P0003-02 — Mid-assembly state
Approximate timeline anchor: 00:05.0.

Purpose:
- lock progressive filling grammar and product identity before the hero state;
- reduce count/layout discontinuity during the longest action phase.

Visual state:
- same box, scale, orientation and camera;
- approximately 15–18 finished colorful truffles seated in their cups;
- remaining cups visibly empty;
- no truffles randomly outside the box;
- strong coating/color diversity;
- no duplicated cloned look.

### KF-P0003-03 — Lift state
Approximate timeline anchor: 00:08.4.

Purpose:
- lock the critical 25-total continuity for the lift/bite ending.

Visual state:
- exactly 24 truffles seated in the box;
- exactly one near-center dark fluted cup visibly empty;
- the corresponding mixed-rainbow truffle floating a short distance above the box;
- all other 24 pieces match the approved hero composition and remain seated;
- no bite yet.

## Not required
A separate full-box hero keyframe is not required because `REF-P0003-001` already provides a strong approved clean hero/product anchor.

A separate bitten final keyframe is deferred unless later video QA shows bite-identity failure. The video prompt can describe the bite transition from KF-P0003-03.

## Generation strategy
Generate one three-panel 16:9 horizontal keyframe sheet in ChatGPT, then QA each panel for role correctness. If passed, crop/register the three panels as independent generation anchors when needed.

Next action: run `11_PROMPT_PACKAGES/PKG_CHATGPT_KEYFRAME_SET_001/resolved_prompt.md` with `REF-P0003-001` and the approved repaired storyboard available as references.