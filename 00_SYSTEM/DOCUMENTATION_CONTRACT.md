# Documentation Contract

این سند یک قانون سیستمی است، نه پیشنهاد. هدف آن این است که هیچ دانشی که برای تکرار، مقایسه، ادامه در chat جدید یا بهبود سیستم ارزش دارد فقط داخل مکالمه باقی نماند.

## اصل اصلی

**اگر یک تصمیم، ورودی، خروجی، خطا، feedback، prompt، تغییر ابزار، تغییر workflow، انتخاب creative، نتیجه QA یا learning بتواند روی اجرای بعدی اثر بگذارد، باید در repository ثبت شود.**

Chat history رابط کار است؛ repository حافظه پایدار است.

## مواردی که ثبتشان اجباری است

### Project facts
- brief و deliverable؛
- original inputs؛
- assumptions و uncertainty؛
- stage فعلی، blocker و next action؛
- approved/selected assets و دلیل انتخاب.

### AI production
- prompt کامل استفاده‌شده؛
- prompt ID/version/status در صورت canonical بودن؛
- tool/model/settings در حد اطلاعات موجود؛
- ingredient/reference list و role هر reference؛
- هر Run معنی‌دار؛
- خروجی منتخب و خروجی شکست‌خورده‌ای که evidence مفید دارد.

### Evaluation
- score/rubric؛
- failure tags؛
- comparison؛
- pass/fail gate؛
- repair/regenerate/stop decision.

### Learning
- raw user feedback مهم؛
- observation؛
- hypothesis؛
- experiment؛
- validated learning؛
- تغییر prompt/SOP/checklist/tool recommendation؛
- دلیل و evidence تغییر.

### Process knowledge
هر بار که در حین پروژه متوجه می‌شویم یک **مرحله جدید، checklist جدید، decision rule، naming rule، continuity rule، prompt-writing rule یا workflow branch** لازم است، خود این نیاز نیز باید ثبت شود و در صورت تکرارپذیری از project knowledge به system documentation ارتقا یابد.

## «خودِ مستندسازی» نیز باید مستند باشد

AI operator موظف است قبل از پایان هر کار مهم بپرسد:

1. چه چیزی تولید یا تصمیم‌گیری شد؟
2. کدام بخش فقط در chat است و هنوز در repo نیست؟
3. آیا این مورد project-local است یا system-reusable؟
4. آیا STATUS/HANDOFF باید برای chat بعدی به‌روزرسانی شود؟
5. آیا Run/Prompt/Observation/Hypothesis/Decision لازم است؟
6. آیا registry/dashboard یا checklist باید sync شود؟

اگر پاسخ یکی از موارد بالا مثبت است، task تا زمان ثبت آن از نظر سیستم کامل محسوب نمی‌شود.

## سطوح ثبت

### Level A — Mandatory provenance
برای هر Run، prompt، final decision و approval.

### Level B — Project memory
برای feedback، انتخاب creative، failure pattern، workaround و نکته‌ای که ادامه همین پروژه به آن نیاز دارد.

### Level C — System knowledge
برای rule یا روش قابل‌استفاده در پروژه‌های دیگر. ابتدا observation/hypothesis؛ سپس طبق Evidence Policy در صورت اعتبار کافی به SOP/prompt/checklist ارتقا پیدا می‌کند.

## مواردی که لازم نیست ثبت شوند
- گفت‌وگوی اجتماعی بدون اثر روی پروژه؛
- توضیح تکراری که دقیقاً در repo موجود است؛
- حدس زودگذر بدون اثر بر تصمیم؛
- intermediate scratch reasoning که evidence یا خروجی عملی ایجاد نکرده است.

## Cross-chat handoff contract
در پایان یک session یا پس از milestone مهم، پروژه باید طوری باشد که یک ChatGPT جدید با خواندن:

1. `AI_START_HERE.md`
2. `project.json`
3. `STATUS.md`
4. `HANDOFF.md`
5. اسناد stage فعال

بتواند بدون درخواست بازگویی تاریخچه از کاربر، موارد زیر را بفهمد:
- هدف پروژه؛
- چه چیزهایی approved شده؛
- چه چیزهایی fail شده و چرا؛
- prompt/reference فعال چیست؛
- چه learningهایی مهم‌اند؛
- دقیقاً next action چیست.

## Definition of Done برای documentation
یک milestone فقط وقتی Done است که:
- خروجی/تصمیم ثبت شده؛
- provenance قابل ردیابی است؛
- status و handoff در صورت نیاز sync هستند؛
- learning مهم فقط در chat باقی نمانده؛
- تغییر system-level طبق governance ثبت شده؛
- chat جدید بتواند context لازم را از repo بازیابی کند.
