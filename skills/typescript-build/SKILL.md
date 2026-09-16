---
name: typescript-build
description: "Resolution. Use for TypeScript compilation, Node.js module loading, packaging, dependency, or toolchain failures and requested build changes."
---

# TypeScript Build

**Resolution.** Identify the affected build or execution step and inspect the effective configuration that can explain it. Follow module resolution, transformation, dependency selection, or packaging when the task points to that layer rather than surveying the entire toolchain. Honor the requested outcome and preserve settled choices outside the requested change.

Match module resolution to the actual executor. Node's ESM/CJS rules, package exports, file extensions, and conditional entry points can differ from a development runner or bundler. TypeScript path aliases do not rewrite runtime imports. A passing development command does not prove the production artifact loads.

Keep checking separate from execution. Native type stripping and transpilers may execute TypeScript without checking it or honoring the full compiler configuration. Select syntax and library declarations for the supported runtime; declarations do not supply runtime features. For compiler upgrades, verify compatibility with tools that consume the compiler API.

For dependency changes or failures, trace resolution to its origin. Declare directly imported packages in the consuming workspace with the appropriate dependency scope; do not rely on transitive hoisting. Preserve package manager, lockfile, install policies, and module system unless changing them is the task. Make the smallest justified update; inspect resulting versions and relevant vulnerability evidence. Use the existing frozen-install mechanism when reproducibility is the claim.

For diagnosis or review, explain the finding without editing. For requested changes, validate the affected layer: type checking, transformation, tests, package contents, or artifact startup with production dependencies. Reuse applicable results for the same revision and environment while preserving required checks. Report what changed, what was verified, and any blocker; successful transpilation alone does not establish a sound build.
