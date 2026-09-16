---
name: typescript-data
description: "Use for TypeScript backend query shape, runtime row conversion, transaction consistency, or schema migration decisions."
---

# TypeScript Data

**Atomicity where required.** Start from the property being changed: query shape, runtime row conversion, transaction consistency, or schema compatibility. Follow the relevant mechanism in the project's actual driver or ORM. Honor the requested outcome and preserve settled choices outside the requested change.

For queries and mapping, work backward from the required result to a bounded query and fetch plan. Inspect emitted SQL when the claim concerns query behavior instead of assuming an ORM method is cheap. Keep runtime row conversion explicit where decimals, large integers, dates, nulls, or JSON differ from their declared TypeScript shape. A pure mapping check can use representative values from the driver's established contract; it does not prove what the driver returns at runtime.

For transactions and concurrency, identify the invariant that must survive overlap or partial failure. Follow the transaction's connection or client, completion, and resource owner. Every participating query must use that context and finish within its lifetime. A promise created inside a transaction is not automatically part of it.

Use constraints, conditional writes, or locking where the invariant requires arbitration. An existence check followed by insertion cannot settle a race. Choose conflict and retry behavior deliberately, distinguishing known rollback from an uncertain commit. A database rollback cannot undo an external effect.

For schema changes, use the existing migration mechanism as authority and consider application versions that must coexist; a migration is more than the final model definition.

For review, explain the relevant finding without editing. For implementation, verify the changed property: mapping at the conversion boundary, query behavior through actual queries, and isolation, constraints, or locking on the relevant database. For transaction claims, observe committed state independently and release resources on failure. Mocks can test orchestration, not database guarantees. State unavailable evidence precisely; do not invent a database setup for a pure mapping task or call a weaker check proof of a stronger property.
