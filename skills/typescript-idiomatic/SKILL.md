---
name: typescript-idiomatic
description: "Use for TypeScript representation, type-contract, or transformation decisions where runtime semantics or readability need attention."
---

# TypeScript Idiomatic

**Contracts.** Make runtime values and static types agree. Identify caller-visible absence, identity, mutation, ordering, effects, and failures. Follow repository conventions. Honor the requested outcome and preserve settled choices outside the requested change.

Treat untrusted values as unknown until the existing boundary validates or narrows them. Types disappear at runtime; an assertion, generic argument, or non-null assertion cannot establish a fact. Keep schema-derived types aligned with the schema instead of maintaining competing descriptions.

Prefer inference for local expressions and explicit contracts where they clarify a public boundary. Use discriminated unions for real alternatives and exhaustive handling where the alternatives are closed. Let generics preserve a meaningful relationship; remove parameters that merely decorate a function. Use `satisfies` to check conformance while retaining useful inference, not as runtime validation.

**Reuse.** Prefer existing runtime, Fastify, or library operations over handwritten utility logic when their semantics match. Keep wrappers only for domain meaning or adaptation. Use ordinary functions and objects for application logic; classes should own state or invariants. Keep effects and branching readable.

Preserve distinctions between missing, undefined, null, and valid falsy values. Readonly types express access restrictions, not deep immutability. Check aliasing and shallow copies before promising independence.

For review, locate the affected expression, show an input or caller condition that violates the contract, and check relevant narrowing or guards before reporting a defect. Distinguish a preference from a bug; no findings is a valid result. Explain the smallest justified change without editing files. For implementation, verify the affected runtime or type contract with focused checks that would fail for a plausible violation; preserve required project checks and report actual results.
