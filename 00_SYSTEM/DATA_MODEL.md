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

## Derivative projects
اگر deliverable جدید از پروژه قبلی ساخته می‌شود ولی duration/story/sequence جدید دارد، به‌طور پیش‌فرض پروژه جدید بساز و parent را link کن؛ پروژه قبلی overwrite نشود.

Recommended fields:
- `parent_project_id`
- `derivative_reason`
- `reused_knowledge_paths`
- `reused_asset_ids` فقط وقتی media واقعاً در دسترس و role مناسب است.

مثال: P0002 یک 30s derivative از P0001 است ولی Run/Scenario/Final مستقل دارد.

## Multi-clip / sequence model

برای deliverable چندکلیپی:
- `sequence_id`: مثال `P0002-S01`
- `clip_id`: مثال `P0002-C01` تا `P0002-C04`
- `clip_count`: 2 / 3 / 4
- `architecture_mode`: `continuous_world` / `hybrid` / `editorial_sequence`
- `master_sequence_path`
- `boundary_contracts`
- `selected_run_per_clip`
- `assembled_final_path` یا metadata

Run ID همچنان project-global است:
`P0002-R0017` می‌تواند `clip_id=P0002-C02` داشته باشد.

### Recommended run fields for multi-clip
- `sequence_id`
- `clip_id`
- `clip_role`
- `boundary_role`: start / middle / end / none

## Scenario architecture records
قبل از انتخاب سناریو در پروژه‌های مناسب ثبت شود:
- `process_state_map_path`
- `scenario_capacity_assessment_path`
- `scenario_menu_path`
- `selected_scenario_id`
- `selected_duration_seconds`
- `selected_clip_count`
- `selected_architecture_mode`

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
- `boundary_start_state`
- `boundary_end_state`

style-only هیچ‌گاه identity محصول را بازتعریف نمی‌کند.

## Media provenance
اگر binary داخل Git نیست، record باید تا حد امکان شامل این موارد باشد:
- filename/path یا external location description؛
- role؛
- originating Run؛
- hash وقتی قابل محاسبه است؛
- whether re-attach may be required in a new chat.

Chat attachment به‌خودی‌خود به معنی media storage در repo نیست.

## Final selection
`selected_final_run` فقط باید Run موجود و ارزیابی‌شده باشد. failed/obsolete Runs حذف نمی‌شوند.

برای multi-clip:
- هر clip باید selected final Run مستقل داشته باشد؛
- assembled master نیز final selection/QA مستقل دارد.
