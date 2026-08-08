# Master Workflow

This workflow uses stable stage IDs `STAGE_00` through `STAGE_23`. The Documentation Contract is part of Definition of Done at every stage.

## Scenario / multi-clip routing
After Creative Direction and before heavy production, run `SCENARIO_ARCHITECTURE_SYSTEM.md`. If duration is not locked, assess 1x10s through 4x10s and present only meaningful options. For 2–4 clips, create the Master Sequence, Clip Contracts, and boundary contracts before per-clip shot/prompt work. A 10-second clip should normally carry no more than 1–2 major state changes; otherwise consider decomposition.

## STAGE_00 — Project Intake
**Input:** brief and original inputs.
**Action/Gate:** preserve originals; register deliverable, provenance, hashes, assumptions, and gaps.
**Output:** project.json, STATUS, inventory.

## STAGE_01 — Source Prompt Analysis
**Input:** immutable source prompt and brief.
**Action/Gate:** separate structural DNA, old-product content, reusable creative concepts, contradictions, and tool assumptions using KEEP/ADAPT/REMOVE.
**Output:** source prompt analysis and risk matrix.

## STAGE_02 — Product Identity
**Input:** product images.
**Action/Gate:** document category, silhouette, proportions, materials, texture, color, packaging/components, natural irregularity, uncertainty, and forbidden transformations.
**Output:** product identity spec, identity lock, uncertainty log.

## STAGE_03 — Reference Strategy
**Input:** identity spec and objective.
**Action/Gate:** decide which cleanup/angle/macro/scene references are truly necessary; separate identity authority from style influence.
**Output:** reference plan and role map.

## STAGE_04 — Reference Generation
**Input:** approved reference plan.
**Action/Gate:** generate only required single-purpose references; each meaningful generation is a Run.
**Output:** reference Runs.

## STAGE_05 — Reference QA
**Input:** originals and generated references.
**Action/Gate:** compare geometry/color/material/labels/identity against authoritative source; approve/reject with reasons.
**Output:** approved reference set.

## STAGE_06 — Creative Direction
**Input:** brief and approved references.
**Action/Gate:** lock campaign idea, emotion, realism, scale, environment, camera, lighting, rhythm, and product priority.
**Output:** creative direction.

## STAGE_07 — Scenario Architecture
**Input:** creative direction + identity + source analysis + tool constraints.
**Action/Gate:** build Process State Map, capacity assessment, duration viability, and adaptive scenario menu without inventing real process.
**Output:** process state map, capacity assessment, scenario menu.

## STAGE_08 — Scenario Selection
**Input:** scenario candidates and rubric.
**Action/Gate:** evaluate focus, feasibility, complexity, commercial payoff, reference burden; lock single/multi-clip architecture after user selection.
**Output:** selected scenario and decision.

## STAGE_09 — Shot Timing
**Input:** selected scenario.
**Action/Gate:** sequence beats, framing, camera, contact/physics, audio cues, and final hero; for multi-clip do this per Clip Contract.
**Output:** timeline, camera plan, continuity rules.

## STAGE_10 — Storyboard
**Input:** shot design.
**Action/Gate:** define composition, subject, action, and transition for every controlling beat.
**Output:** storyboard specification.

## STAGE_11 — Storyboard QA
**Input:** storyboard.
**Action/Gate:** gate continuity, composition, timing, accidental complexity, and product focus.
**Output:** storyboard QA report.

## STAGE_12 — Keyframe Generation
**Input:** storyboard and identity lock.
**Action/Gate:** generate only controlling keyframes/boundary frames with full provenance.
**Output:** keyframe Runs.

## STAGE_13 — Keyframe QA
**Input:** keyframes and authoritative references.
**Action/Gate:** evaluate identity, scale, light, scene, character, and boundary continuity.
**Output:** approved keyframe set.

## STAGE_14 — Video Prompt
**Input:** identity + references + scenario + timeline.
**Action/Gate:** combine base logic, tool adapter, explicit reference roles, physics/count constraints, temporal plan, and final-state rules.
**Output:** video prompt package.

## STAGE_15 — Video Preflight
**Input:** prompt package.
**Action/Gate:** check contradictions, complexity, reference roles, timing, camera, known failure modes, and settings.
**Output:** preflight report.

## STAGE_16 — Video Generation
**Input:** approved package and settings.
**Action/Gate:** register every generation with exact prompt/tool/model/settings/references/output metadata.
**Output:** video Runs.

## STAGE_17 — Video QA
**Input:** video Run.
**Action/Gate:** perform frame-by-frame evaluation of identity, morphing, count, contact, gravity, camera, lighting, temporal stability, and final hero.
**Output:** video QA report.

## STAGE_18 — Repair Decision
**Input:** QA and failure tags.
**Action/Gate:** repair local cosmetic issues; regenerate or return to root stage for identity/structural/continuity failures.
**Output:** repair/regenerate decision.

## STAGE_19 — Final Selection
**Input:** evaluated Runs.
**Action/Gate:** select with rubric and brief; never select an unevaluated final; multi-clip selects one final per clip.
**Output:** selected final Run(s).

## STAGE_20 — Post Production
**Input:** final candidate(s).
**Action/Gate:** record trims, assembly, transitions, color/exposure, text/logo overlays, audio, and delivery format.
**Output:** edit/composite/assembly record.

## STAGE_21 — Final QA
**Input:** deliverable.
**Action/Gate:** verify brief, format, brand, text/logo, audio, sequence continuity, and commercial readiness.
**Output:** final QA report.

## STAGE_22 — Postmortem
**Input:** Runs and QA.
**Action/Gate:** record successes/failures, retries, best prompts/tools, recurring failures, and next experiments.
**Output:** postmortem.

## STAGE_23 — System Learning
**Input:** postmortem and evidence.
**Action/Gate:** classify OBS/HYP/EXP/LRN and promote only evidence-supported changes.
**Output:** learning/change records.

## Source prompt analysis standard
Preserve the source prompt unchanged. Record a KEEP / ADAPT / REMOVE matrix covering duration, aspect, camera, lighting, scale, background, characters, timing, physics, sound, hero framing, old-product-specific details, reusable creative metaphors, contradictions, and risk. An adapted prompt is a new provenance-tracked asset, never an overwrite of the source.

## Documentation and language gates
Every meaningful decision, prompt, Run, feedback item, failure, learning, workflow discovery, and next action needed for continuation must be persisted. All persisted repository text is English-only.
