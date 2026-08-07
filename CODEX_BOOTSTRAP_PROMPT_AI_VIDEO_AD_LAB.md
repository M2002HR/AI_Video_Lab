# CODEX BOOTSTRAP PROMPT — AI Video Ad Lab / Prompt Improvement OS

> **How to use this file:**  
> Create a new empty folder for this system, open that folder as the Codex working repository, and give Codex this entire file as the initial task.  
> Codex must **execute** the bootstrap, not merely propose a plan.  
> After bootstrap is complete, this repository becomes the durable source of truth and the user should be able to continue working by speaking naturally with Codex.

---

# 0. YOUR ROLE

You are the **architect, maintainer, operator, documentarian, experiment manager, and prompt-optimization agent** for a version-controlled AI advertising production system.

The system is called:

**AI Video Ad Lab**

Its purpose is to turn a small set of starting inputs—typically:

1. one or more product images,
2. an existing/template/reference prompt,
3. optional creative/style references,
4. optional user constraints,

into a highly systematic production pipeline for creating short AI-generated advertising images and videos.

The system must support, document, and continuously improve workflows involving:

- source prompt analysis,
- product image analysis,
- product identity specification,
- reference asset preparation,
- background removal / cleanup planning,
- multi-view product image generation,
- product consistency evaluation,
- scene/style reference preparation,
- creative direction,
- scenario generation,
- scenario critique and selection,
- shot design,
- timing design,
- storyboard generation,
- keyframe generation,
- keyframe consistency checks,
- image prompting,
- video prompting,
- image-to-video prompting,
- reference/ingredient prompting,
- video generation,
- generation logging,
- visual QA,
- frame-by-frame QA,
- failure classification,
- repair/regeneration decisions,
- final selection,
- post-production handoff,
- final QA,
- postmortem,
- experiments,
- tool/model comparisons,
- prompt comparisons,
- learning capture,
- SOP improvement,
- checklist improvement,
- prompt library improvement.

The most important long-term output of this system is **not only the final media**.

The most important compounding asset is the system’s growing knowledge of:

- how to write better prompts,
- which prompt structures work for which AI tasks,
- what details should always be included,
- what mistakes cause failures,
- which models/tools are best for which jobs,
- how to preserve product identity,
- how to reduce visual artifacts,
- how to improve realism and continuity,
- how to structure scenarios for generative video,
- how to evaluate generations consistently,
- how to learn from failed runs,
- how to improve the next project.

Treat this as a **production system + R&D lab + prompt engineering knowledge base**.

---

# 1. PRIMARY BOOTSTRAP OBJECTIVE

Inside the current folder, build a complete **version-controlled, local-first repository** that can be used as the permanent operating system for AI-generated product advertising.

**Treat the current working directory itself as the repository root. Do not create a second nested `AI_VIDEO_AD_LAB/` directory inside it.** The tree shown below is conceptual: its top line represents the current working directory.

Preserve this bootstrap prompt file. After bootstrap, `AGENTS.md` and the repository documentation become the operational source of truth; this bootstrap file remains historical setup documentation.

Do not merely create empty folders.

Create a useful **v1.0 working system** with:

- a clear repository structure,
- substantive documentation,
- permanent Codex instructions,
- master workflow,
- SOPs,
- prompt engineering standards,
- prompt templates,
- prompt library structure,
- tool knowledge structure,
- checklists,
- scoring rubrics,
- failure taxonomy,
- project templates,
- experiment templates,
- benchmark structure,
- learning loop,
- change/promotion rules,
- metadata schemas,
- registries,
- lightweight automation scripts,
- validation tooling,
- user-facing documentation,
- examples,
- a system dashboard,
- Git setup,
- storage policy,
- changelog,
- version file.

The repository should be usable immediately after bootstrap.

---

# 2. NON-NEGOTIABLE DESIGN PRINCIPLES

These principles must be encoded into the repository documentation and into `AGENTS.md`.

## 2.1 The repository is the memory

Do not depend on chat history as the durable memory of the system.

Anything important must be written into version-controlled files.

Chat is an interface.

The repository is the source of truth.

---

## 2.2 Preserve evidence

Never overwrite or silently replace:

- original user inputs,
- original product images,
- original prompts,
- historical prompt versions,
- historical generations,
- historical evaluations,
- failed runs,
- experiment results,
- old system versions.

Create new versions instead.

If an item is deprecated, move or mark it as deprecated; do not erase history unless the user explicitly requests deletion.

---

## 2.3 Every AI output needs provenance

No meaningful AI-generated image, video, scenario, storyboard, keyframe, or prompt should exist without a record of:

- project,
- stage,
- run ID,
- date/time when known,
- task,
- tool,
- model when known,
- prompt ID/version when applicable,
- full prompt used,
- reference assets used,
- settings when known,
- output files,
- evaluation,
- failure tags,
- selection status,
- notes.

If the generation happened outside Codex, make it easy for the user to drop the output into the project and have Codex register it afterward.

---

## 2.4 Separate WHAT from WHICH TOOL

The workflow must describe **what task needs to be performed** independently of the current preferred model/tool.

Example:

Bad system design:

> Generate multi-view product images with Nano Banana.

Better system design:

> Generate product reference views that preserve product identity.

Then Tool Knowledge may currently say:

> Preferred tool: Nano Banana, based on current evidence.

This makes the system resilient to changing models.

---

## 2.5 Prompt improvement is a first-class subsystem

Prompts must not be treated as disposable text.

Prompts are versioned production assets.

Every important prompt needs:

- stable prompt ID,
- version,
- status,
- purpose,
- supported task,
- expected inputs,
- variables,
- complete prompt body,
- expected output,
- tool/model scope,
- known failure modes,
- evaluation history,
- evidence links,
- change history.

---

## 2.6 Feedback does not automatically become truth

The user may say:

> ChatGPT Image did badly here; Nano Banana was better.

Capture this as an **observation**.

Do not immediately convert it into a global permanent rule.

Use the progression:

**Observation → Hypothesis → Controlled Experiment → Evidence → Validated Learning → System Change**

A single observation can justify a local project decision.

It should normally not justify a universal SOP change unless the evidence is unusually clear and the rule is narrow.

---

## 2.7 Make the system easy to use

The user should not need to remember file paths, IDs, registry schemas, or every checklist.

Codex should handle system bookkeeping whenever possible.

The user should be able to say things like:

- «یه پروژه جدید برای این محصول بساز»
- «این عکس‌ها و پرامپت ورودی پروژه هستن»
- «این خروجی Nano Banana بهتر شد، ثبتش کن»
- «این دو ویدیو رو مقایسه کن»
- «از این شکست چی یاد گرفتیم؟»
- «بهترین پرامپت فعلی برای product multiview رو بده»
- «برای مرحله بعد prompt package بساز»
- «این پروژه رو postmortem کن»
- «این نکته رو به سیستم اضافه کن، ولی اول ببین شواهد کافی داریم یا نه»

Codex should translate natural-language intent into repository operations.

---

## 2.8 Ask only necessary questions

Prefer making safe, reversible, documented choices.

Ask the user only when:

- a critical creative decision is ambiguous,
- a destructive action is requested,
- a permanent system standard would materially change,
- a required input truly cannot be inferred,
- two mutually exclusive choices have major consequences.

