# OBS-0009 — Scene-master camera derivation preserved combined-world continuity

status: provisional_observation  
project: P0001  
linked_runs: P0001-R0015, P0001-R0016, P0001-R0017

## Observation
After a stable combined product+character scene was selected (`R0015`), generating adjacent storyboard views by treating that scene as the primary authority and requesting mostly a camera/framing change produced more reliable continuity than rebuilding the scene from separate product/character reference stacks.

In P0001:
- R0011–R0013 independent combined-scene synthesis failed the strict gate with role bleed, props, scene anchoring problems and scale drift.
- R0014–R0015 minimal two-reference synthesis created a stable inside-box scene grammar.
- R0016–R0017, derived from R0015 + one product backup reference, preserved the same box world, cast, hero product, lighting and scene cleanliness while changing camera distance successfully.

## Evidence
R0016 and R0017 both:
- contain exactly three chefs;
- preserve readable cast identities;
- remain inside the kraft box;
- contain zero invented worksite props;
- provide a clearly closer camera state than R0015;
- maintain plausible continuity toward the R0015 mid-state.

## Remaining caveats
- pose leakage can persist from the inherited scene/cast;
- framing requests may not reduce surrounding context as aggressively as specified;
- generated product geometry can remain more regular than the source product.

## Working implication
For storyboard continuity in this project, prefer:

`stable scene master → derive nearby camera states`

over
`independently regenerate each keyframe from many references`.

Do not promote as a global canonical rule until repeated on additional projects or benchmark cases.
