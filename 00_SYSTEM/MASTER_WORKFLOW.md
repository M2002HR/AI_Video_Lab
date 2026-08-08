# Master workflow

## Production mode branch

بعد از Creative Direction، قبل از production سنگین، `00_SYSTEM/SCENARIO_ARCHITECTURE_SYSTEM.md` اجرا می‌شود. اگر duration/clip count از قبل قفل نشده باشد، سیستم ظرفیت `1×10s / 2×10s / 3×10s / 4×10s` را می‌سنجد و یک Scenario Architecture Menu adaptive می‌سازد. فقط durationها و سناریوهای واقعاً معنادار پیشنهاد می‌شوند.

### SINGLE_CLIP
یک کلیپ مستقل، معمولاً 4–10 ثانیه. مراحل Stage 07 تا Stage 23 مستقیم اجرا می‌شوند.

### MULTI_CLIP
به‌صورت رسمی 2، 3 یا 4 کلیپ پشتیبانی می‌شود؛ در setup 10s یعنی معمولاً 20s، 30s یا 40s. قبل از shot/prompt هر clip باید `00_SYSTEM/MULTI_CLIP_ARCHITECTURE.md` و `01_SOPS/SOP_MULTI_CLIP_SEQUENCE.md` اجرا شوند و این موارد ایجاد شوند:
- Master Story / `MASTER_SEQUENCE`؛
- sequence ID و clip IDs؛
- role هر clip؛
- shared identity bible؛
- boundary contracts؛
- architecture = continuous / hybrid / editorial؛
- shared vs clip-specific reference strategy.

سپس Stage 09 تا Stage 19 برای هر clip به‌عنوان unit مستقل اجرا می‌شود و Stage 20 مونتاژ sequence و Stage 21 QA کل sequence را نیز پوشش می‌دهد.

اگر یک سناریوی 10s بیش از 1–2 state change اصلی و چند interaction فیزیکی دارد، قبل از پیچیده‌تر کردن prompt باید multi-clip decomposition بررسی شود. اگر 4 clips filler ایجاد می‌کند، 3 یا 2 clips ترجیح دارد.

## Stage map

### STAGE_00 — PROJECT_INTAKE
ورودی: brief و ورودی‌های اصلی

خروجی: project.json، STATUS و inventory

عملیات و Gate: اصل‌ها را بدون تغییر نگه‌دار؛ deliverable، hash، assumption و کمبود را ثبت کن.

### STAGE_01 — SOURCE_PROMPT_ANALYSIS
ورودی: پرامپت immutable و brief

خروجی: تحلیل KEEP/ADAPT/REMOVE و risk

عملیات و Gate: DNA ساختاری، محتوای محصول قدیمی، مفهوم reusable و contradictionها را جدا کن.

### STAGE_02 — PRODUCT_IDENTITY
ورودی: تصاویر محصول

خروجی: identity spec، identity lock، uncertainty

عملیات و Gate: silhouette، نسبت‌ها، material، texture، رنگ، packaging و forbidden transformations را ثبت کن.

### STAGE_03 — REFERENCE_STRATEGY
ورودی: identity spec و هدف

خروجی: reference plan و roleها

عملیات و Gate: نیاز cleanup/angle/macro/scene را تعیین و identity را از style جدا کن.

### STAGE_04 — REFERENCE_GENERATION
ورودی: reference plan

خروجی: Runهای reference

عملیات و Gate: هر رفرنس تولیدی Run مستقل و QA دارد؛ اصل را جایگزین نکن.

### STAGE_05 — REFERENCE_QA
ورودی: اصل‌ها و رفرنس تولیدی

خروجی: approved reference set

عملیات و Gate: geometry/color/material/label را با اصل مقایسه و drift را رد کن.

### STAGE_06 — CREATIVE_DIRECTION
ورودی: brief و رفرنس approved

خروجی: creative direction

عملیات و Gate: campaign، emotion، realism، scale، camera، lighting و product priority را ثبت کن.

### STAGE_07 — SCENARIO_ARCHITECTURE_AND_GENERATION
ورودی: creative direction + identity + source/template analysis + tool constraints

خروجی:
- Process State Map؛
- Scenario Capacity Assessment؛
- Duration Viability Matrix در صورت نیاز؛
- Scenario Architecture Menu؛
- candidate scenarios.

عملیات و Gate: `SOP_07_SCENARIO_GENERATION.md` و `CHK_SCENARIO_ARCHITECTURE_MENU.md` اجرا شوند. سناریوها باید از نظر action/story architecture متفاوت باشند، process واقعی جعل نشود، candidate count adaptive باشد، و برای 2/3/4 clips نقش هر clip در card مشخص باشد. قبل از production سنگین user selection gate وجود دارد.

### STAGE_08 — SCENARIO_SELECTION
ورودی: candidate/menu و rubric

خروجی: scenario selected و decision

عملیات و Gate: focus، feasibility، complexity، commercial payoff و reference burden را بسنج. production mode single/multi، clip count و architecture نهایی اینجا قفل می‌شوند. برای multi-clip پس از انتخاب Master Sequence و Clip Contracts ساخته می‌شوند.

### STAGE_09 — SHOT_TIMING
ورودی: سناریو منتخب

خروجی: timeline، camera plan، continuity

