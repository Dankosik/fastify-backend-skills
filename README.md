# Fastify Backend Skills

Small, independent skills for clean, idiomatic TypeScript and Fastify backend development.

Each skill starts with a familiar engineering concept and directs a decision: what to inspect, how to reason, and what would make the result convincing. The model brings its language and framework knowledge. Your project supplies the versions, conventions, and constraints.

One `SKILL.md` per skill. No reference libraries, setup ceremony, mandatory process, or dependencies between skills.

## Install

This checkout prepares **1.0.1 (unreleased)**. Published installation examples stay pinned to the existing release until the candidate is published.

Versioned release: [v1.0.0](https://github.com/Dankosik/fastify-backend-skills/releases/tag/v1.0.0).
Install selected skills, or the entire pack, into your current project:

```sh
npx skills@1.5.25 add "Dankosik/fastify-backend-skills#v1.0.0" --agent codex --skill '*' --copy
```

Use `--skill typescript-implement` for one skill, or `--agent claude-code` for Claude
standalone placement. Node.js >=22.20.0 is required by this installer, not by
the skill instructions.

For native Claude Code and Codex installation, add the
[Dankosik marketplace](https://github.com/Dankosik/agent-skills-marketplace), then
install `fastify-backend-skills@dankosik-skills`. The author catalog is available independently
of review for either provider's public directory.

[All installation methods, updates and rollback](docs/distribution.md) ·
[Versioning](docs/versioning.md) · [Changelog](CHANGELOG.md)

## Choose the decision

| Skill | Leading concept | Use it for |
| --- | --- | --- |
| [typescript-implement](skills/typescript-implement/SKILL.md) | Execution | Turn clear requirements or an agreed technical design into working code |
| [typescript-idiomatic](skills/typescript-idiomatic/SKILL.md) | Contracts | Representation, type-contract, and transformation decisions |
| [typescript-design](skills/typescript-design/SKILL.md) | Cohesion | Responsibilities, domain models, and useful module boundaries |
| [typescript-async](skills/typescript-async/SKILL.md) | Ownership | Promises, cancellation, sequencing, streams, capacity, and cleanup |
| [typescript-debugging](skills/typescript-debugging/SKILL.md) | Causality | Bugs, startup failures, hanging requests, and flaky behavior |
| [typescript-performance](skills/typescript-performance/SKILL.md) | Evidence | Audit or measure Node.js latency, throughput, CPU, memory, and startup claims |
| [typescript-build](skills/typescript-build/SKILL.md) | Resolution | Type checking, ESM/CJS, packaging, toolchains, and dependencies |
| [fastify-plugins](skills/fastify-plugins/SKILL.md) | Encapsulation | Registration, decorators, configuration, plugin scope, and resource lifetime |
| [fastify-routes](skills/fastify-routes/SKILL.md) | Contract | HTTP endpoints, schemas, type providers, hooks, serialization, and errors |
| [typescript-data](skills/typescript-data/SKILL.md) | Atomicity where required | Query shape, row conversion, transaction consistency, and schema compatibility |
| [fastify-security](skills/fastify-security/SKILL.md) | Authorization | Authentication, resource access, tenancy, cookies, and proxy trust |
| [typescript-integrations](skills/typescript-integrations/SKILL.md) | Delivery semantics | Outbound calls, retries, messages, jobs, and caches |
| [fastify-observability](skills/fastify-observability/SKILL.md) | Operability | Logs, metrics, traces, probes, and shutdown |
| [typescript-unit-testing](skills/typescript-unit-testing/SKILL.md) | Behavior | Focused tests with Node.js test runner, Vitest, or Jest |
| [fastify-testing](skills/fastify-testing/SKILL.md) | Mechanism | Injection, real plugin composition, transport, and infrastructure tests |

Use `typescript-implement` when the task is clear and the work is to implement it. Use a specialist when its particular decision needs attention. Each honors the requested outcome and preserves settled choices outside the requested change; none requires a design phase. Debugging separates diagnosis from fixing; performance work separates an audit from measured optimization. Unit tests isolate ordinary behavior; Fastify tests retain the framework or infrastructure mechanism being tested.

Select skills for decisions that need their guidance, not merely because the repository uses TypeScript or Fastify. Specialists are not mandatory stages. Combine them when distinct parts of the task need them; there is no one-skill limit.

A skill supplements the requested task; it does not expand its authorized scope or require every topic in its body to be investigated. Analysis and review do not silently authorize edits. An explicitly requested technology change does not reopen unrelated settled choices.

Match evidence to the changed property: types for type-only claims, runtime tests for ordinary behavior, Fastify injection for in-process request contracts, and real transport or databases for their respective mechanisms. Preserve required project checks and reuse applicable results for the same revision and environment. Report unavailable verification honestly rather than inventing a test environment or claiming a weaker check proves a stronger property.

## Use

Ask naturally, or select a skill through your agent's explicit skill invocation:

- “Use typescript-implement to implement this specification without changing its technical design.”
- “Use typescript-idiomatic to simplify this function while preserving its runtime behavior.”
- “Use fastify-plugins to fix the dependency visibility in these nested plugins.”
- “Use fastify-routes to implement this endpoint with our existing schemas.”
- “Use fastify-testing to cover validation, response serialization, and denied access.”

The pack targets TypeScript backends running on Node.js with Fastify. It preserves the project's runtime, compiler, module system, schema library, driver or ORM, and testing stack. It does not prescribe an upgrade, a new architecture, or a migration between Zod, TypeBox, JSON Schema, or persistence libraries. Provider-specific deployment and specialist infrastructure remain project concerns.

## Contribute

Keep each skill independent and decision-focused. Prefer an established concept over a new glossary, a discriminating trigger over a capability catalog, and an observable outcome over a long checklist. Improve wording against a realistic task that exposed a weakness. Keep version lookups and API tutorials out of the skill.

The [behavioral evaluation scenarios and comparison protocol](https://github.com/Dankosik/fastify-backend-skills/blob/main/docs/evaluation.md) are maintainer materials, not runtime skill dependencies. Compare unassisted, prior-pack, and candidate behavior on pinned fixtures before claiming an improvement. The scenarios are specifications, not recorded model results.

The pack uses the [Agent Skills format](https://agentskills.io/specification). Structural validity and a few useful examples do not establish a universal improvement across models.

## Acknowledgements

Follows the compact style of [Dankosik/java-backend-skills](https://github.com/Dankosik/java-backend-skills), with inspiration from [Dankosik/go-service-template-rest](https://github.com/Dankosik/go-service-template-rest) and [mattpocock/skills](https://github.com/mattpocock/skills). The instructions are written for TypeScript, Node.js, and Fastify semantics.

[MIT license](LICENSE).
