# Storyboard QA — SB-P0003-001R1

## Decision
**REPAIR REQUIRED / NOT YET APPROVED**.

The first continuity repair improved the lift/bite logic, but it over-corrected the count lock in Panels 7 and 8 by creating **two empty cups** while showing only one lifted truffle.

## Provenance
- User returned a ChatGPT-generated repaired storyboard contact sheet in the active project chat.
- Generation tool/model/settings: ChatGPT image generation; exact model/settings unknown.
- Output dimensions: 1672 × 941 px.
- Output bytes: 3,033,916.
- SHA-256: `a73be9895fd6258607470971aedfddcc7c3373bb78e3bcdf140864380302d2e7`.
- Binary is not published to the public repository; this record preserves metadata and QA findings.

## Passed checks
- Eight-panel 2×4 contact-sheet structure is preserved.
- Panels 1–6 remain visually consistent with the intended storyboard and Panel 6 still reads as the complete 25-piece hero state.
- Exact top-down white-studio grammar is preserved.
- No visible human anatomy appears.
- Kraft-box identity, dark paper cups, coating families, color diversity, and invisible-chef mechanism remain readable.
- Panel 8 bite is clear and physically plausible at storyboard level.

## Blocking continuity failure
### Panels 7 and 8 — two vacancies for one lifted truffle
Panel 7 now shows one floating truffle above the box, but **two dark empty paper cups are visibly vacant near the center**. That implies only 23 truffles remain seated, so 23 seated + 1 lifted = 24 total rather than the locked 25.

Panel 8 inherits the same two-vacancy state. Therefore the correction still fails the required continuity equation:
- Panel 6 = 25 seated;
- Panel 7 = 24 seated + 1 lifted;
- Panel 8 = same 24 seated + same lifted truffle with bite.

## Repair scope
Do not regenerate the storyboard concept.

Preserve Panels 1–6 exactly as they are. In Panels 7 and 8 only:
1. keep **one** of the two current near-center empty cups as the lifted-piece origin;
2. restore the **other** currently empty cup with the exact truffle that occupies that position in Panel 6;
3. make the floating truffle match the exact truffle removed from the single remaining empty cup;
4. keep exactly 24 seated truffles in both Panels 7 and 8;
5. keep the same single empty cup in both Panels 7 and 8;
6. Panel 8 adds only the bite to the same floating piece; no other object changes.

Preferred continuity choice: keep the **upper near-center vacancy** as the lifted origin and restore the lower/central vacancy from Panel 6. The floating truffle should match the multicolor coated truffle removed from that retained vacancy.

## Gate result
Storyboard QA: **FAIL — SECOND LOCAL REPAIR REQUIRED**.

Return `SB-P0003-001R2` for a focused count-lock QA pass before keyframe generation.