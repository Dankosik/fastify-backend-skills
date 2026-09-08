---
name: typescript-debugging
description: "Causality. Use for an uncertain TypeScript or Fastify defect, startup failure, rejected promise, hanging request, or flaky behavior."
---

# TypeScript Debugging

**Causality.** Find the first observable divergence between expected behavior and the real execution path. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Build the smallest repeatable signal for the reported symptom. Read the error and its cause, affected callers, effective configuration, and resolved runtime. Separate compiler failures, module-loading failures, plugin boot failures, and request execution before proposing a fix.

Treat types as claims about runtime values. Inspect the parser, schema, transformation, or assertion that established the claim. A cast added at the failure site cannot explain why the value was wrong.

Choose the next observation for its ability to distinguish plausible causes. In Fastify, follow registration order, encapsulation, and the actual hook and reply path. Across asynchronous boundaries, account for which promise, callback, timer, stream, or event owns completion and failure.

Change one causal variable at a time. Control scheduling and shared state enough to expose intermittent defects. Use source maps and targeted runtime diagnostics when they improve the signal; keep captured payloads and secrets protected.

Fix the cause at its owner, replay the original case, and check relevant neighboring paths. Remove temporary instrumentation. Finish with a supported explanation and observed verification; if evidence is incomplete, identify the remaining hypothesis and the next discriminating check.
