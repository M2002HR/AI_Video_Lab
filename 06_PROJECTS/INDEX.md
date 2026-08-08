# Projects

This directory contains real projects only. Fictional demos belong in `13_EXAMPLES/` and must not contaminate real statistics.

## Active projects

| Project | Title | Status | Current stage | Next action |
|---|---|---|---|---|
| `P0001_truffle_chocolate` | Colorful Chocolate Truffle Miniature Commercial | active | STAGE_19 Final Selection | R0022 accepted for the 10s objective; optimization remains paused/backlog unless the user asks to resume |
| `P0002_truffle_chocolate_30s` | Colorful Chocolate Truffle 30s Derivative | active | STAGE_07 Scenario Architecture | User selects S30-A/B/C/D; then build the Master Sequence and Clip Contracts |

## New project

Create new projects from `05_TEMPLATES/PROJECT_TEMPLATE/`. When the user supplies product image(s) + source/template prompt, run `00_SYSTEM/FAST_START_PROTOCOL.md`.

Derivative projects must record `parent_project_id` and must not overwrite the parent project's history.

## New chat / continuation

To recover context:
1. identify active/relevant project(s) from registry or `project.json`;
2. read the target project's `STATUS.md` and `HANDOFF.md` first;
3. then load only current-stage files and evidence.

## Required continuity contract

Every active project should keep these synchronized as far as practical:
- `project.json`
- `STATUS.md`
- `HANDOFF.md`
- `18_CONVERSATION_LOG/`
- relevant Run, prompt, and evaluation records.

Large original media may live outside Git. Record its role, hash/location when available, and any re-attachment requirement in the handoff. Low-resolution Git proxies may be used for cross-chat visual recall according to `00_SYSTEM/MEDIA_PROXY_PIPELINE.md`.

Repository text is English-only. User-facing chat may use another language, but any persisted repository text must be translated or paraphrased into English before commit.
