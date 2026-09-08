---
name: fastify-testing
description: "Mechanism. Use for Fastify tests of routing, schemas, plugin composition, authentication, lifecycle and infrastructure, including Testcontainers integration."
---

# Fastify Testing

**Prove the mechanism.** Choose the smallest boundary containing the mechanism behind the promised behavior. Choose scenarios that expose the relevant failure at that boundary. Calling a handler directly cannot establish validation, serialization or hooks. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Preserve the project's runner, schema library and infrastructure setup. Build the application without listening. Await `inject` for request contracts; it boots plugins. Await `ready` when inspecting composed instances, and register awaited `close` cleanup immediately so failures release resources.

Keep relevant plugin registrations and scopes real. Assert status, headers, serialized payload and effects where they matter. Preserve contract-relevant distinctions in observed responses and effects; decoding, normalization, or test helpers must not conceal a violation. Exercise rejected input and forbidden access, including sibling scopes when placement determines protection. Fabricating an authenticated user proves downstream authorization, not credential verification.

Injection uses no socket. Real transport, listening hooks, TLS, streaming backpressure and disconnect behavior require a running server and client. State what the boundary demonstrates.

Use the target database engine for constraints, transactions, locking and visibility. Align container, application and connection lifetimes; isolate fixtures across parallel tests. A test-side rollback cannot clean up another connection's committed work. Coordinate competing operations at meaningful boundaries, await every outcome, and verify committed state independently.

Run the relevant tests, confirm discovery and cleanup, and report any infrastructure or transport boundary not exercised.
