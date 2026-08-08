# Project status — P0001

- Current stage: `STAGE_18_REPAIR_DECISION` — first Flow/Omni V01 baseline evaluated; one strong pass and one hard character-count failure.
- Product identity: `product_identity.md` + active injection `identity_lock_v02.md`.
- Active scenario: `07_SCENARIOS/selected/scenario_v02_quiet_inspection_reveal.md`.
- Active timing: `08_SHOT_DESIGN/timeline_v02.md`.
- Base video package: `11_PROMPT_PACKAGES/PKG_FLOW_OMNI_VIDEO_V01/`.

## Locked storyboard anchors
- `KF01` ~00:01: `R0016` — approved.
- `KF02` / scene master ~00:05: `R0015` — approved.
- `KF03` ~00:09.2: `R0020` — approved.

## Flow V01 baseline — completed
Identical setup for both runs:
1. R0016
2. R0015
3. R0020
4. R0003
5. R0010

Google Flow / Gemini Omni Flash / 10s / 16:9 / 5 ingredients / same V01 prompt.

### R0022 — SELECTED CURRENT BEST
Score ~4.6/5. Passed with caveats.
- exactly three chefs remain stable through sampled timeline;
- central multicolor hero remains traceable;
- smooth continuous backward + upward reveal;
- no props/bowls/loose ingredients;
- box/product world remains coherent;
- stable final hero hold.

Caveats: hero remains somewhat too regular/spherical versus the real handmade source; final arrangement is not a literal KF03 spatial match although continuity inside the generated clip is strong.

### R0023 — REJECT
Score ~3.6/5. Hard failure: `duplicate_character`.
- begins with intended three chefs;
- an additional red-uniform chef becomes partially visible from the far-right edge around ~2.4s and is clearly present by ~3.0s;
- fourth chef persists through final reveal.

Camera/product continuity is otherwise good, so this is interpreted as stochastic off-screen population hallucination during reveal.

Evidence: `13_EVALUATION/reports/video_qa_flow_v01_r0022_r0023.md`.
Learning: `OBS-0012`.

## Decision
Do NOT change ingredients yet. V01 demonstrated the architecture can produce a strong result.

Next perform a controlled prompt-only repair: same five ingredients, same order, same settings, same base prompt plus one explicit OFF-SCREEN POPULATION LOCK. This changes only the character-count constraint and preserves experiment interpretability.

V02 delta:
`11_PROMPT_PACKAGES/PKG_FLOW_OMNI_VIDEO_V02_COUNT_LOCK/prompt_delta.md`

## Exact next action
Generate exactly TWO V02 videos with the same five-image stack and all settings unchanged.
Expected Runs:
- `P0001-R0024`
- `P0001-R0025`

Success target:
- exactly three chefs for the full clip;
- no new human/chef revealed as the camera widens;
- retain R0022-level camera continuity, hero traceability and clean final hold.

If both V02 runs preserve three characters without degrading the rest, promote the count-lock wording into the project video prompt. If duplication persists, next controlled experiment should change ingredient architecture rather than making the prompt longer.
