# 2026-08-08 — Historical media proxy backfill

## User request
User asked to retroactively store reduced-quality Git copies of previously supplied P0001 images and videos so future ChatGPT sessions can inspect them without requiring immediate re-attachment.

Requested identifiers:
`R0003`, `R0010`, `R0015`, `R0016`, `R0020`, `R002`, plus previously supplied videos.

Interpretation:
- `R002` was interpreted as `R0002` because P0001 contains a selected 45° product reference with that ID and no meaningful `R002` identifier.
- videos = evaluated Flow V01 runs `R0022` and `R0023`.

## Backfilled Git proxies
- `R0002` — `REF-PROD-HERO-45`
- `R0003` — `REF-PROD-TOP-CLEAN`
- `R0010` — `REF-CHAR-CHOCOLATIERS`
- `R0015` — `REF-SCENE-MASTER`
- `R0016` — `KF01`
- `R0020` — `KF03`
- `R0022` — selected final 10s video
- `R0023` — rejected video retained as fourth-chef duplication failure evidence

Storage directory:
`19_HANDOFF_ASSETS/git_previews/`

Manifest:
`19_HANDOFF_ASSETS/proxy_manifest.json`

## Quality / purpose
These are intentionally low-resolution cross-chat previews and `source_of_truth=false`.
They are intended for:
- scene recall;
- broad product identity;
- character count/style recall;
- composition;
- keyframe relationship;
- broad video motion/failure inspection.

They are not intended for:
- generation-grade source uploads;
- texture-critical QA;
- color-critical judgment;
- final delivery quality.

## Privacy decision
Repository is public. User explicitly requested these already-supplied P0001 assets and videos be stored in reduced quality in Git, so this backfill is treated as publication approval for these specific proxies only.

Future sensitive/client/confidential media remains subject to the Media Proxy Pipeline privacy gate.

## Implementation note
The active connector did not provide a direct local-file-to-Git binary upload action in the initial path. A repository GitHub Actions workflow, `.github/workflows/decode-media-proxies.yml`, was added to decode temporary base64 staging payloads into actual `.webp`/`.mp4` Git files. The decoded binaries were verified in the Git preview directory. This workaround is implementation-specific and does not change the higher-level storage policy.
