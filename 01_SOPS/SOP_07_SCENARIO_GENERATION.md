# SOP 07 SCENARIO GENERATION

## هدف

تولید چند سناریوی واقعاً متفاوت و قابل‌اجرا برای تبلیغ AI، به‌جای تغییرات سطحی یک ایده واحد. سناریو باید قبل از prompt نهایی، نسبت بین `commercial value / process richness / generative risk / product identity` را روشن کند.

## ورودی لازم
- creative direction؛
- product identity؛
- approved reference set؛
- duration target؛
- tool/model constraints در صورت معلوم بودن؛
- user intent درباره process/action/reveal.

## خانواده‌های سناریو

برای جلوگیری از اینکه همه پروژه‌ها به یک reveal ساده ختم شوند، حداقل این خانواده‌ها را در نظر بگیر:

### A. Hero / Inspection
محصول از ابتدا آماده است؛ حرکت دوربین، inspection و final reveal. کم‌ریسک‌ترین حالت.

### B. Micro Process
فقط یک مرحله واقعی از فرآیند را نشان می‌دهد؛ مثال: coating یک ترافل با nonpareil یا قرار دادن ترافل در paper cup. معمولاً برای 10s مناسب‌تر از نمایش کل تولید است.

### C. Assembly / Packaging
چند محصول آماده جابه‌جا/مرتب/بسته‌بندی می‌شوند. ریسک interaction و object count متوسط است.

### D. Transformation
یک state واقعاً به state بعدی تبدیل می‌شود؛ مثال bare truffle → coated truffle. فقط وقتی ابزار/model و reference strategy توان حفظ geometry را دارند.

### E. Process Chain
چند مرحله تولید پشت‌سرهم. برای یک 10s پرریسک است و معمولاً باید به multi-clip sequence شکسته شود.

### F. Conceptual / Metaphor
دنیای مینیاتوری، کارخانه استعاری، scale play یا ایده بصری غیرliteral؛ محصول نهایی باید همچنان identity-safe بماند.

## رویه

1. `STATUS`، creative direction، product identity و evidence مرتبط را بخوان.
2. قبل از ideation مشخص کن کاربر بیشتر چه می‌خواهد: `hero`, `process`, `assembly`, `story`, `multi_clip` یا ترکیبی.
3. حداقل 3 candidate ایجاد کن که از نظر **نوع action architecture** متفاوت باشند، نه فقط camera/color.
4. برای هر candidate بنویس:
   - premise؛
   - 10s timeline یا clip allocation؛
   - product state at start/end؛
   - character role؛
   - required tools/props؛
   - required references/keyframes؛
   - object interactions؛
   - likely failure modes؛
   - risk level؛
   - commercial payoff.
5. اگر سناریو بیش از 2 state change اصلی دارد، بررسی کن آیا باید به 2×10s یا 3×10s شکسته شود.
6. canonical scenario prompt را instantiate و reference roleها را صریح نگه دار.
7. candidateها را با rubric Stage 08 مقایسه کن؛ انتخاب باید دلیل داشته باشد.
8. feedback/decision را ثبت و STATUS/HANDOFF را sync کن.

## قاعده complexity برای 10 ثانیه

به‌صورت پیش‌فرض یک 10s باید یکی از این الگوها را داشته باشد:
- 1 state + camera reveal؛
- 1 main transformation؛
- 2 simple sequential actions؛
- 1 assembly action + hero.

اگر سناریو شامل `forming + coating + transporting + packaging + reveal` است، آن را در یک 10s فشرده نکن مگر evidence قوی وجود داشته باشد. ترجیح: multi-clip decomposition.

## Process scenario design

برای مراحل آماده‌سازی محصول، قبل از نوشتن سناریو یک `PROCESS STATE MAP` ایجاد کن:

مثال عمومی:
`raw/base → formed → coated/decorated → cupped → arranged → boxed → hero`

برای هر transition مشخص کن:
- آیا واقعاً لازم است در تصویر دیده شود؟
- آیا AI باید geometry/material را transform کند؟
- آیا interaction فیزیکی لازم است؟
- آیا می‌توان state را با cut/match cut به‌جای morphing نشان داد؟

سناریوی خوب همه مراحل واقعی تولید را لزوماً نشان نمی‌دهد؛ فقط مراحلی را انتخاب می‌کند که هم visually clear و هم generatively controllable هستند.

## خروجی و Gate

خروجی: candidate scenarios + process/state map در صورت نیاز.

Pass یعنی:
- candidateها واقعاً متفاوت‌اند؛
- product focus روشن است؛
- timeline قابل فهم است؛
- complexity و risk مستند است؛
- مشخص است single-clip یا multi-clip مناسب‌تر است؛
- provenance کامل است.

## خطا و escalation

خطاهای رایج:
- scenario فقط لیستی از اتفاق‌هاست بدون state logic؛
- actionهای همزمان زیاد؛
- transformation مبهم؛
- product identity در میانه گم می‌شود؛
- final hero زمان کافی ندارد؛
- ابزار/کاراکتر بیشتر از نیاز؛
- process واقعی با metaphor اشتباه ترکیب می‌شود.

اگر complexity با duration ناسازگار است، scenario را simplify یا به `SOP_MULTI_CLIP_SEQUENCE.md` منتقل کن.
