# P0001 — REF-PROD-TOP-CLEAN Prompt Package v02

## Why this package exists
HERO-45 QA showed that novel-angle generation can regularize handmade geometry. The top reference therefore becomes the **primary product-identity Ingredient** and must be source-derived with minimum intervention.

## Preferred execution order
1. Best: non-generative cleanup / segmentation / careful background replacement that leaves the actual product pixels untouched.
2. If not practical: image-edit mode using the original real product photo and the prompt below.
3. Avoid free regeneration from text alone.

## Input
Use **only the original real product photograph** as the visual input. Do not use generated HERO-45, old cheesecake storyboard or style image for this task.

## Prompt

```text
PRIMARY OBJECTIVE — CONSERVATIVE SOURCE-PRESERVING PRODUCT EDIT

Edit the uploaded real product photograph with the smallest possible intervention. This is not a request to recreate, redesign, beautify, restage or reinterpret the product. The actual visible truffles, their handmade shapes, relative sizes, coating patterns, approximate arrangement, individual dark fluted paper cups and kraft-box geometry are protected product-identity information and must remain as close to the source photograph as technically possible.

SOURCE AUTHORITY
The uploaded real photograph is the only authority for product identity in this edit. Do not replace it with a cleaner imagined version. Do not regularize it. Do not make the arrangement more symmetrical. Do not make the truffles more perfectly spherical. Do not standardize their diameter, coating density or placement.

HANDMADE CHARACTER — CRITICAL
Preserve the natural artisan variation visible in the original product. The truffles are handmade and intentionally not mathematically identical. Preserve subtle differences in roundness, diameter, coating density, sprinkle distribution, seating angle and spacing. The box should feel hand-packed by a small chocolatier, not factory-perfect or procedurally arranged.

PRODUCT IDENTITY
The product is an assortment of handmade chocolate truffles. Dark chocolate is densely coated directly with either tiny round edible sugar nonpareils or thin elongated edible sprinkles. Preserve the source's multiple coating/color families, including the visible white, pink, blue, purple, yellow/lime, red-green-white, orange/brown and multicolor combinations. Do not invent a new decoration family and do not collapse the assortment into repeated clones.

Each truffle remains seated in its own dark charcoal-gray fluted matte paper candy cup. Preserve the paper folds and dark-gray character; do not turn them into black plastic, shiny foil or cupcake wrappers.

Preserve the original simple open natural kraft-brown cardboard box. Do not thicken its walls, rebuild its corners, add a lid, hinge, insert, ribbon, window, branding or luxury finishing.

CAMERA AND PRODUCT REGION
Maintain the existing true overhead/top-down viewpoint and the source box orientation. Preserve the product region's geometry and arrangement. Keep the complete box visible with comfortable margin around it. Do not rotate into a new perspective and do not create a new 3D hero angle.

CHANGES ALLOWED — ONLY THESE
1. Remove the visible `CHOCOLAT.CHOCOLATE` watermark/text from the source image.
2. Remove or replace the surrounding wooden tabletop outside the product box with a clean seamless matte neutral charcoal-gray to near-black studio background.
3. If necessary, make only very mild global exposure/white-balance corrections so the product remains readable, without changing actual product colors or texture.

BACKGROUND
The new surrounding background should be simple, matte and visually empty. No wood planks, props, utensils, ingredients, characters, decoration, text, logo, border or graphic design. A very soft natural contact shadow beneath the box is acceptable if needed to avoid a pasted cutout appearance.

LIGHTING PRESERVATION
Do not relight the product so aggressively that the surface identity changes. Preserve believable food texture and source-like shadows. If the background replacement requires integration, use restrained neutral studio illumination only. Do not create glossy luxury highlights or plastic-looking surfaces.

FORBIDDEN CHANGES
Do not add or remove truffles merely to improve composition.
Do not rearrange the assortment into a more symmetric grid.
Do not replace individual truffles with prettier copies.
Do not change nonpareils into sprinkles or sprinkles into nonpareils.
Do not change the paper cups.
Do not redesign the kraft box.
Do not introduce branding.
Do not reproduce the source watermark.
Do not create multiple panels, a contact sheet, alternate views or captions.

QUALITY TEST
The correct result should feel like the original photograph was professionally isolated and cleaned for use as an AI product reference — not like a new AI-generated photograph of a similar box of truffles.

When there is any conflict between visual perfection and source fidelity, choose source fidelity.
```

## Generation protocol
- Generate 2 candidates with the same original input and exact same prompt.
- Do not change settings between A/B candidates when possible.
- Register as next Runs.
- Stage 05 QA compares each candidate directly against the original, with special weight on **number/arrangement/shape changes**.

## Pass condition
A candidate passes only if it preserves substantially more literal source identity than the HERO-45 generated views. Beauty alone is not sufficient.

## Evidence behind v02
- `P0001-R0001`, `P0001-R0002`
- `13_EVALUATION/reports/reference_qa_hero45_v01.md`
- `OBS-0003`
- `03_PRODUCT_IDENTITY/identity_lock_v02.md`
