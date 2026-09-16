---
name: typescript-design
description: "Use when deciding or reviewing TypeScript backend responsibilities, domain boundaries, or abstractions for a concrete change."
---

# TypeScript Design

**Cohesion.** Give a business decision one natural home and keep the knowledge its callers need small. Honor the requested outcome and preserve settled choices outside the requested change.

Trace the behavior through the existing implementation before introducing a pattern. Place invariants where every relevant caller encounters them. Separate pure decisions from effects when that makes the operation clearer, while preserving the actual transaction and resource boundaries.

Choose functions, object values, classes, and factories for the responsibility they express. A service does not need an interface/class pair merely because it has dependencies. Fastify plugin composition can provide an existing construction boundary; another dependency-injection layer needs a concrete benefit.

Evaluate an abstraction through its callers. Keep it when it hides meaningful policy, variation, or lifecycle ownership. Collapse it when it forwards the same knowledge through another layer. Prefer domain vocabulary over generic repositories, handler factories, or type machinery that obscures a simple operation.

Keep public contracts deliberate. Structural compatibility does not make two domain values interchangeable, and a shared shape does not make two operations share semantics. Preserve meaningful distinctions without branding or wrapping every value by habit.

For analysis or review, explain the responsibility problem and smallest justified change without editing files. For requested refactoring, compare returned data, mutation, failure behavior, asynchronous ordering, and effects. Finish when the changed responsibility is clearer, retained boundaries earn their cost, and focused checks preserve the affected behavior. Report actual verification rather than extending the task to redesign adjacent modules.