Do not turn the workflow into a questionnaire if Codex can make a sensible draft and mark assumptions.

---

## 2.9 Prefer simple, inspectable infrastructure

For v1.0, prefer:

- Markdown for human-readable documentation,
- JSON for machine-readable metadata,
- CSV for generated overview registries,
- Python standard library for automation,
- Git for text/version history.

Do not introduce a database, web app, Docker stack, complex framework, vector database, or external dependency unless it provides clear immediate value.

Design the repository so SQLite, DVC, Git LFS, cloud storage, dashboards, or automation can be added later without restructuring the core knowledge model.

---

## 2.10 Documentation language and prompt language

Default human-facing documentation and Codex conversational summaries to **Persian**.

Use **English file names, directory names, IDs, machine-readable keys, code, and schemas**.

For image/video generation prompts, use English by default unless:

- the target tool performs demonstrably better with another language,
- the user requests another language,
- text inside the generated creative requires a specific language.

Record the prompt language in metadata.

---

# 3. REQUIRED ROOT STRUCTURE

Create this structure, adapting only if there is a strong technical reason:

```text
AI_VIDEO_AD_LAB/
├── AGENTS.md
├── README.md
├── START_HERE.md
├── DASHBOARD.md
├── CHANGELOG.md
├── VERSION
├── .gitignore
│
├── 00_SYSTEM/
├── 01_SOPS/
├── 02_PROMPT_SYSTEM/
├── 03_TOOL_KNOWLEDGE/
├── 04_CHECKLISTS/
├── 05_TEMPLATES/
├── 06_PROJECTS/
├── 07_EXPERIMENTS/
├── 08_BENCHMARKS/
├── 09_LEARNING/
├── 10_REGISTRY/
├── 11_TOOLS/
├── 12_REPORTS/
├── 13_EXAMPLES/
└── 99_ARCHIVE/
```

Keep `AGENTS.md` concise and navigational.

Do not turn `AGENTS.md` into the entire encyclopedia.

The deeper durable knowledge should live in the structured documentation folders.

---

# 4. ROOT FILE REQUIREMENTS

## 4.1 `README.md`

Explain:

- what the system is,
- what problem it solves,
- overall architecture,
- main concepts,
- how projects, runs, prompts, experiments, and learnings relate,
- local-first design,
- versioning philosophy,
- where media is stored,
- how Codex is expected to operate.

---

## 4.2 `START_HERE.md`

This is the most user-friendly file.

It must explain in Persian:

### For a new user:
1. how to start a project,
2. where to place source images,
3. where to place a source/template prompt,
4. how to tell Codex to register them,
5. how to request the next stage,
6. how to register external AI outputs,
7. how to compare runs,
8. how to submit feedback,
9. how to finish a project,
10. how the system learns.

Include example messages the user can copy/paste to Codex.

Also include a compact “common actions” section such as:

```text
شروع پروژه:
«برای محصول X یک پروژه جدید بساز.»

ثبت ورودی:
«این فایل‌ها ورودی اصلی پروژه هستند. ثبتشان کن و مرحله Intake را اجرا کن.»

ادامه پروژه:
«وضعیت پروژه را بررسی کن و مرحله منطقی بعدی را انجام بده.»

ثبت Run خارجی:
«این خروجی را با ابزار X و مدل Y ساختم. prompt و referenceهایش این‌ها بودند. به عنوان Run ثبتش کن.»

مقایسه:
«Run 003 و Run 006 را بر اساس rubric سیستم مقایسه کن.»

یادگیری:
«این نکته را به عنوان feedback ثبت کن و تعیین کن observation است یا شواهد کافی برای تغییر استاندارد داریم.»

Prompt:
«بهترین prompt تاییدشده فعلی برای [task] را بده و برای این پروژه instantiate کن.»
```

---

## 4.3 `DASHBOARD.md`

Create a human-readable dashboard with:

- system version,
- active projects,
- project current stages,
- pending approvals,
- open experiments,
- prompt candidates awaiting validation,
- recent validated learnings,
- pending system change proposals,
- recent failures by category,
- next recommended actions.

In v1.0 this can be generated/updated by script and Codex.

---

## 4.4 `VERSION`

Start with:

```text
1.0.0
```

---

## 4.5 `CHANGELOG.md`

Use a clear format with sections for:

- Added
- Changed
- Deprecated
- Fixed
- Learning-derived changes

Every promoted system-level change should eventually appear here.

---

# 5. `AGENTS.md` — PERMANENT CODEX OPERATING RULES

Create a concise root `AGENTS.md` that tells future Codex sessions:

1. This repository is the durable source of truth.
2. Read `START_HERE.md` for user experience and `00_SYSTEM/INDEX.md` for system documentation.
3. Before modifying a workflow, prompt standard, checklist, or tool recommendation, inspect relevant evidence and learning files.
4. Never overwrite original inputs or historical prompt/run files.
5. Every meaningful AI generation must be traceable to a Run record.
6. Every canonical prompt modification must be versioned.
7. A single anecdote is normally an observation, not a validated global rule.
8. Prefer reversible changes.
9. Keep machine-readable metadata synchronized.
10. Rebuild registries after creating or changing projects/runs/prompts/experiments.
11. Run repository validation before declaring major work complete.
12. Do not fabricate tool capabilities. If a capability cannot be verified, mark it unknown/unverified.
13. Do not claim external AI media was generated unless the actual tool was used or the user supplied the result.
14. Keep responses to the user concise and operational:
   - what you did,
   - key finding,
   - files created/changed,
   - current stage,
   - next recommended action,
   - any decision needed.
15. Default conversational language: Persian.
16. Default generation-prompt language: English, unless project/tool evidence says otherwise.
17. Do not push to a remote Git repository or delete media without explicit user request.
18. Use relative repository paths in documentation whenever practical.
19. Preserve failed runs because they are evidence.
20. If the system itself becomes inconsistent, repair documentation/data integrity before adding more automation.

Add links to deeper documents rather than duplicating them.

---

# 6. `00_SYSTEM/` — CORE SYSTEM DOCUMENTATION

Create substantive files, not placeholders:

```text
00_SYSTEM/
├── INDEX.md
├── ARCHITECTURE.md
├── MASTER_WORKFLOW.md
├── CORE_PRINCIPLES.md
├── QUALITY_STANDARD.md
├── NAMING_AND_IDS.md
├── VERSIONING_POLICY.md
├── STORAGE_POLICY.md
├── DATA_MODEL.md
├── EVIDENCE_POLICY.md
├── LEARNING_LOOP.md
├── CHANGE_PROMOTION_POLICY.md
├── FAILURE_TAXONOMY.md
├── EVALUATION_SYSTEM.md
├── CODEX_OPERATING_MANUAL.md
├── PROJECT_LIFECYCLE.md
├── GLOSSARY.md
└── DECISION_LOG.md
```

## `MASTER_WORKFLOW.md`

Define an initial v1 workflow with explicit stages and quality gates.

Use approximately this lifecycle:

### Stage 00 — Project Intake
- create project,
- define deliverable,
- preserve original inputs,
- identify missing information,
- record assumptions.

### Stage 01 — Source Prompt Analysis
- preserve original prompt,
- reverse-engineer structure,
- separate generalizable prompt DNA from old-product-specific content,
- classify sections as KEEP / ADAPT / REMOVE,
- identify contradictions,
- identify hidden assumptions,
- extract camera grammar, lighting grammar, timing grammar, style grammar, scale logic, character logic, physics rules, audio rules, negative constraints.

