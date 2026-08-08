# New Chat Start — 30s Truffle Derivative

این فایل برای شروع یک chat جدید و ساخت تبلیغ 30 ثانیه‌ای / 3×10s از همان محصول P0001 است.

## هدف

یک **پروژه مشتق جدید** از P0001 ایجاد شود؛ P0001 و Run نهایی R0022 overwrite نشوند.

پروژه جدید باید:
- همان محصول ترافل و template/creative DNA را بشناسد؛
- learningهای P0001 را reuse کند؛
- deliverable = 30s / 3×10s / 16:9 باشد؛
- قبل از تولید تصویر/ویدیو یک Scenario Architecture Menu مخصوص 3×10s ارائه کند؛
- 3–5 سناریوی واقعاً متفاوت پیشنهاد دهد فقط اگر ظرفیت واقعی وجود دارد؛
- process واقعی را جعل نکند؛
- بعد از انتخاب کاربر Master Sequence + Clip Contracts بسازد؛
- سپس per-clip reference strategy و production را جلو ببرد؛
- media معنی‌دار جدید را طبق Git proxy policy کم‌حجم و commit کند.

## Exact prompt to send in a fresh ChatGPT chat

```text
این GitHub Repository سیستم AI Video Lab ماست:
M2002HR/AI_Video_Lab

اول `AI_START_HERE.md` و `AGENTS.md` را بخوان و طبق خود سیستم context را بازیابی کن. تاریخچه چت قبلی را از من نخواه؛ هر چیزی که در repo ثبت شده خودت پیدا کن.

من می‌خواهم از همان محصول ترافل پروژه `P0001` این بار یک تبلیغ جدید 30 ثانیه‌ای بسازم که از 3 ویدیوی 10 ثانیه‌ای تشکیل شود و در نهایت به هم متصل شوند.

P0001 را overwrite نکن و optimization قبلی R0022 را ادامه نده مگر برای استفاده از learningهایش. یک پروژه مشتق جدید بساز و parent را P0001 ثبت کن.

قبل از هر تولید جدید:
1. `06_PROJECTS/P0001_truffle_chocolate/HANDOFF.md` و `STATUS.md` را بخوان.
2. `06_PROJECTS/P0001_truffle_chocolate/19_HANDOFF_ASSETS/proxy_manifest.json` را بخوان و Git previewهای موجود را برای visual context بررسی کن.
3. source-prompt analysis، product identity، reference strategy و learningهای P0001 را بررسی کن.
4. `00_SYSTEM/SCENARIO_ARCHITECTURE_SYSTEM.md`، `00_SYSTEM/MULTI_CLIP_ARCHITECTURE.md`، `01_SOPS/SOP_07_SCENARIO_GENERATION.md`، `01_SOPS/SOP_MULTI_CLIP_SEQUENCE.md` و checklistهای مرتبط را بخوان.
5. برای 30s / 3×10s یک Process State Map و Scenario Capacity Assessment بساز.
6. سپس 3 تا 5 Scenario Architecture واقعاً متفاوت و باارزش برای همین محصول + creative DNA پیشنهاد بده. اگر واقعاً فقط 3 گزینه معنادار وجود دارد، 5 تا را مصنوعی نکن.
7. در سناریوها فقط reveal ساده پیشنهاد نده؛ در صورت مناسب بودن process/making/coating/assembly/packaging/character-driven/editorial/hybrid را هم بررسی کن.
8. هر process را مشخص کن که verified/user-confirmed است یا creative metaphor؛ فرآیند واقعی را از خودت نساز.
9. برای هر سناریو clip map سه‌قسمتی، architecture mode، process depth، visual impact، generation risk، reference burden، مزیت تجاری و failure risk را خلاصه کن.
10. هنوز promptهای کامل تصویر/ویدیو یا storyboard سنگین نساز. اول من باید سناریو را انتخاب کنم.
11. همه تصمیم‌ها، candidateها و انتخاب بعدی را طبق Documentation Contract در repo ثبت و commit کن.
12. `00_SYSTEM/MEDIA_PROXY_PIPELINE.md` را هم بخوان. هر تصویر/ویدیوی معنی‌دار جدید یا re-attached که non-sensitive و locally accessible است باید low-resolution proxy بگیرد، در `19_HANDOFF_ASSETS/git_previews/` ذخیره شود، `proxy_manifest.json` به‌روز شود و commit بخورد. Original/full-resolution را داخل Git معمولی نگذار.

بعد از context load ابتدا یک خلاصه کوتاه از چیزهایی که از P0001 یاد گرفتی بده و بعد Scenario Menu مخصوص 30 ثانیه را ارائه کن.

نکته رسانه: P0001 اکنون low-resolution Git preview برای R0002, R0003, R0010, R0015, R0016, R0020, R0022 و R0023 دارد. برای Scenario Planning و visual recall ابتدا از همین proxyها استفاده کن و از من نخواه دوباره آن‌ها را بفرستم. فقط زمانی original/full-resolution را بخواه که برای generation input یا QA دقیق واقعاً لازم باشد.
```

## Git media already available

Low-resolution cross-chat proxies currently exist for:
- `R0002` 45° product hero reference؛
- `R0003` clean top product reference؛
- `R0010` three-chef character reference؛
- `R0015` scene master؛
- `R0016` KF01؛
- `R0020` KF03؛
- `R0022` selected video؛
- `R0023` rejected fourth-chef failure video.

Manifest:
`19_HANDOFF_ASSETS/proxy_manifest.json`

These are not generation-grade originals. For Scenario Menu and broad visual planning they should normally be sufficient.

## Recommended original re-attachment timing

برای Scenario Menu هیچ re-attachment لازم نیست.

بعد از انتخاب سناریو، operator باید فقط زمانی original/full-resolution بخواهد که clip production به fidelity بیشتر نیاز داشته باشد. نقطه شروع ممکن است:
1. original real product photo؛
2. full-resolution R0003؛
3. full-resolution R0010؛
4. original/full-resolution R0022 فقط اگر motion/world آن قرار است مستقیماً reuse شود.

R0006/R0008 یا سایر assetهای بدون Git proxy فقط بر اساس نیاز سناریوی انتخاب‌شده درخواست شوند.
