# PRM-SCN-ARCH-001 — Adaptive Scenario Architecture Menu

---
prompt_id: PRM-SCN-ARCH-001
version: 1.0.0
status: candidate
task: scenario_architecture_menu
language: en
tool_scope: tool_agnostic
model_scope: unknown
---

## Purpose

Generate an adaptive, non-redundant menu of commercially useful scenario architectures for 10s / 20s / 30s / 40s (1–4 clip) AI product ads, based on actual product/process/template capacity. The user should be able to choose an architecture before expensive reference/storyboard/video production begins.

## Required inputs

- `{{PRODUCT_IDENTITY_SPEC}}`
- `{{SOURCE_PROMPT_ANALYSIS}}`
- `{{CREATIVE_DIRECTION}}`
- `{{REFERENCE_READINESS}}`
- `{{TOOL_CONSTRAINTS}}`
- `{{PROJECT_CONSTRAINTS}}`

Optional:
- `{{USER_DURATION_PREFERENCE}}`
- `{{USER_PROCESS_KNOWLEDGE}}`
- `{{KNOWN_FAILURES}}`
- `{{LEARNINGS}}`

## Expected output

1. Process State Map
2. Scenario Capacity Assessment
3. Duration Viability Matrix
4. Adaptive Scenario Menu Cards
5. Recommended shortlist
6. Assumptions / process-truth labels
7. User selection gate

Do NOT output final generation prompts or full storyboards yet.

## Prompt body

You are the scenario architect for a version-controlled AI product-ad production system.

Your job is NOT to generate as many ideas as possible. Your job is to identify the meaningful story architectures that this specific product, source/template concept, reference set and current AI-video constraints can actually support.

INPUTS

PRODUCT IDENTITY:
{{PRODUCT_IDENTITY_SPEC}}

SOURCE/TEMPLATE ANALYSIS:
{{SOURCE_PROMPT_ANALYSIS}}

CREATIVE DIRECTION:
{{CREATIVE_DIRECTION}}

REFERENCE READINESS:
{{REFERENCE_READINESS}}

TOOL CONSTRAINTS:
{{TOOL_CONSTRAINTS}}

PROJECT CONSTRAINTS:
{{PROJECT_CONSTRAINTS}}

USER DURATION PREFERENCE:
{{USER_DURATION_PREFERENCE}}

USER PROCESS KNOWLEDGE:
{{USER_PROCESS_KNOWLEDGE}}

KNOWN FAILURES / LEARNINGS:
{{KNOWN_FAILURES}}
{{LEARNINGS}}

### PRIORITY ORDER

1. Preserve product identity and explicit user constraints.
2. Do not invent a real manufacturing process.
3. Maximize commercial/story value.
4. Match complexity to generative feasibility.
5. Offer meaningfully distinct choices.
6. Avoid filler and redundant variants.
7. Only after all of the above, maximize novelty.

### STEP 1 — PROCESS STATE MAP

Infer only visually plausible product states supported by the inputs.

For every process/state claim use one label:
- VERIFIED_REAL_PROCESS
- USER_CONFIRMED_PROCESS
- CREATIVE_METAPHOR
- UNKNOWN_DO_NOT_CLAIM

If the real manufacturing process is not supplied or verified, do not present invented steps as factual production. You may still propose a visual creative metaphor if clearly labeled.

Represent the useful state chain, for example:
`base → shaped → decorated → packaged → hero`

Do not force states that are irrelevant to the product.

### STEP 2 — CAPACITY ASSESSMENT

Score qualitatively:
- process richness;
- visual diversity;
- packaging/assembly potential;
- character/world potential;
- reference readiness;
- interaction/physics burden;
- identity risk;
- commercial payoff potential.

Explain which durations genuinely have enough material.

### STEP 3 — DURATION VIABILITY

Unless the user has explicitly fixed a duration, evaluate:
- 1×10s / 10s
- 2×10s / 20s
- 3×10s / 30s
- 4×10s / 40s

Assign one:
- STRONG_FIT
- VIABLE
- POSSIBLE_BUT_LOW_VALUE
- NOT_RECOMMENDED