### Stage 02 — Product Analysis & Identity Specification
- analyze the original product image(s),
- define exact product category,
- geometry,
- proportions,
- materials,
- texture,
- colors,
- surface characteristics,
- packaging,
- labels/logos/text,
- component count,
- acceptable imperfections,
- forbidden transformations,
- identity-critical features,
- confidence/uncertainty.

### Stage 03 — Reference Strategy
Decide:
- whether original image is sufficient,
- whether cleanup is needed,
- whether background removal is needed,
- which additional angles are needed,
- whether a packaging reference should be separate,
- whether macro texture references are needed,
- whether scene/style references are needed,
- which references should be used only for product identity versus only for style.

### Stage 04 — Reference Asset Creation
Possible tasks:
- cleanup,
- segmentation,
- additional product views,
- macro detail views,
- neutral-background references,
- scene references,
- style references.

Every generated reference must have its own Run and QA.

### Stage 05 — Reference Consistency Gate
Before scenario/video work:
- compare generated references against original product,
- reject identity drift,
- approve only reliable references,
- create an approved reference set.

### Stage 06 — Creative Direction
Define:
- campaign idea,
- emotional target,
- visual metaphor,
- premium level,
- realism level,
- scale,
- environment,
- character use if any,
- camera language,
- lighting,
- visual rhythm,
- brand/product priority.

### Stage 07 — Scenario Generation
Generate multiple scenarios.

Each scenario must include:
- premise,
- 10-second timeline,
- product role,
- shot complexity,
- required references,
- required AI capabilities,
- likely failure modes,
- difficulty/risk score.

### Stage 08 — Scenario Critique & Selection
Evaluate scenarios for:
- product focus,
- clarity,
- feasibility,
- visual impact,
- realism,
- temporal complexity,
- generative-video risk,
- identity risk,
- commercial usefulness,
- brand fit.

### Stage 09 — Shot & Timing Design
Convert selected scenario into:
- temporal beats,
- camera framing,
- camera movement,
- action sequence,
- continuity constraints,
- final hero shot,
- audio/SFX plan if needed.

### Stage 10 — Storyboard
Generate storyboard plan and/or storyboard images.

### Stage 11 — Storyboard QA
Check:
- narrative continuity,
- product consistency,
- action feasibility,
- composition,
- timing,
- accidental complexity.

### Stage 12 — Keyframe Generation
Generate only the keyframes needed to control the video.

### Stage 13 — Keyframe Identity & Continuity Gate
Check:
- product identity,
- geometry,
- texture,
- color,
- packaging,
- scale,
- scene continuity,
- lighting continuity,
- character continuity.

### Stage 14 — Final Video Prompt Synthesis
Build the tool-specific video prompt package from:
- product identity,
- approved references,
- scenario,
- shot design,
- timing,
- physics,
- camera,
- lighting,
- failure prevention rules.

### Stage 15 — Video Preflight
Ensure:
- no contradictions,
- reference roles are explicit,
- product identity is locked,
- timing is realistic,
- action complexity is bounded,
- camera motion is not over-specified,
- final frame is defined,
- known failure modes are addressed.

### Stage 16 — Video Generation
Create tracked Runs.

### Stage 17 — Video QA
Inspect:
- frame-by-frame product identity,
- morphing,
- object counts,
- hands/characters,
- physics,
- contact continuity,
- gravity,
- scale,
- camera,
- lighting,
- background stability,
- text/logo corruption,
- temporal continuity,
- final hero shot.

### Stage 18 — Repair vs Regenerate Decision
Classify failure:
- local/cosmetic,
- structural,
- identity,
- continuity,
- prompt,
- reference,
- tool limitation.

Choose:
- edit,
- targeted repair,
- prompt revision,
- reference revision,
- scenario simplification,
- full regeneration.

### Stage 19 — Final Selection
Select best generation using standardized evaluation.

### Stage 20 — Post-production
Track:
- edit,
- trim,
- color,
- text/logo overlay,
- audio,
- compositing,
- delivery format.

### Stage 21 — Final QA
Verify deliverable against brief and commercial requirements.

### Stage 22 — Project Postmortem
Record:
- what worked,
- what failed,
- best prompt decisions,
- best tool decisions,
- wasted attempts,
- recurring failures,
- suggested experiments,
- proposed checklist/SOP/prompt changes.

### Stage 23 — Learning & System Improvement
Convert project evidence into:
- observations,
- hypotheses,
- experiments,
- validated learnings,
- prompt updates,
- checklist updates,
- tool recommendations,
- SOP revisions.

The workflow must support inserting new stages later without breaking old projects.

Use stable stage IDs.

---

# 7. `01_SOPS/` — STANDARD OPERATING PROCEDURES

Create one detailed SOP per major workflow stage.

At minimum:

```text
01_SOPS/
├── INDEX.md
├── SOP_00_PROJECT_INTAKE.md
├── SOP_01_SOURCE_PROMPT_ANALYSIS.md
├── SOP_02_PRODUCT_IDENTITY.md
├── SOP_03_REFERENCE_STRATEGY.md
├── SOP_04_REFERENCE_GENERATION.md
├── SOP_05_REFERENCE_QA.md
├── SOP_06_CREATIVE_DIRECTION.md
├── SOP_07_SCENARIO_GENERATION.md
├── SOP_08_SCENARIO_SELECTION.md
├── SOP_09_SHOT_TIMING.md
├── SOP_10_STORYBOARD.md
├── SOP_11_STORYBOARD_QA.md
├── SOP_12_KEYFRAME_GENERATION.md
├── SOP_13_KEYFRAME_QA.md
├── SOP_14_VIDEO_PROMPT.md
├── SOP_15_VIDEO_PREFLIGHT.md
├── SOP_16_VIDEO_GENERATION.md
├── SOP_17_VIDEO_QA.md
├── SOP_18_REPAIR_DECISION.md
├── SOP_19_FINAL_SELECTION.md
├── SOP_20_POST_PRODUCTION.md
├── SOP_21_FINAL_QA.md
├── SOP_22_POSTMORTEM.md
└── SOP_23_SYSTEM_LEARNING.md
```

Each SOP must include:

- objective,
- required inputs,
- optional inputs,
- outputs,
- prerequisite gate,
- detailed procedure,
- AI tasks involved,
- relevant canonical prompts,
- relevant tool knowledge,
- checklist,
- pass/fail criteria,
- common failures,
- escalation rules,
- what metadata must be recorded,
- what files are created,
- definition of done.

Avoid vague advice.

Make each SOP operational.

---

# 8. `02_PROMPT_SYSTEM/` — THE CORE PROMPT-IMPROVEMENT ENGINE

This is one of the most important parts of the repository.

Create:

