# Multi-Clip Architecture

This document defines longer advertisements made from **2, 3, or 4 short clips**; for 10-second clip tools this usually means 20s, 30s, or 40s.

## Design principle
A longer ad must not be random short videos glued together. Design a **Master Sequence** first, then treat each clip as an independently producible/QA-able unit with explicit start/end contracts.

Run `SCENARIO_ARCHITECTURE_SYSTEM.md` before locking clip count.

## Common chapter patterns
### 2 clips
Process -> Payoff; Craft -> Collection; Detail -> Hero; Problem/Metaphor -> Product Resolution.

### 3 clips
Craft -> Assembly -> Hero; One Item -> Collection -> Packaging; Material -> Making -> Payoff; three editorial worlds.

### 4 clips
Use only when four chapters add independent value, e.g. Form -> Decorate -> Package -> Reveal. Downgrade to three clips if one chapter is filler.

## Architecture modes
### Continuous world
Audience should perceive clips as consecutive portions of one world. Requires shared product/character/environment/lighting locks, boundary states, camera/position continuity, and exact object-count/placement where necessary. Highest generative risk.

### Editorial sequence
Each clip is a mini-scene; connection comes from product identity, style, rhythm, conceptual match, edit, and audio. Spatial continuity burden is lower and is often safer.

### Hybrid
Continuity is strict inside each clip; boundaries use controlled approved frames, match cuts, motion cuts, or editorial cuts. Often the best reliability/cinematic balance for 20–40s, but not mandatory.

## Master Sequence requirements
Before Clip 01 production, define:
- total duration and clip count/duration;
- selected scenario ID/title;
- architecture mode;
- overall story arc and final payoff;
- role of every clip;
- product state at clip starts/ends;
- character state/count;
- environment, camera, and lighting state;
- transition type at every boundary;
- shared vs clip-specific references;
- shared prompt blocks;
- audio/music continuity.

## Clip Contract
Every clip records:
### Start state
Product state, character count/identity/position, environment, camera/framing, lighting, important visible props.

### Action arc
Main action, state changes, object interactions, camera move. Default to no more than 1–2 major state changes unless evidence supports more.

### End state
Product state, character state, camera state, and transition-ready composition.

### Risk / references / QA
Interaction/physics/count/identity risks, minimum sufficient reference stack, boundary-critical assets, and QA criteria.

## Boundary Contract
For each `Cn -> Cn+1` define exact invariants and allowed changes. For hard/hybrid continuity, prefer generating and approving the End Keyframe of Clip N before using that state as the primary Start-State reference for Clip N+1. For editorial cuts, exact geometry may change, but identity/style/direction/pacing must be intentional.

## Reference strategy
Shared references may include clean product identity, character identity, packaging identity, global scale rules, and style/lighting bible when necessary. Clip-specific references may include start/end states, scene master, process-state evidence, or required tool/prop evidence.

Do not fill reference slots merely because they exist. Design a minimum sufficient role-clean stack per clip. A reference useful in one task can contaminate another.

## Production order
Create/approve each boundary-critical asset before locking the dependent next clip. Each clip follows its own shot/storyboard/keyframe/prompt/preflight/generation/QA/final-selection loop.

## Assembly
After selecting each clip final: frame-accurate trim, intentional transition, exposure/color match, audio/music bridge, optional post text/logo, and delivery-format assembly. Record all post changes.

## Sequence QA
In addition to per-clip QA, check product identity, character identity/count, scale, lighting/color, movement direction, product/action state continuity, transition smoothness, repeated/contradictory moments, total pacing, escalation of interest, and final commercial payoff.

## Escalation
If a hard boundary requires more than two repair cycles because of stochastic reconstruction, consider downgrading to hybrid/editorial or using a post-production match cut. Overall commercial quality matters more than proving impossible pixel-perfect continuity.

## IDs
A project may have `P0002-S01` sequence ID and `P0002-C01...C04` clip IDs. Run IDs remain project-global and include `sequence_id`/`clip_id` in metadata.
