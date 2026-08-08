# P0001 — KF01 v02 Minimal-Reference QA

## Scope
Evaluate `P0001-R0014` and `P0001-R0015`, generated from the revised no-prop KF01 prompt using ONLY:
- R0003 TOP-CLEAN product reference;
- R0010 CHARACTER reference.

This test evaluates `HYP-0002`: whether fewer role-clean references plus removal of active worksite props improves combined-scene compliance.

## Result
The hypothesis receives strong project-level support.

Compared with v01 (R0011–R0013), both v02 candidates materially improve:
- same-box continuity;
- prop cleanliness;
- character count stability;
- face readability;
- scene coherence;
- product/character integration.

The repeated v01 failures involving bowls, tools, loose ingredients and separate workshop surfaces disappear in both v02 outputs.

## R0014
Status: pass as scene-grammar evidence, not final opening KF01.  
Approx score: 4.1/5.

Strengths:
- inside-box physical world;
- exact three chefs;
- no props or loose ingredients;
- all faces readable;
- coherent product assortment.

Remaining issues:
- too wide for opening macro;
- chef scale larger than requested 1:3 ratio;
- character pose leakage;
- mild product regularization.

## R0015
Status: selected as combined scene master / KF02-like mid-frame anchor.  
Approx score: 4.3/5.

Strengths:
- strongest inside-box continuity;
- clean product-dominant composition;
- exact three chefs with readable identities;
- no prop contamination;
- useful box/assortment depth for later camera path;
- strong candidate for deriving tighter and wider views.

Remaining issues:
- temporal framing is too advanced for 00:01 opening;
- original 1:3 scale target not reached;
- poses partially inherit character reference;
- hero geometry remains more regular than real handmade source.

## Key conclusion
Do NOT discard a high-quality scene solely because it misses the intended storyboard timestamp. When scene grammar is strong but temporal framing is wrong, reassign the image to the storyboard role it actually fits.

For P0001, R0015 becomes a `SCENE MASTER / KF02-like` anchor. The true KF01 should now be derived as a conservative tighter camera view of R0015 rather than independently synthesizing the entire product+character world again.

## Scale decision
The requested hero-truffle diameter ≈ 3× chef height was not achieved in either v02 candidate. Both images still communicate an unambiguous miniature-world relationship. For this project, treat the stable visual ratio in R0015 as an acceptable working scale for continuity unless a later generation can reduce chef scale without destabilizing identity. Do not force a global rule from this single case.

## Next test
Generate two `KF01 v03` derived-camera candidates from R0015.

Recommended references:
1. R0015 — authoritative scene master for composition, character placement and combined-world continuity;
2. R0003 — secondary product-identity authority only.

Do not upload R0010 in this derivation pass unless character identity visibly drifts; R0015 already contains the accepted recurring cast and direct reuse avoids reintroducing pose-reference pressure.

Primary change: camera/crop only — closer, slightly lower view that reveals much less of the surrounding assortment while preserving the same physical scene.
