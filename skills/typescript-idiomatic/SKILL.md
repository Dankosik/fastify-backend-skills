---
name: typescript-idiomatic
description: "Contracts. Use when writing or simplifying TypeScript values, functions, types, or collection transformations while preserving runtime behavior."
---

# TypeScript Idiomatic

**Contracts.** Make runtime values and static types agree. Identify caller-visible absence, identity, mutation, ordering, effects, and failures. Follow repository conventions. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Treat untrusted values as unknown until the existing boundary validates or narrows them. Types disappear at runtime; an assertion, generic argument, or non-null assertion cannot establish a fact. Keep schema-derived types aligned with the schema instead of maintaining competing descriptions.

Prefer inference for local expressions and explicit contracts where they clarify a public boundary. Use discriminated unions for real alternatives and exhaustive handling where the alternatives are closed. Let generics preserve a meaningful relationship; remove parameters that merely decorate a function. Use `satisfies` to check conformance while retaining useful inference, not as runtime validation.

Choose ordinary functions, objects, and collection operations when they express the task directly. Classes fit owned state or invariants; avoid classes that merely wrap functions. Keep effects and branching readable instead of compressing them into transformations.

Preserve distinctions between missing, undefined, null, and valid falsy values. Readonly types express access restrictions, not deep immutability. Check aliasing and shallow copies before promising independence.

Finish with focused checks of the behavior and type contract that changed.
