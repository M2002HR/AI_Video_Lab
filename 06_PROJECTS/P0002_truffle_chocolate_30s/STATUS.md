# Project status — P0002

- Current stage: `STAGE_09_SHOT_TIMING` — scenario selection and sequence architecture are complete; visual production has not started.
- Parent: `P0001`; parent history and `P0001-R0022` remain untouched.
- Deliverable: 30s / 3×10s / 16:9.
- Selected scenario: `S30-A — Artisan Care → Collection Build → Gift-Box Hero`.
- Sequence: `P0002-S01`.
- Architecture: `hybrid`.
- Clip IDs: `P0002-C01`, `P0002-C02`, `P0002-C03`.
- Process truth: all character labor/arrangement remains `creative_metaphor`; literal truffle manufacturing is not claimed.
- Master Sequence: created.
- Clip Contracts: created for C01–C03.
- Boundary Contracts: created for C01→C02 and C02→C03 using match/editorial logic rather than hard spatial continuity.
- Per-clip reference plan: created with minimum-sufficient role-clean stacks.
- Heavy storyboard/keyframe/full image/video prompts: not created yet.

## Current blocker
Visual production/QA now needs exactly five P0001 binaries re-attached because they are not persisted in Git:
1. original real product photo;
2. `R0003` clean top product reference;
3. `R0010` recurring three-chocolatier reference;
4. `R0006` macro material/particle reference;
5. `R0008` assortment diversity reference.

No need to re-attach `R0015`, `R0016`, `R0020`, `R0022` or `R0002` at this stage.

## Next action
After the five required assets are attached, execute per-clip shot timing/reference preflight beginning with C01, then move to storyboard/keyframe planning without changing the selected sequence architecture unless evidence reveals a blocker.

## Files that matter now
- `project.json`
- `07_SCENARIOS/selected/scenario_s30_a_artisan_care_collection_hero.md`
- `04_REFERENCE_STRATEGY/reference_plan_s30_a.md`
- `20_SEQUENCES/P0002-S01/MASTER_SEQUENCE.md`
- `20_SEQUENCES/P0002-S01/CLIP_C01.md`
- `20_SEQUENCES/P0002-S01/CLIP_C02.md`
- `20_SEQUENCES/P0002-S01/CLIP_C03.md`
- `20_SEQUENCES/P0002-S01/BOUNDARY_C01_C02.md`
- `20_SEQUENCES/P0002-S01/BOUNDARY_C02_C03.md`
- `HANDOFF.md`
