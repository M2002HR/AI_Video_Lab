# SOP — Multi-Clip Sequence Production

## هدف

تولید یک تبلیغ 20–30 ثانیه‌ای یا بیشتر از چند کلیپ کوتاه مستقل، به شکلی که هر کلیپ قابل تولید/QA مستقل باشد ولی sequence نهایی روایت، هویت محصول و continuity کنترل‌شده داشته باشد.

## ورودی لازم
- product identity approved؛
- creative direction؛
- total target duration؛
- target clip duration/tool constraints؛
- architecture انتخابی: continuous / editorial / hybrid.

## خروجی
- `MASTER_SEQUENCE.md`؛
- clip IDs؛
- clip contracts؛
- shared reference set؛
- clip-specific reference sets؛
- prompt package مستقل هر clip؛
- final runs مستقل؛
- assembly plan؛
- sequence QA.

## رویه

### 1. Master Story Arc
قبل از نوشتن prompt تک‌کلیپ، کل داستان را در 2–5 beat کلان تعریف کن. تعیین کن مخاطب در ابتدا، میانه و پایان چه چیزی می‌بیند/می‌فهمد.

### 2. Clip Decomposition
داستان را بر اساس **state change** تقسیم کن، نه صرفاً زمان مساوی.

هر clip بهتر است حداکثر 1–2 state change اصلی داشته باشد.

### 3. Clip Role
برای هر clip نقش ثبت کن، مانند:
- hook؛
- making؛
- decorating؛
- assembly؛
- packaging؛
- inspection؛
- reveal؛
- hero.

### 4. Boundary Contract
برای هر مرز C01→C02 و C02→C03 مشخص کن:
- چه چیزی باید دقیقاً حفظ شود؛
- چه چیزی اجازه تغییر دارد؛
- transition نوع cut است یا continuous handoff؛
- آیا End KF کلیپ قبل، Start KF کلیپ بعد می‌شود یا خیر.

### 5. Shared Bible
یک shared bible برای تمام کلیپ‌ها داشته باش:
- product identity lock؛
- character identity؛
- scale rules؛
- packaging؛
- style/lighting؛
- forbidden transformations.

### 6. Clip-Specific Workflow
برای هر clip به‌صورت مستقل مراحل Scenario/Shot Timing/Storyboard/Keyframe/Prompt/Preflight/Generation/QA را اجرا کن. Final clip N قبل از قفل شدن clip N+1 لازم نیست 100% نهایی باشد، اما boundary state مورد استفاده باید approved باشد.

### 7. Transition Strategy
سه حالت:

#### Hard continuity
End frame همان state اولیه clip بعد است. مناسب وقتی action باید واقعاً ادامه پیدا کند.

#### Match cut
shape/composition/motion مشابه است ولی geometry دقیق لازم نیست. برای AI اغلب مطمئن‌تر.

#### Editorial cut
دو صحنه مستقل با product/character/style continuity. اتصال توسط edit/audio انجام می‌شود.

### 8. Sequence Assembly
Final Runهای clipها را در Stage 20 مونتاژ کن. trim، transition، audio و color match را ثبت کن.

### 9. Sequence QA
علاوه بر clip QA، checklist multi-clip را اجرا کن.

## Gate
Pass زمانی است که:
- story arc کل مشخص است؛
- هر clip نقش مستقل دارد؛
- boundary contractها ثبت شده‌اند؛
- identity bible مشترک است؛
- هر final clip provenance/QA دارد؛
- sequence assembled از نظر pacing و continuity قابل قبول است.

## Escalation
اگر boundary continuity بیش از دو cycle repair ایجاد کرد و مشکل ناشی از stochastic reconstruction است:
- continuous را به hybrid یا editorial downgrade کن؛
- از match cut یا post-production transition استفاده کن؛
- learning را ثبت کن.

## Documentation
هر clip باید `clip_id` داشته باشد و Runهایش به آن link شوند. MASTER_SEQUENCE، boundary decisions، selected clip runs و final assembly باید در HANDOFF قابل بازیابی باشند.
