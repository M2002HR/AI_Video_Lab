# AI Video Ad Lab

AI Video Ad Lab یک سیستم local-first و version-controlled برای ساخت و بهبود تبلیغات محصول با AI است. ورودی رایج: **عکس محصول + source/template prompt**. خروجی: media نهایی به‌علاوه یک knowledge base قابل‌ردیابی که بعد از هر پروژه بهتر می‌شود.

## هسته سیستم
- `06_PROJECTS/`: پرونده کامل هر پروژه از input تا final/postmortem.
- هر اجرای AI = یک **Run** با prompt/reference/settings/output/evaluation.
- `02_PROMPT_SYSTEM/`: promptهای نسخه‌دار؛ prompt مهم دارایی تولیدی است، نه متن موقت.
- `03_TOOL_KNOWLEDGE/`: تفاوت task با tool؛ توصیه ابزار باید evidence-based و قابل تغییر باشد.
- `04_CHECKLISTS/`: quality gates برای اینکه مرحله مهمی جا نیفتد.
- `07_EXPERIMENTS/`: A/B و controlled experiments.
- `09_LEARNING/`: Observation → Hypothesis → Experiment → Validated Learning → System Change.
- `10_REGISTRY/`: viewهای تولیدشده برای پروژه/Run/prompt/tool/learning.

## ChatGPT به‌عنوان اپراتور
ChatGPT اپراتور اصلی workflow است و repo حافظه پایدار است. یک chat جدید نباید به chat history وابسته باشد: `AI_START_HERE.md` مسیر context recovery را تعریف می‌کند؛ هر پروژه `STATUS.md` و `HANDOFF.md` دارد.

## چرخه تولید
Input → source prompt analysis → product identity → reference strategy/generation/QA → creative direction → scenario → shot/timing → storyboard/keyframes → prompt package → video Runs → QA/repair → final → postmortem → learning → prompt/SOP/checklist/tool improvement.

## اصول
1. original و history overwrite نمی‌شوند.
2. product identity بر style مقدم است.
3. WHAT باید از WHICH TOOL جدا باشد.
4. هیچ claim ابزار بدون verification/evidence به‌عنوان حقیقت دائمی ثبت نمی‌شود.
5. failed Runs حذف نمی‌شوند؛ failure evidence است.
6. canonical prompt فقط با version/evidence تغییر می‌کند.
7. chat تصمیم می‌سازد؛ repo تصمیم را حفظ می‌کند.

## شروع
- کاربر: `START_HERE.md`
- ChatGPT/agent جدید: `AI_START_HERE.md`
- نقشه سیستم: `00_SYSTEM/INDEX.md`
- workflow: `00_SYSTEM/MASTER_WORKFLOW.md`
- اپراتور: `00_SYSTEM/AI_OPERATOR_MANUAL.md`

Media سنگین طبق `00_SYSTEM/STORAGE_POLICY.md` مدیریت می‌شود. metadata، prompt، evaluation، decision و handoff باید در Git باقی بمانند تا پروژه بین sessionها قابل ادامه باشد.
