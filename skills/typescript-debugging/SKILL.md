---
name: typescript-debugging
description: "Causality. Use for an uncertain TypeScript or Fastify defect, startup failure, rejected promise, hanging request, or flaky behavior."
---

# TypeScript Debugging

**Causality.** Find the first observable divergence between expected behavior and the real execution path. Honor the requested outcome and preserve settled choices outside the requested change.

Build the smallest repeatable signal for the reported symptom. Start with the error and its cause; inspect callers, effective configuration, or the resolved runtime when they can distinguish plausible causes. Locate the failing layer: compilation, module loading, plugin boot, or request execution.

Treat types as claims about runtime values. Inspect the parser, schema, transformation, or assertion that established the relevant claim. A cast added at the failure site cannot explain why the value was wrong.

Choose the next observation for its ability to distinguish plausible causes. In Fastify, follow the implicated registration, encapsulation, hook, and reply boundaries. Across asynchronous boundaries, account for which promise, callback, timer, stream, or event owns completion and failure.

Change one causal variable at a time. Control scheduling and shared state enough to expose intermittent defects. Use source maps and targeted runtime diagnostics when they improve the signal; keep captured payloads and secrets protected.

For diagnosis, finish with the supported cause or the next discriminating observation, without editing files. When a fix is requested, fix the cause at its owner, replay the original case, and check affected neighboring paths. Remove temporary instrumentation. Report the observed result and remaining uncertainty; do not turn unrelated investigation into a completion gate.
