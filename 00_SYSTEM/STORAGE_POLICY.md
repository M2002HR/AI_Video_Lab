# STORAGE POLICY

## اصل
media اصلی و تولیدی بخشی از evidence پروژه است. **Original/full-resolution media به‌صورت خودکار داخل Git معمولی ذخیره نمی‌شود.** در عوض، برای continuity بین chatها سیستم از preview/proxy کم‌حجم version-controlled استفاده می‌کند و metadata، prompt، evaluation، decision، handoff و hash نیز version-controlled می‌مانند.

## وضعیت فعلی repository
Repository در زمان آخرین بررسی `public` است.

این نکته حیاتی است: **کم‌کردن کیفیت، فایل را private نمی‌کند.** هر previewی که در این repo commit شود برای عموم قابل مشاهده است.

بنابراین:
- preview رسانه‌های غیرحساس می‌تواند طبق policy زیر به‌صورت خودکار commit شود؛
- asset محرمانه، فایل مشتری، محتوای دارای اطلاعات حساس یا هر چیزی که کاربر explicitly `do_not_publish` اعلام کند نباید حتی به‌صورت preview در repo public ذخیره شود؛
- در صورت شک درباره حساسیت، operator قبل از publication سؤال می‌پرسد یا metadata-only ثبت می‌کند.

## بسیار مهم — Chat upload → Proxy Git Sync

تصویر یا ویدیویی که کاربر داخل ChatGPT attach می‌کند همچنان مستقیماً همان binary را به GitHub منتقل نمی‌کند. workflow جدید این است:

`CHAT/TOOL MEDIA → register original metadata/hash → generate low-res proxy → commit proxy + manifest → use proxy for cross-chat continuity`

Original منبع حقیقت است؛ Git proxy فقط برای context، visual recall و QA سبک است.

جزئیات عملی: `00_SYSTEM/MEDIA_PROXY_PIPELINE.md`.

## Media storage modes

### MODE A — Metadata-only
برای media حساس یا زمانی که binary قابل دسترسی/پردازش نیست. Git فقط text/metadata/hash را نگه می‌دارد.

### MODE B — Git previews — CURRENT SYSTEM DEFAULT FOR NON-SENSITIVE MEDIA
ChatGPT/AI operator باید برای هر **media معنی‌دار پروژه که locally accessible است** یک proxy کم‌حجم بسازد و در project `19_HANDOFF_ASSETS/git_previews/` commit کند.

معنی‌دار یعنی یکی از این موارد:
- original/source image مورد استفاده در پروژه؛
- generated image candidate که به Run ثبت شده؛
- approved reference/keyframe؛
- generated video Run که QA/مقایسه می‌شود؛
- selected/final media.

برای scratch خروجی‌ای که نه Run شده، نه بررسی شده و نه روی تصمیم اثر دارد proxy اجباری نیست.

### MODE C — Git LFS
برای originals/full-res یا پروژه‌های بسیار media-heavy در repo خصوصی قابل بررسی است. قبل از فعال‌سازی تصمیم صریح user لازم است.

### MODE D — External private media store
DVC / cloud object storage / NAS / synced private folder؛ Git manifest/hash/path و proxyهای لازم را نگه می‌دارد.

## Proxy profiles — default

### Images
- output: `WebP`
- maximum long edge: `1280 px`
- quality target: `72`
- EXIF/metadata stripped
- no upscaling
- preserve aspect ratio
- target typical size: roughly `100–600 KB`

اگر text/label micro-detail برای cross-chat judgment حیاتی است، operator می‌تواند به‌طور مستدل profile را تا 1600px افزایش دهد و در manifest ثبت کند.

### Videos
- output: `MP4 / H.264 / yuv420p`
- maximum long edge: `1280 px` (برای 16:9 معمولاً 1280×720)
- frame rate: cap/normalize near `24 fps` برای proxy
- quality: approximately `CRF 30`
- audio: AAC approximately `96 kbps` در صورت وجود
- `faststart` enabled
- target typical size for a 10s clip: preferably below about `8 MB`

اگر proxy از budget بزرگ‌تر شد، fallback به CRF 32 یا maximum long edge 960/720 مجاز است و profile واقعی باید manifest شود.

## Naming

Proxyها باید به asset/Run قابل ردیابی باشند:

`<SOURCE_ID>__<ROLE>__preview.webp`

`<RUN_ID>__video__preview.mp4`

مثال:
- `P0002-R0014__KF01__preview.webp`
- `P0002-R0031__video__preview.mp4`

نام مبهم مانند `final2.jpg` ممنوع است.

## Proxy manifest

هر پروژه باید `19_HANDOFF_ASSETS/proxy_manifest.json` یا معادل مستند داشته باشد و تا حد امکان شامل این موارد باشد:
- source asset ID / run ID؛
- role؛
- original filename/location description؛
- original SHA-256 وقتی قابل محاسبه است؛
- proxy path؛
- proxy SHA-256؛
- proxy width/height؛
- duration/fps برای video؛
- compression profile؛
- created_at؛
- privacy/publication status؛
- `source_of_truth: false` برای proxy.

## Commit contract

وقتی media جدید روی تصمیم پروژه اثر می‌گذارد و proxy sync مجاز است، task تا زمانی که این موارد انجام نشده کامل نیست:
1. Run/asset metadata ثبت شود؛
2. proxy ساخته شود؛
3. proxy در `19_HANDOFF_ASSETS/git_previews/` ذخیره شود؛
4. manifest به‌روز شود؛
5. Git commit زده شود؛
6. `HANDOFF.md` در صورت اهمیت cross-chat به proxy اشاره کند.

در صورت batch کوچک، proxy و metadata مرتبط ترجیحاً در یک commit موضوعی باشند.

## Git rule

`.gitignore` originals و media سنگین را همچنان ignore می‌کند، ولی فقط مسیر استاندارد `06_PROJECTS/**/19_HANDOFF_ASSETS/git_previews/` برای `*.webp` و `*.mp4` re-include می‌شود.

بنابراین media binary خارج از آن مسیر نباید اتفاقی وارد Git شود.

## استفاده در chat جدید

Chat جدید ابتدا proxy موجود در Git را برای context می‌خواند. اگر تصمیم نیازمند جزئیات full-resolution، pixel-level QA یا generation input با کیفیت اصلی است، operator باید original را دوباره attach/request کند.

**Proxy جای original generation ingredient را نمی‌گیرد مگر کاربر یا tool limitation صریحاً این را ایجاب کند.**

## Media classes
1. **Original/source**: هرگز overwrite نشود؛ full-res به‌صورت پیش‌فرض خارج Git.
2. **Generated candidate**: Run provenance + proxy در صورت meaningful بودن.
3. **Approved reference**: role/approval + proxy.
4. **Final media**: final metadata + proxy؛ master full-res خارج Git مگر storage mode دیگری انتخاب شود.
5. **Handoff proxy**: کم‌حجم، version-controlled، `source_of_truth=false`.

## Hashing
`hash-assets` در صورت دسترسی محلی SHA-256 می‌سازد تا دقیقاً معلوم باشد کدام media در Run استفاده شده است. proxy نیز hash مستقل دارد.

## آینده / change rule
Git LFS، DVC، NAS، cloud object storage یا synced private storage می‌توانند بعداً اضافه شوند. originals/full-res نباید صرفاً به دلیل فعال بودن proxy mode وارد Git معمولی شوند.
