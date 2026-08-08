# Changelog

## 1.3.0 — 2026-08-08
### Added
- `00_SYSTEM/MEDIA_PROXY_PIPELINE.md` برای ساخت و commit نسخه کم‌حجم تصاویر/ویدیوهای معنی‌دار پروژه.
- `11_TOOLS/media_proxy.py` برای image WebP proxy و video H.264 MP4 proxy.
- project-level `19_HANDOFF_ASSETS/git_previews/` و `proxy_manifest.json` به‌عنوان visual memory بین chatها.

### Changed
- Storage mode پیش‌فرض media غیرحساس از metadata-only به `git_previews` تغییر کرد؛ original/full-resolution همچنان خارج Git معمولی می‌ماند.
- `.gitignore` فقط WebP/MP4های مسیر استاندارد `19_HANDOFF_ASSETS/git_previews/` را re-include می‌کند و binaryهای دیگر را همچنان ignore نگه می‌دارد.
- default image proxy: long edge≤1280، WebP quality≈72، metadata stripped.
- default video proxy: MP4/H.264، long edge≤1280، ≈24fps، CRF≈30، AAC≈96kbps.
- `AGENTS.md` و `AI_START_HERE.md` اکنون proxy generation/manifest/commit را بخشی از cross-chat persistence می‌دانند.
- project template و P0001 media-storage metadata به `git_previews` ارتقا یافتند.

### Safety / privacy
- repository ممکن است public باشد؛ low-resolution media همچنان public است و کاهش کیفیت privacy control محسوب نمی‌شود.
- sensitive/client/confidential یا `do_not_publish` media باید metadata-only بماند مگر user storage/private-repo policy دیگری تعیین کند.

### Backfill
- media تاریخی P0001 به‌صورت خودکار backfill نشده است چون binaryهای اصلی در Git موجود نیستند. هنگام دسترسی/reattach شدن sourceها می‌توان proxyهای تاریخی را تولید و manifest را تکمیل کرد.

## 1.2.0 — 2026-08-08
### Added
- `00_SYSTEM/SCENARIO_ARCHITECTURE_SYSTEM.md` برای پیشنهاد adaptive سناریوهای 10/20/30/40 ثانیه‌ای و 1–4 کلیپ.
- `PRM-SCN-ARCH-001_v1.0.0` به‌عنوان candidate prompt برای Scenario Architecture Menu.
- `CHK_SCENARIO_ARCHITECTURE_MENU.md`.
- `SCENARIO_MENU_TEMPLATE.md`.
- `MULTI_CLIP_SEQUENCE_TEMPLATE/MASTER_SEQUENCE.md` و `CLIP_CONTRACT.md`.
- exact new-chat handoff برای ساخت derivative 30s از P0001 در `30S_DERIVATIVE_START.md`.

### Changed
- `MASTER_WORKFLOW` اکنون Scenario Architecture Gate را قبل از production سنگین اجرا می‌کند.
- `SOP_07_SCENARIO_GENERATION` از ایده‌پردازی ثابت به Process State Map + Capacity Assessment + Duration Viability + adaptive menu ارتقا یافت.
- Multi-clip architecture و SOP/checklist به‌صورت صریح 2، 3 و 4 کلیپ / 20، 30 و 40 ثانیه را پوشش می‌دهند.
- Hybrid architecture به‌عنوان default candidate برای بسیاری از sequenceهای چندکلیپی مستند شد، نه الزام.
- reference stack در هر clip باید minimum sufficient و role-clean باشد؛ پرکردن slotها هدف نیست.
- `AI_START_HERE`, `AGENTS.md`, `START_HERE.md` و `INDEX.md` برای routing سناریو/مدت/چندکلیپی به‌روزرسانی شدند.
- Storage Policy صریحاً ثبت می‌کند که ChatGPT attachments خودکار در GitHub ذخیره نمی‌شوند و binary media فعلاً توسط `.gitignore` خارج Git هستند.

### Fixed
- سیستم دیگر فرض نمی‌کند multi-clip فقط 2×10s یا 3×10s است؛ 4×10s نیز با filler guard پشتیبانی می‌شود.
- candidate count دیگر quota ثابت نیست؛ اگر ظرفیت واقعی وجود نداشته باشد گزینه مصنوعی تولید نمی‌شود.
- فرآیند واقعی محصول باید verified/user-confirmed باشد یا به‌صورت creative metaphor برچسب بخورد.

### Learning-derived changes
- P0001 نشان داد referenceهای بیشتر الزاماً scene synthesis بهتری نمی‌دهند و scene-master-derived camera states می‌توانند continuity را بهتر حفظ کنند؛ این یافته‌ها هنوز project/provisional هستند و به‌عنوان rule مطلق global promote نشده‌اند.
- تجربه P0001 نشان داد یک 10s کم‌ریسک برای hero/reveal مناسب است، اما process chain بهتر است در صورت ارزش روایی به چند clip شکسته شود.

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
- هستهٔ AI Video Ad Lab، چرخهٔ 24 مرحله‌ای، SOP/checklist، template، registry و CLI.
### Changed / Deprecated / Fixed / Learning-derived changes
- هنوز موردی ثبت نشده بود.
