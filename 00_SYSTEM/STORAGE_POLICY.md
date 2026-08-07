# STORAGE POLICY

## اصل
media اصلی و تولیدی بخشی از evidence پروژه است، اما binary حجیم به‌صورت پیش‌فرض در Git معمولی commit نمی‌شود. metadata، prompt، evaluation، decision، handoff و hash باید version-controlled باشند.

## وضعیت فعلی repository
این repo ممکن است public باشد. تا وقتی private بودن آن صریحاً تأیید نشده است:
- asset محرمانه، فایل مشتری، source با اطلاعات حساس یا full-resolution proprietary media را commit نکن؛
- از Git برای metadata/text و در صورت نیاز previewهای غیرحساس و موردتأیید استفاده کن.

## Continuity بین chatها
برای ادامه آسان پروژه:
- مسیر/نام/role/hash asset در project docs ثبت شود؛
- `HANDOFF.md` مشخص کند کدام asset برای session بعدی لازم است؛
- `19_HANDOFF_ASSETS/` می‌تواند preview کم‌حجم و غیرحساس نگه دارد **فقط وقتی privacy اجازه می‌دهد**؛
- اگر asset از connector قابل render نیست، user فقط همان asset لازم را دوباره attach می‌کند.

## Media classes
1. **Original/source**: هرگز overwrite نشود.
2. **Generated candidate**: Run provenance داشته باشد.
3. **Approved reference**: role و approval ثبت شود.
4. **Final media**: final metadata و selected Run مشخص باشد.
5. **Handoff preview**: اختیاری، کم‌حجم، فقط برای continuity؛ source of truth نیست.

## Hashing
`hash-assets` در صورت دسترسی محلی SHA-256 می‌سازد تا دقیقاً معلوم باشد کدام media در Run استفاده شده است.

## آینده
Git LFS، DVC، NAS، cloud object storage یا synced private storage می‌توانند بعداً اضافه شوند. هیچ remote media storage خودکار فعال نشود مگر user تصمیم بگیرد.
