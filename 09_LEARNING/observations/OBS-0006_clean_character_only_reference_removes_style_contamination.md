# OBS-0006 — Clean character-only reference removes old creative contamination

status: observation  
confidence: provisional  
project: P0001  
date: 2026-08-08

## Observation
Starting from an old creative reference that contained both miniature chefs and an unrelated cheesecake scene, a dedicated character-only generation produced two clean, highly consistent three-chef references (`P0001-R0009`, `P0001-R0010`) with no visible cheesecake, cherry, product or prop contamination.

## What appears to have helped
- explicitly assigning the source image `character-style-only` authority;
- exhaustive exclusion of old product/scene objects;
- exact intended cast count (`three`);
- consistent simple uniform design;
- simple robust identity differences (moustache / clean-shaven / small goatee);
- dark empty reference background;
- full-body group framing.

## Caveat
The generated character reference also encodes pose. Therefore downstream use should explicitly say the image defines character appearance/style only and that scene prompts define pose/action. This observation does not yet prove that a group reference is globally better than separate individual character references.

## Current local rule for P0001
Use selected `P0001-R0010` as one `character_only` Ingredient for the recurring three-chef team. Do not upload the contaminated old cheesecake creative to the final video generation.

## Future validation
On later projects, compare clean group-character references against separate individual-character ingredients when ingredient budget permits and character consistency is a dominant risk.
