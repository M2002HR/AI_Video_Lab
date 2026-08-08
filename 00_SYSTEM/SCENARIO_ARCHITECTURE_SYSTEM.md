# Scenario Architecture System

این سند منبع اصلی برای پیشنهاد سناریو قبل از تولید است. هدف این است که سیستم برای تبلیغ‌های 10، 20، 30 و 40 ثانیه‌ای آماده باشد، بدون اینکه کاربر با ده‌ها گزینه مشابه و کم‌ارزش بمباران شود.

## اصل UX

قبل از Storyboard/Keyframe، AI operator باید ابتدا یک **Scenario Architecture Menu** بسازد و به کاربر اجازه دهد مسیر را انتخاب کند.

اگر کاربر duration/clip count را از قبل مشخص کرده است، فقط همان معماری را با گزینه‌های مناسب پیشنهاد بده. اگر مشخص نکرده است، ظرفیت 1 تا 4 کلیپ 10 ثانیه‌ای را ارزیابی کن و فقط گزینه‌های واقعاً معنادار را نمایش بده.

هیچ duration یا تعداد کلیپ نباید فقط برای پر کردن منو پیشنهاد شود.

## واحدهای استاندارد

پیش‌فرض سیستم برای ابزارهایی که کلیپ 10 ثانیه‌ای می‌سازند:

- `1×10s` = 10 ثانیه
- `2×10s` = 20 ثانیه
- `3×10s` = 30 ثانیه
- `4×10s` = 40 ثانیه

اگر ابزار یا brief duration دیگری دارد، همین منطق با clip duration واقعی adapt می‌شود؛ مفهوم اصلی **Master Sequence + Clip Contracts** است.

## Step 1 — Scenario Capacity Assessment

قبل از ایده‌پردازی، ظرفیت creative واقعی پروژه را بسنج:

### A. Product process richness
چند state واقعی/قابل‌نمایش داریم؟ مثال:
`raw/base → shaped → coated → wrapped/cupped → arranged → packaged → hero`

اگر فرآیند واقعی معلوم نیست، آن را جعل نکن. stateها را با یکی از این برچسب‌ها ثبت کن:
- `verified_real_process`
- `user_confirmed_process`
- `creative_metaphor`
- `unknown_do_not_claim`

### B. Visual diversity
آیا محصول چند component، رنگ، coating، material، packaging state یا macro detail معنادار دارد؟

### C. World/character capacity
آیا template یا creative direction یک جهان مثل miniature workers، factory metaphor، luxury studio یا transformation world دارد که بیش از یک scene معنادار تولید کند؟

### D. Reference readiness
آیا برای stateهای مختلف reference کافی داریم یا ساخت هر سناریو نیازمند referenceهای جدید است؟

### E. Generative feasibility
برای tool فعلی، چند state change، interaction، character و object count قابل‌اعتماد است؟

### F. Commercial arc
آیا داستان طولانی‌تر واقعاً payoff بهتری می‌دهد یا فقط filler اضافه می‌کند؟

## Step 2 — Duration Viability Matrix

برای هرکدام از 10/20/30/40 ثانیه یکی از این وضعیت‌ها را بده:
- `strong_fit`
- `viable`
- `possible_but_low_value`
- `not_recommended`

و یک دلیل کوتاه بنویس.

مثال:

| Duration | Fit | Why | Meaningful scenario count |
|---|---|---|---:|
| 10s | strong_fit | یک hero/reveal روشن | 3 |
| 20s | strong_fit | process + payoff | 4 |
| 30s | strong_fit | craft + assembly + payoff | 4 |
| 40s | viable | فقط اگر چهار state مستقل ارزش تجاری دارند | 3 |

## Step 3 — Adaptive Candidate Budget

سیستم نباید تعداد ثابت و مصنوعی سناریو تولید کند.

راهنمای پیش‌فرض:
- 10s: معمولاً 2–4 گزینه distinct.
- 20s: معمولاً 3–5 گزینه distinct.
- 30s: معمولاً 3–5 گزینه distinct.
- 40s: معمولاً 2–5 گزینه distinct.

ولی **فقط تا جایی که تفاوت واقعی وجود دارد**.

اگر بعد از 2 سناریو بقیه صرفاً rename/reorder هستند، متوقف شو.

اگر محصول/process/template واقعاً ظرفیت بالایی دارد، می‌توان گزینه بیشتری ارائه کرد، ولی کل منوی اولیه بهتر است معمولاً از حدود 10–14 معماری معنادار بیشتر نشود. گزینه‌های اضافی را فقط با دلیل روشن اضافه کن.

## Step 4 — Scenario Family Coverage

به‌جای تولید variationهای سطحی، خانواده‌های متفاوت را پوشش بده. بسته به محصول:

- `hero_reveal`
- `inspection`
- `making`
- `coating_decorating`
- `assembly`
- `packaging`
- `process_chain`
- `before_after_transformation`
- `ingredient_to_product` فقط اگر واقعی/مجاز است
- `miniature_worksite`
- `editorial_macro_sequence`
- `premium_product_journey`
- `conceptual_metaphor`
- `character_driven`
- `material_texture_story`

