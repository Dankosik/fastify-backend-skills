---
name: typescript-implement
description: "Execution. Use to turn clear requirements, a specification, a technical design, or a straightforward backend request into working TypeScript and Fastify code."
---

# TypeScript Implement

**Execution.** When the intended behavior is clear, implement it directly. Treat supplied requirements and settled technical decisions as constraints, not invitations to redesign.

Read the affected code and callers, then extend the existing path. Resolve local details using the project's TypeScript, runtime, module system, and conventions.

**Reuse.** Before writing technical helpers, check existing project code, runtime and Fastify APIs, and declared utilities such as Remeda. Use a matching API directly. Write custom mechanics only for a concrete semantic or operational gap; keep business policy explicit. A wrapper should add domain meaning or adaptation, not merely rename a library call.

**Clarity.** Write for the next reader: intention-revealing names, cohesive responsibilities, explicit control flow, and visible effects and failure paths. Keep changes local and follow the language and framework's idioms. Apply SOLID, DRY, and YAGNI as heuristics: abstract shared knowledge, preserve distinct business rules, and add only structure justified by current requirements. Prefer the simplest implementation that remains easy to read and change.

New dependencies, configuration, and adjacent cleanup still need a present requirement. Preserve specified schema, persistence, and testing choices.

Preserve the real contract across types and execution: accepted input, asynchronous completion, failures, and observable effects. A type assertion can silence the checker without implementing the requirement. Finish the operation's actual path rather than leaving a typed stub or detached promise.

If a concrete contradiction prevents correct implementation, identify the exact conflict and continue independent work. Ask only for information that changes the required outcome; routine implementation choices remain yours.

Verify the requested behavior with focused runtime checks that would fail for a plausible contract violation, and the relevant type check. Match testing effort to the change and respect existing required checks. Finish with working code, actual verification, and any specific unresolved requirement, without expanding the task.