```text
02_PROMPT_SYSTEM/
├── INDEX.md
├── PROMPT_ENGINEERING_STANDARD.md
├── PROMPT_VERSIONING.md
├── PROMPT_EVALUATION.md
├── VARIABLE_CONVENTIONS.md
├── PROMPT_CHANGE_POLICY.md
├── registry/
│   └── prompt_registry.json
├── standards/
│   ├── GENERAL_AI_PROMPTING.md
│   ├── SOURCE_PROMPT_ANALYSIS_PROMPTING.md
│   ├── PRODUCT_ANALYSIS_PROMPTING.md
│   ├── IMAGE_GENERATION_PROMPTING.md
│   ├── PRODUCT_MULTIVIEW_PROMPTING.md
│   ├── SCENE_REFERENCE_PROMPTING.md
│   ├── SCENARIO_PROMPTING.md
│   ├── STORYBOARD_PROMPTING.md
│   ├── KEYFRAME_PROMPTING.md
│   ├── VIDEO_PROMPTING.md
│   ├── VIDEO_REPAIR_PROMPTING.md
│   ├── CRITIQUE_PROMPTING.md
│   └── POSTMORTEM_PROMPTING.md
├── library/
├── candidates/
└── deprecated/
```

## 8.1 Prompt Library philosophy

Canonical prompts are reusable production assets.

Create initial canonical prompt families for at least:

**These initial prompts must be substantial, production-oriented v1.0 templates—not one-paragraph placeholders.** They should be detailed enough to use in a real first project, while still being parameterized and easy to revise from evidence.

- source prompt reverse engineering,
- product image analysis,
- product identity specification,
- product reference planning,
- product multi-view image generation,
- product reference QA,
- creative direction generation,
- scenario ideation,
- scenario critique,
- scenario selection,
- storyboard specification,
- storyboard image generation,
- keyframe generation,
- keyframe QA,
- video prompt synthesis,
- video prompt critique,
- video preflight,
- generation evaluation,
- failure diagnosis,
- repair prompt generation,
- postmortem,
- learning extraction,
- experiment design.

Do not assume one giant prompt should do everything.

Prefer modular prompts with clear task boundaries.

---

## 8.2 Prompt IDs

Define a stable convention such as:

```text
PRM-ANL-SOURCE-001
PRM-ANL-PRODUCT-001
PRM-IMG-MULTIVIEW-001
PRM-IMG-KEYFRAME-001
PRM-SCN-IDEATE-001
PRM-SCN-CRITIQUE-001
PRM-VID-SYNTH-001
PRM-VID-QA-001
PRM-LRN-POSTMORTEM-001
```

Document the convention.

---

## 8.3 Prompt versions

Use semantic-like versions:

```text
1.0.0
1.1.0
1.1.1
2.0.0
```

Define:

- **MAJOR**: changes task contract, output structure, or fundamental strategy.
- **MINOR**: meaningful behavior/quality improvement while preserving task contract.
- **PATCH**: wording/clarity/format fix not expected to materially change strategy.

Never overwrite a historical prompt version.

---

## 8.4 Prompt status

Use:

- `draft`
- `candidate`
- `validated`
- `deprecated`

Only `validated` prompts should be considered canonical defaults.

A new improved version begins as `candidate` unless it is merely a patch-level documentation correction.

---

## 8.5 Prompt file structure

Every canonical/candidate prompt file should include metadata and these sections:

```text
Prompt ID
Version
Status
Task
Purpose
Language
Tool scope
Model scope
Inputs
Required variables
Optional variables
Expected output
Known failure modes
Evidence
Tested projects/benchmarks
Prompt body
Usage notes
Evaluation notes
Changelog
```

Use a consistent format.

If Markdown front matter is used, ensure the same fields are also understandable to humans.

---

## 8.6 Prompt variables

Use explicit variables such as:

```text
{{PRODUCT_NAME}}
{{PRODUCT_CATEGORY}}
{{PRODUCT_IDENTITY_SPEC}}
{{SOURCE_PROMPT}}
{{REFERENCE_ASSET_LIST}}
{{CREATIVE_DIRECTION}}
{{SCENARIO}}
{{SHOT_TIMELINE}}
{{TOOL_NAME}}
{{MODEL_NAME}}
{{DURATION}}
{{ASPECT_RATIO}}
```

Do not embed project-specific values inside canonical prompt templates.

---

## 8.7 Base logic vs tool adapters

Where tool-specific syntax or behavior matters, separate:

- reusable task logic,
- tool/model-specific adapter instructions.

Example concept:

```text
PRM-IMG-MULTIVIEW-001/
├── base_prompt_v1.2.0.md
└── adapters/
    ├── nano_banana.md
    ├── chatgpt_image.md
    └── other_tool.md
```

Do this only where it improves maintainability; avoid unnecessary fragmentation.

---

## 8.8 Prompt change evidence

Every meaningful prompt improvement should answer:

- what problem was observed?
- in which runs?
- what hypothesis explains it?
- what prompt change was made?
- what stayed constant?
- how was it tested?
- did metrics improve?
- did new regressions appear?
- should this become the default?

Link prompt changes to observation, experiment, and learning IDs.

---

# 9. `03_TOOL_KNOWLEDGE/` — CURRENT TOOL/MODEL KNOWLEDGE

Create:

```text
03_TOOL_KNOWLEDGE/
├── INDEX.md
├── TOOL_EVALUATION_STANDARD.md
├── TOOL_RECOMMENDATION_POLICY.md
├── registry/
│   └── tool_registry.json
├── image_generation/
├── video_generation/
├── language_reasoning/
├── editing/
└── post_production/
```

Create initial tool-card templates.

Create cards for the tools explicitly relevant to this workflow if appropriate, including currently mentioned tools such as:

- Google Flow / relevant Google video models,
- Nano Banana / relevant Google image model naming when verified,
- ChatGPT image generation,
- ChatGPT/Codex for analysis, prompt work, scenario work.

However:

**Do not fabricate current capabilities.**

If internet access is available, prefer official documentation and record:

- source,
- URL,
- `last_verified`,
- capability confidence.

If verification is unavailable, mark fields as:

```text
verification_status: unverified
```

A tool card should document:

- tool ID,
- tool/model name,
- category,
- current status,
- last verified date,
- official references,
- supported tasks,
- strengths observed in our projects,
- weaknesses observed,
- known failure patterns,
- prompt behavior,
- reference-image behavior,
- output constraints,
- best-practice notes,
- preferred tasks,
- tasks where it should not currently be default,
- evidence IDs,
- experiments,
- recommendation confidence.

Tool recommendations must be evidence-based and revisable.

---

# 10. `04_CHECKLISTS/` — NOTHING IMPORTANT SHOULD BE FORGOTTEN

Create detailed checklists.

At minimum:

```text
04_CHECKLISTS/
├── INDEX.md
├── CHK_PROJECT_INTAKE.md
├── CHK_SOURCE_PROMPT_ANALYSIS.md
├── CHK_PRODUCT_IDENTITY.md
├── CHK_REFERENCE_PLAN.md
├── CHK_REFERENCE_IMAGE_QA.md
├── CHK_CREATIVE_DIRECTION.md
├── CHK_SCENARIO_QA.md
├── CHK_STORYBOARD_QA.md
├── CHK_KEYFRAME_QA.md
├── CHK_IMAGE_PROMPT_PREFLIGHT.md
├── CHK_VIDEO_PROMPT_PREFLIGHT.md
├── CHK_VIDEO_FRAME_BY_FRAME_QA.md
├── CHK_REPAIR_DECISION.md
├── CHK_FINAL_DELIVERY.md
├── CHK_POSTMORTEM.md
└── CHK_SYSTEM_CHANGE.md
```

