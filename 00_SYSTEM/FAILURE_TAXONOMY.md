# Failure Taxonomy

A failure tag describes a symptom, not a proven root cause. Every tagged Run should record visible symptoms, likely cause(s), origin stage, severity, and repair/regenerate decision.

## Product identity
- `product_identity_drift` — output no longer matches locked product identity.
- `wrong_product_category` — product becomes another category.
- `geometry_morphing` — shape changes unexpectedly across frame/time.
- `proportion_drift` — dimensions/ratios deviate.
- `texture_drift` — surface treatment/material changes.
- `color_drift` — unsupported color shift.
- `packaging_drift` — package geometry/material/style changes.
- `component_count_error` — incorrect count of product/package components.
- `logo_corruption` — logo is malformed or inconsistent.
- `text_corruption` — required visible text is malformed/invented.

## Temporal continuity
- `object_teleportation` — object changes position without plausible motion.
- `object_duplication` — extra copy appears.
- `object_disappearance` — required object vanishes.
- `scale_instability` — apparent physical scale pumps independently of camera.
- `continuity_break` — scene state cannot be reconciled across time.
- `sudden_pose_change` — character/object pose changes discontinuously.
- `temporal_texture_flicker` — texture or decoration flickers.

## Physics / interaction
- `bad_contact` — contact point is visually/physically wrong.
- `intersecting_geometry` — objects pass through each other.
- `floating_object` — unsupported object floats.
- `incorrect_gravity` — motion contradicts gravity.
- `impossible_deformation` — implausible shape deformation.
- `liquid_behavior_error` — liquid flow/contact is implausible.
- `tool_interaction_error` — tool/hand/object mechanics are incorrect.

## Character
- `bad_hands` — malformed hands/fingers.
- `extra_limbs` — extra or missing limbs.
- `duplicate_character` — extra copy of a character appears.
- `character_identity_drift` — face/body identity changes.
- `clothing_drift` — wardrobe changes unexpectedly.
- `task_confusion` — character performs the wrong action/role.

## Camera / focus
- `camera_jump` — camera state changes discontinuously.
- `unintended_zoom` — digital/optical zoom not requested.
- `unstable_framing` — jitter or inconsistent composition.
- `excessive_camera_motion` — motion overwhelms the intended action/product.
- `focus_error` — important subject becomes unintentionally unreadable.

## Lighting / scene
- `lighting_flicker` — lighting intensity/color changes over time.
- `shadow_inconsistency` — shadows contradict object/light continuity.
- `background_morph` — background/environment reconstructs unexpectedly.
- `reference_contamination` — unwanted content from a reference leaks into output.
- `unwanted_prop` — undeclared prop appears.
- `environment_drift` — world/location/material language changes.

## Prompt / planning
- `contradictory_instruction` — prompt contains incompatible requirements.
- `over_complex_timeline` — too many actions/state changes for duration/model.
- `ambiguous_reference_role` — reference influence is unclear or competing.
- `insufficient_identity_lock` — product/character identity constraints are underspecified.
- `reference_overload` — too many competing references degrade control.
- `missing_end_state` — final frame/state is not explicitly constrained.

## Audio / delivery
- `audio_mismatch` — audio does not match action/brief.
- `format_error` — wrong aspect, duration, codec, resolution, or delivery format.
- `branding_error` — required branding placement/state is wrong.

## Repair rule
For every failure determine whether it is local/cosmetic or structural. Repair local issues when feasible. Regenerate or return to the likely root stage for identity, structural, continuity, or repeated stochastic failures. Record the decision and evidence.
