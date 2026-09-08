---
name: typescript-data
description: "Atomicity. Use when TypeScript backend queries, transactions, migrations, or data mappings affect consistency, concurrency, or persistence behavior."
---

# TypeScript Data

**Atomicity.** Start with the invariant that must survive overlapping requests or partial failure. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Follow the operation through the project's actual driver or ORM. Identify the transaction's connection or client, when work completes, and who releases resources. Every participating query must use that transaction context and finish within its lifetime. A promise created inside a transaction is not automatically part of it.

Use constraints, conditional writes, or locking where the invariant requires arbitration. An existence check followed by insertion cannot settle a race. Choose conflict and retry behavior deliberately, distinguishing known rollback from an uncertain commit. A database rollback cannot undo an external effect.

Work backward from the required result to a bounded query and fetch plan. Inspect emitted SQL and query behavior instead of assuming an ORM method is cheap. Keep runtime row conversion explicit where decimals, large integers, dates, nulls, or JSON differ from their declared TypeScript shape.

Use the existing migration mechanism as schema authority. Consider the application versions that must coexist during a schema change; a migration is more than the final model definition.

Verify the claimed boundary with the relevant database and real transaction behavior. Observe committed state independently and release resources on failure. Mocks can test orchestration but cannot establish isolation, constraints, or locking.
