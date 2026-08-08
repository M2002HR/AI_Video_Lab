# SOP — Multi-Clip Sequence

## Purpose
Produce 20s, 30s, or 40s advertisements from 2, 3, or 4 short clips so that each clip can be generated/QA'd independently while the assembled sequence preserves intentional identity, story, and continuity.

Run `00_SYSTEM/SCENARIO_ARCHITECTURE_SYSTEM.md` and `SOP_07_SCENARIO_GENERATION.md` before locking clip count.

## Required input
- selected Scenario Architecture;
- approved product identity;
- creative direction;
- total duration;
- clip count 2/3/4;
- target clip duration and tool constraints.

## Required outputs
- `MASTER_SEQUENCE.md`;
- `sequence_id` and clip IDs;
- Clip Contracts;
- boundary contracts;
- shared and clip-specific reference sets;
- independent prompt package and final Run for each clip;
- assembly plan and final sequence QA.

## Procedure
1. Define the full story/commercial arc before per-clip prompting. Every clip must have one clear responsibility.
2. Divide by state change and narrative function, not merely equal time. Default to no more than 1–2 major state changes per clip.
3. Create a Clip Contract for every clip: start state, action arc, end state, references, risks, and QA.
4. Create a boundary contract for every `Cn -> Cn+1`: invariants, allowed discontinuities, transition type, product/character/object state, camera/motion direction, environment, lighting, and boundary reference.
5. Define shared identity/scale/packaging/style rules.
6. Build a minimum sufficient role-clean reference stack per clip. Avoid filling all available slots.
7. Produce each clip through the standard shot/storyboard/keyframe/prompt/preflight/generation/QA loop. Approve boundary-critical state before locking the dependent next clip.
8. Prefer at least two baseline Runs with identical setup per clip when cost/brief allows so stochastic stability can be assessed.
9. Select a final Run for each clip, assemble with intentional trims/transitions/color/audio, and run sequence QA.

## Transition choices
- Hard continuity — exact continuing action/world; highest risk.
- Match cut — visual/action relationship without pixel-perfect geometry.
- Editorial cut — independent scenes linked by identity/style/rhythm.
- Hybrid — strict continuity within clips plus controlled boundaries; strong default candidate for many AI ads.

## QA gate
Pass when the Master Sequence is locked, every clip role is distinct, every boundary has a contract, shared identity rules are defined, every selected clip Run is evaluated, and the assembled master passes multi-clip continuity/commercial QA.

If a hard boundary repeatedly fails because of stochastic reconstruction, downgrade to hybrid/match/editorial rather than endlessly repairing. If an extra clip adds no new value, shorten the sequence.

Persist all sequence decisions and evidence in English only.
