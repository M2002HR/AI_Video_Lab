# P0001 — Stage 05 Reference QA: HERO-45 v01

Date: 2026-08-07  
Compared Runs: `P0001-R0001`, `P0001-R0002`  
Tool: ChatGPT Image  
Source: original top-down truffle product photo + identical `PKG_REFERENCE_IMAGES_V01/RUN_1` prompt.

## Verdict
Both candidates **PASS WITH CAVEATS** as secondary geometry references. `P0001-R0002` is the preferred HERO-45 candidate because the box depth, truffle height and cup relationship are slightly more legible for later video generation.

Neither candidate should replace the original/cleaned top-down photo as the highest-authority product-identity reference. Novel-view generation necessarily inferred hidden geometry and regularized some handmade variation.

## Scores — 0 to 5

| Criterion | R0001 | R0002 | Notes |
|---|---:|---:|---|
| Product category | 4.7 | 4.7 | Clearly truffles; no category leakage. |
| Overall identity | 4.2 | 4.2 | Strong family resemblance, but not exact reconstruction. |
| Geometry / proportions | 3.8 | 4.0 | Useful 3D inference; truffles too uniform/round vs original. |
| Material realism | 4.3 | 4.2 | Convincing edible surface; mild polished/CG regularity. |
| Coating / texture fidelity | 4.5 | 4.4 | Round nonpareils and elongated sprinkles both represented well. |
| Color-family fidelity | 4.6 | 4.6 | Strong assortment diversity. |
| Paper cups | 4.2 | 4.2 | Correct dark fluted concept; somewhat blacker/cleaner than source. |
| Kraft-box fidelity | 3.9 | 4.0 | Correct material/category; walls look thicker/more designed than source. |
| Handmade imperfection | 3.4 | 3.4 | Main weakness: excessive sphere/size/order regularization. |
| Background cleanliness | 5.0 | 5.0 | Excellent neutral production reference background. |
| Text / watermark exclusion | 5.0 | 5.0 | No unwanted source watermark or invented branding. |
| Angle usefulness | 4.5 | 4.7 | R0002 provides slightly stronger depth/height evidence. |
| Artifact severity | 4.6 | 4.6 | No major structural artifacts visible. |
| Reference usability | 4.3 | 4.5 | Good secondary Ingredient candidates. |

Approximate overall assessment: R0001 `4.2/5`, R0002 `4.3/5`.

## Main strengths
- Stable truffle category.
- Strong color/coating diversity.
- Clean dark studio presentation.
- Clear individual dark fluted cups.
- Useful 3D information absent from the source top view.
- Two independent outputs show low inter-run variance.

## Main failure tendencies / caveats
- Product becomes more manufactured than the real source: spheres, sizes and spacing are too regular.
- Box structure is inferred and slightly upgraded/thickened.
- Paper cups read darker and cleaner than the original.
- Arrangement changes; these images cannot be treated as exact factual records of the original layout.

Failure tags: `proportion_drift`, `packaging_drift`, `style_drift` (mild / non-blocking).

## Decision
- `P0001-R0002` → selected temporary role: `REF-PROD-HERO-45`, **secondary geometry reference**.
- `P0001-R0001` → retained as evidence/alternate, not selected.
- Change reference hierarchy: cleaned original top view should become `product_identity_primary`; generated HERO-45 becomes `geometry_view` / secondary identity evidence.
- Strengthen future prompts with explicit artisan-imperfection preservation.
- Continue to `REF-PROD-TOP` using a conservative edit strategy before generating Macro and Assortment Detail.

## Media provenance
The generated binaries were attached in the ChatGPT session and are not committed to normal Git.
- R0001 attached file SHA-256: `85713aa7b6f46a11ac8685d9fe857ed91458ab89b5f3b705a600c933dcfd1b1a`
- R0002 attached file SHA-256: `5a34729bb49b1a4f96f2e0a2671439cba1150f0dd2016b9d803bfe229a6d9f76`
