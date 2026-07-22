# Contributing

This is the organisation-wide default. A repository that ships its own `CONTRIBUTING.md` overrides
this file — see
[playwright-ai-triage/CONTRIBUTING.md](https://github.com/flaketrace/playwright-ai-triage/blob/main/CONTRIBUTING.md)
for that project's build commands, eval workflow, and prompt-change policy.

Issues and PRs are welcome.

## Ground rules

- Check the repository's roadmap before proposing a feature — it may already be planned, and an
  issue saying it matters to you is what reorders it.
- Conventional commits (`feat:`, `fix:`, `docs:`, `chore:`, …).
- Whatever the repository's quality gate is, it must pass before a PR is reviewed.
- Never commit secrets or real API keys.
- Sign off every commit (see below).

## Developer Certificate of Origin

By contributing you certify the
[Developer Certificate of Origin 1.1](https://developercertificate.org/) — that you wrote your
contribution, or otherwise have the right to submit it under the project's license.

Sign each commit with `git commit -s`, which adds the `Signed-off-by:` trailer. CI checks it on
every pull request. Forgot? `git commit --amend -s` for one commit, or `git rebase --signoff` for
several.

## Code of Conduct

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
