# Platform organization

Keep actual instruction sets with the host that owns their behavior. Shared guidance is not a hidden runtime dependency: a set must contain the instructions its user needs.

Supported authoring areas are `claude`, `openai/chatgpt`, `openai/codex`, `microsoft/copilot`, `cursor`, `gemini`, and `perplexity`. Directory existence means authors can propose a set, not that the host has been tested. Distinguish Claude Projects from Claude Code with explicit metadata and setup. Keep Copilot Studio separate from GitHub Copilot; it is reserved here.

Do not copy AI-Skills installers, `.skill` archives, skill triggers, or generation pipelines into this project. Project instructions have different scope and activation rules. Additional ecosystems should be added with documented placement and validation tests when needed, rather than empty promises of support.
