# Scenario Architecture System

This is the primary source for proposing scenario options before heavy production. The system supports 10, 20, 30, and 40-second deliverables (typically 1–4 short clips) without overwhelming the user with low-value variations.

## UX rule
Before storyboard/keyframe production, build a **Scenario Architecture Menu** and let the user choose. If duration/clip count is already specified, focus on that architecture. If not, assess 1–4 clips and show only durations that add real value.

## Standard units
For tools that generate 10-second clips:
- `1x10s` = 10s
- `2x10s` = 20s
- `3x10s` = 30s
- `4x10s` = 40s

Adapt the same logic when the actual clip duration differs.

## Scenario Capacity Assessment
Assess before ideation:
1. **Process State Map** — what real or useful product states exist?
2. **Product diversity** — components, colors, coatings, materials, packaging states, macro details.
3. **Creative-world capacity** — e.g. miniature workers, factory metaphor, luxury studio, material transformation.
4. **Reference readiness** — whether states can be supported without excessive new reference generation.
5. **Generative feasibility** — state changes, interactions, characters, object counts, and continuity burden.
6. **Commercial arc** — whether extra duration adds payoff or merely filler.

Every process/state claim must be labeled `verified`, `user_confirmed`, `creative_metaphor`, or `unknown`. Never invent a real manufacturing process from appearance alone.

## Duration viability
For each relevant duration assign one of:
- `strong_fit`
- `viable`
- `possible_but_low_value`
- `not_recommended`

Give a concise reason and recommended candidate count.

## Adaptive candidate count
Candidate count is not a quota. Typical ranges:
- 10s: 2–4 distinct options
- 20s: 3–5
- 30s: 3–5
- 40s: 2–5

Stop when additional ideas are only renamed/reordered versions of existing ones. The initial menu should normally remain under roughly 10–14 meaningful architectures even when several durations are considered.

## Scenario families to consider when appropriate
- hero / reveal / inspection
- making / forming
- coating / decorating
- assembly / arrangement
- packaging
- transformation
- multi-stage process chain
- miniature worksite / factory metaphor
- editorial macro/material sequence
- character-driven product story
- ingredient-to-product only when verified/appropriate

Not every family fits every product.

## Scenario card
Each menu option should be compact and selectable, containing:
- scenario ID/title;
- duration and clip count;
- architecture mode: `continuous_world`, `hybrid`, or `editorial_sequence`;
- premise;
- clip-by-clip role summary;
- process depth;
- visual impact;
- generation risk;
- new-reference burden;
- strongest commercial advantage;
- main failure risk;
- process truth label.

Do not generate full image/video prompts or detailed beat-by-beat production before the user selects an architecture.

## Duration-specific guidance
### 10s
Prefer one clear idea: one stable state + camera reveal, one main transformation, or two simple sequential actions. Avoid compressing forming + coating + transport + packaging + reveal into one clip.

### 20s / 2 clips
Strong patterns include Process -> Payoff, Craft -> Collection, Macro Detail -> Hero, or two editorial worlds with shared identity.

### 30s / 3 clips
Strong patterns include Craft -> Assembly -> Hero, One Item -> Collection -> Packaging, Material -> Making -> Payoff, or three editorial chapters. This is often a good length for process storytelling because each clip can own one responsibility.

### 40s / 4 clips
Use only when four genuinely valuable chapters exist, such as Form -> Decorate -> Package -> Reveal. If two middle clips repeat the same responsibility, recommend 30s instead.

## Architecture modes
- **Continuous world** — all clips are consecutive parts of one physical world; highest continuity burden.
- **Editorial sequence** — independent scenes connected by identity, style, rhythm, edit, and audio; usually safer for generative video.
- **Hybrid** — hard continuity inside clips with controlled match/action/editorial boundaries; often a strong default candidate, never mandatory.

Do not choose continuous mode merely because it feels more cinematic; reliability and commercial quality take priority.

## Boundary planning
For every `Cn -> Cn+1`, define what remains fixed, allowed changes, transition type, product/object/character state, camera/motion direction, environment/lighting, and whether the previous End Keyframe becomes the next Start-State evidence.

## Selection gate
Do not enter heavy production until the user/brief selects a Scenario Architecture. After selection: expand the scenario, create `MASTER_SEQUENCE.md` for multi-clip work, create a Clip Contract per clip, revisit per-clip reference strategy, then proceed to shot timing/storyboard/keyframes/video prompting.

## Anti-overgeneration rules
- Merge near-duplicates.
- A color/angle/name change is not a new scenario.
- Do not recommend longer duration without new state/story value.
- Do not invent real process.
- Do not recommend 40s just because the system supports four clips.
- The menu should reduce decision burden, not increase it.

## Documentation
Persist Process State Map, capacity assessment, duration viability, scenario cards shown to the user, important omitted families and reasons, user selection, and next gate.
