# Video prompt preflight — PKG_FLOW_OMNI_VIDEO_V01

Checklist source: `04_CHECKLISTS/CHK_VIDEO_PROMPT_PREFLIGHT.md`.

## Gate
- [x] Duration explicitly 10 seconds.
- [x] Aspect ratio explicitly 16:9.
- [x] Timeline uses four simple phases with one primary camera action.
- [x] Camera instruction is non-contradictory: one backward dolly + shallow upward crane, same side, no cut/orbit/top-down jump.
- [x] Physics/contact/count are constrained: products stationary, exactly three chefs, empty hands, zero props.
- [x] Start/mid/end visual anchors defined through selected KF01 / scene master / KF03.
- [x] Reference roles and conflict priority are explicit.
- [x] Complexity is bounded: camera is main motion; only minimal character micro-motion.
- [x] Final ~1s hero hold explicitly defined.
- [x] Product identity and forbidden category transformations included.
- [x] Character identity/facial-hair continuity included.
- [x] Scene-reconstruction failure mode explicitly prohibited.
- [x] Ingredient stack intentionally limited to five; two operational slots reserved.

## Known residual risks
1. Keyframe stills contain a central hero truffle larger than the source box's normal size distribution. This is retained for sequence continuity and miniature scale, not treated as universal product geometry.
2. Character poses in source stills are somewhat static; prompt explicitly treats pose as flexible and asks only for restrained micro-motion.
3. Flow may still reinterpret spatial arrangement despite anchor hierarchy. First two runs are controlled baseline tests and must be evaluated frame-by-frame.
4. More references are intentionally excluded because P0001 image experiments showed reference competition/over-conditioning.

## Decision
**PASS — proceed to STAGE_16 VIDEO GENERATION.**

Expected first video Runs:
- `P0001-R0022`
- `P0001-R0023`
