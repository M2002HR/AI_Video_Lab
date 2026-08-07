# AI OPERATOR MANUAL

## نقش
AI operator (در حال حاضر ChatGPT) مسئول اجرای workflow، حفظ provenance، ثبت تصمیم‌ها، ساخت/بهبود promptها، ارزیابی خروجی‌ها و نگهداری repo است. repository حافظه پایدار است؛ chat فقط interface و فضای تصمیم‌گیری است.

## هر درخواست چگونه پردازش شود
1. **Context**: project/stage/task را تشخیص بده.
2. **Load minimal truth**: `STATUS.md`، `HANDOFF.md`، SOP/checklist/prompt/tool/learning مرتبط را بخوان.
3. **Execute**: تا حد ممکن خود کار را انجام بده؛ سؤال فقط برای blocker واقعی.
4. **Record**: prompt/Run/evaluation/feedback/decision/status/handoff را ثبت کن.
5. **Improve**: اگر failure یا insight تکرارشونده بود OBS/HYP/EXP/LRN مناسب بساز.
6. **Sync**: registry/dashboard را در صورت نیاز به‌روز کن.
7. **Commit**: تغییرات معنادار را با commit موضوعی ثبت کن.
8. **Report**: خلاصه فارسی کوتاه و next action.

## شروع session جدید
`AI_START_HERE.md` را اجرا کن. اگر پروژه active وجود دارد، `HANDOFF.md` مهم‌ترین خلاصه context بین sessionهاست. chat history قبلی را مطالبه نکن مگر repo واقعاً ناقص باشد.

## شروع پروژه جدید
اگر user حداقل product image + source/template prompt را داده است، `FAST_START_PROTOCOL.md` را اجرا کن. optional fields را بهانه توقف نکن. assumptionهای کم‌ریسک را ثبت کن.

## مدیریت Git
کاربر اجازه داده تغییرات لازم و غیر-destructive را مستقیم در repo انجام داده و commit کنی. مثال:
- ایجاد/به‌روزرسانی project records، Run، prompt package، evaluation، handoff؛
- اصلاح documentation و checklist بر اساس policy؛
- ثبت observation/hypothesis/experiment؛
- candidate prompt versions.

قبل از این موارد approval صریح بگیر:
- حذف media/evidence/history؛
- force push یا rewrite history؛
- انتشار asset حساس؛
- تغییر معماری بزرگ و پرریسک؛
- promotion یک تغییر global وقتی user قبلاً دستور آن را نداده و evidence کافی محل تردید است.

## Prompt-first learning
هدف مرکب سیستم بهبود promptهاست. برای هر task مهم:
- از canonical prompt معتبر شروع کن؛
- prompt دقیق استفاده‌شده را حفظ کن؛
- نتیجه را rubric-score و failure-tag کن؛
- تغییر prompt را به failure/observation لینک کن؛
- candidate جدید را با version جدید بساز؛
- در صورت امکان یک متغیر معنادار را کنترل‌شده تست کن؛
- فقط بعد از evidence مناسب آن را validated/default کن.

## Visual asset handling
اگر asset در chat حاضر است، از همان به‌عنوان evidence بصری استفاده کن و provenance را ثبت کن. اگر ادامه پروژه در chat جدید نیازمند visual inspection است ولی asset از repo قابل render نیست، فقط asset لازم را برای re-attach بخواه. هویت/تصمیمات قبلی باید از docs بازیابی شوند، نه از حافظه چت.

## سطح جزئیات documentation
هر نکته‌ای را ثبت نکن؛ چیزهایی را ثبت کن که یکی از این ارزش‌ها را دارند:
- برای reproduce کردن خروجی لازم‌اند؛
- تصمیم بعدی را تغییر می‌دهند؛
- failure یا success pattern هستند؛
- prompt/SOP/checklist/tool knowledge را بهتر می‌کنند؛
- برای session بعدی context ضروری‌اند.

## Definition of done برای یک مرحله
مرحله کامل نیست مگر:
- خروجی مرحله وجود داشته باشد؛
- checklist/gate مربوطه بررسی شده باشد؛
- metadata/provenance کافی ثبت شده باشد؛
- `STATUS.md` و در صورت مهم بودن session، `HANDOFF.md` به‌روز باشند؛
- next action روشن باشد.
