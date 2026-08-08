# Media Proxy Pipeline

## Purpose
Ensure important project media does not exist only inside one chat. For meaningful publishable images/videos, the AI operator creates a compact proxy, commits it with provenance, and keeps the original/full-resolution source outside normal Git.

## Trigger conditions
Run proxy sync when an important original/reference image is attached, a generated image is registered as a Run, an approved/rejected reference/keyframe provides useful evidence, a generated video is submitted for QA, or a final Run is selected.

First confirm that the media is locally accessible and publishable.

## Privacy/publication gate
- Sensitive/client/confidential/`do_not_publish` -> `metadata_only`.
- Non-sensitive + project mode `git_previews` -> proxy sync.
- Genuine uncertainty -> ask a short publication/privacy question or use metadata-only.

Low quality is not a privacy control.

## Image procedure
1. Read the source without overwriting it.
2. Normalize EXIF orientation.
3. Convert to RGB/sRGB when practical.
4. Resize long edge to at most 1280px without upscaling.
5. Encode WebP around quality 72.
6. Remove metadata/EXIF.
7. Record dimensions, bytes, SHA-256, and profile.

## Video procedure
1. Read the source without overwriting it.
2. Preserve aspect ratio.
3. Resize long edge to at most 1280px without upscaling.
4. Normalize/cap frame rate near 24fps.
5. Encode H.264 MP4 around CRF 30.
6. Use a broadly compatible pixel format such as yuv420p.
7. Retain audio only when useful, e.g. AAC around 96kbps.
8. Use fast-start metadata when practical.
9. If a 10s proxy is much larger than the project budget, fall back to CRF 32 or 960/720 dimensions.
10. Record duration/fps/dimensions/bytes/SHA-256/profile.

## Repository path
`06_PROJECTS/<PROJECT>/19_HANDOFF_ASSETS/git_previews/`

Manifest:
`06_PROJECTS/<PROJECT>/19_HANDOFF_ASSETS/proxy_manifest.json`

## Commit methods
With a local checkout, generate the proxy, update manifest/docs, stage only related proxy+metadata files, and make a focused commit.

With a GitHub connector, use binary-capable blob/tree/commit operations when available. If direct binary upload is unavailable but the repository contains an approved decoder workflow, a temporary base64 payload may be staged and decoded by CI; remove the staging payload after decoding. Never pretend a binary commit succeeded if it did not.

## Required manifest fields
At minimum: source/run ID, role, media type, original hash when available, proxy path/hash, dimensions, bytes, profile, publication/privacy status, and `source_of_truth=false`; for video also duration/fps/audio status.

## What should be proxied
- original product reference used by the project;
- approved reference images;
- selected keyframes;
- every video Run that receives meaningful QA;
- rejected outputs when they are useful failure evidence;
- selected final media.

## What may be skipped
- unregistered throwaway scratch generations;
- exact duplicates with no new evidence;
- media marked private/no-public;
- inaccessible media when only metadata can be persisted.

## New-session usage
1. Load `proxy_manifest.json` and `HANDOFF.md`.
2. Inspect Git preview first.
3. Do not request re-attachment if proxy quality is sufficient for current planning/recall.
4. Request original/full-res only for tasks where proxy detail is insufficient.

Proxy is suitable for scene recognition, object count, composition, character continuity, broad product identity, and general motion/flicker review. It is not authoritative for micro-texture, fine label typography, exact compression artifacts, or final delivery quality.

## Media documentation gate
A media-related milestone is incomplete until provenance is recorded, proxy is committed or a metadata-only exception is documented, manifest is synchronized, and `HANDOFF.md` accurately states what a future session can see.
