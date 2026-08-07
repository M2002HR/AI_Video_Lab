# Google Flow — Gemini Omni Flash

tool_id: TOOL-VID-FLOW-OMNI-FLASH  
tool_name: Google Flow / Gemini Omni Flash  
category: video_generation  
verification_status: mixed_official_and_operational  
last_verified: 2026-08-07

## Officially verified capabilities
Google Flow Help currently states that Gemini Omni Flash supports:
- Text to Video in both supported aspect ratios, 4s/6s/8s/10s.
- First Frame to Video, 4s/6s/8s/10s.
- Ingredients/References to Video, both aspect ratios, 4s/6s/8s/10s.
- advanced character/avatar and audio references.
- video-to-video editing up to 10 seconds.

Official source:
- https://support.google.com/flow/answer/16352836?hl=en

Google's Flow generation guidance states:
- provide product/subject ingredients on plain or segmented backgrounds;
- avoid extra subjects in location/style references unless intentional;
- avoid contradictions between text and visual inputs;
- explicitly describe how ingredients should be used;
- consistent look/feel across ingredient images helps blending.

Official source:
- https://support.google.com/flow/answer/16353334?hl=en

## Image-reference count / operational limit
### Current working rule
**Up to 7 image-reference slots for Omni Flash reference-to-video.**

Evidence status:
- User reports the current Flow UI permits a maximum of seven Ingredients.
- Third-party documentation of the Flow backend/API exposes `referenceImage_1` through `referenceImage_7` for Omni Flash and describes a seven-image combined reference budget.
- The current official Google Help pages verified above do not state the numeric seven-image maximum.

Corroborating non-Google source:
- https://useapi.net/docs/articles/omni-flash-bash

Therefore record `7` as a **provisional operational constraint**, not a timeless officially documented fact. Re-verify when model/UI changes.

## Internal reference-budget policy v1
- Hard operational cap: 7.
- Default target: 4–6 active ingredients.
- Keep 1–2 slots unused in the first pass when possible.
- Every ingredient must have an explicit role.
- More references are not automatically better: redundant/conflicting images increase ambiguity.
- Prefer orthogonal information: primary 3/4 geometry, top/composition, macro texture, assortment diversity, character-only, scene/keyframe.

## Contact sheet / multi-view collage policy
Default: **not recommended as a production substitute for multiple ingredient slots.**

Reasoning is inferential, based on Google's advice for clean references and avoiding extra subjects. A collage creates several visual instances inside one image and can blur whether the model should treat them as identity evidence or simultaneous scene objects. It may also increase duplication/composition leakage.

This is not an official prohibition. Track as a hypothesis and test with controlled A/B experiments.

If testing a collage:
- product only;
- clean neutral consistent background;
- no style/scene reference mixed into the sheet;
- 2–4 views maximum;
- no unnecessary text/labels;
- never replace the primary single-view identity image;
- compare against the identical views uploaded separately.

## Recommended product-ad use
For identity-sensitive commercial products, prioritize reference quality and role clarity over filling the slot limit. Use the old creative/style image only upstream to derive a clean project-specific style or character asset when it contains a different product that could contaminate the final generation.

## Known risks
- product/reference contamination;
- identity drift from conflicting refs;
- duplicated objects when multi-object reference images are ambiguous;
- model/UI limits can change rapidly;
- vendor feature availability may vary by region/account.

## Evidence to collect
Record future project Runs with:
- number of ingredient slots used;
- roles per ingredient;
- whether any collage/contact sheet was used;
- product-identity score;
- prompt adherence;
- duplication/reference-contamination failures.
