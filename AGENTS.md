# Maintaining this skill pack

This repository ships instructions, not a Fastify application. Preserve the 15
independently installable skills and their names. Each skill directory contains
only `SKILL.md` and `LICENSE`. Do not add application dependencies, a mandatory
workflow, or cross-skill prerequisites to improve prose.

Read the changed skill and the nearest relevant example before editing. Its
`description` should distinguish the decision that needs guidance; its body should
add judgment the agent would otherwise miss. Preserve project choices, review-only
scope, appropriate evidence, and completion of authorized implementation work.
Do not replace useful Fastify-specific constraints with generic brevity.

For behavioral changes, read [the evaluation protocol](docs/evaluation.md) and
[the prompt suite](evals/README.md). For a broad instruction audit, read
[the authoring rationale](docs/authoring.md). Neither is an instruction to load all
reference material or to run every behavioral case for every wording change.

## Verification

Install maintainer dependencies from `requirements-dev.txt` when needed. The
ordinary local check is `python -m unittest discover -s scripts/tests`; it includes
distribution validation and the evaluation contract tests. Run affected tests
while iterating, then the required checks once for the final relevant revision.
One owner consolidates results; another skill or reviewer is not a reason to rerun
an unchanged check. Never equate these tests with model evaluations.

`plugin.json` is canonical metadata. Run `python scripts/distribution.py sync` only
when derived manifests or licenses need synchronization. The existing CI also
runs the network-dependent installer smoke test and a clean-checkout archive
build. Preserve those gates; do not claim they ran when unavailable locally.

Use real subagents only when available and useful for independent questions;
otherwise report self-review as self-review. Reviewers do not duplicate the test
suite, edit the same files concurrently, or recursively recruit more reviewers.
Stop after actionable issues are resolved and required evidence is collected, or
report the concrete remaining limitation. Do not publish a release, change
installation pins, merge, or broaden permissions as part of an instruction edit.
