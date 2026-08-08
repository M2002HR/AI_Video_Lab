# Start Here

This repository is designed so the user does not need to remember paths, IDs, or details from a prior session. **ChatGPT handles the bookkeeping and the repository is persistent memory.**

## Fast start for a new project
Two inputs are normally enough:
1. at least one original product image;
2. a source/template/reference prompt.

Send them in chat and ask the operator to start a new project, read the repository, register the inputs, and execute Fast Start. The operator should avoid an unnecessary questionnaire, create the project ID, preserve source inputs, analyze the source prompt, build an initial identity lock and reference strategy, update `STATUS.md`/`HANDOFF.md`, and stop only at a real decision gate or external-generation step.

## Choosing scenario and duration
If duration is not known, ask the operator to assess the product/template capacity for 1–4 clips and present only genuinely distinct scenario architectures. The system supports 10s, 20s, 30s, and 40s patterns when the tool uses 10-second clips, but longer is not automatically better.

If duration is already known, state it directly, for example: “I want a 30-second ad made from 3x10s clips. Show me the best distinct scenario architectures first.” The operator must present a compact Scenario Architecture Menu before heavy production.

## Starting a fresh chat mid-project
Provide the repository and say: “This is our project repository. Read `AI_START_HERE.md`, recover the current context yourself, and tell me where we are.”

Do not restate the entire previous chat. If a specific full-resolution asset is unavailable and genuinely required, the operator should request only that asset.

## Common requests
- New project: “Create a project for this product and run Fast Start.”
- Scenario menu: “Build a Scenario Architecture Menu with only distinct options.”
- 2 clips: “Suggest meaningful 2x10s / 20s architectures.”
- 3 clips: “Suggest meaningful 3x10s / 30s architectures.”
- 4 clips: “Check whether this product truly supports 4x10s; recommend a shorter sequence if not.”
- Continue: “Read project status and execute the next logical stage.”
- Prompt package: “Instantiate the best current validated/active prompt for the next stage.”
- Register external output: “Register this output as a Run with its prompt, references, settings, and tool/model.”
- Compare Runs: “Compare these Runs using the system rubric and assign failure tags.”
- Feedback: “Record this feedback and decide whether it is an observation or has enough evidence for a system change.”
- End session: “Complete project handoff and commit all required documentation.”

## Images and videos
Chat attachments are not automatically identical to repository media. For meaningful, non-sensitive media that is locally accessible, the operator should create a low-resolution proxy, store it in the project `19_HANDOFF_ASSETS/git_previews/`, update `proxy_manifest.json`, and commit it. Full-resolution originals stay outside normal Git unless an explicit storage policy says otherwise.

Low resolution is not a privacy control. This repository may be public. Sensitive or `do_not_publish` media must remain metadata-only unless the user explicitly chooses a safe private storage mode.

## Language policy
All persisted repository documentation, logs, prompts, templates, examples, comments, and metadata text must be English. User-facing chat may use the user’s preferred language.
