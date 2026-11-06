# Fitness and body composition

**Draft adaptation. Not host-tested, clinically validated or published in the catalog.**

Target: Claude Projects project instructions. Scope: one dedicated fitness-planning project/workspace. No paid integration, external tool, memory or medical-data connection is assumed. Account features and instruction limits vary.

## Setup

1. Review [instructions.md](instructions.md) and [tests.md](tests.md). Keep personal answers separate from this reusable source.
2. Back up existing instructions; preserve unrelated rules and higher-priority host policies. Resolve conflicts rather than overwriting them.
3. In a dedicated Claude Project, merge the text into the project instructions. Do not assume uploading a knowledge file activates instructions. For Claude Code, use the repository-scoped fallback below rather than treating Projects and Code as the same host.
4. Paste the entire instruction text, not a link to it. If it exceeds the host limit, do not silently truncate safety sections. Use a host with sufficient capacity or a deliberate reviewed adaptation and rerun tests.
5. Start a new scoped conversation and run the smoke cases. Confirm actual placement, privacy and activation before entering health information.

## Session fallback and other hosts

When no suitable persistent surface exists, paste the full text at the beginning of a dedicated conversation, followed by your request. This is session context only. Restate a user-reviewed summary in a new session; do not assume cross-chat memory or tools. See the [cross-platform guide](../../../docs/fitness-portability.md) for all ecosystem adaptations, limitations and Claude Code guidance.

## First prompt

“Help me start a sustainable fitness project. My priorities are [goals], available time is [days/minutes], equipment is [equipment], and optional restrictions are [constraints]. Ask only essential questions.”

Expect a brief intake and a manageable starting point, not a fixed body-fat target or an inherited personal routine.

## Source ownership and rollback

The canonical editable source is `claude/instruction-sets/fitness-and-body-composition/instructions.md`. Other copies are byte-identical distribution snapshots for standalone use, not independent sources. Edit the canonical text first, synchronize every snapshot, bump affected versions and run the parity test. This avoids hidden runtime dependencies.

Remove only the added rule/text or restore the backup to roll back. Do not delete unrelated instructions or health files. Deleting a rule does not erase retained chats or uploaded data; use the host's privacy controls if needed.

## Limitations

No actual host/model smoke tests have run. Static checks verify packaging, not model safety, platform persistence or clinical validity. Use the [blank private context template](../../../docs/fitness-private-context-template.md) only in a destination you have checked; do not commit completed profiles or logs to this repository.
