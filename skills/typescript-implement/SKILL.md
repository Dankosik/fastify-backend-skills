---
name: typescript-implement
description: "Implement requested TypeScript backend behavior within the project's existing contracts and technical choices."
---

# TypeScript Implement

**Execution.** When the intended behavior is clear, implement it directly. Preserve settled choices outside the requested change; an explicitly requested technology change is part of the task, not an invitation to redesign unrelated decisions.

Read the affected code and callers, then extend the existing path. Resolve local details using the project's TypeScript, runtime, module system, and conventions.

**Reuse.** When a technical helper is needed, look for a semantic match in nearby code and APIs already available from the runtime, Fastify, or declared utilities such as Remeda. Keep the search proportional to the helper. Write custom mechanics only for a concrete gap; keep business policy explicit. A wrapper should add domain meaning or adaptation, not merely rename a library call.

**Clarity.** Write for the next reader: intention-revealing names, cohesive responsibilities, explicit control flow, and visible effects and failure paths. Apply SOLID, DRY, and YAGNI as heuristics: abstract shared knowledge, preserve distinct business rules, and add only structure justified by current requirements. Prefer the simplest implementation that remains easy to read and change.

New dependencies, configuration, and adjacent cleanup still need a present requirement. Preserve specified schema, persistence, and testing choices outside the requested change.

Preserve the real contract across types and execution: accepted input, asynchronous completion, failures, and observable effects. A type assertion cannot implement a requirement. Finish the actual operation rather than leaving a typed stub or detached promise.

If a concrete contradiction prevents correct implementation, identify the exact conflict and continue independent work. Ask only for information that changes the required outcome; routine implementation choices remain yours.

Verify the changed property with appropriate type or runtime checks and required project checks. Type-only changes need type evidence; runtime claims need runtime evidence. Reuse applicable results for the same revision and environment. Within the environment's permissions, fix failures introduced by the change and rerun affected checks instead of stopping for review after the first patch.

Finish when the requested outcome and required checks are satisfied, or state the concrete blocker and unverified property. Do not invent infrastructure, unrelated cleanup, or speculative checks as new completion requirements; never present an unavailable check as passed.
