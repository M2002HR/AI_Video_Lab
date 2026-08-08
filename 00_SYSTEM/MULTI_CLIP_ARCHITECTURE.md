# Multi-Clip Architecture

این سند روش ساخت تبلیغ‌های طولانی‌تر از چند کلیپ کوتاه مستقل (مثلاً 2×10s یا 3×10s) را تعریف می‌کند.

## اصل طراحی

یک ویدیوی 20 یا 30 ثانیه‌ای نباید صرفاً «سه ویدیوی 10 ثانیه‌ای تصادفی که بعداً کنار هم چسبیده‌اند» باشد.

ابتدا یک **Master Sequence** طراحی می‌شود، سپس هر کلیپ یک واحد تولید مستقل با قرارداد ورودی/خروجی روشن است.

ساختار:

`MASTER STORY → CLIP 01 → TRANSITION CONTRACT → CLIP 02 → TRANSITION CONTRACT → CLIP 03 → ASSEMBLY → SEQUENCE QA`

## دو نوع معماری اصلی

### A. Continuous-world sequence
برای زمانی که می‌خواهیم مخاطب احساس کند همه کلیپ‌ها بخش‌های متوالی یک جهان واحد هستند.

نیازمند:
- product identity lock مشترک؛
- character bible مشترک؛
- environment/lighting lock مشترک؛
- clip boundary frame یا handoff state؛
- camera/position continuity؛
- exact object count/placement continuity در مرزها.

مثال:
- Clip 1: آماده‌سازی/تزئین ترافل؛
- Clip 2: قرار دادن و مرتب‌سازی داخل جعبه؛
- Clip 3: inspection و final box reveal.

### B. Editorial sequence
برای زمانی که هر 10 ثانیه یک mini-scene مستقل است و اتصال از طریق تدوین، مفهوم، product identity، رنگ و rhythm انجام می‌شود.

نیازمند continuity سخت spatial کمتر است و معمولاً برای AI video مطمئن‌تر است.

مثال:
- Clip 1: macro making/decorating؛
- Clip 2: miniature packaging world؛
- Clip 3: premium final product hero.

این سه کلیپ می‌توانند با cut/match cut/sound bridge به هم وصل شوند بدون اینکه لازم باشد مدل exact geometry فریم قبل را ادامه دهد.

## انتخاب architecture

قبل از تولید، برای هر sequence باید یکی از این‌ها ثبت شود:
- `continuous_world`
- `editorial_sequence`
- `hybrid`

### Hybrid
در hybrid، continuity داخل هر clip سخت است ولی بین clipها با یک transition کنترل‌شده سبک‌تر می‌شود؛ معمولاً بهترین گزینه برای 20–30 ثانیه AI ads است.

## Master Sequence Document

قبل از ساخت Clip 01 باید یک فایل `MASTER_SEQUENCE.md` وجود داشته باشد که شامل این موارد باشد:
- total duration؛
- clip count و duration هر clip؛
- overall story arc؛
- role هر clip؛
- product state در ابتدای/انتهای هر clip؛
- character state؛
- environment state؛
- camera state؛
- transition type؛
- shared references؛
- clip-specific references؛
- shared prompt blocks؛
- audio/music continuity؛
- final commercial payoff.

## Clip Contract

هر clip باید قرارداد مستقلی داشته باشد:

### START STATE
- product state؛
- character count/identity/position؛
- environment؛
- camera/framing؛
- lighting؛
- important visible props.

### ACTION ARC
حداکثر چند beat روشن که داخل مدت clip واقعاً قابل اجرا باشند.

### END STATE
فریمی که باید یا:
- به clip بعدی تحویل داده شود؛
- یا یک cut/editorial transition را ممکن کند.

## Boundary Continuity

برای continuous/hybrid sequence، مرز دو کلیپ یک asset درجه‌یک است.

روش ترجیحی:
1. End Keyframe Clip N ساخته و QA می‌شود.
2. همان تصویر به‌عنوان Start Reference/Ingredient اصلی Clip N+1 استفاده می‌شود.
3. prompt Clip N+1 صریحاً می‌گوید این تصویر state اولیه است، نه فقط style reference.
4. object count، product state، character positions و lighting در transition checklist بررسی می‌شوند.

## Shared vs Clip-Specific References

### Shared across clips
- clean product identity؛
- character identity؛
- packaging identity؛
- style/lighting bible در صورت نیاز.

### Clip-specific
- start frame؛
- scene master؛
- end frame؛
- process-specific prop/tool reference؛
- clip-specific environment.

نباید صرفاً چون reference slot خالی است، همه assetها را در همه کلیپ‌ها آپلود کرد.

## Scenario distribution برای 3×10s

یک الگوی پیشنهادی عمومی:

### Clip 01 — Hook / Making
هدف: جذب توجه + یک process action واضح.

### Clip 02 — Development / Assembly
هدف: گسترش جهان، assembly، packaging یا transformation کنترل‌شده.

### Clip 03 — Payoff / Product Hero
هدف: completion، inspection، reveal، برندینگ/hero.

برای 2×10s:
- Clip 01: process/hook؛
- Clip 02: completion/reveal.

## چرا تقسیم کردن بهتر از فشرده‌کردن همه چیز در یک 10s است؟

اگر فرآیند شامل چند state change باشد (ساخت، تزئین، جابه‌جایی، بسته‌بندی، reveal)، قراردادن همه در یک 10 ثانیه ریسک این موارد را بالا می‌برد:
- morphing؛
- teleportation؛
- duplicate objects/characters؛
- compressed/unclear action؛
- impossible physics؛
- scene reconstruction.

تقسیم به چند clip اجازه می‌دهد هر clip فقط 1–2 تغییر state مهم داشته باشد.

## Assembly Stage

پس از انتخاب Final Run هر clip:
- trim frame-accurate؛
- transition؛
- speed only if justified؛
- color matching؛
- audio bridge؛
- logo/text overlay؛
- master export.

## Sequence QA

بعد از assembly علاوه بر QA تک‌کلیپ، باید بررسی شود:
- product identity بین کلیپ‌ها؛
- character identity؛
- scale؛
- lighting/color؛
- direction of movement؛
- continuity of action/state؛
- transition smoothness؛
- repeated or contradictory moments؛
- pacing across total duration؛
- final payoff.

## Run/Data Model

هر project می‌تواند چند Clip داشته باشد:
- `P0002-C01`
- `P0002-C02`
- `P0002-C03`

Run ID همچنان project-global باقی می‌ماند، ولی `clip_id` در metadata ثبت می‌شود. مثال:
- run_id: `P0002-R0017`
- clip_id: `P0002-C02`

این کار registry و مقایسه را ساده نگه می‌دارد.

## Stop rule

اگر continuity بین دو clip باعث generation loop بی‌پایان شد، sequence باید از `continuous_world` به `hybrid` یا `editorial_sequence` downgrade شود و transition در post-production کنترل شود. کیفیت کل تبلیغ مهم‌تر از اثبات continuity مصنوعی است.
