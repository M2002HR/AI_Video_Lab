# FAST START PROTOCOL — Product Image + Source Prompt

این پروتکل برای حالتی است که کاربر می‌خواهد با حداقل اصطکاک یک پروژه واقعی را شروع کند.

## Minimum inputs
برای شروع فقط این دو مورد ضروری‌اند:
1. حداقل یک تصویر اصلی محصول؛
2. یک source/template/reference prompt.

اطلاعات زیر optional هستند و نبودشان به‌تنهایی blocker نیست:
- نام پروژه/محصول؛
- مدت ویدیو؛
- aspect ratio؛
- پلتفرم؛
- audience؛
- style references؛
- audio؛
- brand constraints.

اگر optionalها مشخص نیستند، assumption کم‌ریسک بساز، واضح ثبت کن و فقط وقتی انتخاب اشتباه می‌تواند کار زیادی را هدر دهد سؤال کن.

## اجرای سریع
وقتی minimum inputs حاضرند:

### A. Create & preserve
- project ID بساز؛
- original product input و original source prompt را immutable ثبت کن؛
- provenance و محدودیت دسترسی به media را ثبت کن؛
- `project.json`، `STATUS.md` و `HANDOFF.md` را initialize کن.

### B. Intake
- deliverable فعلی را از user/context استخراج کن؛
- unknownها و assumptions را ثبت کن؛
- اگر user صریحاً 10-second ad یا format دیگری گفته همان را authoritative بگیر.

### C. Source prompt reverse engineering
- Structure/DNA را جدا کن؛
- KEEP / ADAPT / REMOVE matrix بساز؛
- product-specific leakage، contradictions، over-complexity و tool-specific assumptions را مشخص کن.

### D. Product identity
از عکس اصلی استخراج کن:
- category، silhouette، geometry/proportion؛
- material/texture/color؛
- packaging/component count؛
- identity-critical details؛
- natural imperfections؛
- uncertainty؛
- forbidden transformations.

یک `identity_lock.md` قابل استفاده در promptهای بعدی بساز.

### E. Reference strategy
تصمیم بگیر:
- عکس اصلی کافی است یا cleanup لازم است؟
- کدام angleهای جدید واقعاً لازم‌اند؟
- macro/detail/packaging reference لازم است؟
- style/scene reference جدا لازم است؟
- کدام reference فقط identity و کدام فقط style است؟

### F. Stop at the first meaningful gate
اگر برای ادامه به generation خارجی یا تصمیم خلاقه واقعی نیاز است، به‌جای ادامه کورکورانه:
- وضعیت را ثبت کن؛
- prompt package مرحله بعد را آماده کن؛
- checklist preflight را اجرا کن؛
- به user بگو دقیقاً چه چیزی باید generate/choose شود.

## سؤال‌هایی که نباید اول کار بپرسی
تا وقتی blocker نیست، با سؤال‌های عمومی مثل «سبک چی باشه؟ نور چی باشه؟ دوربین چی باشه؟» شروع نکن. ابتدا source prompt و محصول را تحلیل کن؛ بعد فقط سؤال‌هایی را مطرح کن که نتیجه تحلیل نشان داده واقعاً تصمیم لازم‌اند.

## خروجی Fast Start
حداقل باید این‌ها وجود داشته باشند:
- registered project؛
- immutable input record؛
- source prompt analysis؛
- product identity + identity lock؛
- initial reference strategy؛
- updated STATUS/HANDOFF؛
- next action روشن.
