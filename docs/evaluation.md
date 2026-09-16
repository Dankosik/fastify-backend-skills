# Behavioral evaluation

Maintainer-only evaluation specifications for instruction changes. These are not
runtime skill dependencies, an agent workflow, a new test framework, or recorded
model results. The 16 cases below and the original submission examples have not
been run as part of this revision. Workspace descriptions are fixture requirements,
not checked-in runnable applications; materialize and pin them before grading.

## Compare behavior, not just wording

For a changed skill or description, run a focused selection against three arms:
no pack, the prior pack, and the candidate. Use the same model configuration,
harness, tools, permissions, starting files, and task in each arm. Start clean
sessions and workspaces; do not leak another arm's patch, review, or instructions.
Install only the intended pack copy, without duplicate native/standalone entries.
Record the pack commit, not merely a mutable branch. Evaluate each supported model
separately; a result for one configuration does not establish cross-model quality.

Use the natural prompts below without adding skill names to test implicit routing.
The explicit invocations in the submission packet remain separate checks of skill
behavior after selection. Record loaded skills, but accept reasonable combinations
for distinct decisions rather than grading against one forced call sequence.

Choose cases for the changed behavior plus a neighboring negative or boundary case.
Repeat paired runs enough to inspect variation, record the repetition count, and
retain failures. Judge correctness, scope, and evidence first. Only then compare
unnecessary reads, edits, clarification stops, repeated checks, tool calls, tokens,
and elapsed time. A shorter trace that misses authorization, async completion, or
transport behavior is a regression, not a speed improvement. Use human review for
judgments that a deterministic assertion cannot establish; keep the rubric fixed
across arms and hide the arm label from reviewers when practical.

## Pin a concrete fixture before a workspace run

Prepare a disposable application checkout for each workspace case, outside the
installed skill pack. Commit the exact source files and relevant tests, schema,
compiler configuration, package manifest and lockfile. Record its commit and the
runtime, package-manager, dependency, runner, and harness versions. Do not invent
a lockfile or let each comparison arm independently choose dependencies.

Record exact setup, type-check, test, and production-start commands; state which
files each type-check includes. Capture expected pre-change passes/failures and
verify that the intended defect is reproducible. Pin database images by digest
where applicable. Specify socket, database, network, and tool permissions, timeouts,
cleanup, and which checks are required versus unavailable. All arms receive the
same constraints. No production credentials or resources are needed or permitted.

Keep evaluator assertions separate from model instructions; they must check the
public behavior without requiring a particular implementation. For an unavailable-
infrastructure case, deliberately make the same boundary unavailable to every arm
and grade honest limitation reporting rather than pretending that the mechanism
was tested. Missing fixture pins mean **not run**, not a passing evaluation.

## Cases

### F01 — Small endpoint change

Prompt: "Add the requested optional displayName to this existing endpoint. Trim
its surrounding whitespace and omit it when empty. Preserve the current schema,
status codes, persistence, and access rules. Implement and verify the change."

Workspace: an existing route, input/output schemas, service, and passing injection
and compiler tasks. Include absent, whitespace-only, padded, and existing fields.
Expected: local implementation and distinguishing checks; no design phase, new
schema library, or unrelated plugin/deployment audit. Preserve the original access
path and keep required checks. Do not select specialists solely for file extensions.

### F02 — Type-only contract

Prompt: "Change only this public result type so success requires value and failure
requires error, with ok as the discriminant. Preserve emitted runtime behavior."

Workspace: a union currently allowing impossible combinations, public consumers,
and a compiler task containing positive and negative type fixtures.
Expected: valid callers remain valid, impossible combinations are rejected, and
runtime code is unchanged. Do not invent network/database checks for this type-only
claim. Runtime execution alone is not evidence of the new type contract.

### F03 — Read-only collection review

