# Storage Policy

## Principle
Original and generated media are project evidence. Full-resolution media is **not automatically stored in normal Git**. For cross-chat continuity, the default system uses low-resolution version-controlled proxies plus metadata, hashes, and provenance.

## Public repository warning
The repository may be public. Lowering quality does not make an asset private. Sensitive, confidential, client, or `do_not_publish` media must not be uploaded even as a proxy unless the user explicitly selects a safe private storage policy.

## Storage modes
### `metadata_only`
Use for sensitive media or when binary access/processing is unavailable. Git stores text metadata/hash/location only.

### `git_previews` — default for publishable meaningful media
For every meaningful, non-sensitive, locally accessible project media item, create a low-resolution proxy under `19_HANDOFF_ASSETS/git_previews/` and register it in `proxy_manifest.json`.

Meaningful media includes original/source images used by the project, registered generated-image candidates, approved references/keyframes, video Runs that receive real QA, and selected final media. Disposable unregistered scratch outputs do not require proxies.

### Optional future modes
Git LFS in a private repository, DVC/object storage, NAS, or synced private storage may hold originals/full-res when explicitly configured. Proxy mode alone does not authorize full-resolution Git storage.

## Default proxy profiles
### Images
- WebP;
- maximum long edge 1280px, no upscaling;
- quality approximately 72;
- normalize orientation / RGB when possible;
- strip EXIF/metadata;
- record dimensions, bytes, SHA-256, and actual profile.

A justified 1600px profile may be used when cross-chat micro-detail is necessary.

### Videos
- MP4 / H.264;
- preserve aspect ratio;
- maximum long edge 1280px, no upscaling;
- normalize/cap near 24fps;
- CRF approximately 30;
- AAC approximately 96kbps if audio is retained;
- record duration, fps, dimensions, bytes, SHA-256, and profile.

If proxy size is excessive, CRF 32 or 960/720 maximum dimensions are acceptable fallbacks when recorded in the manifest.

## Naming and manifest
Proxy filenames must be traceable to a project asset/Run, not ambiguous names such as `final2.jpg`.

Each project should maintain `19_HANDOFF_ASSETS/proxy_manifest.json` with source asset/Run ID, role, source location/filename, original hash when available, proxy path/hash, dimensions, duration/fps for video, compression profile, creation time, publication/privacy status, and `source_of_truth: false`.

## Definition of Done for media persistence
When meaningful media affects a project decision and proxy sync is allowed:
1. register Run/asset metadata;
2. create the proxy;
3. store it in `19_HANDOFF_ASSETS/git_previews/`;
4. update the manifest;
5. commit the proxy and metadata;
6. update `HANDOFF.md` when cross-chat visibility matters.

## Git safety
`.gitignore` should keep originals and heavy media excluded and re-include only the standard proxy path/formats. Binary media outside that path should not enter normal Git accidentally.

## New-chat use
A new session should inspect Git proxies first for visual context. Request original/full-resolution media only when pixel-level QA, fine texture/typography, final delivery judgment, or generation input requires it. A proxy is not automatically an authoritative generation ingredient.

## Provenance classes
1. Original/source — never overwrite; full-res outside Git by default.
2. Generated candidate — Run provenance plus proxy if meaningful.
3. Approved reference/keyframe — explicit status plus proxy.
4. Final media — final metadata plus proxy; master full-res outside Git unless another storage mode is chosen.
5. Handoff proxy — low-resolution, version-controlled, `source_of_truth=false`.
