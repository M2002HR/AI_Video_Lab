# Changelog

## 1.1.0 — 2026-08-07
### Added
- `AI_START_HERE.md` برای context recovery در chat/session جدید.
- AI-agnostic `00_SYSTEM/AI_OPERATOR_MANUAL.md` با ChatGPT به‌عنوان operator فعلی.
- `CHAT_CONTINUITY_PROTOCOL.md` و `FAST_START_PROTOCOL.md`.
- project-level `HANDOFF.md`.
- `18_CONVERSATION_LOG/` برای feedback و session summaries.
- `19_HANDOFF_ASSETS/` برای previewهای اختیاری و امن.
- checklistهای New Chat Context Load و Session Handoff.

### Changed
- سیستم از Codex-specific به AI-operator architecture تغییر کرد؛ ChatGPT می‌تواند repo را در حین production نگهداری و commit کند.
- `START_HERE.md` و `README.md` برای شروع سریع با product image + source prompt و ادامه بین chatها بازطراحی شدند.
- project template برای handoff و conversation continuity گسترش یافت.
- Storage/Data Model برای media provenance و cross-chat continuity شفاف‌تر شد.

### Deprecated
- `00_SYSTEM/CODEX_OPERATING_MANUAL.md` به legacy pointer تبدیل شد؛ منبع جاری `AI_OPERATOR_MANUAL.md` است.

### Fixed
- dependency عملیاتی به حافظه chat قبلی حذف شد؛ repo باید context لازم برای session بعدی را نگه دارد.

### Learning-derived changes
- فعلاً این تغییر معماری بر اساس نیاز عملیاتی صریح کاربر است، نه نتیجه benchmark؛ به‌عنوان system design decision ثبت شده است.

## 1.0.0 — 2026-08-07
### Added
- هستهٔ AI Video Ad Lab، چرخهٔ 24 مرحله‌ای، SOP/checklist، prompt library، template، registry و CLI.
### Changed / Deprecated / Fixed / Learning-derived changes
- هنوز موردی ثبت نشده بود.
