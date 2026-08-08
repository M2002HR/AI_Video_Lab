# SOP 07 — Scenario Architecture & Generation

## هدف

تولید یک **Scenario Architecture Menu** انتخاب‌پذیر برای تبلیغ AI که بین commercial value، process richness، generative risk و product identity تعادل ایجاد کند و به‌صورت رسمی از 1 تا 4 کلیپ پشتیبانی کند.

منبع اصلی: `00_SYSTEM/SCENARIO_ARCHITECTURE_SYSTEM.md`.

## ورودی لازم
- creative direction؛
- product identity / identity lock؛
- source/template analysis؛
- approved/reference readiness در حد موجود؛
- tool/model constraints در صورت معلوم بودن؛
- user intent درباره process/action/reveal؛
- duration/clip-count preference در صورت وجود.

## 1. Process State Map

قبل از ideation، stateهای بالقوه محصول را استخراج کن. مثال عمومی:

`raw/base → formed → coated/decorated → cupped/wrapped → arranged → packaged → hero`

هر process/state claim باید یکی از این برچسب‌ها را داشته باشد:
- `verified_real_process`
- `user_confirmed_process`
- `creative_metaphor`
- `unknown_do_not_claim`

فرآیند واقعی را فقط از روی ظاهر محصول جعل نکن.

برای هر transition مشخص کن:
- آیا ارزش تصویری دارد؟
- آیا geometry/material transformation لازم است؟
- interaction فیزیکی دارد؟
- آیا cut/match cut امن‌تر از morphing است؟

## 2. Scenario Capacity Assessment

ارزیابی کن:
- process richness؛
- visual diversity؛
- world/character capacity؛
- reference readiness؛
- generative feasibility؛
- commercial arc.

## 3. Duration Viability

اگر duration از قبل مشخص نیست، برای این معماری‌ها fit بده:
- `1×10s = 10s`
- `2×10s = 20s`
- `3×10s = 30s`
- `4×10s = 40s`

Status:
- `strong_fit`
- `viable`
- `possible_but_low_value`
- `not_recommended`

اگر duration مشخص است، روی همان تمرکز کن؛ اگر واضحاً نامناسب است alternative کوتاه پیشنهاد بده.

## 4. Adaptive Scenario Menu

سناریوهای واقعاً distinct تولید کن، نه تغییر اسم/زاویه یک ایده.

راهنمای تعداد:
- 10s: معمولاً 2–4 گزینه؛
- 20s: معمولاً 3–5 گزینه؛
- 30s: معمولاً 3–5 گزینه؛
- 40s: معمولاً 2–5 گزینه.

فقط تا وقتی ادامه بده که تفاوت واقعی وجود دارد. کل menu اولیه معمولاً از حدود 10–14 architecture معنادار بیشتر نشود مگر محصول واقعاً ظرفیت استثنایی داشته باشد.

## 5. خانواده‌های سناریو

در حد مناسب محصول این خانواده‌ها را بررسی کن:

### A. Hero / Inspection
محصول آماده است؛ camera/reveal و inspection. کم‌ریسک.

### B. Micro Process
یک مرحله واقعی/استعاری روشن مثل coating یا cupping.

### C. Assembly / Packaging
چند محصول آماده مرتب/بسته‌بندی می‌شوند.

### D. Transformation
یک state به state بعدی؛ فقط با reference/tool مناسب.

### E. Process Chain
چند state پشت‌سرهم؛ معمولاً مناسب multi-clip.

### F. Conceptual / Metaphor
miniature worksite، factory metaphor، material world و ایده‌های غیرliteral با identity-safe product.

### G. Editorial Macro Sequence
چند vignette مستقل با style/product continuity و اتصال تدوینی.

### H. Character-driven Product Journey
شخصیت‌ها نقش روایی دارند ولی محصول همچنان hero است.

همه خانواده‌ها اجباری نیستند.

## 6. Complexity rule

برای یک 10s به‌صورت پیش‌فرض یکی از این الگوها:
- 1 state + camera reveal؛
- 1 main transformation؛
- 2 simple sequential actions؛
- 1 assembly action + hero.

اگر سناریو شامل `forming + coating + transporting + packaging + reveal` است، آن را در 10s فشرده نکن؛ بررسی کن 2/3/4 clips بهتر است.

## 7. Scenario Menu Card

هر گزینه اولیه باید مختصر ولی قابل انتخاب باشد:
- Scenario ID / Title؛
- duration + clip count؛
- architecture: `continuous_world` / `hybrid` / `editorial_sequence`؛
- premise؛
- clip-by-clip role summary؛
- process depth؛
- visual impact؛
- generation risk؛
- new reference burden؛
- strongest commercial advantage؛
- main failure risk؛
- real-process / creative-metaphor status.

در این مرحله prompt کامل و beat-by-beat سنگین نساز.

## 8. Candidate cleanup

قبل از نمایش به کاربر:
- گزینه‌های duplicate را merge کن؛
- filler را حذف کن؛
- scenario صرفاً با تغییر رنگ/نام/زاویه را حذف کن؛
- 40s بدون چهار chapter واقعی را downgrade کن؛
- process جعلی را حذف یا creative metaphor اعلام کن.

## 9. User Selection Gate

منو را نمایش بده و اجازه بده کاربر architecture را انتخاب کند، مگر brief از قبل انتخاب را قطعی کرده باشد.

تا قبل از انتخاب وارد تولید سنگین reference/storyboard/keyframe نشو.

## 10. Expand selected scenario

پس از انتخاب:
- timeline کامل؛
- product state start/end؛
- character role/count؛
- tools/props ضروری؛
- required references/keyframes؛
- interaction/physics؛
- failure modes؛
- commercial payoff.

اگر multi-clip است:
- `MASTER_SEQUENCE.md`؛
- clip IDs؛
- `CLIP_CONTRACT` هر clip؛
- boundary contracts؛
- shared vs clip-specific references؛
- سپس `SOP_MULTI_CLIP_SEQUENCE.md`.

## خروجی‌های اجباری
- `process_state_map.md`؛
- `scenario_capacity_assessment.md`؛
- `scenario_menu.md`؛
- user selection/decision؛
- selected scenario؛
- برای multi-clip: master sequence + clip contracts.

## Gate

Pass یعنی:
- candidateها واقعاً متفاوت‌اند؛
- duration/clip count با ظرفیت واقعی محصول سازگار است؛
- process claims روشن‌اند؛
- risk/reference burden مستند است؛
- user می‌تواند آگاهانه انتخاب کند؛
- انتخاب ثبت شده است.

## Escalation

اگر user ایده پیچیده را انتخاب کرد، به‌جای رد کردن:
- complexity decomposition انجام بده؛
- duration مناسب‌تر 20/30/40s پیشنهاد کن؛
- hybrid/editorial را برای کاهش ریسک در نظر بگیر.

اگر 4 clips filler می‌شود، 3 clips را بهتر اعلام کن.

## Documentation

تمام candidateهای نمایش‌داده‌شده، انتخاب کاربر، candidateهای مهم حذف‌شده و دلیل، assumptions، architecture و next gate باید در repo ثبت شوند. `00_SYSTEM/DOCUMENTATION_CONTRACT.md` لازم‌الاجراست.
