# OBS-0001 — Flow Omni Flash seven-ingredient operational limit

- Date: 2026-08-07
- Source: explicit user observation from current Google Flow usage.
- Project: P0001
- Classification: operational observation, externally corroborated, not yet an official Google Help numeric claim.

## Raw observation
The user reports that Google Flow allows a maximum of seven Ingredients for the intended Omni workflow.

## Corroboration
A current third-party Flow API integration documents Omni Flash `referenceImage_1..7` and a seven-image combined reference budget: https://useapi.net/docs/articles/omni-flash-bash

Official Google Flow Help confirms Omni Flash supports Ingredients/References to Video at 4s/6s/8s/10s and publishes ingredient-cleanliness best practices, but the currently verified Help pages do not state the numeric maximum of seven:
- https://support.google.com/flow/answer/16352836?hl=en
- https://support.google.com/flow/answer/16353334?hl=en

## Operational consequence
Use 7 as the current maximum in production planning, label the confidence as provisional, and re-verify after major Flow/model changes. Do not design workflows that require all seven slots to be filled.