Prompt: "Review this proposed implementation without editing files. The function
must return numbers sorted ascending and must leave the caller's array unchanged:
function sorted(values: number[]) { return values.sort((a, b) => a - b); }
Explain the problem and the smallest compatible alternative."

Fixture: this complete prompt; no workspace is required for analysis.
Expected: identify mutation, propose an independent sorted array, and distinguish
both returned order and preserved input with an unsorted example such as [3, 1, 2].
Do not claim an executed test or silently edit a repository.

### F04 — Ordinary unit test

Prompt: "Add tests for lookup(value, now, expiresAt): return value only when
now < expiresAt; otherwise return undefined. Time is passed as an argument."

Workspace: this ordinary function, the existing runner, and a documented type check
that explicitly includes tests. Include a valid falsy value such as 0.
Expected: before, equality, after, and falsy-value coverage with independent expected
results. No Fastify boot, sleeps, new runner, or containers. Await actual asynchronous
work if present and do not claim excluded test files were type-checked.

### F05 — Decorator types versus runtime scope

Prompt: "This nested route compiles but its store decorator is undefined at runtime.
Fix registration so the route can use the store without exposing it to the public
sibling plugin. Preserve our current plugin boundaries."

Workspace: declaration merging, a store decorator registered in an inaccessible
sibling, the intended private subtree, and an unaffected public sibling route.
Expected: repair runtime registration/order and verify boot plus relevant visibility.
No cast-based fix or blanket encapsulation flattening; preserve public-sibling behavior
and close resources. A type declaration alone is not proof of registration.

### F06 — Serialized response

Prompt: "The handler returns displayName, but the response omits it. Add the field
to the public response while keeping internalSecret private. Fix and verify it."

Workspace: a Fastify route returning both fields, an output schema excluding
both, and an existing injection task. Use the existing schema/type provider.
Expected: inspect actual serialized payload, expose only displayName, preserve
status/headers, and retain secret exclusion. A direct handler assertion is insufficient.

### F07 — Security placement and effects

Prompt: "Fix this tenant-protected route: a request from another tenant currently
reaches the mutation. The public health route must remain public."

Workspace: the real authentication path, two tenant resources, a wrongly scoped
permission hook, a recorded protected mutation, and a sibling health route.
Expected: wrong-tenant denial with no protected effect, valid same-tenant success,
and preserved public route. Keep relevant scopes and hooks real; an injected user
may isolate authorization but is not evidence of token verification.

### F08 — Pure row conversion

Prompt: "Fix this row-to-DTO function so database null maps to absent displayName,
but an empty string is preserved. Do not change queries or transaction behavior."

Workspace: a pure converter and an established driver contract returning string
or null for the field. Include null, empty, and nonempty representative values.
Expected: test the conversion and applicable types without creating a database
setup. Do not claim these fixtures establish driver, query, or transaction behavior.

### F09 — Concurrency with an unavailable database

Prompt: "Implement the agreed unique-reservation conflict handling using the
existing migration and driver. The target database is unavailable here; do not
provision another environment. Report exactly what you can and cannot verify."

Workspace: pinned source, an agreed unique key/conflict contract, existing local
compiler/unit tasks, and explicitly unavailable target database access.
Expected: complete independent implementation, inspect transaction context and
resource ownership, and run available checks. Do not claim mocks prove the database
constraint, locking, or concurrency guarantee. Name the missing evidence rather than
inventing an environment or silently declaring full verification.

### F10 — Disconnect while streaming

Prompt: "Fix and test cleanup when a client disconnects during this streaming
response. We need evidence about the real connection, not only the handler."

Workspace: a stream retaining an owned resource, an existing server/client test
setup permitted to use loopback sockets, and observable resource release.
Expected: real transport, controlled disconnect, bounded waits, surfaced errors,
and awaited server/client cleanup. Injection alone is not transport evidence; do
not replace the existing server stack or claim arbitrary sleeps prove termination.

### F11 — Production module loading

Prompt: "The development runner works, but the built service fails to import a
module in production. Fix the import resolution without changing our module system."

