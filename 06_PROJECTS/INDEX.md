# Projects

این پوشه فقط پروژه‌های واقعی را نگه می‌دارد. پروژه demo در `13_EXAMPLES/` است و نباید وارد آمار واقعی شود.

## Active projects

| Project | Title | Status | Current stage | Next action |
|---|---|---|---|---|
| `P0001_truffle_chocolate` | Colorful Chocolate Truffle Miniature Commercial | active | STAGE_04 Reference Asset Creation | Generate Slots 1–4 from the reference-image prompt package, register Runs, then Reference QA |

## New project
پروژه جدید از `05_TEMPLATES/PROJECT_TEMPLATE/` ساخته می‌شود. وقتی user product image + source/template prompt می‌دهد، `00_SYSTEM/FAST_START_PROTOCOL.md` اجرا شود.

## New chat / continuation
برای پیدا کردن context:
1. projectهای `active` را از registry یا `project.json`ها پیدا کن.
2. در پروژه موردنظر اول `STATUS.md` و `HANDOFF.md` را بخوان.
3. سپس فقط فایل‌های stage فعلی را load کن.

## Required continuity contract
هر پروژه active باید تا حد امکان این‌ها را sync نگه دارد:
- `project.json`
- `STATUS.md`
- `HANDOFF.md`
- `18_CONVERSATION_LOG/`
- Run/prompt/evaluationهای مرتبط.

Media بزرگ ممکن است در Git نباشد؛ مسیر/role/hash و نیاز احتمالی به re-attach باید در handoff ثبت شود.
