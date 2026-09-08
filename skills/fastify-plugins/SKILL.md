---
name: fastify-plugins
description: "Encapsulation. Use when Fastify plugins, decorators, configuration, dependency registration, or startup behavior need implementation or diagnosis."
---

# Fastify Plugins

**Encapsulation.** Follow the plugin tree to understand what each route can see, which dependencies must exist first, and who owns their lifetime. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Use ordinary functions and explicit arguments for ordinary application logic. Use plugins where Fastify scope, lifecycle, or shared infrastructure provides a useful boundary. Preserve existing registration conventions.

Treat `register` as a scope boundary and registration order as dependency order. Use `fastify-plugin` deliberately: its default sharing changes visibility. Dependency metadata does not justify flattening a boundary that should remain encapsulated.

Await initialization within the owning plugin, propagate startup failures, and release acquired resources through its close lifecycle. Validate required configuration before accepting traffic. Keep callback and promise completion separate; an async plugin or hook must not also call `done`.

Decorate the actual runtime scope before use. TypeScript declaration merging cannot establish that a decorator exists there; keep types consistent with registration. Apply the chosen type provider in the scope that needs its inference. Allocate mutable request state per request, never on a shared object.

Exercise changed composition through boot and the relevant scope boundary. Confirm dependencies and hooks reach the intended routes while sibling scopes retain their behavior.
