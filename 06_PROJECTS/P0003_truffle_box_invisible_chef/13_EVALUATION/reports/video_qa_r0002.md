# Video QA — P0003-R0002

## Decision
**FAIL / REJECTED — TIMELINE INCOMPLETE, FINAL ACTION FAILS.**

R0002 is a meaningful improvement over R0001 because it restores the correct broad direction from empty box toward filled box. However it still fails the selected scenario and cannot advance to final selection.

## Provenance
- User returned a second 10-second video candidate in the active project chat.
- Generation tool/model/prompt/reference stack: **unknown** because they were not supplied with the file.
- Output: 1280 × 720, 24 fps, 10.0 s, 3,176,110 bytes.
- SHA-256: `df5717de4e6add5b8ea53b10bfe232a74fae6697204160a9c55d225e0d900272`.
- Binary is not published to the public repository.

## What passes / improves
- Technical format is correct: 16:9, 1280×720, 24 fps, 10 seconds.
- The clip begins with the kraft box in a stable top-down white-studio world.
- Opening state visibly contains the required **25 empty dark fluted cups and zero truffles**.
- Temporal direction is no longer reversed: the box fills progressively rather than deconstructing.
- Kraft box, dark paper cups, colorful handmade-truffle family, white background and invisible-operator grammar remain recognizable.
- No visible hands, arms, people, text, watermark or wooden background appear in sampled frames.

## Blocking failures
### 1. Mandatory making-process beats are still absent
The selected timeline requires a glass-bowl / chocolate-center formation beat and a coating-dish / sprinkle-adhesion beat before box assembly. R0002 skips both. Truffles begin appearing directly in the box at about 2 seconds.

### 2. Assembly consumes almost the whole clip
The box stays empty until roughly 1.5–2.0 seconds, then progressively fills from about 2.0 seconds through the late part of the clip. This leaves insufficient time for the required hero settle, lift and bite ending.

### 3. The rainbow action is directionally wrong
Around 7.2–7.6 seconds, a mixed-rainbow truffle appears above the box but **descends into an empty top cup** as part of filling. The required action is the opposite: after a completed 25-piece hero state, one identifiable rainbow truffle must lift out of its cup and leave that cup empty.

### 4. No valid 25-piece hero -> 24+1 transition
The clip never clearly establishes a complete 25-seated hero state followed by exactly one removal. Near the end, the box appears to hold about 24 seated truffles with one empty cup, but the missing 25th piece is not held above the box.

### 5. Bite ending is absent
No floating truffle receives the required realistic bite. No bitten dark-chocolate interior is held through the final moment.

### 6. Camera lock breaks late
From roughly 8.7 seconds onward, the image performs a pronounced zoom/reframe into the box. This violates the fixed exactly-90-degree, no-zoom/no-reframing camera lock.

## Sampled temporal evidence
- ~00:00–00:01.5: clean empty-box state with 25 cups.
- ~00:02.0: first finished truffles begin appearing directly in cups; no bowl or coating stage precedes them.
- ~00:02.0–00:07.0: progressive filling dominates the clip.
- ~00:07.2–00:07.6: a rainbow truffle is above the box and then moves downward into the arrangement rather than lifting out after completion.
- ~00:08.5: box is nearly full with one visible vacancy.
- ~00:08.7–00:10.0: strong zoom/reframe; no floating bitten hero; final state remains incomplete.

## Interpretation
R0002 provides evidence that an empty opening state can correct the gross reversal seen in R0001. The remaining failure now appears to be **temporal allocation / endpoint control**: Gemini spends most of the 10 seconds on direct filling and sacrifices the mandatory middle process beats and final lift/bite payoff.

Because the exact generation stack for R0002 is unknown, this interpretation is provisional and must not be generalized beyond this project/run.

## Gate result
Video QA: **FAIL**.

Remain in `STAGE_18` Repair Decision. Do not accept or cosmetically patch this run. Use its first frame as a candidate standalone opening anchor, create a separate standalone final bite-state anchor, then build the next preflighted video package around explicit start/end state control and tighter timing constraints.
