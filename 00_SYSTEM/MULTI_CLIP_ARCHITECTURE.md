# Multi-Clip Architecture

این سند روش ساخت تبلیغ‌های طولانی‌تر از چند کلیپ کوتاه مستقل را تعریف می‌کند. سیستم به‌صورت رسمی برای **2، 3 و 4 کلیپ** آماده است؛ در setupهای 10 ثانیه‌ای یعنی معمولاً 20s، 30s و 40s.

## اصل طراحی

یک ویدیوی 20/30/40 ثانیه‌ای نباید صرفاً «چند ویدیوی 10 ثانیه‌ای تصادفی که بعداً کنار هم چسبیده‌اند» باشد.

ابتدا یک **Master Sequence** طراحی می‌شود، سپس هر کلیپ یک واحد تولید مستقل با قرارداد ورودی/خروجی روشن است.

ساختار عمومی:

`SCENARIO MENU → MASTER STORY → C01 → BOUNDARY → C02 → [BOUNDARY → C03] → [BOUNDARY → C04] → ASSEMBLY → SEQUENCE QA`

قبل از انتخاب تعداد کلیپ، `SCENARIO_ARCHITECTURE_SYSTEM.md` اجرا می‌شود تا فقط duration/architectureهای واقعاً معنادار پیشنهاد شوند.

## Supported sequence sizes

### 2×10s — 20s
برای زمانی که داستان دو chapter طبیعی دارد.

الگوهای رایج:
- Process → Payoff
- Craft → Collection
- Hook → Product World
- Editorial Process → Hero

### 3×10s — 30s
برای process storytelling چندمرحله‌ای با سه مسئولیت روشن.

الگوهای رایج:
- Craft → Assembly → Hero
- Material/Origin → Transformation → Product
- One Item → Collection → Packaging
- Three Editorial Chapters

### 4×10s — 40s
فقط وقتی چهار chapter مستقل و ارزشمند وجود دارد.

الگوهای رایج:
- Origin → Craft → Assembly → Hero
- Form → Decorate → Package → Reveal
- Macro Detail → Process → Collection → Brand Hero
- Four Editorial Worlds

اگر یک 4-clip sequence filler ایجاد کند، سیستم باید 3 clips را پیشنهاد کند.

## سه نوع معماری اصلی

### A. Continuous-world sequence
برای زمانی که مخاطب باید حس کند همه کلیپ‌ها بخش‌های متوالی یک جهان واحد هستند.

نیازمند:
- product identity lock مشترک؛
- character bible مشترک؛
- environment/lighting lock مشترک؛
- clip boundary frame یا handoff state؛
- camera/position continuity؛
- exact object count/placement continuity در مرزهای لازم.

ریسک generative بالاتر است و نباید فقط برای زیبایی انتخاب شود.

### B. Editorial sequence
هر 10 ثانیه یک mini-scene مستقل است؛ اتصال از طریق product identity، style، rhythm، match concept، edit و audio انجام می‌شود.

continuity سخت spatial کمتر است و معمولاً برای AI video مطمئن‌تر است.

### C. Hybrid — default candidate for many AI ads
داخل هر clip continuity سخت است، ولی بین clipها با transition کنترل‌شده مانند approved boundary frame، match cut، motion cut یا editorial cut وصل می‌شوند.

برای 20–40s معمولاً بهترین تعادل بین کیفیت سینمایی و reliability است، مگر brief دلیل روشنی برای continuous/editorial خالص داشته باشد.

## Master Sequence Document

قبل از ساخت Clip 01 باید `MASTER_SEQUENCE.md` وجود داشته باشد و شامل این موارد باشد:
- total duration؛
- clip count و duration هر clip؛
- selected scenario ID/title؛
- architecture mode؛
- overall story arc؛
- role هر clip؛
- product state در ابتدای/انتهای هر clip؛
- character state/count؛
- environment state؛
- camera state؛
- transition type برای هر boundary؛
- shared references؛
- clip-specific references؛
- shared prompt blocks؛
- audio/music continuity؛
- final commercial payoff؛
- accepted discontinuities.

## Clip Contract

هر clip باید قرارداد مستقل داشته باشد.

### START STATE
- product state؛
- character count/identity/position؛
- environment؛
- camera/framing؛
- lighting؛
- important visible props؛
- inherited state from previous clip.

### ACTION ARC
حداکثر 1–2 state change اصلی به‌طور پیش‌فرض؛ actionهای همزمان محدود.

### END STATE
فریمی که باید:
- به clip بعدی handoff شود؛ یا
- match/editorial cut را ممکن کند؛ یا
- sequence را به final payoff برساند.

