# Handoff Assets

Low-resolution visual memory for cross-chat continuity.

- `git_previews/`: version-controlled WebP/MP4 proxies.
- `proxy_manifest.json`: source/Run-to-proxy mapping.

Rules:
- Proxy is not source of truth; original/full-resolution remains at its authoritative location.
- Default image proxy: WebP, long edge <=1280, quality about 72.
- Default video proxy: MP4/H.264, long edge <=1280, about 24fps, CRF about 30.
- Commit only media whose privacy/IP status permits publication.
- Public repository proxies are still public media.
- Confidential/client/sensitive/`do_not_publish` media -> metadata-only.
- Filename must trace to project asset/Run.
- `HANDOFF.md` must explain what each proxy represents and whether original media is required for generation or detailed QA.
- Sync proxy + manifest according to `00_SYSTEM/MEDIA_PROXY_PIPELINE.md`.
