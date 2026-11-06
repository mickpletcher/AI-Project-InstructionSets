# Example project instruction set

**Template only. Not a published or host-tested set.**

Copy this folder into a platform's `instruction-sets/<name>/` directory. Rename the ID and title, set the exact platform/surface, and replace example project context. `instructions.md` is the editable source of truth. Do not publish until the README and tests match the actual target.

## Setup

Requires a host with a project-scoped instruction surface; no external tools are assumed. Back up existing instructions. Merge `instructions.md` into the chosen surface, preserving unrelated rules. Document exact placement and any host-native wrapper here. Start a new task and run `tests.md`. Restore the backup to roll back.

## First prompts

- “Help me plan the first milestone for this project.” Expect a scoped plan and questions about missing goals.
- “What can you help with here?” Expect a concise scope explanation and starter prompt.

## Limitations

Replace this section with host limits and tested prerequisites. No live host tests have been run. This example is documentation, not an installation artifact.