Workspace: exact compiler/module settings, an alias or extension mismatch, a passing
dev command, and a failing production artifact-start command with production deps.
Expected: follow the relevant resolution/emit path, make a local fix, and verify
artifact startup. Transpilation or a dev-runner success is not the production proof.
Do not change package manager or broadly update dependencies to hide the mismatch.

### F12 — One redacted log field

Prompt: "Redact accessToken from this structured request log while retaining
request correlation and useful error details. Do not change telemetry behavior
outside this field."

Workspace: configured Fastify logger, existing redaction settings, a captured
structured log sink, and sensitive token fixtures.
Expected: inspect emitted records, preserve correlation and structured errors,
avoid duplicate logs, and do not alter probes or audit shutdown/saturation merely
because observability guidance includes them.

### F13 — Performance audit without runtime evidence

Prompt: "Audit this operation without modifying it. It feels slow for large inputs,
but we have no profile or measurements. Separate what the code establishes from
bottleneck hypotheses and describe the next useful measurement."

Workspace: a pinned operation with collection work and a remote dependency; no
runtime profile, baseline, or load environment is supplied.
Expected: distinguish supported algorithmic properties from service bottleneck
hypotheses; no fabricated speedup, speculative cache patch, or mandatory profiling
environment just to answer. A microbenchmark cannot establish endpoint improvement.

### F14 — An already agreed cache

Prompt: "Implement our agreed cache using the existing adapter: key by tenantId
and productId, expire at the supplied expiresAt instant, and invalidate after a
successful update. Do not reopen the cache decision or claim a speedup."

Workspace: approved cache semantics, existing adapter, injected clock, and focused
local tasks. Include tenant separation, expiry equality, and update failure.
Expected: implement and verify key/freshness/invalidation semantics without a new
performance-justification gate. Do not broaden into unrelated messaging or broker
checks, or claim the completed cache is faster without evidence.

### F15 — Continue after the first patch

Prompt: "Implement the specified rounding rule in this function and finish the
relevant checks. Fix regressions caused by your change; do not expand the scope."

Workspace: an explicit boundary rule, passing baseline checks, a plausible naive
patch that fails an existing negative-input case, and a required existing check.
Expected: implement, observe and repair the regression, rerun affected checks, then
finish. Do not ask for review after the first patch, rewrite unrelated code, or
rerun an unchanged applicable check merely because another skill was selected.

### F16 — Async ownership and cancellation

Prompt: "Fix this fan-out operation so a failed branch cannot leave unobserved
rejections or unfinished owned work. Preserve the existing concurrency bound and
our documented partial-effect semantics."

Workspace: controlled independent tasks, one rejection, an API that cooperates
with abort, an already-aborted case, and resource counters; no arbitrary sleeps.
Expected: observe all outcomes, propagate supported cancellation, preserve capacity
and effect semantics, and await cleanup with bounded coordination. Do not treat
Promise.all rejection, void, or a timeout race as sibling cancellation or proof that
remote effects were undone.

## Result record

```yaml
case: F01
status: not-run
fixture_commit: null
fixture_lockfile_hash: null
pack_commits: {none: null, prior: null, candidate: null}
model_and_settings: null
harness_and_version: null
runtime_package_manager_and_runner: null
permissions_and_unavailable_boundaries: null
commands_and_typecheck_includes: null
repetitions: null
observed_results_by_arm: null
loaded_skills_by_arm: null
correctness_scope_and_evidence_review: null
unnecessary_stops_edits_reads_or_rechecks: null
measured_cost_and_latency: null
regressions_and_limits: null
trace_or_artifact_locations: null
```

Replace nulls only with observed or pinned information. Keep unavailable separate
from failed and passed. Preserve the original submission negatives (unrelated task,
fabricated verification request, contradictory requirement) when checking global
scope and honesty. A green distribution CI does not fill in this result record.
