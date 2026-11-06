# Repository scaffolding baseline

## Requirements

Adapt AI-Skills conventions for project instruction sets. Preserve the existing license and original project purpose. Provide a novice path, platform organization, reusable template, community policies, and runnable automated checks.

## Decisions

Use platform-owned `instruction-sets/` sources, not skill packages. Keep ChatGPT/Codex and Copilot/Copilot Studio distinct. Start with an empty explicit catalog rather than advertise template content as shipped. JSON metadata and Python standard-library tooling avoid setup dependencies. Static checks and host/model evaluations remain separate.

## Exclusions

No installer, skill archive, generated multi-host copies, published starter sets, live model runs, repository setting changes, deployment, or merge.

## Validation

Run `python tools/validate.py` and `python -m unittest discover -s tests -v`. CI exercises both on Linux and Windows. Test missing files, malformed metadata, invalid inventory paths, draft publication, catalog drift, and broken relative links. Record PR-specific check results in the PR.
