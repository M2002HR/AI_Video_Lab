# HYP-0001 — Separate single-role ingredients outperform multi-view collage for product consistency

- Status: open hypothesis
- Linked experiment: `EXP-0001`
- Origin: P0001 reference-strategy design

## Hypothesis
For identity-sensitive product video in Google Flow / Gemini Omni Flash, uploading clean product views as separate Ingredients with explicit roles will produce higher product-identity and continuity scores than combining the same views into one contact-sheet/collage image to save slots.

## Rationale
Google recommends clean product/subject ingredient images, avoiding extra subjects in style/location references, explicitly describing ingredient roles, and maintaining a consistent look across ingredients. A collage introduces multiple instances and compositions inside a single image, potentially increasing object duplication or reference-role ambiguity.

## Important uncertainty
Google does not currently publish an explicit rule saying multi-view collages are bad. This is an inference and must be tested, not promoted as universal truth.

## Test design
Once P0001 has approved product views:
- Variant A: upload the same views separately.
- Variant B: combine those views into one clean product-only contact sheet.
- Keep model, prompt, duration, character/scene refs and generation count as constant as possible.
- Compare product identity, geometry stability, duplication, contamination, prompt adherence and commercial usability.

Until the experiment is completed, production default = separate single-purpose ingredients.
