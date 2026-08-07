# AI Video Ad Lab dashboard

- System version: 1.1.1
- Primary operator: ChatGPT / AI operator architecture
- Active projects: 1
- Project current stages: `P0001` → STAGE_04 Reference Asset Creation
- P0001 HERO-45 QA: completed. `R0002` selected as secondary geometry reference (~4.3/5); `R0001` alternate (~4.2/5).
- P0001 TOP-CLEAN QA: completed. `R0003` selected as primary clean product identity ingredient (~4.8/5); `R0004` approved alternate (~4.7/5).
- P0001 MACRO QA: completed. `R0006` selected as texture/material-only reference (~4.5/5); `R0005` alternate (~4.4/5).
- Next pending reference role: `REF-PROD-ASSORTMENT-DETAIL`, then character reference.
- Open experiments: 1 (`EXP-0001` separate ingredients vs contact sheet; planned, non-blocking).
- Active prompt package: `PKG_REFERENCE_IMAGES_V04_ASSORTMENT` for the next two controlled image generations.
- Recent validated learnings: 0 global; project observations continue accumulating.
- Open observations/hypotheses:
  - `OBS-0001` Flow seven-ingredient operational limit;
  - `OBS-0002` ChatGPT Image low inter-run variance for P0001 HERO-45;
  - `OBS-0003` conservative source-preserving top edit retained identity better than novel-angle generation;
  - `OBS-0004` macro refs can improve material evidence while still regularizing silhouette/wrapper details;
  - `HYP-0001` separate single-role ingredients outperform collage.
- Recent failure tags: mild `proportion_drift`, `packaging_drift`, `style_drift`, `paper_cup_material_drift`, `mild_geometry_regularization`.
- Cross-chat readiness: enabled via `AI_START_HERE.md` + project `HANDOFF.md`.
- Next recommended action: generate exactly two assortment-detail candidates using original real photo + R0003 clean top + R0006 as texture/material-scale support and `PKG_REFERENCE_IMAGES_V04_ASSORTMENT/prompt.txt`; attach both for QA before character generation.

Generated/maintained dashboard; not source of truth. Project truth lives in project metadata/status/handoff and underlying evidence.
