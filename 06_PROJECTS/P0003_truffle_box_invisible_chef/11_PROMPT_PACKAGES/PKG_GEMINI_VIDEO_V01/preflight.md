# Video Preflight — PKG_GEMINI_VIDEO_V01

## Decision
**PASS / GENERATION AUTHORIZED**.

Target tool: Gemini video generation. Exact model/settings remain unknown and must not be guessed.

## Reference stack
Use only:
1. `REF-P0003-001` — clean product/packaging/environment authority.
2. `KFSET-P0003-001` — temporal/state authority for opening, partial fill, and lift state.

Do not upload the storyboard contact sheet unless troubleshooting later. The final prompt explicitly forbids reproduction of multi-panel layouts.

## Checklist
- [x] Exact task/duration/aspect resolved: one continuous 10-second 16:9 video.
- [x] Reference hierarchy explicit and role-clean.
- [x] Camera instructions consistent: fixed exactly 90-degree top-down, no movement.
- [x] Timeline sums to exactly 10.0 seconds.
- [x] High-risk count/contact/physics constraints are explicit.
- [x] Complexity controlled by allowing only one dominant action family at a time and clearing prior utensils/dishes before the next beat.
- [x] Final state defined: 24 seated + one bitten floating truffle + one empty cup, held through the end.
- [x] Known failure modes addressed: extra-object count drift, multiple vacancies, visible anatomy, contact-sheet leakage, background contamination, packaging redesign, perfect-sphere drift, magical levitation look, and utensil clutter.

## Known risks
1. **10-second process density:** still demanding, but actions are grouped into seven readable beats and object clutter is explicitly cleared between beats.
2. **Final count drift:** strongest risk. Prompt repeats exact 25 -> 24+1 continuity and requires a single visible vacancy.
3. **Reference-sheet leakage:** keyframe input is a three-panel sheet. Prompt explicitly treats it as state reference only and forbids split-screen/panel reproduction.
4. **Handmade identity drift:** clean derivative/keyframes are slightly more regular than the real source. Prompt explicitly restores subtle irregularity and keeps simple kraft packaging.
5. **Invisible-chef motion may look magical:** prompt requires acceleration, gravity, collisions, settling and prohibits glow/trails/fantasy VFX.

## Generation instructions
Upload `REF-P0003-001` and the approved three-panel keyframe sheet `KFSET-P0003-001`, then paste `resolved_prompt.md` unchanged for the first baseline run.

Do not tune the prompt before the baseline. Register the first returned video as `P0003-R0001` and run Video QA before deciding any repair or iteration.

## Gate result
Video Preflight: **PASS**.
Advance to `STAGE_16` — Video Generation.