# DATA MODEL

## Source of truth
- `project.json`: project-level machine state.
- `run.json`: provenance هر اجرای AI.
- prompt metadata/front matter: prompt identity/version/status.
- Markdownهای analysis/evaluation/decision/handoff: human-readable evidence and context.
- CSVهای `10_REGISTRY/`: generated views، نه فایل editable دستی.

JSON باید UTF-8 معتبر باشد. مقدار نامعلوم `unknown` یا `null` است، نه حدس.

## Project continuity fields
هر project علاوه بر stage/state باید این context را داشته باشد:
- `STATUS.md`: وضعیت عملیاتی کوتاه.
- `HANDOFF.md`: خلاصه کامل برای AI/session بعدی.
- `18_CONVERSATION_LOG/`: feedback و session summaryهای ارزشمند.
- `19_HANDOFF_ASSETS/`: preview اختیاری برای continuity طبق Storage Policy.

`HANDOFF.md` source detail را duplicate نمی‌کند؛ به fileهای authoritative link می‌دهد.

## Reference roles
roleهای استاندارد:
- `product_identity_primary`
- `product_identity_secondary`
- `geometry_view`
- `texture_detail`
- `packaging`
- `style_only`
- `lighting_only`
- `scene_only`
- `composition_only`
- `character_only`
- `start_frame`
- `end_frame`

style-only هیچ‌گاه identity محصول را بازتعریف نمی‌کند.

## Media provenance
اگر binary داخل Git نیست، record باید تا حد امکان شامل این موارد باشد:
- filename/path یا external location description؛
- role؛
- originating Run؛
- hash وقتی قابل محاسبه است؛
- whether re-attach may be required in a new chat.

## Final selection
`selected_final_run` فقط باید Run موجود و ارزیابی‌شده باشد. failed/obsolete Runs حذف نمی‌شوند.
