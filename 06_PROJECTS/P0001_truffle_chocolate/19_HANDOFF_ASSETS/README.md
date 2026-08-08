# P0001 Handoff Assets

Storage mode: `git_previews` for non-sensitive media.

- New meaningful images/videos should receive low-resolution proxies in `git_previews/`.
- Manifest: `proxy_manifest.json`.
- Originals/full-resolution remain outside Git.
- Historical P0001 assets are not yet backfilled because source binaries are not currently stored in the repository.
- When a historical asset is re-attached or otherwise locally accessible, ChatGPT may create its proxy and append it to the manifest.
- Repository may be public; do not add sensitive/client/confidential media.
