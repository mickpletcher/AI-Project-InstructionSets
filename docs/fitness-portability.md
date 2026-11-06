# Portable fitness project instructions

## Status and scope

These are draft adaptations, not tested compatibility claims. The platform areas remain authoring locations, not certification. The fitness text is host-neutral and standalone; host rules, actual context limits, account features and user authorization still apply. No integration, tool access, clinical efficacy or universal AI-ecosystem support is promised.

## Choose an application method

- Claude Projects: project instructions. Claude Code: in a dedicated private planning repository, merge the same full text into the applicable CLAUDE.md after checking inherited instructions; no separate Code host evaluation has run.
- ChatGPT Projects: project instructions, not global personalization.
- Codex: scoped AGENTS.md in a dedicated private planning repository.
- GitHub Copilot: repository custom instructions in a supported client; not consumer Copilot or Copilot Studio.
- Cursor: dedicated project rule created with the native rule editor and reviewed scope metadata.
- Gemini: candidate dedicated Gem instructions, a reusable assistant rather than an asserted project container.
- Perplexity: candidate private Space custom instructions, if available in the current account.
- Other ecosystems or missing features: paste the full text into a dedicated conversation as session context. This is not an integration or persistence guarantee. For API applications, the application owner must choose the appropriate instruction role and storage/consent design under that provider's rules; this repository supplies no API deployment.

Use the README beside each copy for setup, conflict handling and rollback. Confirm current vendor documentation and actual behavior before treating a candidate surface as supported. No current UI walkthrough or live account test was performed for these adaptations.

## Privacy and application checks

Use the generic text unchanged, then supply only the private context you choose in a separate user message or private file. Check project membership, sharing, retention and connected tools. A private repository is still a third-party data destination; do not assume it is suitable for health records. Never upload someone else's health information without authorization. Avoid automatic synchronization of completed profiles.

If the host cannot load the full text, do not drop safety and privacy sections to make it fit. Apply a deliberately reviewed shorter adaptation or choose another surface. Test scope in a fresh conversation and run the behavioral cases. Do not rely solely on the model saying it has read the instructions.

## Maintenance and verification

The Claude-area instructions.md owns the editable text. Each of the seven platform folders contains an identical complete snapshot, with target-specific README and metadata. Synchronize snapshots in the same change and run `python -m unittest discover -s tests -v`; parity failures block drift. These offline tests are not medical review or actual host tests. All sets remain draft and absent from catalog.json until appropriate review and recorded host results support publication.
