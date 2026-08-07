# P0001 — Reference QA: Macro v01

## Candidates
- `P0001-R0005` — first macro candidate
- `P0001-R0006` — second macro candidate

## Decision
Select `P0001-R0006` as `REF-PROD-MACRO` for the first active reference set.
Retain `P0001-R0005` as alternate evidence.

## Why R0006 wins
The Macro slot exists primarily to teach the downstream video model texture/material scale. R0006 provides:
- clean multicolor round-nonpareil scale;
- believable attachment/contact between particles;
- useful dark-chocolate visibility in tiny gaps;
- better dark fluted paper-cup material than R0005;
- clean isolated background;
- high macro readability.

## Caveat / authority boundary
R0006 is slightly too spherical/regular compared with the real handmade product. It must therefore be used only as `texture_detail` authority. It does **not** override:
1. the original real product photograph;
2. `P0001-R0003` TOP-CLEAN for visible handmade geometry/arrangement.

R0005 has somewhat better irregular handmade silhouette but a noticeably glossier/translucent cup that reads less like matte confectionery paper.

## Approx scores
| Criterion | R0005 | R0006 |
| --- | ---: | ---: |
| Product category | 4.8 | 4.8 |
| Handmade geometry | 4.5 | 4.0 |
| Nonpareil scale | 4.4 | 4.6 |
| Particle physics/contact | 4.6 | 4.7 |
| Material realism | 4.3 | 4.5 |
| Paper-cup fidelity | 3.8 | 4.5 |
| Macro usefulness | 4.6 | 4.8 |
| Overall | 4.4 | **4.5** |

## Learning
A clean Macro reference can improve material/particle evidence while still regularizing large-scale geometry. Reference roles must therefore remain explicitly bounded: texture references should not silently become shape authorities.

## Next gate
Proceed to `REF-PROD-ASSORTMENT-DETAIL`, using the original real photo as highest authority, R0003 as clean identity support, and R0006 only for particle/material scale.
