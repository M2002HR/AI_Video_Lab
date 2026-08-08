# KF03 v05 QA — master-only camera derivation

## Context
Goal: derive the final wide hero frame from `P0001-R0015` without allowing a second full-box reference to replace the established combined scene.

Input stack for both runs:
- `P0001-R0015` only.

Prompt package:
- `PKG_SCENE_KEYFRAME_V05_KF03_MASTER_ONLY`

Expected runs:
- `P0001-R0020`
- `P0001-R0021`

## Gate criteria
- same central multicolor hero remains traceable;
- same three recurring chefs remain inside the box in the same broad region;
- camera reads farther and moderately higher;
- more of the same box/world is extrapolated around the old scene;
- no tools, bowls, loose ingredients, duplicate chefs or debris;
- plausible sequence path from `R0016 → R0015 → KF03`.

## R0020 — SELECTED
Score: **4.5 / 5**

Strengths:
- central oversized multicolor hero remains clearly traceable;
- all exact three chefs remain inside the box and retain the same broad front/local relationship;
- no props, bowls, tools, loose sprinkles or debris;
- camera is clearly farther and higher than R0015;
- the complete box becomes readable without deleting the existing hero/local scene;
- dark studio look and material language remain coherent;
- sequence interpolation from R0015 is visually plausible.

Caveats:
- the wider box geometry is inferred and not source-exact;
- newly revealed surrounding assortment is extrapolated and mildly reorganized;
- the central hero remains intentionally larger than surrounding truffles, which is continuity-friendly but differs from the true real-box size distribution.

Decision: **PASS / SELECT KF03**.

## R0021 — ALTERNATE
Score: **4.2 / 5**

Strengths:
- master-only strategy again preserves the central hero and exact three chefs;
- no prop contamination;
- clear farther/higher camera state;
- coherent dark-studio scene.

Weaknesses:
- more aggressive assortment extrapolation than R0020;
- stronger rectangular-box/world reconstruction;
- new brown/orange coating families become more prominent;
- local scene feels less directly inherited from R0015.

Decision: **PASS WITH CAVEATS / RETAIN AS ALTERNATE**.

## Comparison to v04
The master-only v05 test materially outperforms v04 (`R0018–R0019`) on strict scene continuity.

Removing `R0003` from the still-image camera-derivation pass prevented the complete full-box product reference from overpowering the partial combined-world scene master. The image model was able to extrapolate outward while preserving the central hero and chef region.

This supports a project-level principle:

> During adjacent-camera-state derivation, a globally complete secondary reference can cause scene snapping/reconstruction. Once a stable scene master exists, deriving neighboring camera states from the master alone may preserve continuity better.

Do not yet promote this as a universal rule without cross-project evidence.

## Storyboard lock
- `KF01` ~00:01 → `P0001-R0016`
- `KF02` ~00:05 → `P0001-R0015`
- `KF03` ~00:09.2 → `P0001-R0020`

The storyboard/keyframe gate is now sufficient to proceed to final video prompt synthesis.
