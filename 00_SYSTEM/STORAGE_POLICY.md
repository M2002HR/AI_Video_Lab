# STORAGE POLICY

## اصل
media اصلی و تولیدی بخشی از evidence پروژه است، اما binary حجیم به‌صورت پیش‌فرض در Git معمولی commit نمی‌شود. metadata، prompt، evaluation، decision، handoff و hash باید version-controlled باشند.

## وضعیت فعلی repository
Repository در زمان آخرین بررسی `public` است.

تا وقتی private بودن آن صریحاً تأیید نشده است:
- asset محرمانه، فایل مشتری، source با اطلاعات حساس یا full-resolution proprietary media را commit نکن؛
- از Git برای metadata/text و در صورت نیاز previewهای غیرحساس و موردتأیید استفاده کن.

## بسیار مهم — Chat upload ≠ Git storage

تصویر یا ویدیویی که کاربر داخل ChatGPT attach می‌کند **به‌صورت خودکار در GitHub repository ذخیره یا commit نمی‌شود**.

همچنین وضعیت فعلی `.gitignore` به‌صورت پیش‌فرض این binaryها را ignore می‌کند:
- `*.jpg / *.jpeg / *.png / *.webp`
- `*.mp4 / *.mov / *.wav`
- media داخل reference/keyframe/run-output/final-media folders.

بنابراین در معماری فعلی، چیزی که حتماً در Git می‌ماند عبارت است از:
- asset ID / role؛
- Run provenance؛
- prompt؛
- evaluation؛
- selected/rejected state؛
- در صورت امکان hash؛
- توضیح اینکه کدام asset در chat/session باید دوباره attach شود.

اگر خود فایل media برای cross-chat continuity لازم باشد، باید یک storage mode صریح انتخاب شود.

## Media storage modes

### MODE A — Metadata-only — CURRENT DEFAULT
Git فقط text/metadata/hash را نگه می‌دارد. media روی سیستم کاربر/Flow/ChatGPT/سرویس تولید باقی می‌ماند.

مزیت: repo سبک، امن‌تر برای public repo.

عیب: chat جدید ممکن است برای visual QA لازم باشد بعضی assetها دوباره attach شوند.

### MODE B — Git previews
previewهای کوچک، غیرحساس و approved در `19_HANDOFF_ASSETS/` نگه داشته می‌شوند؛ originals/full-res همچنان خارج Git.

مناسب برای continuity بصری سبک، فقط وقتی privacy اجازه دهد.

### MODE C — Git LFS
برای repo خصوصی می‌توان originals/approved references/final videos را با Git LFS version کرد.

قبل از فعال‌سازی باید user تصمیم صریح بگیرد چون storage/bandwidth و privacy implications دارد.

### MODE D — External private media store
DVC / cloud object storage / NAS / synced private folder؛ Git فقط manifest/hash/path را نگه می‌دارد.

برای پروژه‌های زیاد یا فایل‌های حجیم معمولاً scalableتر است.

## Continuity بین chatها
برای ادامه آسان پروژه:
- مسیر/نام/role/hash asset در project docs ثبت شود؛
- `HANDOFF.md` مشخص کند کدام asset برای session بعدی لازم است؛
- `19_HANDOFF_ASSETS/` می‌تواند preview کم‌حجم و غیرحساس نگه دارد فقط وقتی privacy اجازه می‌دهد؛
- اگر asset از connector قابل render نیست، user فقط همان asset لازم را دوباره attach می‌کند.

## Media classes
1. **Original/source**: هرگز overwrite نشود.
2. **Generated candidate**: Run provenance داشته باشد.
3. **Approved reference**: role و approval ثبت شود.
4. **Final media**: final metadata و selected Run مشخص باشد.
5. **Handoff preview**: اختیاری، کم‌حجم، source of truth نیست.

## Hashing
`hash-assets` در صورت دسترسی محلی SHA-256 می‌سازد تا دقیقاً معلوم باشد کدام media در Run استفاده شده است.

## آینده / change rule
Git LFS، DVC، NAS، cloud object storage یا synced private storage می‌توانند بعداً اضافه شوند. هیچ remote media storage یا تغییر `.gitignore` برای binaryهای تجاری خودکار فعال نشود مگر user تصمیم صریح بگیرد.
