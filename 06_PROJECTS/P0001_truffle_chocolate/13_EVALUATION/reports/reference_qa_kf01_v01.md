# P0001 — KF01 Combined-Scene QA v01

## Scope
Candidates: `P0001-R0011`, `P0001-R0012`, `P0001-R0013`.
Prompt package: `PKG_SCENE_KEYFRAME_V01_KF01`.
Reference stack: original real product + R0003 TOP-CLEAN + R0008 ASSORTMENT + R0006 MACRO + R0010 CHARACTERS.

## Decision
**NO CANDIDATE PASSES THE SCENE-KEYFRAME GATE.**

`R0012` is the best diagnostic candidate (~3.4/5) but is explicitly not approved as a production scene ingredient.

## Cross-candidate failure pattern
All three candidates preserve the basic tiny-chef + giant-truffle concept, but recurring failures appear across the set:

1. **Prop invention** — bowls, extra tools, loose confectionery particles and/or chocolate debris appear despite strict restrictions.
2. **Scale drift** — chefs are substantially larger relative to the truffle than the requested miniature ratio.
3. **Product regularization** — hero truffle becomes an almost perfect sphere.
4. **Particle-scale drift** — nonpareils become visually oversized compared with the original real product.
5. **Character identity evidence loss** — the center character often faces away from camera.
6. **Continuity setup failure** — the opening scene is staged on a separate studio/workbench surface rather than physically inside the same kraft gift box that the camera must later reveal.
7. **Reference/environment bleed** — R0011 reintroduces wooden-workshop/background-product elements.

## Candidate ranking
1. `R0012` — 3.4/5 — best diagnostic; cleanest scene, still fails gate.
2. `R0013` — 3.2/5 — attractive but cluttered with extra food/props.
3. `R0011` — 2.9/5 — strongest workshop/background contamination.

## Root-cause interpretation
Do not treat this as a wording-only failure. The v01 setup likely contains too many simultaneous creative demands and too many supporting references with imperfect role fidelity:
- R0006 MACRO itself contains larger/more regular nonpareils and a more regular sphere than the original;
- R0008 ASSORTMENT also regularizes truffle geometry;
- the prompt asks for an active finishing action, which encourages the image model to invent tools, bowls and worksite details;
- the phraseology of a miniature worksite encourages generic workshop staging;
- the opening composition was not explicit enough that it must already exist **inside the final kraft box**.

## Strategy change for v02
- remove R0006 and R0008 from the scene-keyframe generation input stack;
- use original real product + R0003 clean top + R0010 character as the core references;
- optionally use R0002 only for conservative box/cup depth, never for truffle appearance;
- remove all tools from the opening keyframe;
- change scenario from `final touch with brush` to `quiet inspection`;
- explicitly place the hero truffle and chefs inside the same real kraft box from frame one;
- require all three character faces to remain visible in 3/4 view;
- express scale as both percentage and simple ratio: truffle diameter about 3× one chef's full standing height;
- shorten and prioritize the prompt instead of adding more negative-list wording.

## Gate
Do not generate KF02/KF03 until a revised KF01 passes product + character + scale + physical-continuity QA.
