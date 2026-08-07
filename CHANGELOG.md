# Changelog

## 1.1.1 — 2026-08-07
### Added
- اولین پروژه واقعی `P0001_truffle_chocolate` با brief، input provenance، source-prompt transcription/analysis، product identity، reference strategy، prompt package و handoff.
- tool card برای Google Flow / Gemini Omni Flash با capabilityهای رسمی و operational seven-reference rule.
- `OBS-0001` برای محدودیت عملیاتی 7 Ingredient و `HYP-0001` برای separate-vs-collage reference strategy.
- `EXP-0001` برای A/B test کردن referenceهای جدا در برابر multi-view contact sheet.

### Changed
- Reference-image production default: one target view per Run؛ product references تمیز و single-purpose باشند و همه slotها صرفاً به دلیل موجود بودن پر نشوند.
- Omni Flash ingredient budget policy: سقف عملیاتی 7، هدف اولیه 4–6 reference با 1–2 slot رزرو.

### Learning-derived changes
- multi-view collage فعلاً production default نیست؛ این نتیجه یک inference از Google best practices است و تا اجرای EXP-0001 به‌عنوان hypothesis باقی می‌ماند.
- عدد 7 توسط تجربه کاربر و مستند third-party Flow API corroborate شده، اما Help رسمی Google که در این نسخه بررسی شد عدد را صریح ذکر نمی‌کند؛ بنابراین provisional و نیازمند re-verification است.

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
- این تغییر معماری بر اساس نیاز عملیاتی صریح کاربر است، نه نتیجه benchmark؛ به‌عنوان system design decision ثبت شده است.

## 1.0.0 — 2026-08-07
### Added
- هستهٔ AI Video Ad Lab، چرخهٔ 24 مرحله‌ای، SOP/checklist، prompt library، template، registry و CLI.
### Changed / Deprecated / Fixed / Learning-derived changes
- هنوز موردی ثبت نشده بود.
