# Prompt-level evaluations

This suite contains 22 self-contained prompts: 15 primary routing cases, three
unrelated/keyword-only negatives, and four boundary cases. It is **not a record of
model runs** and does not replace the 16 application scenarios in
[the workspace protocol](../docs/evaluation.md). Those scenarios still need pinned
runnable applications; these prompts exercise analysis, routing and scope only.

## Run a comparison

Pin no-pack, prior-pack and candidate conditions. Use separate fresh sessions and
disposable workspaces outside this repository so its maintainer instructions and
rubric cannot influence the tested agent. For each pack arm, install only that
pinned copy. Disable unintended global/native/standalone copies through the host's
supported isolation mechanism. Record exactly how isolation was achieved. Never
relax account permissions merely to make an evaluation run.

Give the tested agent only a case's `prompt`. Do not add its expected skill name,
`routing`, or `rubric`. These are implicit-routing cases; explicit invocation is a
separate experiment. Capture real skill loads from the harness trace, not a claim
in the final answer. Accept any listed specialist and justified combinations;
additional relevant skills are not automatically a failure. Investigate irrelevant
loads separately as cost/scope evidence. For the no-pack arm, grade behavior but
mark pack routing not applicable.

Use the same model, settings, tool access and prompt for paired repetitions. Freeze
the rubric before comparing arms; record each repetition separately, preserve
failures and randomize arm order where practical. Use read-only tools for these
analysis cases. Full implementation, transport and database claims need the
workspace protocol, not a good prose answer. No tool here starts a model or
provisions infrastructure.

## Mechanical commands

From a complete checkout with Python 3.12:

```sh
python scripts/eval_skills.py check
python scripts/eval_skills.py template P02 --arm candidate > /tmp/p02-candidate.json
python scripts/eval_skills.py validate /tmp/p02-candidate.json
```

The template starts at `not-run`; validating it returns exit **3**, never success.
Replace fields only after an actual run. Pin the full pack commit (null only for
no-pack), model, settings, harness, permissions, isolation method and repetition.
Place a nonempty sanitized trace beside the result record, set its relative path
and SHA-256, and list observed pack skills. The trace must show the prompt, tool
activity/skill loads and final answer; a hashes-only manifest is not a trace.
Record the sanitization in the environment description and hash the retained
artifact. Never retain credentials or private production payloads.

A separate human reviewer or configured grader assesses `contract`, `scope` and
`evidence`, citing trace events or lines. Do not expose its rubric to the tested
agent. Record unavailable judgments with a reason rather than converting them to
passes. No substring matcher grades semantics and no self-reported test success
substitutes for a real observation.

The validator checks suite identity, metadata completeness, local trace integrity,
routing expectations and grade-record consistency. It **does not verify the
truthfulness of a trace, a skill-load transcription, or a grader's judgment**.
Exit 0 means `recorded-pass`, not independently established model quality. Exit 1
means `recorded-fail`; 2 means malformed data or missing evidence; 3 means not run,
unavailable or incomplete. Recheck judgment against the retained trace before
reporting a result. Structural CI only tests this contract with synthetic data.

Report correctness/scope failures and routing failures separately, with the model,
case selection and repetition count. Inspect variation before claiming an
improvement; compare tokens, calls or elapsed time only for comparably correct
runs. No overall benchmark score or cross-model improvement is claimed by this
repository's mechanical checks.
