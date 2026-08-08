# AI START HERE — New Chat / New Agent Context Loader

این فایل نقطه ورود هر ChatGPT/AI agent جدید است. هدف: بدون نیاز به chat قبلی، در چند دقیقه بفهمد سیستم چیست، پروژه کجاست و مرحله بعد چیست.

## مأموریت سیستم
AI Video Ad Lab یک production + R&D system برای ساخت تبلیغات AI از ورودی‌هایی مثل **عکس محصول + prompt/template اولیه** است. خروجی مهم فقط ویدیو نیست؛ promptها، checklistها، SOPها، failure knowledge و tool knowledge باید بعد از هر پروژه بهتر شوند.

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

## Scenario / duration routing

اگر کاربر درباره انتخاب سناریو، 10/20/30/40 ثانیه، یا ساخت 2/3/4 کلیپ صحبت می‌کند، قبل از storyboard/prompt این‌ها را بخوان:
- `00_SYSTEM/SCENARIO_ARCHITECTURE_SYSTEM.md`
- `01_SOPS/SOP_07_SCENARIO_GENERATION.md`
- `04_CHECKLISTS/CHK_SCENARIO_ARCHITECTURE_MENU.md`

اگر بیش از یک clip انتخاب شد، additionally:
- `00_SYSTEM/MULTI_CLIP_ARCHITECTURE.md`
- `01_SOPS/SOP_MULTI_CLIP_SEQUENCE.md`
- `04_CHECKLISTS/CHK_MULTI_CLIP_CONTINUITY.md`

سیستم باید ابتدا Scenario Architecture Menu adaptive بسازد و فقط گزینه‌های واقعاً معنادار را پیشنهاد کند؛ 4 clips صرفاً چون پشتیبانی می‌شود نباید پیشنهاد شود.

## وقتی کاربر فقط می‌گوید «خودت برو در جریان قرار بگیر»
این را اجازه برای **خواندن repo و بازیابی context** در نظر بگیر. ابتدا پروتکل بالا را اجرا کن؛ از کاربر نخواه تاریخچه گفتگو را دوباره توضیح دهد مگر اطلاعات واقعاً در repo ثبت نشده باشد.

## سریع‌ترین شروع پروژه جدید
Minimum viable inputs:
- حداقل یک تصویر اصلی محصول؛
- source/template/reference prompt به صورت متن یا فایل.

اختیاری ولی مفید:
- مدت ویدیو یا clip count؛
- aspect ratio؛
- پلتفرم؛
- creative constraints؛
- style references؛
- process اطلاعات واقعی.

اگر optionalها وجود ندارند، assumption کم‌ریسک را ثبت کن و فقط وقتی تصمیم blocker است سؤال بپرس.

## Media persistence بین chatها

سیستم از نسخه 1.3 به بعد برای media غیرحساس از **low-resolution Git proxies** استفاده می‌کند.

وقتی تصویر/ویدیوی مهم locally accessible است:
1. original metadata/hash را ثبت کن؛
2. طبق `00_SYSTEM/MEDIA_PROXY_PIPELINE.md` یک proxy کم‌حجم بساز؛
3. آن را در `19_HANDOFF_ASSETS/git_previews/` commit کن؛
4. `proxy_manifest.json` و HANDOFF را sync کن.

Default proxy:
- image: WebP ≤1280px long edge, quality≈72؛
- video: MP4/H.264 ≤1280px long edge, ≈24fps, CRF≈30.

Original/full-resolution همچنان خارج Git معمولی می‌ماند و proxy source of truth نیست.

Repository ممکن است public باشد؛ low quality به معنی private نیست. asset حساس یا `do_not_publish` باید metadata-only بماند.

در chat جدید ابتدا Git proxy را برای visual context استفاده کن. فقط وقتی full-resolution/detail واقعی لازم است original را از user بخواه دوباره attach کند.

جزئیات:
- `00_SYSTEM/STORAGE_POLICY.md`
- `00_SYSTEM/MEDIA_PROXY_PIPELINE.md`

## پایان هر session مهم
قبل از رها کردن یک پروژه فعال:
- `STATUS.md` را به‌روز کن؛
- `HANDOFF.md` را به‌روز کن؛
- feedback/decision مهم را در `18_CONVERSATION_LOG/` ثبت کن؛
- Run/prompt/evaluation جدید را ثبت کن؛
- media proxy/manifest لازم را sync کن یا دلیل metadata-only را ثبت کن؛
- workflow discovery یا system knowledge را طبق `DOCUMENTATION_CONTRACT.md` ثبت کن؛
- تغییرات لازم را commit کن.

هدف این است که session بعدی بتواند تا حد ممکن فقط با repo کار را ادامه دهد.
