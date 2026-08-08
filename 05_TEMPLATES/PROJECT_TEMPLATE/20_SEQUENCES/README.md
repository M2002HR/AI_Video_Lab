# 20_SEQUENCES

این folder فقط برای پروژه‌های multi-clip استفاده می‌شود.

برای هر sequence یک folder مانند `P0002-S01/` بساز و از templateهای زیر copy کن:
- `05_TEMPLATES/MULTI_CLIP_SEQUENCE_TEMPLATE/MASTER_SEQUENCE.md`
- `05_TEMPLATES/MULTI_CLIP_SEQUENCE_TEMPLATE/CLIP_CONTRACT.md`

Suggested structure:

```text
20_SEQUENCES/
└── P0002-S01/
    ├── MASTER_SEQUENCE.md
    ├── sequence.json
    ├── C01/
    │   └── CLIP_CONTRACT.md
    ├── C02/
    │   └── CLIP_CONTRACT.md
    ├── C03/              # optional
    │   └── CLIP_CONTRACT.md
    ├── C04/              # optional
    │   └── CLIP_CONTRACT.md
    ├── boundaries/
    ├── assembly/
    └── SEQUENCE_QA.md
```

Runها همچنان در project `12_RUNS/` می‌مانند و با `sequence_id` + `clip_id` link می‌شوند تا registry تکه‌تکه نشود.
