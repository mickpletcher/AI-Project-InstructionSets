# AI Project Instruction Sets

A collection of reusable instruction sets for planning, building, testing, and deploying AI projects.

This repository follows the platform organization and authoring workflow of [AI-Skills](https://github.com/mickpletcher/AI-Skills), adapted for persistent **project context, constraints, and working agreements** rather than trigger-based skills or installable skill packages.

## Start here

1. Browse the [catalog](CATALOG.md). This initial scaffold contains no published instruction sets yet.
2. To author a set, copy [the example folder](templates/example-project/) into the appropriate platform's `instruction-sets/<kebab-case-name>/` folder.
3. Replace its example content, declare the exact host and project scope, and document setup in its README.
4. Adapt instructions to your project and merge with existing rules; never overwrite them blindly.
5. Run the local checks below, then try the documented smoke tests in the actual host. Record results honestly.

A project instruction set stays in scope across related tasks. A skill provides a reusable capability. Neither grants tools, account access, permission to publish, or authority to override host rules.

## Platform areas

- [Claude](claude/README.md): Claude Projects and Claude Code are distinct targets.
- [OpenAI](openai/README.md): separate [ChatGPT](openai/chatgpt/README.md) and [Codex](openai/codex/README.md) targets.
- [Microsoft](microsoft/README.md): [GitHub Copilot](microsoft/copilot/README.md); Copilot Studio is reserved.
- [Cursor](cursor/README.md): project rules.
- [Gemini](gemini/README.md) and [Perplexity](perplexity/README.md): reserved until an exact project-scoped surface is documented and tested.

These folders are organizational scaffolding, not a compatibility or installation claim. See [application guidance](docs/installation.md).

## Repository structure

- Platform `instruction-sets/` folders: future published sources, each with its own README, instructions, metadata, and tests.
- `shared/`: [authoring standard](shared/instruction-set-standard.md) and [platform organization](shared/platform-organization.md).
- `templates/`: complete example plus a [test record](templates/test-template.md).
- `specs/`: requirements and decisions for substantial changes.
- `tools/` and `tests/`: offline validation and regression tests.
- `catalog.json`: explicit published-set inventory; `CATALOG.md` is generated from it.

## Validate locally

Python 3.11 or newer is the only requirement; no third-party packages or credentials are needed.

```sh
python tools/validate.py
python -m unittest discover -s tests -v
```

After changing the inventory, run `python tools/validate.py --write-catalog`, then rerun both checks. CI runs the same checks on Linux and Windows. Static validation checks structure, metadata, catalog freshness, and inline relative Markdown file links; it does not prove model behavior or check external URL availability, reference-style links, or heading anchors.

## Contribute and get help

Read [CONTRIBUTING.md](CONTRIBUTING.md), [SUPPORT.md](SUPPORT.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md), and [ACCESSIBILITY.md](ACCESSIBILITY.md).

See [changelog.md](changelog.md) for repository changes. Licensed under the existing [MIT License](LICENSE), copyright 2026 Mick Pletcher. Preserve third-party licenses and attribution.
