---
name: fastify-testing
description: "Mechanism. Use for Fastify tests of routing, schemas, plugin composition, authentication, lifecycle and infrastructure, including Testcontainers integration."
---

# Fastify Testing

**Prove the mechanism.** Choose the smallest boundary containing the mechanism behind the promised behavior and a scenario exposing its relevant failure. Calling a handler directly cannot establish validation, serialization or hooks. Honor the requested outcome and preserve settled choices outside the requested change.

Preserve the project's runner, schema library and infrastructure setup. For in-process request contracts, build the application without listening and await `inject`; it boots plugins. Await `ready` when inspecting composed instances, and register awaited `close` cleanup immediately so failures release resources.

Keep relevant plugin registrations and scopes real. Assert status, headers, serialized payload and effects where they matter. Preserve contract-relevant distinctions; decoding, normalization, or helpers must not conceal a violation. Exercise rejected input or forbidden access when that contract changes, including sibling scopes when placement determines protection. Fabricating an authenticated user proves downstream authorization, not credential verification.

Injection uses no socket. Start a server and client when the claim depends on real transport, listening hooks, TLS, streaming backpressure or disconnect behavior. Do not use a network listener merely to test ordinary validation, or present injection as transport evidence.

For database guarantees, use the target engine for constraints, transactions, locking and visibility. Align container, application and connection lifetimes; isolate fixtures across parallel tests. A test-side rollback cannot clean up another connection's committed work. Coordinate competing operations at meaningful boundaries, bound waits, await every outcome, and verify committed state independently.

For test design or review, explain the necessary boundary without editing unless implementation is requested. When implementing tests, run the relevant existing tasks, confirm discovery and cleanup, and reuse applicable results for the same revision and environment while preserving required checks. Report unavailable infrastructure or transport verification precisely; do not create an unsolicited test environment as a new completion gate or substitute mocks as proof of a real mechanism.
