---
name: typescript-build
description: "Resolution. Use for TypeScript compilation, Node.js module loading, packaging, dependency, or toolchain failures and requested build changes."
---

# TypeScript Build

**Resolution.** Follow source through checking and transformation to the file Node executes. Inspect runtime, compiler, package manager, scripts, effective configuration, and resolved dependencies. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Match module resolution to the actual executor. Node's ESM/CJS rules, package exports, file extensions, and conditional entry points can differ from a development runner or bundler. TypeScript path aliases do not rewrite runtime imports. A passing development command does not prove the production artifact loads.

Keep checking separate from execution. Native type stripping and transpilers may execute TypeScript without checking it or honoring the full compiler configuration. Select syntax and library declarations for the supported runtime; declarations do not supply runtime features. Verify compatibility of compiler upgrades with tools that consume the compiler API.

Trace dependency failures to their origin. Declare directly imported packages in the consuming workspace with the appropriate dependency scope; do not rely on transitive hoisting. Preserve the package manager, lockfile, install policies, and module system. Make the smallest justified update; inspect resulting versions and vulnerability evidence. Use the existing frozen-install mechanism when reproducibility is the claim.

Validate the affected layer: type checking, transformation, tests, package contents, or artifact startup with production dependencies. Explain the resolution mismatch and verified correction; successful transpilation alone does not establish a sound build.
