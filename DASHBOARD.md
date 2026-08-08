# AI Video Ad Lab dashboard

- System version: 1.2.0
- Primary operator: ChatGPT / AI operator architecture
- Current system focus: adaptive scenario architecture + 2/3/4 clip production

## P0001 — truffle chocolate
- Current stage: `STAGE_19_FINAL_SELECTION`
- Accepted current final: `R0022` (~4.6/5, with known caveats)
- Further V02 count-lock optimization: paused/backlog by user
- P0001 should not be overwritten when creating a new 20/30/40s derivative.

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

## Scenario architecture v1.2.0
System now supports an adaptive menu for:
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

Candidate prompt:
- `PRM-SCN-ARCH-001_v1.0.0` — candidate pending broader project validation.

## Next intended use
A new chat can create a new 30s / 3×10s derivative from P0001 using:
`06_PROJECTS/P0001_truffle_chocolate/30S_DERIVATIVE_START.md`

The first action in that new project is Scenario Architecture Menu, not immediate video generation.

## Media storage status
Current mode: metadata-only/default.
ChatGPT image/video attachments are NOT automatically stored in GitHub, and binary media is currently ignored by `.gitignore`.
See `00_SYSTEM/STORAGE_POLICY.md`.

## Cross-chat readiness
Enabled via `AI_START_HERE.md`, `AGENTS.md`, project `HANDOFF.md`, and Documentation Contract.

Dashboard is a generated/maintained overview; source of truth remains underlying project/system documents.
