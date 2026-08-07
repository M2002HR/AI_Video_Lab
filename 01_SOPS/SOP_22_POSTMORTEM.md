# SOP 22 POSTMORTEM

## هدف

اجرای قابل‌تکرار STAGE_22 با حفظ evidence و gate روشن.

## ورودی لازم

Runها و QAها. ورودی اختیاری: feedback کاربر، reference style/scene و constraint ابزار. پیش‌نیاز: stage قبلی approved یا blocker/assumption ثبت‌شده.

## رویه

1. STATUS، SOP/checklist و evidence مرتبط را بخوانید.
2. موفقیت/شکست، retry، prompt/tool، failure و experiment بعدی را ثبت کن.
3. canonical prompt مرتبط را instantiate و reference roleها را صریح نگه دارید.
4. خروجی، تصمیم، uncertainty و failure tag را در فایل stage یا Run ثبت کنید.
5. checklist را اجرا کنید؛ فقط پس از pass STATUS را جلو ببرید و registry را rebuild کنید.

## خروجی و Gate

postmortem. Pass یعنی usable، provenance کامل و معیار stage؛ Fail یعنی blocker/failure و تصمیم repair/regenerate/بازگشت ثبت شده.

## AI، ابزار و metadata

AI task مستقل از tool است؛ tool/model نامعلوم unknown ثبت می‌شود. generation به Run ID، prompt ID/version/body، reference role، settings، manifest، evaluation و selected نیاز دارد. analysis به source، confidence و assumption نیاز دارد.

## خطا و escalation

identity drift، role مبهم reference، prompt متناقض و timeline بیش‌پیچیده‌اند. خطای local repair؛ identity/structural/continuity regenerate؛ failure تکراری بازگشت به stage ریشه و hypothesis/experiment. Done: فایل‌های stage، STATUS و metadata sync و gate مستند.
