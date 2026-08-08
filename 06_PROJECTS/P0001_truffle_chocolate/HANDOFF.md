# Project Handoff — P0001

## Project
- ID: `P0001`
- Deliverable: 10s, 16:9 AI product ad
- Target: Google Flow / Gemini Omni Flash / Ingredients-to-Video
- Current stage: `STAGE_19_FINAL_SELECTION`
- Current accepted final for this objective: `P0001-R0022`

## Locked storyboard / scene anchors
- `R0016` — SELECTED KF01 / opening close camera state (~4.5/5).
- `R0015` — SELECTED SCENE MASTER / KF02-like mid state (~4.3/5).
- `R0020` — SELECTED KF03 / final farther+higher hero camera state (~4.5/5).

## Identity anchors
- `R0003` — TOP-CLEAN product/packaging truth (~4.8/5).
- `R0010` — exact recurring three-chef appearance/style identity (~4.8/5).
- `R0008` — assortment diversity/coating evidence (~4.5/5).
- `R0006` — macro texture/particle evidence (~4.5/5).

## Current video result
### `R0022` — SELECTED FINAL FOR CURRENT OBJECTIVE
Google Flow / Gemini Omni Flash / 10s / 16:9.
Overall ~4.6/5.

Strong points:
- exactly three chefs remain stable;
- central multicolor hero remains traceable;
- smooth backward + shallow upward reveal;
- no tools/bowls/loose ingredients;
- coherent box/product world;
- stable final commercial hold.

Accepted caveats:
- hero/product geometry slightly more spherical/regular than real handmade source;
- final wide arrangement is not a literal KF03 spatial match, although internal clip continuity is strong.

### `R0023` — REJECT
Overall ~3.6/5. Hard failure: fourth chef appears from newly revealed off-screen space around ~2.4–3.0s and persists.

Evidence:
- `13_EVALUATION/reports/video_qa_flow_v01_r0022_r0023.md`
- `13_EVALUATION/reports/final_selection_r0022.md`
- `09_LEARNING/observations/OBS-0012.md`

## Optimization status
User explicitly accepted R0022 and paused indefinite optimization so system design can continue.

The V02 off-screen population-lock repair remains documented as backlog:
`11_PROMPT_PACKAGES/PKG_FLOW_OMNI_VIDEO_V02_COUNT_LOCK/prompt_delta.md`

Do NOT resume that experiment unless user asks.

## Important system lessons from P0001
- clean role-separated references outperform blindly filling reference slots in several tested scene tasks;
- a useful reference for one task can contaminate another task;
- scene-master-first + adjacent-camera derivation improved keyframe continuity;
- independent baseline videos with identical setup can differ materially due stochastic character-count behavior;
- every important learning remains observation/hypothesis unless promotion policy is satisfied.

## If user requests a new 20s/30s/40s ad for the same product
Create a **new derivative project** rather than overwriting P0001.

Recommended parent linkage:
- parent_project: `P0001`
- reuse textual source-prompt analysis, product identity, tool evidence and project learnings;
- reuse visual assets only when the actual media/proxy is available and role-appropriate;
- do not assume a full-resolution original exists just because a low-res Git proxy exists.

Before generating new keyframes/video:
1. read `00_SYSTEM/SCENARIO_ARCHITECTURE_SYSTEM.md`;
2. run `SOP_07_SCENARIO_GENERATION.md`;
3. for 2–4 clips use `MULTI_CLIP_ARCHITECTURE.md` and `SOP_MULTI_CLIP_SEQUENCE.md`;
4. present Scenario Architecture Menu and wait for user selection;
5. then create Master Sequence + Clip Contracts + per-clip reference plan.

For a requested 30s / 3×10s derivative, do NOT assume the old 10s scenario should simply be repeated. It may become a useful final/payoff chapter, but only if the selected Master Sequence supports it.

## Media persistence
System storage mode is `git_previews` for non-sensitive media.

Paths:
- `19_HANDOFF_ASSETS/git_previews/`
- `19_HANDOFF_ASSETS/proxy_manifest.json`

Original/full-resolution media remains outside Git normal storage; proxy is `source_of_truth=false`.

### Historical P0001 backfill — COMPLETED for requested assets
On 2026-08-08 the user explicitly requested public low-resolution Git copies of the previously supplied selected assets and both evaluated videos. The following proxies now exist in Git:

- `R0002` — 45° hero product reference. (`R002` in the user's backfill request was interpreted as `R0002` based on project context.)
- `R0003` — clean top product identity reference.
- `R0010` — three-chef character identity reference.
- `R0015` — scene master / mid camera state.
- `R0016` — selected KF01 opening frame.
- `R0020` — selected KF03 final camera state.
- `R0022` — selected 10s video, low-resolution motion proxy.
- `R0023` — rejected 10s video retained as failure evidence for the fourth-chef duplication issue.

Exact paths, dimensions, roles, hashes where available, and compression profiles are recorded in `19_HANDOFF_ASSETS/proxy_manifest.json`.

These Git media files are intentionally very low resolution. They are adequate for cross-chat scene recall, composition, character count and broad motion/context review, but are NOT authority for fine texture, final quality, exact color, or generation-grade source input.

For a new chat, inspect the Git proxies first. Ask the user to reattach an original/full-resolution asset only when the next generation or detailed QA genuinely needs it.

Important: repository is public; these proxies are publicly accessible. The user explicitly requested this historical backfill. Sensitive/client/confidential or `do_not_publish` assets remain metadata-only in future projects.

## Cross-chat continuity
A fresh ChatGPT session working on a new 30s derivative should read:
1. `AI_START_HERE.md`
2. `AGENTS.md`
3. this `HANDOFF.md`
4. `STATUS.md`
5. `00_SYSTEM/MEDIA_PROXY_PIPELINE.md`
6. `19_HANDOFF_ASSETS/proxy_manifest.json`
7. `00_SYSTEM/SCENARIO_ARCHITECTURE_SYSTEM.md`
8. `00_SYSTEM/MULTI_CLIP_ARCHITECTURE.md`
9. `01_SOPS/SOP_07_SCENARIO_GENERATION.md`
10. `01_SOPS/SOP_MULTI_CLIP_SEQUENCE.md`
11. `13_EVALUATION/reports/video_qa_flow_v01_r0022_r0023.md`

Use Git proxies for planning/visual recall when sufficient. Ask the user to reattach original media only when full-resolution quality or generation input actually requires it.
