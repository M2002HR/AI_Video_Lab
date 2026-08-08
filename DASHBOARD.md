# AI Video Ad Lab dashboard

- System version: 1.4.0
- Primary operator: ChatGPT / AI operator architecture
- Current system focus: sequential stage-gated production + adaptive scenario architecture + 2/3/4 clip production + documented cross-chat media handling

## P0003 — invisible-chef truffle box assembly
- Current stage: `STAGE_16` — Video Generation.
- Parent project: none; fresh independent project by explicit user request.
- Objective: adapt the supplied 10s / 16:9 invisible-chef Gemini food-video template to the supplied colorful handmade truffle gift box.
- Product authority: original uploaded real truffle-box photograph.
- Approved clean derivative: `REF-P0003-001` — 90-degree top-down white-studio product/packaging/composition support.
- Approved storyboard: `SB-P0003-001R2` — repaired and count-locked.
- Approved keyframe set: `KFSET-P0003-001` — opening, partial-fill, and lift-state control.
- Keyframe lift lock: exactly 24 seated + 1 mixed-rainbow floating + exactly one empty cup.
- Creative direction/scenario/timing: locked.
- Active video package: `11_PROMPT_PACKAGES/PKG_GEMINI_VIDEO_V01`.
- Video preflight: **PASS**.
- Video generation authorized: **yes**.
- Baseline upload stack: `REF-P0003-001` + `KFSET-P0003-001` only.
- Next action: generate one unchanged Gemini baseline and return it as `P0003-R0001` for Video QA before any prompt iteration.
- Current attachments are metadata-only in Git; no current-chat binaries were published.

## P0002 — invisible-chef truffle assembly
- Current stage: `STAGE_03` — Reference Strategy.
- Parent project: `P0001`.
- Objective: new 10s / 16:9 single-clip creative direction for the same truffle product.
- Source-template DNA: fixed 90-degree overhead invisible-chef food-commercial grammar.
- Product authority: current uploaded truffle product image.
- Active video prompt: **none**.
- Approved P0002 reference set: **none yet**.
- Previous scenario/timeline/Gemini package are preserved as `premature_draft` artifacts and are not generation-authorized.
- Next action: complete reference-role strategy; if needed, generate/clean only the first required product reference and QA it before moving to Creative Direction.
- New turn attachments are metadata-only in Git; no new binary publication was performed.

## P0001 — truffle chocolate
- Current stage: `STAGE_19_FINAL_SELECTION`
- Accepted current final: `R0022` (~4.6/5, with known caveats)
- Further V02 count-lock optimization: paused/backlog by user
- P0001 is preserved and is not overwritten by P0002/P0003.

### P0001 locked anchors
- `R0003` product/packaging clean identity
- `R0010` recurring three-chef identity
- `R0015` scene master
- `R0016` KF01 opening
- `R0020` KF03 final camera state
- `R0022` selected 10s video

### P0001 important learning
- role-clean reference stacks can outperform max-filled stacks in tested scene tasks;
- scene-master-derived adjacent camera states improved continuity;
- identical video setup can produce stochastic character-count failure (`R0023` fourth chef);
- these remain project/provisional unless promoted through evidence policy.

## Sequential stage-gate policy v1.4.0
New projects may not jump from product image + source/template prompt directly to a final video prompt. Fast Start accelerates setup only; active progression must stop at the earliest incomplete gate.

Core docs:
- `00_SYSTEM/SEQUENTIAL_STAGE_GATE_PROTOCOL.md`
- `00_SYSTEM/FAST_START_PROTOCOL.md`
- `00_SYSTEM/MASTER_WORKFLOW.md`
- `01_SOPS/INDEX.md`
- `09_LEARNING/decisions/DEC-0002_SEQUENTIAL_STAGE_GATES.md`

## Scenario architecture
System supports an adaptive menu for:
- 1×10s / 10s
- 2×10s / 20s
- 3×10s / 30s
- 4×10s / 40s

Candidate count is adaptive, not a quota. Longer duration is proposed only when process/story capacity justifies it.

Core docs:
- `00_SYSTEM/SCENARIO_ARCHITECTURE_SYSTEM.md`
- `00_SYSTEM/MULTI_CLIP_ARCHITECTURE.md`
- `01_SOPS/SOP_07_SCENARIO_GENERATION.md`
- `01_SOPS/SOP_MULTI_CLIP_SEQUENCE.md`
- `04_CHECKLISTS/CHK_SCENARIO_ARCHITECTURE_MENU.md`
- `04_CHECKLISTS/CHK_MULTI_CLIP_CONTINUITY.md`

## Media storage status
P0001 includes user-approved public low-resolution Git previews for selected historical assets. P0002 and P0003 currently store their new/current attachment metadata only; full-resolution current-chat inputs remain outside Git.

See `00_SYSTEM/STORAGE_POLICY.md` and `00_SYSTEM/MEDIA_PROXY_PIPELINE.md`.

## Cross-chat readiness
Enabled via `AI_START_HERE.md`, `AGENTS.md`, project `HANDOFF.md`, Documentation Contract, and the mandatory Sequential Stage-Gate Protocol.

Dashboard is a maintained overview; source of truth remains underlying project/system documents.
