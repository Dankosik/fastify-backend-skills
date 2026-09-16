---
name: fastify-observability
description: "Operability. Use when Fastify logs, metrics, traces, probes, or shutdown need implementation or diagnosis."
---

# Fastify Observability

Design for **operability**: begin with the operational question and choose its smallest useful signal. Honor the requested outcome and preserve settled choices outside the requested change.

Follow the existing instrumentation through the affected operation. Use Fastify's configured request logger and correlation context. Keep errors structured and redact credentials and sensitive data before emission. A caller-provided request identifier is untrusted input, not identity authority; choose its acceptance deliberately.

Metrics describe aggregate behavior, traces explain a path, and logs preserve actionable events. Bound metric dimensions; use route templates instead of raw URLs or user identifiers. Distinguish logical outcomes from retry attempts and HTTP completion from durable business completion.

Choose lifecycle hooks that observe the event being claimed. Avoid duplicating existing request logs or spans. Preserve the telemetry stack; check installed Fastify API support when the change depends on it.

When probes are affected, treat them as control inputs: liveness reflects local progress, readiness reflects ability to serve. Consider how dependency failures change routing or restart behavior.

When shutdown is affected, follow admission, in-flight work, and resource release. Await Fastify closure; release owned clients in the appropriate close hook and handle long-lived connections when relevant. Align draining with the environment's deadline. A log or metric change does not itself require a shutdown audit.

For diagnosis or review, explain the finding without editing. When implementing, verify the changed signals and affected lifecycle behavior. Report what was observed, separating local evidence from deployment behavior; do not add unrelated probes, saturation checks, or telemetry as completion requirements.
