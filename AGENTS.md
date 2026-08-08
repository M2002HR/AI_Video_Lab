# AI operator rules

این repository حافظه و **source of truth پایدار** برای AI Video Ad Lab است. ChatGPT در این workflow اپراتور اصلی است، اما قواعد برای هر AI agent آینده نیز معتبرند.

## شروع هر chat/session جدید
1. اول `AI_START_HERE.md` را بخوان.
2. سپس `START_HERE.md`، `DASHBOARD.md` و `00_SYSTEM/INDEX.md` را بخوان.
3. اگر پروژه active وجود دارد، `project.json`، `STATUS.md` و `HANDOFF.md` همان پروژه را قبل از ادامه کار بخوان.
4. فقط اسناد مرحله فعلی را load کن: SOP، checklist، canonical prompt، tool knowledge و learning مرتبط.
5. chat history را حافظه پایدار فرض نکن؛ تصمیم/feedback/نتیجه مهم باید در repo ثبت شود.

## قواعد غیرقابل‌مذاکره
- original input، Run تاریخی و prompt version تاریخی را overwrite نکن.
- هر تولید معنی‌دار AI باید provenance قابل‌ردیابی داشته باشد.
- هر reference نقش صریح داشته باشد؛ product identity بر style مقدم است.
- یک تجربه منفرد معمولاً `observation` است، نه قانون جهانی.
- تغییر canonical prompt/workflow/rubric/checklist/preferred tool طبق evidence و `CHANGE_PROMOTION_POLICY.md` انجام شود.
- مقدار نامعلوم را حدس نزن؛ `unknown`/`null` ثبت کن.
- capability ابزار را جعل نکن؛ vendor claim و evidence داخلی را جدا نگه دار.
- بعد از تغییرات مهم، metadata/registry/dashboard را sync و integrity را بررسی کن.
- **هر چیزی که برای تکرار، ادامه در chat جدید، مقایسه یا بهبود سیستم اثر دارد باید طبق `00_SYSTEM/DOCUMENTATION_CONTRACT.md` در repo ثبت شود.**
- خودِ requirement مستندسازی نیز بخشی از Definition of Done است: task مهم تا وقتی تصمیم/Run/prompt/feedback/learning لازم فقط در chat مانده، کامل نیست.
- هر بار process جدید، workflow branch، checklist need یا rule جدید در عمل کشف شد، ابتدا project evidence ثبت و در صورت reusable بودن به system documentation ارتقا داده شود.

## Multi-clip
اگر deliverable بیش از یک کلیپ دارد یا سناریو برای یک clip بیش‌ازحد پیچیده است، `00_SYSTEM/MULTI_CLIP_ARCHITECTURE.md` و `01_SOPS/SOP_MULTI_CLIP_SEQUENCE.md` را بخوان و قبل از promptهای تک‌کلیپ `MASTER_SEQUENCE` و boundary contractها را بساز.

## اجازه تغییر GitHub
کاربر اجازه داده ChatGPT در جریان تولید پروژه، تغییرات لازم، کم‌ریسک، مستند و قابل‌بازگشت را در repo انجام دهد و commit بزند. commitها باید موضوعی و خوانا باشند. برای حذف داده، force/rewrite history، تغییر معماری گسترده، انتشار اطلاعات حساس یا اقدام destructive approval صریح بگیر.

## UX
پاسخ کاربر پیش‌فرض فارسی و عملیاتی باشد: `کار انجام‌شده → یافته → فایل/Run → stage → next action`. prompt تولیدی پیش‌فرض English است مگر evidence یا درخواست پروژه خلافش را نشان دهد.

راهنمای کامل: `00_SYSTEM/AI_OPERATOR_MANUAL.md`.
