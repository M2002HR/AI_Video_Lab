# Handoff Assets / Git Previews

این پوشه حافظه بصری کم‌حجم پروژه برای cross-chat continuity است.

## Structure

- `git_previews/` — low-resolution WebP/MP4 proxies که version-controlled هستند.
- `proxy_manifest.json` — mapping بین source/run و proxy.

## Rules

- proxy source of truth نیست؛ original/full-resolution در محل اصلی خود می‌ماند.
- default image proxy: WebP، long edge≤1280، quality≈72.
- default video proxy: MP4/H.264، long edge≤1280، ≈24fps، CRF≈30.
- فقط assetی را commit کن که privacy/IP اجازه می‌دهد.
- repository ممکن است public باشد؛ low-resolution هنوز public media است.
- confidential/client/sensitive یا `do_not_publish` media → metadata-only.
- نام فایل باید به project asset/Run مربوط قابل ردیابی باشد.
- `HANDOFF.md` باید توضیح دهد هر preview چیست و آیا original برای generation یا قضاوت دقیق باید دوباره attach شود.
- proxy + manifest بعد از media Run/approval معنی‌دار باید طبق `00_SYSTEM/MEDIA_PROXY_PIPELINE.md` sync شوند.

Recommended filename:

`<SOURCE_OR_RUN_ID>__<ROLE>__preview.webp`

`<RUN_ID>__video__preview.mp4`
