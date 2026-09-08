---
name: typescript-implement
description: "Execution. Use to turn clear requirements, a specification, a technical design, or a straightforward backend request into working TypeScript and Fastify code."
---

# TypeScript Implement

**Execution.** When the intended behavior is clear, implement it directly. Treat supplied requirements and settled technical decisions as constraints, not invitations to redesign.

Read the affected code and callers, then extend the existing path. Resolve ordinary local details using the project's TypeScript, runtime, module system, and established libraries. A clear task does not need another architecture exercise.

Choose the smallest complete change that delivers the requested behavior. Prefer ordinary functions, values, and existing Fastify composition where they fit. New abstractions, dependencies, configuration, or adjacent cleanup need a present requirement. Keep specified schema, persistence, and testing choices intact.

Preserve the real contract across types and execution: accepted input, asynchronous completion, failures, and observable effects. A type assertion can silence the checker without implementing the requirement. Finish the operation's actual path rather than leaving a typed stub or detached promise.

If a concrete contradiction prevents correct implementation, identify the exact conflict and continue independent work. Ask only for information that changes the required outcome; routine implementation choices remain yours.

Verify the requested behavior with focused runtime checks and the relevant type check. Respect existing required checks. Finish with working code, actual verification, and any specific unresolved requirement, without expanding the task.
