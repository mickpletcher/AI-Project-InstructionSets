# Contributing

Start with the [authoring standard](shared/instruction-set-standard.md) and [example folder](templates/example-project/). Use a branch and a pull request. Small, scoped changes are easiest to review.

1. Choose the exact target host, project scope, and stable kebab-case name.
2. Copy the example and replace all example content, including metadata. Keep one editable source.
3. Include a beginner-friendly setup/rollback guide and three concrete smoke cases. Record unrun host tests honestly.
4. Add published paths to `catalog.json`; leave drafts unlisted. Run `python tools/validate.py --write-catalog` after catalog changes.
5. Run `python tools/validate.py` and `python -m unittest discover -s tests -v` with Python 3.11+.
6. Update `changelog.md` for meaningful changes. Use `specs/` for substantial structural or automation changes.
7. Open a draft PR describing purpose, scope, tests, and limits. Do not include secrets, private prompts, or proprietary content without permission.

Respect the [code of conduct](CODE_OF_CONDUCT.md). Contributions should be compatible with the [MIT License](LICENSE); preserve attribution and identify third-party material. Report security concerns using [SECURITY.md](SECURITY.md), not public exploit details.
