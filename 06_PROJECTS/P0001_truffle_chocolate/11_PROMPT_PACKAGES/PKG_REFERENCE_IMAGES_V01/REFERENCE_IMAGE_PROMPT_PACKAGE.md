# P0001 — Reference Image Prompt Package v01

## Goal
Create clean, identity-faithful reference assets for later Google Flow / Gemini Omni Flash Ingredients-to-Video generation. This package is **not** for the final ad yet.

## Recommended first tool
**Google Flow image generation → Nano Banana Pro**, if available on the account.

Why as the first test: current Google Flow Help describes Nano Banana Pro as the advanced image model for complex designs, highly accurate details and professional-grade control, and Flow can save generated/edited images directly as video ingredients. This is a vendor capability claim, not yet an internal P0001 benchmark result. Each generation must be registered as a Run so we can compare later.

Official source verified 2026-08-07: https://support.google.com/flow/answer/16352836?hl=en

## Non-negotiable generation method
- Use the **original product photo** as the product reference for every Slots 1–4 generation.
- Generate **one target view per run**. Do not ask for a four-panel contact sheet or multiple angles in the same output.
- Do not use the old cheesecake/tiny-chef storyboard as an ingredient while generating product references. It is style DNA only and could contaminate product identity.
- Product reference images should be clean, single-purpose and visually compatible with one another.
- First optimize identity; only then optimize cinematic beauty.
- If an output materially changes product category, box structure, coating style, paper cups or assortment logic, reject rather than repair it into the approved set.

---

# MASTER PRODUCT IDENTITY LOCK

Use this block at the beginning of every product-reference prompt.

```text
PRODUCT REFERENCE PRIORITY — STRICT IDENTITY PRESERVATION

Use the uploaded original truffle product photograph as the highest-priority and authoritative visual source for the product. Preserve the product category, handmade geometry, material identity, coating types, color-family diversity, individual paper cups, kraft-box packaging and overall artisanal character. The goal is to reveal the same real product from a cleaner or more useful photographic view, not to redesign it.

The product is a collection of handmade chocolate truffles. Each truffle is a small near-spherical chocolate form with subtle organic handmade irregularities; the spheres are not mathematically perfect and must not look factory-molded. The dark chocolate body is densely covered directly on its surface with either tiny round edible sugar nonpareils or thin elongated edible sprinkles. The assortment includes multiple visibly different coating/color families such as white, pink, bright or dark blue, purple, yellow/lime, red-green-white, orange/brown and mixed rainbow combinations. Preserve the impression of a varied colorful assortment rather than turning all truffles into one uniform design.

Every finished truffle sits inside its own small dark charcoal-gray fluted paper candy cup. The holder must read as folded matte paper, not foil, plastic or a cupcake wrapper. The assortment is presented closely together inside an open natural kraft-brown cardboard gift box with a simple unbranded handmade appearance. Preserve the warm matte paperboard material and believable box depth.

The chocolate and decorations must look physically edible and photographic: dark chocolate with matte-to-satin food reflections; tiny dry sprinkles/nonpareils with individual irregularity and micro-shadows; natural paper texture on the cups and kraft box. Avoid glossy plastic, toy-like beads, synthetic candy-shell appearance or CGI-perfect surfaces.

Never reinterpret the product as cake pops, bonbons with hard geometric shells, cupcakes, cookies, macarons, donuts, chocolate bars or generic candy balls. No sticks. No invented logos. No invented labels. Do not reproduce the watermark or external text visible in the source photograph. Do not add decorative packaging that is not supported by the source.

Identity-critical traits have priority over composition and style. If a requested camera angle requires inferring hidden geometry, infer conservatively from the visible product and keep the design simple and consistent rather than inventing new features.
```

---

# RUN 1 — REF-PROD-HERO-45

## Purpose
Primary product identity and geometry reference for Omni Flash. This should be the most informative single product ingredient.

## Target
Full open kraft box, 3/4 approximately 35–45 degree camera angle, showing box depth, truffle height, paper cups, assortment density and surface coatings.

## Prompt

