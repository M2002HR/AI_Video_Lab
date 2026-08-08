# P0001 Reference Strategy v4

## Target generation mode
Google Flow → Video → Ingredients/References → Gemini Omni Flash → 10 seconds → 16:9.

## Ingredient budget
- Operational maximum for Omni Flash: **7 image-reference slots**.
- Treat 7 as provisional and re-verify after major Flow/model changes.
- Do not fill all seven automatically. Prefer the smallest high-information non-conflicting set.

## Core principle — reference roles are task-specific
A reference can be useful for one task and harmful for another.

Example from P0001:
- R0006 MACRO is useful as a video material/particle reference;
- R0008 ASSORTMENT is useful as a video diversity reference;
- but using both during combined scene-keyframe synthesis amplified their generated regularization and contributed to oversized particles/perfect-sphere drift.

Therefore the **scene-keyframe generation stack does not need to equal the final Flow ingredient stack**.

## Product authority order
1. original real product photograph — ultimate truth/evidence;
2. `R0003` TOP-CLEAN — selected clean visible identity surrogate;
3. `R0008` ASSORTMENT — diversity/coating-family authority;
4. `R0006` MACRO — material/particle-scale authority only;
5. `R0002` HERO-45 — optional inferred depth/geometry support only.

### Environment caveat
The original real photo contains wooden-table context. `OBS-0005` shows that source environment can leak into multi-reference image synthesis even when prompt instructions try to isolate product identity. Therefore the original may remain the project's truth source while being intentionally omitted from a specific generation step if a cleaned surrogate (R0003) carries the needed visible identity information with lower contamination risk.

## Character authority
`R0010` independently defines the recurring three-chef cast appearance/style only:
- moustached foreman;
- clean-shaven chocolatier;
- small-goatee specialist;
- matching deep-red jackets/hats;
- dark trousers/shoes;
- compact premium stylized miniature proportions.

It does NOT define pose, action, tool, scene position or chef-to-truffle scale.

## Collage policy
Do not combine alternate product views into one collage as a production shortcut pending `EXP-0001`. Separate role-clean images remain preferred.

## Approved core references
### R0003 — TOP-CLEAN
Primary clean visible product identity. Selected ~4.8/5.

### R0008 — ASSORTMENT
Diversity/color/coating-family authority. Selected ~4.5/5. Not geometry authority.

### R0006 — MACRO
Texture/material/particle-scale role. Selected ~4.5/5. Not scene-shape authority.

### R0010 — CHARACTERS
Exact recurring trio appearance/style. Selected ~4.8/5.

### R0002 — HERO-45
Optional secondary geometry/depth support. Use only when a test shows a specific need.

## Scene-keyframe v01 evidence — failed
`R0011`, `R0012`, `R0013` were generated with original + R0003 + R0008 + R0006 + R0010.

No candidate passed. Repeated issues:
- extra props and loose ingredients;
- wrong chef scale;
- oversized nonpareils;
- perfect-sphere regularization;
- back-facing character identity loss;
- scene not physically embedded in the final kraft box;
- one wooden/workshop contamination case.

See `13_EVALUATION/reports/reference_qa_kf01_v01.md`, `OBS-0007`, `HYP-0002`.

## Scene-keyframe v02 stack — ACTIVE
For the first repaired KF01 test, upload ONLY:
1. `R0003` TOP-CLEAN — product + packaging + clean environment;
2. `R0010` CHARACTERS — recurring trio appearance/style.

Do NOT upload original, R0008, R0006 or R0002 in the first v02 pass.

Reason: isolate two role-clean authorities and reduce scene/reference bleed. If a later QA identifies one specific missing fact, add only the single reference needed in a controlled follow-up.

Active prompt: `11_PROMPT_PACKAGES/PKG_SCENE_KEYFRAME_V02_KF01/prompt.txt`.

## Active scene design
Scenario v02: `Quiet Inspection → Full Box Reveal`.
- hands empty;
- no tools/bowls/loose ingredients;
- opening already inside the same kraft box;
- hero truffle diameter ≈ 3× chef height;
- all three faces readable;
- one continuous pull-back/upward reveal.

## Provisional final Flow ingredient stack — only after scene passes
The final Flow stack may still use more roles than the image-keyframe generation stack because Omni video prompting can assign separate ingredient roles directly.

Provisional:
1. R0003 TOP-CLEAN — product identity;
2. R0008 ASSORTMENT — diversity;
3. R0006 MACRO — material/particle scale;
4. R0010 CHARACTERS — recurring trio;
5. selected scene keyframe — composition/scale/physical scene anchor;
6. optional R0002 only if needed;
7. reserved.

This stack is not final until video preflight and the scene-keyframe evidence are complete.

## Current gate
Do not generate KF02/KF03 until one KF01 v02 candidate passes:
- same-box physical continuity;
- exact three readable characters;
- correct miniature scale;
- no props/loose food;
- source-like product particle scale and handmade shape;
- clean dark presentation.
