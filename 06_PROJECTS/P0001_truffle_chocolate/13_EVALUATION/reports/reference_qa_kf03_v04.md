# KF03 v04 QA — R0018 / R0019

## Goal
Derive a farther + higher final hero camera state from `R0015` while using `R0003` only as product/packaging truth backup. The strict requirement was camera-path continuity: `R0016 → R0015 → KF03` without rebuilding the world.

## R0018 — 3.9/5 — FAIL STRICT CONTINUITY / RETAIN AS STANDALONE HERO CANDIDATE
Strengths:
- complete kraft box is clearly readable;
- premium clean dark studio framing;
- exactly three chefs remain present and are still inside the box;
- no tools, bowls, loose ingredients or debris;
- product assortment is commercially strong and close to R0003.

Critical failure:
- the distinct multicolor hero truffle from R0015 disappears as a traceable local object;
- its immediate neighboring arrangement is rebuilt;
- the frame snaps toward the global product-layout grammar of R0003 instead of behaving as a pure farther camera state of R0015.

Decision: do not use as trajectory KF03. Retain as a useful standalone final-product/aesthetic target.

## R0019 — 3.3/5 — FAIL
Strengths:
- clean full-box product presentation;
- good assortment readability;
- no tools/debris.

Critical failures:
- same hero/local-layout continuity loss as R0018;
- stronger source-reference snap toward R0003;
- all three chefs move outside/in front of the box, breaking the established physical positions from R0015;
- therefore camera-only continuity is implausible.

Decision: reject as sequence endpoint.

## Root-cause interpretation
The secondary `R0003` product reference is extremely strong because it carries a complete coherent full-box arrangement. During a wide-camera derivation, the image model appears to prefer reconstructing toward that globally coherent product layout rather than extrapolating the partial world in R0015. This creates a conflict between two goals:

1. scene-master spatial continuity;
2. source-product full-box fidelity.

For the next controlled pass, remove `R0003` from the image derivation and use `R0015` alone as the scene/world authority. Product truth remains available later as a separate Flow ingredient and prompt constraint; it does not need to be injected into every storyboard derivation.

## Next experiment / repair
Generate two KF03 v05 candidates from `R0015` ONLY.

Success criteria:
- same central multicolor hero remains traceable in the same cup/local region;
- same three chefs remain in the same broad inside-box region;
- camera is simply farther and moderately higher;
- additional box/assortment may be extrapolated around the existing scene, but the existing local scene may not be replaced;
- no tools/loose ingredients;
- no character teleportation.

If master-only still cannot create a coherent full-box endpoint, stop forcing a single still-image interpolation architecture. Use `R0018` as a final aesthetic/product target and design the Flow prompt around a continuous camera reveal without a strict end-frame identity requirement, or split the production into separate controlled clips.