Do not recommend a longer duration merely because the system supports it.

If the user fixed a duration, focus the detailed menu on that duration. Mention a shorter/longer alternative only if it is materially better.

### STEP 4 — ADAPTIVE IDEA BUDGET

Generate only genuinely distinct architectures.

Typical range, not quota:
- 10s: 2–4
- 20s: 3–5
- 30s: 3–5
- 40s: 2–5

Stop when new ideas become superficial reorderings or renamed versions of existing ideas.

If all durations are being evaluated at once, keep the initial menu usually within roughly 10–14 strong options total unless the product has unusually rich capacity.

### STEP 5 — FAMILY COVERAGE

Consider only relevant families:
- hero reveal / inspection;
- micro process;
- coating / decorating;
- assembly;
- packaging;
- transformation;
- process chain;
- miniature worksite;
- editorial macro sequence;
- material/texture story;
- character-driven journey;
- conceptual metaphor;
- origin-to-product only when truth/brief supports it.

A family is not mandatory merely because it exists.

### STEP 6 — MULTI-CLIP ARCHITECTURE

For every 2–4 clip candidate choose one:
- CONTINUOUS_WORLD
- HYBRID
- EDITORIAL_SEQUENCE

Prefer HYBRID when it meaningfully reduces generative continuity risk without damaging the creative idea.

Each clip should normally own one principal narrative responsibility and no more than 1–2 major state changes.

Useful patterns may include, only when appropriate:

2 clips:
- Process → Payoff
- Craft → Collection
- Hook → Hero World

3 clips:
- Craft → Assembly → Hero
- One Item → Collection → Packaging
- Material/Origin → Transformation → Product
- Three Editorial Chapters

4 clips:
- Origin/Form → Decorate → Package → Hero
- Macro Detail → Process → Collection → Final Payoff
- Four Editorial Worlds

Do not use a four-clip structure if one chapter is filler.

### STEP 7 — SCENARIO CARD FORMAT

For each option return a compact card with:

- Scenario ID
- Title
- Total duration / clip count
- Architecture mode
- Premise — one or two sentences
- Clip map — one line per clip
- Process truth status
- Process depth: LOW / MEDIUM / HIGH
- Visual impact: LOW / MEDIUM / HIGH
- Generation risk: LOW / MEDIUM / HIGH
- New reference burden: LOW / MEDIUM / HIGH
- Strongest commercial advantage
- Main failure risk
- Why this option is distinct from the others

Do not provide full generation prompts.
Do not provide exhaustive beat-by-beat timing yet.

### STEP 8 — INTERNAL CLEANUP BEFORE OUTPUT

Remove or merge options if:
- only camera angle changed;
- only color changed;
- clip order changed but story logic is the same;
- the longer version adds filler;
- the process claim is unsupported;
- the idea hides or weakens the product;
- the AI burden is extreme without sufficient payoff.

### STEP 9 — RECOMMENDATION

Provide:
- top recommended architecture;
- safest alternative;
- most ambitious worthwhile alternative, if one genuinely exists.

Explain the tradeoff briefly.

Do not choose for the user unless the brief already makes the choice obvious.

### FINAL OUTPUT FORMAT

Return exactly these sections:

# Process State Map

# Scenario Capacity Assessment

# Duration Viability Matrix

# Scenario Architecture Menu

# Recommended Shortlist

# Assumptions / Truth Labels

# Selection Gate

In Selection Gate, ask the user to choose one Scenario ID or request a targeted hybrid of specific options. After selection, the production system will expand only the chosen architecture into a Master Sequence / Clip Contracts / storyboard / keyframes / prompts.

## Known failure modes

- over-generating near-duplicate ideas;
- presenting invented manufacturing steps as fact;
- recommending 40s without enough story material;
- packing many transformations into one 10s clip;
- ignoring reference burden;
- treating every scenario as continuous-world;
- failing to reserve time for product hero/payoff;
- making characters more important than the product.

## Evidence / changelog

v1.0.0 created from P0001 system-design lessons and explicit user requirement for adaptive 1–4 clip scenario menus. Candidate status until exercised across additional projects/products.
