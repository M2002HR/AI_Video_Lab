# Reference QA — Character Trio v01

## Candidates
- `P0001-R0009` — approved alternate, ~4.7/5.
- `P0001-R0010` — approved / selected, ~4.8/5.

## Decision
Select `P0001-R0010` as `REF-CHAR-CHOCOLATIERS`.

## Why R0010 wins
Both candidates correctly isolate the character style from the old cheesecake creative and remove dessert/scene contamination. R0010 is preferred because all three bodies read slightly more evenly, Character C exposes more arm/body anatomy, and the trio functions better as a reusable one-slot cast reference.

## Shared strengths
- exactly three miniature adult chocolatiers;
- consistent deep-red double-breasted chef jackets and red chef hats;
- dark trousers and shoes;
- coherent premium stylized miniature language;
- readable moustache / clean-shaven / small-goatee identities;
- no old dessert, product or prop contamination;
- clean dark background;
- full-body framing and good simultaneous sharpness.

## Shared caveat
Both outputs encode specific standing poses. The selected character ingredient must therefore be described downstream as **identity/style authority only**. Video and scene prompts must explicitly override pose/action while preserving character appearance.

## Production implication
A single clean group image containing the exact three intended recurring chefs is acceptable for the planned Flow ingredient budget because the three are meant to appear as one recurring cast, not as multiple alternative views of one subject. This is different from a product multi-view collage: the group composition represents three real intended scene entities.

## Next gate
Core reference asset roles are now sufficiently established to leave pure reference generation and lock scenario/shot timing. Scene-specific combined keyframes should be created only after that lock.
