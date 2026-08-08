# DEC-0001 — ChatGPT Operator and Repository-Based Chat Continuity

## Status
Accepted design decision.

## Context
The original v1.0 repository assumed a Codex-oriented operator. The user chose to perform real production, prompt/scenario/image/video iteration, and system maintenance primarily with ChatGPT and expects work to continue across fresh chats.

## Decision
1. The architecture is AI-operator neutral; ChatGPT is the current primary operator.
2. The repository, not chat history, is durable project memory.
3. Every active project maintains `STATUS.md`, `HANDOFF.md`, and durable conversation logs.
4. `AI_START_HERE.md` is the context-recovery protocol for a new agent/session.
5. The user authorizes necessary low-risk documented repository changes/commits during production.
6. Minimum-input Fast Start is product image(s) + source/template prompt.

## Alternatives rejected
- Codex-only workflow: does not match the desired operating model.
- Dependence on chat memory: unreliable across sessions and weak for auditability.
- Full transcript storage by default: excessive noise/duplication; persist only durable feedback/session summaries.

## Consequences
- Operator documentation is AI-neutral.
- Project template includes explicit handoff/conversation continuity.
- Media availability/re-attachment requirements must be explicit.
- Repository maintenance during production is normal workflow behavior.

## Evidence / scope
This is a direct system-design requirement from the user, not a benchmark claim about comparative ChatGPT/Codex quality.
