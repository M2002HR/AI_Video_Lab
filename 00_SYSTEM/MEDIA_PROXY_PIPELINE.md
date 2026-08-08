# Media Proxy Pipeline

## هدف

این pipeline تضمین می‌کند که media مهم پروژه فقط داخل یک chat باقی نماند. ChatGPT/AI operator برای تصاویر و ویدیوهای معنی‌دار یک نسخه کم‌حجم تولید می‌کند، آن را با provenance به Git commit می‌کند و original/full-resolution را خارج Git نگه می‌دارد.

## Trigger

هر زمان یکی از این اتفاق‌ها رخ دهد:
- user یک original/reference image مهم attach می‌کند؛
- یک generated image candidate به Run ثبت می‌شود؛
- یک keyframe/reference approve یا reject می‌شود ولی evidence مفید دارد؛
- یک generated video برای QA وارد می‌شود؛
- یک final run انتخاب می‌شود؛

operator باید بررسی کند آیا media locally accessible و publishable است. اگر بله، proxy sync انجام شود.

## Privacy gate

Repository ممکن است public باشد. قبل از upload binary:
- اگر asset sensitive/client/confidential است یا user گفته publish نشود → `metadata_only`؛
- اگر non-sensitive و project policy `git_previews` است → proxy sync؛
- اگر uncertainty واقعی وجود دارد → از user یک سؤال کوتاه بپرس.

کیفیت پایین privacy control محسوب نمی‌شود.

## Image pipeline

Default profile: `IMG-PROXY-1280-WEBP-Q72`.

1. source را بدون overwrite بخوان.
2. EXIF orientation را normalize کن.
3. رنگ را در صورت امکان به sRGB/RGB تبدیل کن.
4. long edge را حداکثر 1280px کن؛ upscale نکن.
5. WebP quality≈72 تولید کن.
6. metadata/EXIF را حذف کن.
7. dimensions/bytes/SHA-256 را ثبت کن.
8. path:
   `06_PROJECTS/<PROJECT>/19_HANDOFF_ASSETS/git_previews/<ID>__<ROLE>__preview.webp`

اگر micro-detail برای visual recall حیاتی است، profile 1600px مجاز است اما باید دلیل/نام profile در manifest ثبت شود.

## Video pipeline

Default profile: `VID-PROXY-H264-720P-CRF30-24FPS`.

1. source را بدون overwrite بخوان.
2. aspect ratio را preserve کن.
3. maximum long edge=1280px؛ upscale نکن.
4. H.264 + yuv420p.
5. approximately CRF 30.
6. normalize/cap proxy fps near 24.
7. audio در صورت وجود AAC≈96kbps.
8. enable faststart.
9. اگر برای 10s خروجی بسیار بزرگ‌تر از ~8MB شد، fallback CRF32 یا max dimension 960/720.
10. duration/fps/dimensions/bytes/SHA-256 را ثبت کن.
11. path:
   `06_PROJECTS/<PROJECT>/19_HANDOFF_ASSETS/git_previews/<RUN_ID>__video__preview.mp4`

## Git commit procedure

### اگر local checkout موجود است
- proxy را در مسیر استاندارد تولید کن؛
- manifest/docs را update کن؛
- `git add` فقط proxy + metadata مرتبط؛
- commit موضوعی بزن.

### اگر ChatGPT از GitHub connector استفاده می‌کند
Binary را با action binary-capable مثل blob/tree/commit upload کن. از text-only file action برای binary استفاده نکن.

High-level:
1. local proxy bytes → base64؛
2. create binary blob؛
3. add blob path to tree based on current branch tree؛
4. create commit؛
5. fast-forward branch ref؛
6. commit manifest/docs metadata در همان commit یا commit موضوعی بلافاصله بعد.

اگر binary upload capability در session موجود نیست، failure را ثبت کن و metadata-only ادامه بده؛ وانمود نکن proxy commit شده است.

## Manifest schema example

```json
{
  "schema_version": "1.0",
  "proxies": [
    {
      "source_id": "P0002-R0014",
      "role": "KF01",
      "media_type": "image",
      "original_sha256": "unknown",
      "proxy_path": "19_HANDOFF_ASSETS/git_previews/P0002-R0014__KF01__preview.webp",
      "proxy_sha256": "...",
      "width": 1280,
      "height": 720,
      "bytes": 284103,
      "profile": "IMG-PROXY-1280-WEBP-Q72",
      "privacy_status": "public_non_sensitive",
      "source_of_truth": false
    }
  ]
}
```

## What gets proxied?

### Mandatory when available + publishable
- original product reference used by project؛
- all approved reference images؛
- selected keyframes؛
- every video Run that receives meaningful QA؛
- selected/final media.

### Recommended
- rejected image/video Run if it provides reusable failure evidence.

### Optional / skip
- throwaway scratch generations never registered as Run؛
- duplicate outputs with no new evidence؛
- media user marks private/no-public؛
- binary inaccessible to operator.

## Cross-chat behavior

New ChatGPT session:
1. load `proxy_manifest.json` and HANDOFF؛
2. inspect Git preview first؛
3. do not ask user to reattach media if proxy is enough for current planning/recall؛
4. request original only when full-resolution accuracy or generation upload requires it.

## QA limitations

Proxy مناسب است برای:
- شناخت صحنه؛
- object count؛
- composition؛
- character continuity؛
- broad product identity؛
- video motion/flicker review در سطح عمومی.

Proxy به‌تنهایی برای این موارد authority نیست:
- texture micro-detail؛
- fine label typography؛
- exact compression/artifact judgment؛
- final delivery quality؛
- color-critical mastering.

## Definition of Done

Media-related milestone تا وقتی این موارد روشن نشده کامل نیست:
- original provenance ثبت شده؟
- proxy ساخته/commit شده یا دلیل metadata-only ثبت شده؟
- manifest sync است؟
- HANDOFF می‌داند session بعدی چه چیزی را می‌تواند از Git ببیند؟