### CLIP-SPECIFIC RISK
interaction، physics، count، identity و reference burden مختص آن clip ثبت شود.

## Boundary Continuity

برای هر `Cn → Cn+1` مرز یک asset درجه‌یک است.

روش ترجیحی در hard/hybrid continuity:
1. End Keyframe Clip N ساخته و QA شود.
2. همان state به‌عنوان Start Reference/Ingredient اصلی Clip N+1 استفاده شود.
3. prompt Clip N+1 صریحاً بگوید این تصویر **initial state** است نه style reference.
4. object count، product state، character positions، camera direction و lighting در transition checklist بررسی شوند.

برای editorial transition exact geometry لازم نیست، ولی identity/style/direction/pacing باید intentional باشد.

## Shared vs Clip-Specific References

### Shared across clips
- clean product identity؛
- character identity؛
- packaging identity؛
- global scale rules؛
- style/lighting bible در صورت نیاز.

### Clip-specific
- start frame؛
- scene master؛
- end frame؛
- process-state reference؛
- tool/prop reference در صورت ضروری بودن؛
- clip-specific environment.

نباید صرفاً چون reference slot خالی است، همه assetها را در همه کلیپ‌ها آپلود کرد.

## Reference-budget rule

برای هر clip reference stack جداگانه طراحی می‌شود.

یادگیری P0001: reference مفید در یک task الزاماً reference مفید برای task دیگر نیست؛ reference competition می‌تواند scene reconstruction ایجاد کند. بنابراین **minimum sufficient role-clean stack** نسبت به maximum-filled stack ترجیح دارد مگر evidence خلافش را نشان دهد.

## Process-state distribution examples

### 2 clips
- C01: one clear craft/transformation state
- C02: completion + packaging/reveal

### 3 clips
- C01: craft/making
- C02: assembly/collection/packaging
- C03: inspection/reveal/hero

### 4 clips
- C01: origin/forming or macro hook
- C02: decorating/transformation
- C03: assembly/packaging
- C04: hero/payoff

این‌ها template هستند نه اجبار. `SCENARIO_ARCHITECTURE_SYSTEM.md` باید بر اساس محصول گزینه‌های واقعی را بسازد.

## چرا تقسیم کردن بهتر از فشرده‌کردن همه چیز در یک clip است؟

اگر فرآیند چند state change دارد، فشرده‌سازی در یک 10s ریسک این موارد را بالا می‌برد:
- morphing؛
- teleportation؛
- duplicate objects/characters؛
- compressed/unclear action؛
- impossible physics؛
- scene reconstruction.

تقسیم به چند clip اجازه می‌دهد هر clip یک مسئولیت اصلی داشته باشد و failure root cause قابل‌تشخیص‌تر شود.

## Clip production loop

برای هر clip:
`Clip Contract → Reference Strategy → Shot Timing → Storyboard → Keyframes → Prompt Package → Preflight → Baseline Runs → Video QA → Final Selection`

لازم نیست همه clipها یک‌جا generate شوند. بهتر است boundary-critical asset کلیپ قبلی قبل از قفل کلیپ بعد approved باشد.

## Assembly Stage

پس از انتخاب Final Run هر clip:
- frame-accurate trim؛
- transition؛
- speed adjustment فقط با دلیل؛
- color/exposure matching؛
- audio/music bridge؛
- logo/text overlay؛
- master export.

## Sequence QA

علاوه بر QA تک‌کلیپ، بررسی شود:
- product identity بین همه clipها؛
- character identity/count؛
- scale؛
- lighting/color؛
- direction of movement؛
- continuity of product/action state؛
- transition smoothness؛
- repeated/contradictory moments؛
- pacing across total duration؛
- escalation of visual interest؛
- final payoff؛
- audio continuity.

## Run/Data Model

هر project می‌تواند چند Clip داشته باشد:
- `P0002-C01`
- `P0002-C02`
- `P0002-C03`
- `P0002-C04`

Run ID project-global باقی می‌ماند، ولی `clip_id` در metadata ثبت می‌شود. مثال:
- run_id: `P0002-R0017`
- clip_id: `P0002-C02`

برای sequence نیز `sequence_id` می‌تواند مانند `P0002-S01` ثبت شود.

## Stop / downgrade rule

اگر continuity بین یک boundary بیش از دو repair cycle ایجاد کرد و root cause stochastic reconstruction بود:
- hard continuous را به hybrid یا editorial downgrade کن؛
- match cut یا post-production transition استفاده کن؛
- learning را ثبت کن.

کیفیت کل تبلیغ مهم‌تر از اثبات continuity مصنوعی است.
