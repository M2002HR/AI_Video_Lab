# Project status — P0001

- Current stage: `STAGE_19_FINAL_SELECTION` — `R0022` accepted by user as the current final video with known caveats; further optimization paused so system design can continue.
- Product identity: `product_identity.md` + active injection `identity_lock_v02.md`.
- Active scenario: `07_SCENARIOS/selected/scenario_v02_quiet_inspection_reveal.md`.
- Selected final run: `P0001-R0022`.
- Final selection evidence: `13_EVALUATION/reports/final_selection_r0022.md`.

## Locked storyboard anchors
- `KF01` ~00:01: `R0016` — approved.
- `KF02` / scene master ~00:05: `R0015` — approved.
- `KF03` ~00:09.2: `R0020` — approved.

## Flow V01 baseline
### R0022 — SELECTED FINAL FOR CURRENT OBJECTIVE
Score ~4.6/5. Passed with caveats.
- exactly three chefs remain stable;
- central multicolor hero remains traceable;
- smooth continuous backward + upward reveal;
- no props/bowls/loose ingredients;
- coherent box/product world;
- stable final hero hold.

Accepted caveats:
- hero remains somewhat too regular/spherical versus the real handmade source;
- final arrangement is not a literal KF03 spatial match although internal generated continuity is strong.

### R0023 — REJECT
Score ~3.6/5. Hard failure: `duplicate_character`; fourth chef appears from newly revealed right-side space around ~2.4–3.0s and persists.

Evidence: `13_EVALUATION/reports/video_qa_flow_v01_r0022_r0023.md`.
Learning: `OBS-0012`.

## Optimization decision
User explicitly chose not to continue indefinite optimization now. The planned V02 off-screen count-lock experiment remains documented in backlog and can be resumed later without losing context.

## Current system-building focus
- ensure documentation completeness is itself a permanent system rule;
- broaden scenario generation beyond low-risk inspection/reveal;
- document process-heavy scenario design;
- add 2×10s / 3×10s multi-clip production architecture and continuity contracts.

Relevant system docs:
- `00_SYSTEM/DOCUMENTATION_CONTRACT.md`
- `00_SYSTEM/MULTI_CLIP_ARCHITECTURE.md`
- `01_SOPS/SOP_07_SCENARIO_GENERATION.md`
- `01_SOPS/SOP_MULTI_CLIP_SEQUENCE.md`
- `04_CHECKLISTS/CHK_MULTI_CLIP_CONTINUITY.md`
