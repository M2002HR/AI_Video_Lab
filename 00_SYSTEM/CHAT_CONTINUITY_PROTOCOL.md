# CHAT CONTINUITY PROTOCOL

هدف: هر پروژه بتواند بین chat/sessionهای مستقل بدون وابستگی به حافظه گفتگو ادامه پیدا کند.

## سه لایه context
1. **System context**: `AI_START_HERE.md` + `00_SYSTEM/*`.
2. **Project context**: `project.json` + `STATUS.md` + `HANDOFF.md`.
3. **Evidence context**: input/prompt/Run/evaluation/feedback/decision files.

## `HANDOFF.md` چه چیزی باید بگوید؟
- پروژه و deliverable؛
- stage فعلی؛
- آخرین تصمیم‌های approved؛
- product identity summary و مسیر full spec؛
- referenceهای approved؛
- scenario/keyframe/prompt package منتخب؛
- آخرین Runهای مهم و نتیجه آن‌ها؛
- known failures؛
- feedback اخیر کاربر؛
- blocker؛
- دقیقاً next action؛
- کدام media برای ادامه باید در chat بعدی re-attach شود، اگر لازم است.

`HANDOFF.md` خلاصه عملیاتی است، نه جایگزین source files.

## Conversation log
`18_CONVERSATION_LOG/` فقط اطلاعات با ارزش پایدار را نگه می‌دارد:
- feedback خام مهم؛
- session summaries؛
- تصمیم/ترجیحی که روی تولید اثر دارد.

Transcript کامل chat لازم نیست ذخیره شود مگر دلیل مشخص وجود داشته باشد.

## پایان session
وقتی یک session تصمیم یا تولید معنادار داشته است:
1. Run/prompt/evaluation را ثبت کن.
2. feedback مهم را ثبت کن.
3. `STATUS.md` را sync کن.
4. `HANDOFF.md` را طوری بنویس که یک AI بی‌خبر بتواند ادامه دهد.
5. اگر insight عمومی است OBS/HYP بساز.
6. commit موضوعی بزن.

## شروع session بعدی
AI نباید از کاربر بخواهد «همه‌چیز را از اول توضیح بده». ابتدا repo را بخواند. فقط gapهای واقعی را سؤال کند.

## Visual continuity
Git metadata به‌تنهایی جای visual inspection را نمی‌گیرد. اگر media سنگین در Git نیست:
- مسیر/نام/hash/role آن در docs ثبت شود؛
- handoff مشخص کند آیا re-attach لازم است؛
- در صورت امکان یک preview غیرحساس طبق Storage Policy نگهداری شود.
