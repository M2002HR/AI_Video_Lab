# SOP — Multi-Clip Sequence Production

## هدف

تولید تبلیغ‌های 20، 30 و 40 ثانیه‌ای از 2، 3 یا 4 کلیپ کوتاه به شکلی که هر clip قابل تولید/QA مستقل باشد و sequence نهایی روایت، identity و continuity کنترل‌شده داشته باشد.

برای انتخاب تعداد کلیپ و سناریو ابتدا `00_SYSTEM/SCENARIO_ARCHITECTURE_SYSTEM.md` و `SOP_07_SCENARIO_GENERATION.md` اجرا شوند.

## ورودی لازم
- selected Scenario Architecture؛
- product identity approved؛
- creative direction؛
- total target duration؛
- clip count: 2 / 3 / 4؛
- target clip duration/tool constraints؛
- architecture: continuous / editorial / hybrid.

## خروجی
- `MASTER_SEQUENCE.md`؛
- `sequence_id`؛
- clip IDs؛
- clip contracts؛
- boundary contracts؛
- shared reference set؛
- clip-specific reference sets؛
- prompt package مستقل هر clip؛
- final run مستقل هر clip؛
- assembly plan؛
- sequence QA.

## رویه

### 1. Master Story Arc
قبل از prompt تک‌کلیپ، کل arc را تعریف کن. هر clip باید یک مسئولیت تجاری/روایی واضح داشته باشد.

### 2. Clip Decomposition
بر اساس **state change** تقسیم کن، نه صرفاً زمان مساوی.

پیش‌فرض: هر clip حداکثر 1–2 state change اصلی.

### 3. Recommended role patterns

#### 2 clips / ~20s
نمونه:
- C01 Hook/Craft/Process
- C02 Completion/Packaging/Hero

#### 3 clips / ~30s
نمونه:
- C01 Craft/Making
- C02 Assembly/Collection/Packaging
- C03 Inspection/Reveal/Hero

#### 4 clips / ~40s
نمونه:
- C01 Origin/Form/Macro Hook
- C02 Decoration/Transformation
- C03 Assembly/Packaging
- C04 Final Hero/Payoff

این‌ها template هستند؛ selected Scenario Architecture تعیین‌کننده است.

### 4. Clip Contract
برای هر `C01...C04` در صورت وجود:

#### START STATE
- product state؛
- character count/identity/position؛
- environment؛
- camera/framing؛
- lighting؛
- visible props؛
- inherited boundary state.

#### ACTION ARC
- main action؛
- state changes؛
- object interactions؛
- camera؛
- failure risks.

#### END STATE
- product state؛
- character state؛
- camera state؛
- transition-ready composition؛
- handoff asset if required.

### 5. Boundary Contract
برای هر `Cn → Cn+1` مشخص کن:
- چه چیزی دقیقاً ثابت می‌ماند؛
- چه چیزی مجاز است تغییر کند؛
- transition = hard continuity / match cut / editorial cut؛
- آیا End KF کلیپ قبل Start KF کلیپ بعد است؛
- product/object count؛
- character count/identity؛
- camera/motion direction؛
- environment/lighting؛
- audio handoff.

### 6. Shared Bible
بین همه clips:
- product identity lock؛
- character identity/count در صورت recurring بودن؛
- scale rules؛
- packaging identity؛
- global style/lighting grammar؛
- forbidden transformations.

### 7. Shared vs Clip-Specific References

Shared فقط وقتی واقعاً لازم است:
- product identity؛
- character identity؛
- packaging/style bible.

Clip-specific:
- start state؛
- scene master؛
- end state؛
- process/tool/prop reference؛
- environment state.

از پرکردن تمام reference slotها خودداری کن؛ minimum sufficient role-clean stack طراحی کن.

### 8. Clip-Specific Production
برای هر clip مستقل:
`Reference Strategy → Shot Timing → Storyboard → Keyframe → Prompt → Preflight → Baseline Generation → QA → Final Selection`

Boundary-critical state کلیپ قبلی قبل از قفل کلیپ بعد باید approved باشد.

### 9. Transition Strategies

#### Hard continuity
برای action واقعاً ادامه‌دار؛ بالاترین risk.

#### Match cut
shape/composition/motion ارتباط دارد ولی geometry pixel-perfect لازم نیست؛ اغلب مناسب AI.

#### Editorial cut
صحنه‌ها مستقل؛ identity/style/rhythm مشترک؛ اتصال توسط edit/audio.

#### Hybrid
continuity داخل clip سخت، boundaryها انتخابی و کنترل‌شده؛ default candidate برای بسیاری از 20–40s ads.

### 10. Baseline policy
برای هر clip به‌طور پیش‌فرض حداقل دو baseline Run با setup یکسان بگیر تا stochastic stability قابل ارزیابی باشد، مگر هزینه/brief تصمیم دیگری داشته باشد.

### 11. Sequence Assembly
پس از final هر clip:
- frame-accurate trim؛
- transitions؛
- color/exposure match؛
- audio/music bridge؛
- logo/text overlay؛
- master export.

### 12. Sequence QA
علاوه بر clip QA:
- product identity across clips؛
- character identity/count؛
- scale؛
- product state logic؛
- boundary continuity؛
- camera/movement direction؛
- lighting/color؛
- transition quality؛
- pacing؛
- repeated action؛
- escalation of interest؛
- final commercial payoff؛
- audio continuity.

## Gate

Pass وقتی:
- Master Sequence قفل است؛
- همه clip roles روشن‌اند؛
- همه boundaries contract دارند؛
- shared bible تعریف شده؛
- هر selected clip Run QA دارد؛
- assembled master sequence QA را پاس می‌کند.

## Escalation / Stop Rule

اگر یک hard boundary بیش از دو repair cycle به stochastic reconstruction خورد:
- hard continuity را به hybrid/match/editorial downgrade کن؛
- post-production transition را ترجیح بده؛
- failure و learning را ثبت کن.

اگر Clip 4 محتوای تازه اضافه نمی‌کند، sequence را به 3 clips کاهش بده. اگر Clip 3 هم filler است، 2 clips بهتر است.

## Documentation

هر clip `clip_id` و sequence یک `sequence_id` داشته باشد. `MASTER_SEQUENCE`, clip contracts, boundary decisions, selected runs, assembly و sequence QA باید در STATUS/HANDOFF قابل بازیابی باشند. `DOCUMENTATION_CONTRACT.md` لازم‌الاجراست.