Each checklist must be version-aware and updateable.

Where useful, distinguish:

- required,
- conditional,
- not applicable.

Include clear pass/fail gates.

---

# 11. QUALITY RUBRICS AND SCORING

Create a common 0–5 scale:

- **0 — Catastrophic / unusable**
- **1 — Severe failure**
- **2 — Weak**
- **3 — Acceptable**
- **4 — Strong**
- **5 — Excellent**

Allow `N/A`.

## 11.1 Product reference image rubric

Include:

- product identity,
- geometry/proportions,
- material accuracy,
- texture accuracy,
- color accuracy,
- component count,
- packaging accuracy,
- label/logo fidelity when relevant,
- angle usefulness,
- lighting usefulness,
- background cleanliness,
- artifact severity,
- reference usability.

---

## 11.2 Scenario rubric

Include:

- product focus,
- commercial clarity,
- visual impact,
- originality,
- brand fit,
- 10-second pacing,
- generative feasibility,
- number of simultaneous actions,
- identity risk,
- physics risk,
- character risk,
- camera complexity,
- reference requirements,
- final hero-shot quality.

---

## 11.3 Keyframe rubric

Include:

- product identity,
- visual composition,
- scenario alignment,
- scene continuity,
- scale continuity,
- lighting continuity,
- character continuity,
- usefulness as a generation reference,
- artifact severity.

---

## 11.4 Video rubric

Include:

- product identity stability,
- prompt adherence,
- temporal continuity,
- geometry stability,
- object-count stability,
- physics,
- contact continuity,
- realism,
- material realism,
- character anatomy if applicable,
- camera quality,
- camera continuity,
- lighting continuity,
- background stability,
- text/logo integrity if applicable,
- visual artifacts,
- final hero frame,
- commercial usefulness.

Create weighted default scoring but allow project-specific weights.

Make **product identity** one of the highest-weight criteria for product advertising.

---

# 12. FAILURE TAXONOMY

Create stable failure IDs.

Include at least categories for:

## Product / identity
- product_identity_drift
- wrong_product_category
- geometry_morphing
- proportion_drift
- texture_drift
- color_drift
- packaging_drift
- component_count_error
- logo_corruption
- text_corruption

## Temporal
- object_teleportation
- object_duplication
- object_disappearance
- scale_instability
- continuity_break
- sudden_pose_change
- temporal_texture_flicker

## Physics / interaction
- bad_contact
- intersecting_geometry
- floating_object
- incorrect_gravity
- impossible_deformation
- liquid_behavior_error
- tool_interaction_error

## Character
- bad_hands
- extra_limbs
- duplicate_character
- character_identity_drift
- clothing_drift
- task_confusion

## Camera
- camera_jump
- unintended_zoom
- unstable_framing
- excessive_camera_motion
- focus_error

## Lighting / scene
- lighting_flicker
- shadow_inconsistency
- background_morph
- reference_contamination
- unwanted_prop
- style_drift

## Prompt / planning
- prompt_contradiction
- underspecified_reference_role
- overcomplex_timeline
- too_many_simultaneous_actions
- ambiguous_subject
- conflicting_camera_instructions
- insufficient_identity_lock

## Tool limitation / operational
- model_capability_limit
- unsupported_setting
- upload/reference_limit
- generation_failure
- unknown_external_factor

Give each failure:

- ID,
- definition,
- symptoms,
- likely causes,
- suggested fixes,
- stages where it usually originates.

---

# 13. `05_TEMPLATES/` — REUSABLE SCAFFOLDS

Create:

```text
05_TEMPLATES/
├── INDEX.md
├── PROJECT_TEMPLATE/
├── RUN_TEMPLATE/
├── PROMPT_TEMPLATE/
├── EXPERIMENT_TEMPLATE/
├── BENCHMARK_TEMPLATE/
├── OBSERVATION_TEMPLATE.md
├── HYPOTHESIS_TEMPLATE.md
├── LEARNING_TEMPLATE.md
├── CHANGE_PROPOSAL_TEMPLATE.md
├── DECISION_RECORD_TEMPLATE.md
├── TOOL_CARD_TEMPLATE.md
└── POSTMORTEM_TEMPLATE.md
```

---

# 14. PROJECT TEMPLATE

Use this project structure:

```text
PROJECT_TEMPLATE/
├── PROJECT_INDEX.md
├── STATUS.md
├── project.json
│
├── 00_BRIEF/
│   └── brief.md
│
├── 01_INPUTS/
│   ├── README.md
│   ├── originals/
│   └── source_prompt/
│
├── 02_SOURCE_ANALYSIS/
│   └── source_prompt_analysis.md
│
├── 03_PRODUCT_IDENTITY/
│   ├── product_identity.md
│   ├── identity_lock.md
│   └── uncertainty_log.md
│
├── 04_REFERENCE_STRATEGY/
│   ├── reference_plan.md
│   └── reference_roles.md
│
├── 05_REFERENCE_ASSETS/
│   ├── original/
│   ├── cleaned/
│   ├── generated/
│   ├── scene/
│   ├── style/
│   └── approved/
│
├── 06_CREATIVE_DIRECTION/
│   └── creative_direction.md
│
├── 07_SCENARIOS/
│   ├── candidates/
│   ├── evaluations/
│   └── selected/
│
├── 08_SHOT_DESIGN/
│   ├── timeline.md
│   ├── camera_plan.md
│   └── continuity_rules.md
│
├── 09_STORYBOARD/
│
├── 10_KEYFRAMES/
│   ├── candidates/
│   └── approved/
│
├── 11_PROMPT_PACKAGES/
│
├── 12_RUNS/
│
├── 13_EVALUATION/
│   ├── comparisons/
│   └── reports/
│
├── 14_REPAIRS/
│
├── 15_FINAL/
│   ├── media/
│   ├── final_metadata.json
│   └── delivery_notes.md
│
├── 16_POSTMORTEM/
│   └── postmortem.md
│
└── 17_LEARNINGS/
    └── project_learning_summary.md
```

## Project status

`STATUS.md` should always make it easy to answer:

- What stage are we at?
- What has been approved?
- What is blocked?
- What is the next action?
- Which prompt package should be used next?
- What files matter right now?

Codex should keep this updated.

---

# 15. PROJECT METADATA

Use JSON for machine-readable metadata.

A project record should support fields similar to:

```json
{
  "project_id": "P0001",
  "slug": "truffle_chocolate",
  "title": "Truffle Chocolate Ad",
  "status": "active",
  "created_at": "ISO-8601",
  "updated_at": "ISO-8601",
  "system_version_started": "1.0.0",
  "current_stage": "STAGE_00",
  "deliverable": {
    "type": "video_ad",
    "duration_seconds": 10,
    "aspect_ratio": "16:9"
  },
  "primary_product_reference": null,
  "source_prompt_path": null,
  "approved_reference_set": [],
  "selected_scenario": null,
  "selected_final_run": null,
  "tags": []
}
```

Use valid JSON and document the schema.

---

# 16. RUN SYSTEM — EVERY GENERATION IS A TRACEABLE EXPERIMENTAL UNIT

Every AI execution/generation should have a Run.

Use IDs such as:

```text
P0001-R0001
P0001-R0002
```

A Run folder should contain:

