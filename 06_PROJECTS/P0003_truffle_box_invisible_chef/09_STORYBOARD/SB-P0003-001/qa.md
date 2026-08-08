# Storyboard QA — SB-P0003-001

## Decision
**REPAIR REQUIRED / NOT YET APPROVED**.

The storyboard is broadly successful and preserves the intended creative grammar, but the final lift/bite continuity fails the 25-piece count lock and must be repaired before advancing to keyframes.

## Provenance
- User returned a ChatGPT-generated storyboard contact sheet in the active project chat.
- Generation tool/model/settings: ChatGPT image generation; exact model/settings unknown.
- Output dimensions: 1672 × 941 px.
- Output bytes: 3,082,317.
- SHA-256: `a516d0da0dfeae835ed8488982db6ba0415c5608ce373697987ea1abf97468d7`.
- Binary is not published to the public repository; this record preserves metadata and QA findings.

## Passed checks
- Correct 8-panel contact-sheet structure in two rows of four.
- Fixed visual grammar remains exactly top-down throughout.
- Pure white studio background is consistent.
- No visible hands, arms, faces, sleeves, people, or human shadows.
- Kraft-box identity and diamond orientation remain consistent whenever the box appears.
- Panel 1 correctly communicates the empty-box / 25-paper-cup setup.
- Panel 2 clearly communicates chocolate-center formation with self-moving utensils.
- Panel 3 clearly communicates coating with both nonpareil and elongated-sprinkle families.
- Panels 4–6 communicate progressive filling and reach a readable 25-piece hero assortment.
- Product colors, dark paper cups, kraft packaging, and handmade truffle identity remain recognizable.
- No wooden-table, watermark, branding, label, or unrelated-product contamination appears.

## Blocking continuity failure
### Panels 7 and 8 — lifted-piece count lock
The floating mixed-rainbow truffle reads visually as an **additional object above an already full box**, rather than as one of the original 25 truffles being removed from the assortment.

There is no clearly visible vacated cup / empty slot in the box corresponding to the lifted truffle. This creates a likely 26-object interpretation and breaks the selected timeline rule that one truffle lifts while the **remaining 24** stay seated and unchanged.

Panel 8 inherits the same problem. The bite itself is readable, but the bitten floating piece must remain the exact same truffle from Panel 7 and the same vacated slot must remain visible in the box.

## Minor non-blocking notes
- Panel 4 contains several finished truffles outside the box; acceptable at storyboard level, but downstream prompts should keep exterior clutter minimal.
- The derivative product is slightly cleaner/more regular than the original real photograph; original source remains ultimate identity authority.

## Repair scope
Do **not** regenerate the concept from scratch. Preserve Panels 1–6 as closely as possible.

Repair only Panels 7 and 8 so that:
1. exactly one identifiable mixed-rainbow truffle is removed from a near-center cup;
2. the corresponding dark fluted paper cup is visibly empty in both panels;
3. exactly 24 truffles remain seated in the box;
4. Panel 7 shows the removed truffle hovering above the box;
5. Panel 8 shows the same truffle, same hover position family, same empty cup, and one realistic bite exposing dark chocolate interior;
6. no other truffle positions, colors, counts, packaging geometry, camera, or background change.

## Gate result
Storyboard QA: **FAIL — LOCAL REPAIR REQUIRED**.

Return repaired storyboard candidate `SB-P0003-001R1` for a focused QA pass before keyframe generation.