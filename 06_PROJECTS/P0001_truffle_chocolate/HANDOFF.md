# Project Handoff — P0001

## Project
- ID: `P0001`
- Deliverable: 10s, 16:9 AI product ad
- Target: Google Flow / Gemini Omni Flash / Ingredients-to-Video
- Current stage: `STAGE_16_VIDEO_GENERATION`

## Locked storyboard / scene anchors
- `R0016` — SELECTED KF01 / opening close camera state (~4.5/5).
- `R0015` — SELECTED SCENE MASTER / KF02-like mid state (~4.3/5).
- `R0020` — SELECTED KF03 / final farther+higher hero camera state (~4.5/5).

These three frames are treated as camera states of one physical scene, not three independently replaceable layouts.

## Product / character identity anchors
- `R0003` — TOP-CLEAN product/packaging truth (~4.8/5).
- `R0010` — exact recurring three-chef appearance/style identity (~4.8/5).

Additional lower-priority evidence:
- `R0008` assortment diversity (~4.5/5).
- `R0006` micro texture/particle scale (~4.5/5).
- `R0002` optional inferred 45-degree geometry (~4.3/5).

These lower-priority assets are intentionally excluded from the first Flow video stack to reduce reference competition.

## Important learning history
1. R0011–R0013: five-reference independent scene synthesis failed due role bleed, props/tools, wrong anchoring and geometry regularization.
2. R0014–R0015: minimal R0003+R0010 scene synthesis created the stable inside-box combined world.
3. R0016–R0017: adjacent closer camera states derived successfully from scene master.
4. R0018–R0019: KF03 derivation with R0015+R0003 failed strict spatial continuity because the complete product reference pulled the model toward a rebuilt full-box layout.
5. R0020–R0021: scene-master-only KF03 derivation preserved core hero/chef continuity; R0020 selected.

Evidence:
- `13_EVALUATION/reports/reference_qa_kf03_v05.md`
- `OBS-0011`

## Active Flow package
`11_PROMPT_PACKAGES/PKG_FLOW_OMNI_VIDEO_V01/`

Files:
- `prompt.txt`
- `references.md`
- `recommended_settings.md`
- `preflight_checklist.md`

Preflight: PASS.

## EXACT FIVE-IMAGE Flow stack — upload in this order
1. `R0016` — KF01 opening state.
2. `R0015` — scene master / mid state.
3. `R0020` — KF03 final state.
4. `R0003` — product/packaging identity only.
5. `R0010` — character identity only.

Leave slots 6–7 unused on the first controlled video run.

Do NOT upload R0006, R0008, R0002, original wooden-background source, cheesecake creative reference or R0018 unless later video QA identifies a specific problem and a reason to add one.

## Exact next action
In Google Flow / Gemini Omni Flash / Ingredients-to-Video:
- duration 10s;
- aspect ratio 16:9;
- upload the five images above in exact order;
- paste `PKG_FLOW_OMNI_VIDEO_V01/prompt.txt`;
- keep all exposed settings identical between the first two generations.

Create exactly TWO baseline videos:
- `P0001-R0022`
- `P0001-R0023`

Do not alter the prompt or ingredient stack between them.

After generation, supply both videos for frame-by-frame QA. Evaluate temporal product identity, hero traceability, chef identity/count, scene layout, camera trajectory, object stability, particle scale, lighting continuity and final hero hold before any repair decision.

## Cross-chat continuity
A fresh ChatGPT session should read:
1. `AI_START_HERE.md`
2. this `HANDOFF.md`
3. `STATUS.md`
4. `11_PROMPT_PACKAGES/PKG_FLOW_OMNI_VIDEO_V01/references.md`
5. `11_PROMPT_PACKAGES/PKG_FLOW_OMNI_VIDEO_V01/prompt.txt`
6. `13_EVALUATION/reports/reference_qa_kf03_v05.md`

Ask the user only for visual assets unavailable in the new session; never ask them to retell the project history.