```text
RUN_TEMPLATE/
├── run.json
├── prompt.md
├── references.md
├── settings.md
├── inputs/
├── outputs/
├── review.md
└── asset_manifest.json
```

Run metadata should support fields like:

```json
{
  "run_id": "P0001-R0001",
  "project_id": "P0001",
  "stage": "STAGE_04",
  "task": "product_multiview_generation",
  "execution_mode": "external_manual",
  "tool": "unknown",
  "model": "unknown",
  "prompt_id": null,
  "prompt_version": null,
  "prompt_language": "en",
  "reference_assets": [],
  "settings": {},
  "outputs": [],
  "evaluation": {
    "status": "pending",
    "overall_score": null
  },
  "failure_tags": [],
  "selected": false,
  "notes": ""
}
```

If the user does not know a field, store `unknown` or `null`.

Do not invent values.

---

# 17. PROMPT PACKAGES — MAKE EXTERNAL TOOL USE EASY

When the user needs to use an external AI tool, Codex should create a self-contained prompt package.

Each package should include:

```text
PKG_<TASK>_<VERSION>/
├── README.md
├── prompt.txt
├── variables_resolved.md
├── references.md
├── recommended_settings.md
├── expected_result.md
├── preflight_checklist.md
└── run_registration_instructions.md
```

The user should be able to:

1. open `prompt.txt`,
2. use the listed references,
3. apply the settings,
4. generate externally,
5. save the output,
6. tell Codex to register it.

This should minimize forgotten details.

---

# 18. `06_PROJECTS/`

Create:

```text
06_PROJECTS/
├── INDEX.md
└── .gitkeep
```

Do not create a fake real project here during bootstrap.

Use `13_EXAMPLES/` for demo material.

---

# 19. `07_EXPERIMENTS/` — CONTROLLED IMPROVEMENT

Create experiment structure and documentation.

Experiment IDs:

```text
EXP-0001
EXP-0002
```

Use the principle:

**change one meaningful variable at a time whenever possible.**

Experiment metadata should include:

- hypothesis,
- motivation,
- linked observations,
- task,
- controlled variables,
- independent variable,
- inputs,
- compared tools/prompts/models,
- evaluation rubric,
- runs,
- result,
- confidence,
- regressions,
- conclusion,
- system-change recommendation.

Examples:

- Nano Banana vs ChatGPT Image for product multi-view identity preservation.
- Prompt v1.2 vs v1.3 for keyframe geometry consistency.
- 3 references vs 5 references for product identity.
- one camera movement vs compound camera movement.
- 3 temporal beats vs 7 temporal beats in 10-second video.
- identity lock wording A vs B.

---

# 20. `08_BENCHMARKS/` — REGRESSION TESTS FOR PROMPTS AND TOOLS

Create:

```text
08_BENCHMARKS/
├── INDEX.md
├── BENCHMARK_POLICY.md
└── suites/
```

Design benchmark suites by difficult visual characteristics, not only product industry.

Possible categories:

- simple_packaging,
- complex_packaging,
- glass_reflective,
- metallic_reflective,
- fabric_softgoods,
- food_irregular_geometry,
- small_repeating_components,
- detailed_labels,
- translucent_material,
- organic_texture,
- complex_multi_part_product.

A benchmark item should preserve:

- original reference,
- task,
- expected constraints,
- evaluation rubric,
- historical results.

Do not require benchmarks before the first real project, but make the system ready.

---

# 21. `09_LEARNING/` — CLOSED LEARNING LOOP

Create:

```text
09_LEARNING/
├── INDEX.md
├── observations/
├── hypotheses/
├── validated_learnings/
├── change_proposals/
└── decisions/
```

Use stable IDs:

```text
OBS-0001
HYP-0001
LRN-0001
CHG-0001
DEC-0001
```

## Learning confidence levels

Use something like:

- `anecdotal`
- `provisional`
- `validated`
- `strongly_validated`

Document criteria.

### Example logic

One failed project:
- observation.

Same pattern across multiple comparable runs:
- provisional learning.

Controlled experiment across representative cases:
- validated learning.

Repeated benchmark/project confirmation with no meaningful regressions:
- strongly validated.

---

# 22. CHANGE PROMOTION POLICY

Codex must not silently rewrite canonical standards.

A system-level change should have:

1. evidence,
2. proposed change,
3. affected files,
4. expected benefit,
5. risk/regression analysis,
6. validation status,
7. decision record,
8. changelog entry.

For low-risk patch corrections, Codex may update directly and document it.

For meaningful changes to:

- master workflow,
- validated prompt,
- scoring rubric,
- global checklist,
- preferred tool,

Codex should create a change proposal and either:
- ask the user for approval, or
- if the user already explicitly instructed the change, execute it while recording the decision.

---

# 23. `10_REGISTRY/` — SEARCHABLE OVERVIEWS

Create generated overview registries for:

- projects,
- runs,
- prompts,
- tools,
- experiments,
- observations,
- validated learnings,
- system changes.

Recommended files:

```text
10_REGISTRY/
├── README.md
├── projects.csv
├── runs.csv
├── prompts.csv
├── tools.csv
├── experiments.csv
├── learnings.csv
└── changes.csv
```

Important:

Per-object JSON/Markdown records are the source of truth.

CSV registries are generated views.

Do not require manual editing of CSV files.

---

# 24. `11_TOOLS/` — LIGHTWEIGHT LOCAL AUTOMATION

Create a standard-library Python CLI, preferably a single entry point:

```text
11_TOOLS/
├── README.md
├── lab.py
└── tests/
```

Use Python standard library unless a dependency is truly justified.

Support commands approximately like:

```bash
python 11_TOOLS/lab.py new-project
python 11_TOOLS/lab.py new-experiment
python 11_TOOLS/lab.py validate
python 11_TOOLS/lab.py rebuild-registry
python 11_TOOLS/lab.py dashboard
python 11_TOOLS/lab.py hash-assets
python 11_TOOLS/lab.py project-status P0001
```

Exact CLI design is up to you, but optimize for reliability and cross-platform use.

## CLI responsibilities

### `new-project`
- allocate next project ID,
- copy project template,
- initialize metadata,
- create status file,
- update registry.

### `new-experiment`
- allocate experiment ID,
- scaffold experiment,
- update registry.

### `validate`
Check:
- required root files,
- project metadata validity,
- duplicate IDs,
- run metadata,
- missing prompt references,
- missing linked files,
- malformed JSON,
- selected runs that do not exist,
- final runs without evaluations,
- canonical prompts without versions,
- registry drift.

Return nonzero exit status on serious integrity problems.

### `rebuild-registry`
Scan source-of-truth metadata and regenerate CSV overviews.

### `dashboard`
Update `DASHBOARD.md`.

### `hash-assets`
Generate SHA-256 manifests for relevant source/output media without altering assets.

### `project-status`
Print a concise project status summary.

Create small tests for critical ID allocation and validation behavior.

---

# 25. MEDIA / STORAGE POLICY

The user wants images and videos to remain in the project for later comparison.

Design for that.

Default v1 policy:

- media files live inside project/experiment folders,
- original and generated media remain locally available,
- large binary media is not necessarily committed to normal Git,
- metadata, prompts, evaluations, manifests, and documentation are committed,
- SHA-256 hashes can prove exactly which asset was used,
- selected lightweight previews may be versioned if useful.

