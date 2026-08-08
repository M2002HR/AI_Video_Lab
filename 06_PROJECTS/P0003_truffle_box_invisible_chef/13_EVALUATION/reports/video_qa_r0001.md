# Video QA — P0003-R0001

## Decision
**FAIL / REJECTED — STRUCTURAL TEMPORAL REVERSAL.**

The baseline preserves several visual locks but fails the intended process order and final state. This is not a cosmetic defect; the clip must be regenerated with a revised temporal-conditioning strategy.

## Provenance
- User returned the baseline Gemini-generated video in the active project chat.
- Tool: Gemini video generation.
- Exact model/settings: unknown except observable output metadata.
- Output: 1280 × 720, 24 fps, 10.005 s, 2,476,184 bytes.
- SHA-256: `c10c62d03e78030d22e75283bb166af0225676423fecbaf31d38b7bede951107`.
- Binary is not published to the public repository.

## What passes
- 16:9 / ~10-second technical format is correct.
- Camera remains visually fixed in the required 90-degree overhead family.
- White minimalist studio environment is stable.
- Kraft-box identity, dark fluted cups and colorful handmade-truffle family remain recognizable.
- No visible hands, arms, face, body or operator appear in sampled frames.
- No split-screen/keyframe-sheet layout, branding, watermark or wooden-table contamination appears.
- The single-truffle lift and bite concept is visually attempted.

## Blocking failures
### 1. Timeline direction is reversed
The video opens on the completed filled hero box instead of the required 25-empty-cup opening state. The intended chronology is therefore broken from frame one.

### 2. Required making-process beats are absent
The clip does not show the required centered glass bowl / chocolate-center formation beat or the coating-dish / sprinkle-adhesion beat in the intended time windows.

### 3. Assembly becomes deconstruction
After the early lift/bite action, the box progressively loses truffles. Sampled frames from roughly the second half show increasing empty cups until the box becomes empty by the end. This is the opposite of the selected progressive-fill timeline.

### 4. Final state fails completely
The required ending is 24 seated truffles + one bitten floating truffle + one empty cup. Instead the clip ends on an empty box with empty paper cups and no held bitten hero piece.

### 5. Object disappearance is nonphysical
The later depletion reads as pieces disappearing rather than being produced, coated and seated with believable contact/gravity. This violates the invisible-chef physical-motion rule.

## Sampled temporal evidence
- ~00:00–00:02: full hero assortment already present and mostly static.
- ~00:02.5–00:05.5: one central/multicolor truffle lifts/enlarges and the bite motif occurs far too early.
- ~00:06–00:09.5: truffles progressively disappear from the box and empty cups multiply.
- ~00:09.5–00:10.0: box is effectively empty, contradicting the locked final hero state.

## Root-cause hypothesis
The strongest evidence points to **temporal reference-role confusion**: the clean full-product image likely dominated as an initial-state visual anchor, while the three-panel keyframe sheet was not reliably interpreted as left-to-right chronology. The model then produced a sequence resembling hero -> lift/bite -> partial -> empty, effectively reversing the desired process.

This is a project-level hypothesis from one run, not a system-wide rule.

## Gate result
Video QA: **FAIL**.

Proceed to `STAGE_18` Repair Decision. Do not tune small cosmetic details on this run. Regenerate from a corrected video-conditioning stack that makes the empty opening frame unambiguous and avoids using the multi-panel keyframe sheet directly in the next baseline.