همه خانواده‌ها برای همه محصولات مناسب نیستند.

## Step 5 — Scenario Menu Card

در منوی اولیه هر گزینه باید **مختصر ولی انتخاب‌پذیر** باشد، نه prompt کامل.

هر card شامل:
- Scenario ID/Title
- total duration / clip count
- architecture: `continuous_world` / `hybrid` / `editorial_sequence`
- one-line premise
- clip-by-clip role summary
- process depth: low / medium / high
- visual impact: low / medium / high
- generation risk: low / medium / high
- new reference burden: low / medium / high
- strongest commercial advantage
- main failure risk
- `real_process` یا `creative_metaphor`

کاربر باید بتواند با خواندن card انتخاب کند؛ beat-by-beat کامل فقط بعد از انتخاب تولید شود.

## Step 6 — Duration-specific Story Patterns

### 1×10s
بهترین برای یک idea اصلی:
- Hook → Hero
- One transformation → Hero
- One inspection/work action → Reveal
- Macro texture journey

به‌طور پیش‌فرض بیش از 1 state change اصلی یا 2 action ساده نگذار.

### 2×10s — 20s
الگوهای قوی:
1. `Process → Payoff`
   - C01 making/decorating
   - C02 packaging/reveal
2. `Hook → Development`
   - C01 striking macro concept
   - C02 expanded product world + hero
3. `Craft → Collection`
   - C01 one-item craftsmanship
   - C02 assortment/box completion
4. `Editorial Duo`
   - C01 independent process vignette
   - C02 independent premium hero vignette

### 3×10s — 30s
الگوهای قوی:
1. `Craft → Assembly → Hero`
2. `Origin/Material → Transformation → Product`
3. `One Item → Collection → Packaging`
4. `Three Editorial Chapters`
5. `Character Journey → Completion → Reveal`

برای product ads معمولاً 30s نقطه خوبی برای process storytelling است، چون هر clip یک مسئولیت اصلی می‌گیرد.

### 4×10s — 40s
فقط وقتی چهار chapter واقعاً ارزش دارند:
1. `Origin → Craft → Assembly → Hero`
2. `Form → Decorate → Package → Reveal`
3. `Macro Detail → Process → Collection → Brand Hero`
4. `Four Editorial Worlds` با identity/style مشترک

40s را فقط برای پرکردن زمان پیشنهاد نکن. اگر Clip 2 و 3 تقریباً یک کار می‌کنند، 30s بهتر است.

## Step 7 — Architecture Modes

### continuous_world
همه clipها یک جهان فیزیکی پیوسته‌اند. بالاترین continuity burden.

### editorial_sequence
هر clip scene مستقل دارد؛ identity/style/pacing مشترک و اتصال در edit. مطمئن‌تر برای AI.

### hybrid — default recommendation for many 20–40s AI ads
داخل هر clip continuity سخت، بین clipها transition کنترل‌شده مانند match cut، action cut یا approved boundary frame.

سیستم نباید continuous را فقط چون «سینمایی‌تر» است انتخاب کند. reliability و commercial quality مقدم‌اند.

## Step 8 — Boundary-first design

برای هر Cn→Cn+1 قبل از generation ثبت کن:
- product state at end/start
- character count and identity
- important object count
- camera orientation
- movement direction
- lighting/environment
- transition type
- exact continuity requirements
- allowed discontinuities

اگر hard continuity لازم است، End KF کلیپ N به عنوان Start-state evidence کلیپ N+1 استفاده شود.

## Step 9 — Selection Gate

تا وقتی کاربر یا brief یک Scenario Architecture را انتخاب نکرده است، وارد production سنگین نشو.

بعد از انتخاب:
1. Scenario را expand کن.
2. `MASTER_SEQUENCE.md` بساز اگر بیش از یک clip است.
3. برای هر clip `CLIP_CONTRACT.md` بساز.
4. سپس reference strategy را per-clip بازبینی کن.
5. بعد shot timing/storyboard/keyframe/video prompt را اجرا کن.

## Anti-overgeneration rules

- سناریوهای تقریباً مشابه را merge کن.
- فقط تغییر رنگ/زاویه/اسم = سناریوی جدید نیست.
- duration بلندتر بدون state/story جدید پیشنهاد نشود.
- process واقعی را invent نکن.
- یک 40s ضعیف را صرفاً چون سیستم 4 clip را پشتیبانی می‌کند پیشنهاد نده.
- منوی اولیه باید انتخاب را آسان‌تر کند، نه سخت‌تر.

## Documentation

برای هر Scenario Menu ثبت شود:
- capacity assessment
- duration viability matrix
- candidate cards
- rejected/omitted family و دلیل در صورت مهم بودن
- user selection
- architecture mode
- confidence/assumptions

این اطلاعات باید در project files بماند تا chat بعدی بفهمد چه گزینه‌هایی بررسی و چرا انتخاب/رد شده‌اند.