```text
[PASTE MASTER PRODUCT IDENTITY LOCK ABOVE]

TASK
Create a clean premium reference photograph of the exact same truffle assortment from a natural three-quarter hero angle, approximately 35–45 degrees above the front edge of the box. This image will be used as a product-identity ingredient for a later generative video, so clarity and faithful geometry are more important than dramatic styling.

COMPOSITION
Show the complete open natural kraft-brown gift box centered in frame. The camera should clearly reveal the top surfaces of the truffles while also revealing enough side height to understand that each truffle is a rounded three-dimensional object seated inside an individual dark fluted paper cup. Keep the box fully legible as a shallow kraft cardboard container; do not redesign its folds or add a lid unless supported by the reference.

ASSORTMENT
Maintain the impression of approximately the same dense multi-color assortment seen in the original photograph. Preserve visibly different coating families: tiny round nonpareils and elongated sprinkles. Preserve the varied palette rather than creating repeated clones. The truffles should be similar in overall scale but naturally handmade and slightly irregular.

BACKGROUND
Use a simple seamless neutral studio background suitable for a clean AI reference asset. Prefer a soft neutral charcoal-gray to near-black matte background with no table planks, no props, no utensils, no decorative food, no text and no watermark. The background must not compete with or redefine the product.

LIGHTING
Soft controlled studio product lighting. Large diffused key light from upper front-left, subtle fill from the opposite side, very gentle edge separation from the dark background. Highlights should reveal chocolate and sprinkle micro-texture without making the product glossy or plastic. Keep illumination even enough that all major truffle colors and paper cups remain readable.

CAMERA / IMAGE CHARACTER
Photorealistic premium food product photography, natural perspective, moderate depth of field. Keep the entire box and most truffles acceptably sharp; do not use such extreme shallow depth of field that identity information disappears. No fisheye, no exaggerated wide-angle distortion, no dramatic tilt.

REFERENCE-ASSET CLEANLINESS
One box only. One assortment only. No duplicate floating truffles around the box. No hands, chefs, characters or old dessert elements. No words, logos, arrows, labels, borders or multi-panel collage.

FINAL QUALITY GATE
The result should look like a believable new studio photograph of the same product, not an AI redesign. Product identity fidelity > aesthetic novelty.
```

---

# RUN 2 — REF-PROD-TOP

## Purpose
Clean top-down identity/composition reference derived from the original product photo, without watermark or distracting wooden environment.

## Preferred method
Use image editing rather than free regeneration if Flow/Nano Banana Pro offers a reliable edit path. Preserve the truffles and box as much as possible; replace only the environment/distractions.

## Prompt

```text
[PASTE MASTER PRODUCT IDENTITY LOCK ABOVE]

TASK — CONSERVATIVE EDIT
Create a clean top-down product-reference version of the uploaded original photograph. Preserve the truffles, their handmade shapes, coating types, approximate color distribution, individual dark fluted paper cups, kraft box geometry and dense arrangement as faithfully as possible. Treat the original product area as protected identity content.

CHANGE ONLY WHAT IS NECESSARY
Remove the external wooden tabletop visual influence and remove the visible `CHOCOLAT.CHOCOLATE` watermark/text. Replace the surrounding environment with a simple seamless matte neutral charcoal-gray or near-black studio background. Do not invent branding. Do not decorate the box. Do not add props.

CAMERA
Maintain a true overhead / top-down view with the full box comfortably inside frame. Keep straight believable box geometry and avoid perspective warping.

LIGHTING
Clean diffused overhead studio light with subtle directional shaping. Preserve readable color differences between the various sprinkles/nonpareils. Maintain realistic tiny shadows between decorations and believable paper texture.

DO NOT
Do not change the product category. Do not turn truffles into hard glossy bonbons. Do not standardize every truffle into an identical sphere. Do not change dark fluted cups into bright cupcake wrappers. Do not add or remove large numbers of truffles merely to make a symmetrical pattern. Do not create a contact sheet, text, border, logo or watermark.

OUTPUT PURPOSE
This image is an identity/composition ingredient for video generation; factual faithfulness is more important than making a new creative hero image.
```

---

# RUN 3 — REF-PROD-MACRO

## Purpose
Texture/material reference that teaches the video model what a single truffle, its coating and paper cup should look like at macro scale.

## Prompt

```text
[PASTE MASTER PRODUCT IDENTITY LOCK ABOVE]

TASK
Create a photorealistic macro reference photograph of one representative handmade chocolate truffle from the supplied product collection, seated naturally in its dark charcoal-gray fluted paper candy cup.

SUBJECT
Choose a representative coating family visible in the source, preferably a dense multicolor round-nonpareil truffle because it exposes both the handmade chocolate geometry and the tiny individual edible particles clearly. The underlying dark chocolate may be subtly visible in microscopic gaps between decorations. Keep the truffle near-spherical but organically handmade, with minor asymmetry.

SCALE / DETAIL
The truffle occupies most of the frame without being cropped so aggressively that its full rounded form and the upper portion of the paper cup become ambiguous. Render individual nonpareils or sprinkles with realistic tiny size, irregular placement, contact shadows and edible matte/satin surfaces. Preserve the scale relationship: decorations must look like small confectionery particles attached to a truffle, not large toy beads.

PAPER CUP
Clearly reveal the dark folded fluting around the lower truffle. Matte slightly rough paper texture, physically believable folds, no foil shine.

LIGHTING
Premium soft macro food-photography lighting. Diffused key from upper-left/front and very subtle fill. Micro-highlights should reveal texture but never create a lacquered plastic coating. Natural contact shadow inside the paper cup.

BACKGROUND
Simple dark neutral seamless background, softly out of focus. No box required unless a tiny neutral hint is naturally visible. No other truffles, props, chefs, text or branding.

CAMERA
True macro photographic appearance, natural lens rendering, shallow-to-moderate depth of field focused on the front/top truffle texture while retaining enough of the silhouette and cup to serve as identity evidence. No surreal bokeh shapes, no extreme lens distortion.

OUTPUT PURPOSE
Texture/material reference only. Do not beautify by redesigning the product.
```

