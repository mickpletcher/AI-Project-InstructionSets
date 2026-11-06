# Applying project instructions

Nothing in this repository installs or activates itself. Review the exact set README and your host's current documentation; feature names and limits can change.

1. Save a copy of existing project instructions.
2. Replace example context with non-sensitive project details.
3. Resolve conflicts deliberately. Preserve unrelated user rules and higher-priority host instructions.
4. Apply only to the intended project or repository, not account-wide instructions by default.
5. Start a new project conversation/task and ask it to explain the scope and constraints.
6. Run the set's smoke tests. If behavior is wrong, restore the previous instructions and document the limitation.

## Host distinctions

- Claude Projects: use the project's instructions surface. Claude Code: adapt to the repository's `CLAUDE.md` guidance, with explicit directory scope. These are not interchangeable installation methods.
- ChatGPT: use project instructions when available, not global Custom Instructions or a custom GPT by default.
- Codex: adapt to `AGENTS.md` at the appropriate repository/directory scope. Review existing guidance and inheritance before editing.
- GitHub Copilot: repository-wide guidance commonly uses `.github/copilot-instructions.md`; scoped files require an appropriate host-supported wrapper. Document the actual client being tested.
- Cursor: use project rules and the host's native rule metadata; plain Markdown stored here is not automatically an active rule.
- Gemini and Perplexity: no specific integration is shipped yet. A reusable assistant or Gem is not automatically a project-scoped instruction surface. Document the exact surface before proposing a set.

No host activation or model evaluation has been performed for this scaffold. There is no automatic installer, exporter, synchronization, or deployment pipeline.
