# AI START HERE — New Chat / New Agent Context Loader

این فایل نقطه ورود هر ChatGPT/AI agent جدید است. هدف: بدون نیاز به chat قبلی، در چند دقیقه بفهمد سیستم چیست، پروژه کجاست و مرحله بعد چیست.

## مأموریت سیستم
AI Video Ad Lab یک production + R&D system برای ساخت تبلیغات کوتاه AI از ورودی‌هایی مثل **عکس محصول + prompt/template اولیه** است. خروجی مهم فقط ویدیو نیست؛ promptها، checklistها، SOPها، failure knowledge و tool knowledge باید بعد از هر پروژه بهتر شوند.

## پروتکل اجباری Context Load
در session جدید این ترتیب را انجام بده:

1. repository/default branch و آخرین commit را بررسی کن.
2. این فایل‌ها را بخوان: `AGENTS.md`، `START_HERE.md`، `README.md`، `DASHBOARD.md`، `00_SYSTEM/INDEX.md`، `00_SYSTEM/AI_OPERATOR_MANUAL.md`.
3. `06_PROJECTS/INDEX.md` یا registry پروژه‌ها را بررسی کن.
4. اگر دقیقاً یک پروژه active است، بدون سؤال اضافی این‌ها را بخوان: `project.json`، `STATUS.md`، `HANDOFF.md` و فایل‌های مرحله فعلی.
5. اگر چند پروژه active است و context کاربر مشخص نمی‌کند کدام را می‌خواهد، فقط نام/ID پروژه لازم را بپرس.
6. اگر پروژه active نیست و کاربر عکس محصول + source/template prompt فرستاده، `00_SYSTEM/FAST_START_PROTOCOL.md` را اجرا کن؛ سؤال عمومی setup نپرس.
7. فقط knowledge مرتبط با task فعلی را load کن؛ کل repo را بی‌هدف خلاصه نکن.
8. قبل از ادامه، یک Context Snapshot کوتاه به کاربر بده: پروژه، stage، approved items، blocker، next action.

## وقتی کاربر فقط می‌گوید «خودت برو در جریان قرار بگیر»
این را اجازه برای **خواندن repo و بازیابی context** در نظر بگیر. ابتدا پروتکل بالا را اجرا کن؛ از کاربر نخواه تاریخچه گفتگو را دوباره توضیح دهد مگر اطلاعات واقعاً در repo ثبت نشده باشد.

## سریع‌ترین شروع پروژه جدید
Minimum viable inputs:
- حداقل یک تصویر اصلی محصول؛
- source/template/reference prompt به صورت متن یا فایل.

اختیاری ولی مفید:
- مدت ویدیو، aspect ratio، پلتفرم، creative constraints، style references.

اگر optionalها وجود ندارند، assumption کم‌ریسک را ثبت کن و فقط وقتی تصمیم blocker است سؤال بپرس.

## محدودیت رسانه بین chatها
متن، prompt، metadata، decision و handoff باید در repo باشد. اگر یک تصویر/ویدیو در repo یا connector قابل مشاهده نیست و برای قضاوت بصری لازم است، فقط همان asset لازم را از کاربر بخواه دوباره attach کند؛ کل context را دوباره نپرس. `HANDOFF.md` باید مشخص کند کدام asset در session بعد ممکن است نیاز به re-attach داشته باشد.

## پایان هر session مهم
قبل از رها کردن یک پروژه فعال:
- `STATUS.md` را به‌روز کن؛
- `HANDOFF.md` را به‌روز کن؛
- feedback/decision مهم را در `18_CONVERSATION_LOG/` ثبت کن؛
- Run/prompt/evaluation جدید را ثبت کن؛
- تغییرات لازم را commit کن.

هدف این است که session بعدی بتواند فقط با همین repo کار را ادامه دهد.
