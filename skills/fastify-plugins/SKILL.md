---
name: fastify-plugins
description: "Use for Fastify registration, decorator visibility, plugin initialization, configuration, or owned-resource lifecycle decisions."
---

# Fastify Plugins

**Encapsulation.** Follow the affected plugin branch to understand what each route can see, which dependencies must exist first, and who owns their lifetime. Honor the requested outcome and preserve settled choices outside the requested change.

Use ordinary functions and explicit arguments for ordinary application logic. Use plugins where Fastify scope, lifecycle, or shared infrastructure provides a useful boundary. Preserve existing registration conventions.

Treat `register` as a scope boundary and registration order as dependency order. Use `fastify-plugin` deliberately: its default sharing changes visibility. Dependency metadata does not justify flattening a boundary that should remain encapsulated.

Await initialization within the owning plugin, propagate startup failures, and release acquired resources through its close lifecycle. Validate required configuration before accepting traffic. Keep callback and promise completion separate; an async plugin or hook must not also call `done`.

Decorate the actual runtime scope before use. TypeScript declaration merging cannot establish that a decorator exists there; keep types consistent with registration. Apply the chosen type provider in the scope that needs its inference. Allocate mutable request state per request, never on a shared object.

For diagnosis or review, explain the composition issue without editing. When changing composition, exercise boot and the relevant scope or lifecycle boundary. Check sibling scopes when visibility or hook placement changes; do not audit unrelated branches. Report actual verification and any unexercised boundary.