---

# RUN 4 — REF-PROD-ASSORTMENT-DETAIL

## Purpose
Show several different coating/color families together from a useful close 3/4 angle so the model understands that the final product is intentionally varied.

## Prompt

```text
[PASTE MASTER PRODUCT IDENTITY LOCK ABOVE]

TASK
Create a clean close three-quarter reference photograph showing a compact group of approximately 4–6 truffles from the exact same product assortment, all seated in their individual dark charcoal fluted paper cups. This is a diversity/assortment reference, not a redesigned promotional arrangement.

VARIETY
Include visibly different coating families supported by the original product: at least one truffle densely covered in tiny round nonpareils, at least one using elongated sprinkles, and several distinct colorways such as pink, blue/purple, white or multicolor. Avoid choosing six nearly identical truffles. Also avoid inventing entirely new decoration styles.

GEOMETRY
All truffles remain handmade near-spheres with subtle individual irregularity and approximately consistent real-world scale. Do not make some truffles huge and others tiny. Keep the paper cups proportionally consistent.

COMPOSITION
Group them naturally close together as they would sit inside the kraft box, but frame tight enough to show surface texture and cup details. A small amount of kraft cardboard may be visible around them to establish packaging context. Do not show unrelated tabletop or props.

LIGHTING / BACKGROUND
Match the neutral studio lighting and dark/neutral background language of the other reference assets. Consistency across all generated ingredients is intentional because these images will be blended by a later video model.

CAMERA
Close food-product photograph from roughly 30–45 degrees above. Moderate depth of field; multiple truffles should remain readable. Avoid extreme macro blur that hides the assortment.

NO CONTAMINATION
No chefs, ladders, cherries, cheesecake, bowls, utensils, logos, labels, text, watermark or contact-sheet layout.
```

---

# RUN 5 — REF-CHAR-CHOCOLATIERS (generated separately after product refs pass QA)

## Purpose
Create a project-specific character-only ingredient so we never need to feed the old cheesecake storyboard into the final video generation.

## Prompt

```text
TASK
Create a clean photorealistic miniature-character reference for a premium food commercial: three tiny friendly adult chocolatiers standing together, presented as consistent recurring miniature workers. They wear coordinated bright deep-red chef jackets, matching red chef hats, dark trousers and practical tiny work shoes. Their bodies are cute and slightly chubby with tasteful stylized proportions, but they must still feel like high-quality physical miniature figures photographed in a real macro studio rather than flat cartoons.

CHARACTER CONSISTENCY
All three characters belong to the same visual world and scale. Distinguish them subtly through face/hair details while preserving matching uniform design. Correct anatomy, two arms/two legs each, coherent hands, no duplicate faces or merged bodies. Friendly focused expressions rather than exaggerated comedy.

REFERENCE-ASSET PRESENTATION
Neutral simple dark studio background. Full bodies visible. Arrange them with enough separation that the video model can understand each silhouette, but keep them in one coherent group rather than a grid/contact sheet. No product, no truffle, no cheesecake, no cherries, no tools, no ladders and no unrelated props. No text or labels.

LIGHTING
Soft premium miniature-photography lighting consistent with a dark luxury food-commercial environment. Clean detail on red fabric and skin/figure materials, subtle shadows, no plastic toy gloss.

OUTPUT PURPOSE
Character identity/scale reference only. This image has no authority over product geometry, colors or packaging.
```

---

# QA BEFORE APPROVAL
For every generated candidate, compare against the original product and score at minimum:
- product category;
- geometry/proportion;
- coating type;
- color-family fidelity;
- dark paper cup fidelity;
- kraft-box fidelity where visible;
- material realism;
- invented branding/text;
- usefulness for its assigned reference role.

Any major identity failure rejects the candidate. Do not approve an image simply because it is beautiful.

## Minimum first batch
Generate at least **2 candidates per product role** (Slots 1–4) if credits allow, one role at a time. This gives 8 product-reference candidates. Register each output as an individual Run. Select one approved winner per role after QA.

## What happens next
After Slots 1–4 pass Stage 05 Reference QA, generate the character reference, finalize the scenario/shot timeline, then create `REF-SCENE-KEYFRAME` and only afterward synthesize the final Omni Flash video prompt.