عملیات و Gate: beat، framing، حرکت، contact، final hero و SFX را sequence کن. در multi-clip برای هر clip جدا و در چارچوب Master Sequence اجرا می‌شود.

### STAGE_10 — STORYBOARD
ورودی: shot design

خروجی: storyboard specification

عملیات و Gate: برای هر beat composition، subject، action و transition را مشخص کن.

### STAGE_11 — STORYBOARD_QA
ورودی: storyboard

خروجی: QA report

عملیات و Gate: continuity، composition، timing و accidental complexity را gate کن.

### STAGE_12 — KEYFRAME_GENERATION
ورودی: storyboard و identity lock

خروجی: keyframe Runها

عملیات و Gate: فقط keyframeهای کنترل‌کننده را تولید و provenance کامل ثبت کن. در multi-clip boundary keyframeها دارایی درجه‌یک‌اند.

### STAGE_13 — KEYFRAME_QA
ورودی: keyframe و اصل

خروجی: approved keyframe set

عملیات و Gate: identity، scale، light، scene و character continuity را بررسی کن؛ برای multi-clip مرز Cn→Cn+1 نیز gate می‌شود.

### STAGE_14 — VIDEO_PROMPT
ورودی: identity/reference/scenario/timeline

خروجی: video prompt package

عملیات و Gate: base logic را با adapter ابزار، نقش رفرنس، physics و final frame ترکیب کن. هر clip در multi-clip package مستقل دارد و shared prompt blocks provenance دارند.

### STAGE_15 — VIDEO_PREFLIGHT
ورودی: package

خروجی: preflight report

عملیات و Gate: contradiction، complexity، role رفرنس، timing، camera و known failure را چک کن.

### STAGE_16 — VIDEO_GENERATION
ورودی: package و settings

خروجی: video Runها

عملیات و Gate: هر generation را با tool/model/settings/outputs کامل ثبت کن؛ در multi-clip `clip_id` و `sequence_id` نیز ثبت شوند.

### STAGE_17 — VIDEO_QA
ورودی: video Run

خروجی: frame-by-frame evaluation

عملیات و Gate: identity، morph، count، contact، gravity، camera، lighting و hero را نمره بده.

### STAGE_18 — REPAIR_DECISION
ورودی: QA و failure tags

خروجی: repair/regenerate decision

عملیات و Gate: local cosmetic را repair و identity/structure/continuity را regenerate یا stage قبلی کن.

### STAGE_19 — FINAL_SELECTION
ورودی: evaluated runs

خروجی: selected final run

عملیات و Gate: با rubric و brief، انتخاب و دلیل را ثبت کن؛ final بدون evaluation ممنوع. در multi-clip یک final run برای هر clip انتخاب می‌شود.

### STAGE_20 — POST_PRODUCTION
ورودی: final candidate یا مجموعه final clipها

خروجی: edit/composite/assembly record

عملیات و Gate: trim، color، transition، text/logo overlay، audio و delivery format را traceable ثبت کن. برای multi-clip sequence assembly اینجا انجام می‌شود.

### STAGE_21 — FINAL_QA
ورودی: deliverable

خروجی: final QA report

عملیات و Gate: brief، format، brand، logo، audio و commercial readiness را تأیید کن. در multi-clip علاوه بر clip QA، `CHK_MULTI_CLIP_CONTINUITY.md` اجرا شود.

### STAGE_22 — POSTMORTEM
ورودی: Runها و QAها

خروجی: postmortem

عملیات و Gate: موفقیت/شکست، retry، prompt/tool، failure و experiment بعدی را ثبت کن.

### STAGE_23 — SYSTEM_LEARNING
ورودی: postmortem و evidence

خروجی: OBS/HYP/LRN/CHG

عملیات و Gate: شواهد را طبقه‌بندی کن؛ فقط learning validated استاندارد را تغییر می‌دهد.

stage تازه با ID جدید افزوده می‌شود و پروژه‌های قدیمی را نمی‌شکند.

## Documentation gate عمومی

در تمام Stageها `00_SYSTEM/DOCUMENTATION_CONTRACT.md` بخشی از Definition of Done است. هر تصمیم، prompt، Run، feedback، failure، learning، workflow discovery یا next-action که برای ادامه/تکرار اثر دارد باید قبل از پایان milestone در repo ثبت شود.

## استاندارد تحلیل پرامپت مرجع

پرامپت اصلی immutable است. تحلیل باید این ماتریس را در فایل مرحله ثبت کند:

| بخش | دسته | اقدام | دلیل/ریسک |
|---|---|---|---|
| duration، aspect، camera، lighting، scale، background، character، timing، physics، sound، hero | DNA ساختاری | KEEP یا ADAPT | فقط در صورت سازگاری با brief جدید |
| نام/بسته‌بندی/مواد/عمل قدیمی | product-specific | REMOVE یا ADAPT | جلوگیری از leakage محصول قدیمی |
| استعارهٔ خلاقه مانند miniature workers یا macro factory | creative concept | ADAPT | feasibility و brand fit را بسنج |
| حرکت متناقض دوربین، scale ناسازگار، اکشن هم‌زمان زیاد | conflict/risk | REMOVE یا simplify | دلیل و تصمیم را ثبت کن |

Adapted prompt دارایی جدید با provenance است، نه ویرایش اصل.
