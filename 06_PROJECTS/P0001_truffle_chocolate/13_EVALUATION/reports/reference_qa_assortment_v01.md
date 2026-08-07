# P0001 — Assortment Detail Reference QA v01

## Candidates
- `P0001-R0007` — 1000015960.png
- `P0001-R0008` — 1000015961.png

Both were generated with ChatGPT Image from the same controlled prompt package `PKG_REFERENCE_IMAGES_V04_ASSORTMENT` and the same authority stack: original real product photo, selected TOP-CLEAN R0003 and selected MACRO R0006.

## Decision
- `R0008` → **SELECTED / APPROVED** as `REF-PROD-ASSORTMENT-DETAIL`, approx `4.5/5`.
- `R0007` → `PASS_WITH_CAVEATS`, approx `4.1/5`, retained as evidence/alternate.

## Why R0008 wins
R0008 satisfies the exact six-subject requirement, contains the requested product-supported diversity, clearly includes both round nonpareils and elongated sprinkles, keeps all six dark fluted paper cups readable and maintains the dark-neutral studio language used across the approved reference set.

R0007 also preserves useful assortment diversity, but reintroduces the original wooden tabletop despite explicit instructions to use a dark-neutral background. That makes it less compatible as a Flow ingredient and is a clear instance of source-background contamination.

## Shared limitation
Both outputs regularize handmade truffles toward cleaner, more uniform spheres and a designed 3+3 arrangement. Therefore R0008 is not a geometry authority. It is approved specifically for:
- supported color-family diversity;
- coexistence of round and elongated decoration types;
- approximate particle scale;
- cup consistency;
- close assortment reference behavior.

Authority hierarchy remains:
`Original real source > R0003 TOP-CLEAN for visible identity/geometry > R0008 for assortment diversity > R0006 for micro texture/material > R0002 for inferred novel-angle depth`.

## Operational learning
A multi-reference generation can obey requested subject count and diversity while still inheriting an unwanted scene feature from the original source image. Explicit negative background instructions reduce but do not eliminate source-background contamination. For future reference generation, if the original source contains a visually dominant environment that should not persist, prefer a cleaned/segmented primary source or give the cleaned source greater operational weight, while preserving the original as an evidence authority.