Create `.gitignore` rules that prevent accidental repository bloat while still preserving directory structure.

Do **not** delete or move user media outside the repository without permission.

Document future optional storage modes:

- Git LFS,
- DVC,
- NAS,
- cloud object storage,
- synced cloud folder.

Do not enable any remote storage automatically.

---

# 26. GIT POLICY

If the current folder is not already a Git repository:

- initialize Git,
- create a sensible `.gitignore`,
- add the bootstrap system files.

If Git identity permits, create an initial commit such as:

```text
Initialize AI Video Ad Lab v1.0.0
```

If committing fails because Git identity is not configured, do not block bootstrap.

Report the issue and leave the working tree ready.

Do not create or push to a remote repository unless the user explicitly asks.

---

# 27. `12_REPORTS/`

Create a structure for generated analysis reports:

```text
12_REPORTS/
├── INDEX.md
├── project_comparisons/
├── prompt_performance/
├── tool_performance/
├── failure_analysis/
└── system_health/
```

The system should eventually be able to answer from recorded evidence:

- Which image tool has the best product-identity score?
- Which prompt version has the highest win rate?
- Which video failures are most common?
- Which failure categories consume the most retries?
- Which reference strategy performs best?
- Does more reference imagery actually improve results?
- Which scenario complexity level is most reliable?
- What changes improved output without causing regressions?

Do not invent statistics before sufficient data exists.

---

# 28. `13_EXAMPLES/`

Create one lightweight, fictional text-only demonstration project.

Do not create generated images or videos.

The demo should illustrate:

- a product brief,
- original prompt placeholder,
- product identity document,
- reference plan,
- one scenario,
- one prompt package,
- one fake run metadata file clearly marked as demonstration data,
- one evaluation,
- one observation,
- one hypothetical experiment.

The example exists only to teach the repository structure.

Do not allow demonstration data to pollute real registries or performance statistics.

---

# 29. `99_ARCHIVE/`

Document what belongs here:

- deprecated non-canonical material,
- retired system structures,
- old reports,
- intentionally archived content.

Do not use archive as a substitute for proper version control.

---

# 30. SOURCE PROMPT REVERSE-ENGINEERING STANDARD

Because many projects begin with a prompt found elsewhere, the system must explicitly support this.

The analysis should separate:

## A. Structural prompt DNA
Examples:
- duration,
- aspect ratio,
- camera grammar,
- visual style,
- lighting,
- scale,
- background,
- character concept,
- timeline,
- action cadence,
- physics,
- sound,
- final hero shot.

## B. Source-product-specific content
Examples:
- old product name,
- old ingredients,
- irrelevant actions,
- old packaging,
- old food process,
- scene objects specific to old creative.

## C. Reusable creative concept
Examples:
- miniature workers,
- macro-scale commercial,
- factory metaphor,
- assembly process,
- premium dark studio,
- continuous camera move.

## D. Conflicts and risk
Examples:
- fixed camera + orbit instruction,
- too many actions,
- incompatible scales,
- impossible physics,
- contradictory lighting,
- wrong duration,
- old-product leakage.

Create a KEEP / ADAPT / REMOVE matrix.

The original prompt is immutable.

The adapted prompt must be a new asset with provenance.

---

# 31. PRODUCT IDENTITY SYSTEM

Product identity is critical.

The identity spec should consider:

- exact category,
- silhouette,
- geometry,
- dimensions/proportional relationships,
- materials,
- surface finish,
- roughness/gloss,
- micro-texture,
- color palette,
- color distribution,
- seams,
- edges,
- openings,
- attachments,
- repeated components,
- packaging,
- label position,
- logo position,
- readable text,
- natural irregularities,
- manufacturing imperfections,
- what may vary,
- what may not vary,
- product/reference uncertainty.

Create an explicit `identity_lock.md` that can be injected into image/video prompts.

The system should distinguish:

- identity-critical traits,
- style traits,
- scene traits.

Do not let a style reference redefine the product.

---

# 32. REFERENCE ASSET SYSTEM

Every reference must have an explicit role.

Possible roles:

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

Record reference role in prompt packages and Runs.

The video/image prompt should state the role where useful.

This is meant to reduce reference contamination.

---

# 33. PROMPT WRITING STANDARDS TO DOCUMENT

The initial prompt standards should cover at least:

- task clarity,
- explicit priority hierarchy,
- subject definition,
- product identity lock,
- reference role assignment,
- camera framing,
- camera motion,
- lens/look when useful,
- lighting,
- material behavior,
- environment,
- scale,
- action,
- temporal sequence,
- continuity,
- physics,
- interaction/contact,
- character constraints,
- object count,
- final frame,
- audio/SFX when relevant,
- negative constraints when useful,
- avoiding contradictions,
- reducing simultaneous actions,
- positive scene description,
- not overloading with meaningless technical jargon,
- distinguishing aesthetic language from actual tool settings,
- tool-specific syntax,
- prompt length tradeoffs,
- when to split one prompt into multiple generation stages,
- when to use images rather than more text,
- when to regenerate rather than repair.

These standards must evolve based on evidence.

---

# 34. FEEDBACK CAPTURE PROTOCOL

When the user gives feedback in natural language, Codex should:

1. identify affected project/run/tool/prompt if possible,
2. preserve the raw user feedback,
3. classify it:
   - local correction,
   - observation,
   - hypothesis,
   - direct project preference,
   - possible system improvement,
4. link it to evidence,
5. decide whether:
   - only the current project should change,
   - an experiment should be proposed,
   - a prompt candidate should be created,
   - a checklist should be amended,
   - a validated rule can be promoted,
6. update relevant files,
7. summarize the change to the user.

Example:

User:
> «برای ساخت نماهای مختلف محصول، ChatGPT Image خوب نبود ولی Nano Banana خیلی بهتر بود.»

Desired system behavior:
- save raw feedback,
- create `OBS-xxxx`,
- link compared Runs if available,
- create a hypothesis if evidence is limited,
- recommend a controlled comparison on other products,
- update the project tool choice,
- do **not** automatically declare a universal tool rule.

---

# 35. CODEX BEHAVIOR AFTER BOOTSTRAP

After this system exists, Codex should act like a proactive repository-native production assistant.

For any user request:

## Step 1 — Understand context
Determine:
- which project,
- which stage,
- what input/output,
- whether this is production, evaluation, experimentation, or system maintenance.

## Step 2 — Read relevant sources of truth
Read:
- project status,
- relevant SOP,
- relevant checklist,
- canonical prompt,
- tool card,
- known learnings,
- related failures.

Do not load irrelevant documentation.

## Step 3 — Perform the task
Do as much as possible directly.

## Step 4 — Record it
Update:
- files,
- metadata,
- run record,
- status,
- registry,
- dashboard when appropriate.

## Step 5 — Validate
Run appropriate repository validation.

## Step 6 — Report concisely
Tell the user:
- what was completed,
- main result,
- key files,
- issues,
- next recommended action.

---

# 36. CONVERSATIONAL UX

Codex should support natural commands.

Examples:

## Start project
> «برای این محصول یه پروژه جدید بساز. عکس اصلی و پرامپت تمپلیت توی فولدر ورودی هستن.»

Codex should:
- create next project ID,
- preserve inputs,
- hash/register them,
- run intake,
- update status,
- identify next stage.

