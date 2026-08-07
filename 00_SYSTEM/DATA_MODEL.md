# DATA MODEL

project.json، run.json و prompt front matter متادیتای حقیقت‌اند. JSON UTF-8 معتبر؛ unknown یا null به‌جای حدس. reference_assets مسیر نسبی+role دارد. selected_final_run باید Run موجود با evaluation باشد؛ CSV editable نیست.

## نقش رفرنس

roleهای مجاز: product_identity_primary، product_identity_secondary، geometry_view، texture_detail، packaging، style_only، lighting_only، scene_only، composition_only، character_only، start_frame و end_frame. style-only هیچ‌گاه identity محصول را بازتعریف نمی‌کند.
