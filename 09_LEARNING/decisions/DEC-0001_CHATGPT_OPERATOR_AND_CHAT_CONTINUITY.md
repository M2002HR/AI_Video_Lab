# DEC-0001 — ChatGPT operator + repository-based chat continuity

- Date: 2026-08-07
- Status: accepted
- Decision type: architecture / operating model
- Requested by: user

## Context
نسخه 1.0 repository با فرض Codex به‌عنوان operator ساخته شد. کاربر تصمیم گرفت production واقعی، prompt/scenario/image/video iteration و maintenance سیستم را عمدتاً با ChatGPT انجام دهد و ممکن است کار را در chatهای جدید ادامه دهد.

## Decision
1. معماری از Codex-specific به **AI-operator** تغییر می‌کند؛ ChatGPT operator فعلی است.
2. repository، نه chat history، حافظه پایدار پروژه است.
3. هر پروژه active باید `STATUS.md` + `HANDOFF.md` + conversation log داشته باشد.
4. `AI_START_HERE.md` پروتکل context recovery برای agent/session جدید است.
5. کاربر اجازه داده ChatGPT تغییرات لازم، non-destructive و مستند را در repo انجام دهد و commit کند.
6. minimum-input fast start برای پروژه جدید: product image(s) + source/template prompt.

## Alternatives considered
- ادامه Codex-only: رد شد؛ با شیوه کار موردنظر user هم‌راستا نیست.
- اتکا به chat memory: رد شد؛ بین sessionها قابل اعتماد و audit-friendly نیست.
- ذخیره transcript کامل: فعلاً رد شد؛ noise و duplication زیاد دارد. فقط feedback/session summary ارزشمند ثبت می‌شود.

## Consequences
- docs/operator files باید AI-neutral شوند.
- project template به handoff/conversation continuity نیاز دارد.
- visual media ممکن است در chat جدید نیاز به re-attach داشته باشد؛ این باید در handoff صریح باشد.
- تغییرات repo در جریان production بخشی از workflow عادی هستند.

## Evidence
این تصمیم بر اساس نیاز عملیاتی صریح user است، نه benchmark عملکرد مدل. بنابراین به‌عنوان design decision پذیرفته شده و نباید به‌عنوان empirical claim درباره کیفیت ChatGPT/Codex تعبیر شود.