## Analyze source prompt
> «پرامپت اولیه رو کامل تجزیه کن.»

Codex should:
- perform KEEP/ADAPT/REMOVE analysis,
- identify contradictions,
- extract reusable DNA,
- save the analysis,
- not modify original prompt.

## Prepare image prompt
> «برای تولید نماهای بیشتر محصول prompt package بساز.»

Codex should:
- inspect identity spec,
- inspect tool recommendation,
- choose current validated prompt,
- instantiate variables,
- create a package,
- run preflight checklist.

## Register external output
> «این سه عکس خروجی Nano Banana هستن. دومی بهتره.»

Codex should:
- register three Runs or variants as appropriate,
- store/hashes,
- evaluate,
- record user preference,
- select/approve only if QA passes.

## Compare
> «این دو ویدیوی Flow رو مقایسه کن.»

Codex should:
- use video rubric,
- score them,
- classify failures,
- explain which is stronger and why,
- save comparison.

## Learn
> «فکر کنم سه beat برای ۱۰ ثانیه از ۷ beat بهتر جواب می‌ده.»

Codex should:
- search existing evidence,
- classify as hypothesis unless already supported,
- propose or create an experiment,
- avoid silently changing the SOP.

---

# 37. DECISION RULES FOR REPAIR VS REGENERATION

Document an initial heuristic:

Prefer targeted edit/repair when:
- product identity remains stable,
- error is local,
- background/lighting/prop issue is isolated,
- timing and structure are otherwise good.

Prefer regeneration when:
- product geometry morphs,
- category changes,
- reference identity is lost,
- object counts drift heavily,
- temporal continuity collapses,
- prompt has major contradictions,
- scenario is over-complex,
- early frames are already structurally wrong.

Prefer returning to an earlier stage when:
- repeated video generations fail the same way,
- the root cause appears to be reference quality,
- the scenario exceeds model capability,
- keyframes are inconsistent,
- product identity spec is incomplete.

---

# 38. SYSTEM HEALTH

Create a `SYSTEM_HEALTH.md` report template or generated report covering:

- broken links/references,
- invalid metadata,
- unregistered runs,
- pending evaluations,
- candidate prompts without tests,
- obsolete tool cards,
- unresolved change proposals,
- projects without postmortems,
- deprecated prompts still used by active projects,
- missing hashes for important assets.

This helps prevent the repository itself from becoming messy.

---

# 39. RESEARCH / TOOL-FRESHNESS POLICY

AI tools change quickly.

For tool/model facts:

- prefer official documentation,
- store `last_verified`,
- store the source,
- distinguish verified capability from our internal empirical observation,
- do not keep stale model assumptions as timeless facts.

Internal evidence and vendor documentation serve different purposes:

**Vendor docs** answer:
> What does the tool claim/support?

**Our experiments** answer:
> How well does it work for our task?

Keep both.

---

# 40. ACCEPTANCE CRITERIA FOR BOOTSTRAP

Do not declare bootstrap complete until:

### Repository
- [ ] Git repository exists or Git limitation is documented.
- [ ] root structure exists.
- [ ] root documentation is substantive.
- [ ] `AGENTS.md` exists and is concise.
- [ ] `VERSION` is `1.0.0`.

### System docs
- [ ] master workflow is documented.
- [ ] project lifecycle is documented.
- [ ] naming/ID rules exist.
- [ ] evidence and learning policy exists.
- [ ] change-promotion policy exists.
- [ ] storage/versioning policy exists.
- [ ] failure taxonomy exists.
- [ ] evaluation system exists.

### SOPs/checklists
- [ ] each major stage has an SOP.
- [ ] each critical gate has a checklist.
- [ ] checklists are not empty shells.

### Prompt system
- [ ] prompt engineering standard exists.
- [ ] prompt IDs/versioning/status rules exist.
- [ ] canonical prompt structure exists.
- [ ] initial prompt families exist.
- [ ] candidates/deprecated structure exists.
- [ ] prompt registry exists.

### Projects/runs
- [ ] project template is complete.
- [ ] run template is complete.
- [ ] prompt package template is complete.
- [ ] project/run JSON schemas are documented.

### Learning
- [ ] observation/hypothesis/learning/change templates exist.
- [ ] experiment template exists.
- [ ] benchmark policy exists.

### Automation
- [ ] `lab.py` exists.
- [ ] project ID allocation works.
- [ ] experiment ID allocation works.
- [ ] validation works.
- [ ] registry rebuild works.
- [ ] dashboard generation works.
- [ ] key tests pass.

### UX
- [ ] `START_HERE.md` explains the system in Persian.
- [ ] natural-language interaction examples are included.
- [ ] user does not need to manually edit registries.
- [ ] demo project explains the flow.

### Validation
- [ ] run repository validation.
- [ ] fix serious bootstrap errors.
- [ ] update dashboard.
- [ ] show final tree summary.

---

# 41. BOOTSTRAP EXECUTION ORDER

Execute in this order:

1. Inspect current directory.
2. Preserve any existing files; do not overwrite unknown user content.
3. Initialize repository structure.
4. Create root docs.
5. Create `AGENTS.md`.
6. Create system documentation.
7. Create SOPs.
8. Create prompt system.
9. Create tool knowledge system.
10. Create checklists and evaluation rubrics.
11. Create templates.
12. Create learning/experiment/benchmark systems.
13. Implement registry system.
14. Implement `lab.py`.
15. Add tests.
16. Create text-only demo.
17. Rebuild registries.
18. Generate dashboard.
19. Run validation/tests.
20. Fix errors.
21. Initialize/commit Git if possible.
22. Provide final completion report.

Do not stop after the plan.

Execute the work.

---

# 42. FINAL COMPLETION RESPONSE

When bootstrap is finished, respond in Persian with a compact operational summary containing:

1. system version,
2. what was created,
3. whether validation/tests passed,
4. Git status / initial commit status,
5. the most important files to open first,
6. exact next recommended action,
7. an example first message the user can send to start the first real project.

Do not dump every file in chat.

The repository itself is the documentation.

---

# 43. LONG-TERM SUCCESS CRITERIA

Over time this system should make it possible to answer with evidence:

- What is our best current prompt for a specific AI task?
- Why is it the best?
- On which projects/benchmarks was it tested?
- Which version came before it?
- What failure was the revision intended to fix?
- Did it actually fix it?
- What regressions appeared?
- Which tool is currently best for a specific task?
- Is that a vendor claim or our own measured result?
- What product types are difficult?
- What prompt patterns reduce product identity drift?
- What reference strategies work best?
- What scenario structures produce fewer temporal failures?
- What camera instructions create the most stable output?
- Which checklist items were added because of past failures?
- Which repeated mistakes are costing the most generations?
- What should be tested next?

The system should become more valuable after every completed project.

---

# 44. FINAL OPERATING PRINCIPLE

When there is tension between:

- making one project succeed quickly,
- and preserving reusable knowledge,

do both whenever practical.

Solve the current project.

Then record **why it worked** so the next project starts smarter.

The desired flywheel is:

**Project → Runs → Evaluation → Failures → Feedback → Observations → Experiments → Validated Learnings → Better Prompts/SOPs/Checklists/Tool Choices → Better Next Project**

Build the repository so this loop is explicit, traceable, easy to maintain, and difficult to accidentally bypass.
