# شروع از اینجا

این repo طوری طراحی شده که لازم نباشد مسیرها، IDها یا جزئیات session قبلی را حفظ کنید. **ChatGPT باید bookkeeping را انجام دهد و repo حافظه پایدار باشد.**

## شروع سریع پروژه جدید
دو ورودی اصلی کافی است:
1. عکس/عکس‌های اصلی محصول؛
2. prompt/template/reference prompt اولیه.

آن‌ها را در chat بفرستید و بگویید:

> «با این عکس محصول و این پرامپت یک پروژه جدید شروع کن؛ خودت repo را بخوان، ورودی‌ها را ثبت کن و طبق سیستم مرحله اول را جلو ببر.»

ChatGPT باید بدون questionnaire غیرضروری:
- context repo را load کند؛
- project ID بسازد؛
- original inputs را immutable ثبت کند؛
- source prompt را reverse-engineer کند؛
- product identity اولیه را بسازد؛
- reference strategy را مشخص کند؛
- `STATUS.md` و `HANDOFF.md` را به‌روز کند؛
- در اولین gate واقعی یا نیاز به generation خارجی توقف کند.

## شروع یک chat جدید در میانه پروژه
repo را در اختیار ChatGPT قرار دهید و فقط بگویید:

> «این repo پروژه ماست. `AI_START_HERE.md` را بخوان، خودت برو در جریان قرار بگیر و بگو الان کجای کاریم.»

لازم نیست chat قبلی را دوباره توضیح دهید. اگر media خاصی از session قبلی از طریق repo قابل مشاهده نباشد، ChatGPT فقط همان asset لازم را برای re-attach درخواست می‌کند.

## کارهای رایج
- شروع پروژه: «برای این محصول پروژه جدید بساز و Fast Start را اجرا کن.»
- ادامه: «وضعیت پروژه را بخوان و مرحله منطقی بعدی را انجام بده.»
- ساخت prompt package: «برای مرحله بعد بهترین prompt تاییدشده فعلی را instantiate کن و package بده.»
- ثبت خروجی خارجی: «این خروجی ابزار X است؛ prompt/reference/settings را به عنوان Run ثبت کن.»
- مقایسه: «این Runها را با rubric سیستم مقایسه کن و failure tag بده.»
- feedback: «این نکته را ثبت کن؛ مشخص کن observation است یا evidence کافی برای تغییر استاندارد داریم.»
- بهبود prompt: «بر اساس Runهای اخیر ببین prompt فعلی چه چیزی کم دارد و candidate version بساز.»
- پایان session: «handoff پروژه را کامل کن و تغییرات لازم را commit کن.»

## اصل مهم
ورودی اصلی، Runها و نسخه‌های تاریخی overwrite نمی‌شوند. سیستم باید بتواند بعداً توضیح دهد هر خروجی با چه prompt، reference، tool/model و تصمیماتی ساخته شده و دقیقاً چرا prompt/checklist/SOP بعدی بهتر شده است.

برای AI جدید: `AI_START_HERE.md`  
نقشه سیستم: `00_SYSTEM/INDEX.md`  
قواعد اپراتور: `AGENTS.md` و `00_SYSTEM/AI_OPERATOR_MANUAL.md`
