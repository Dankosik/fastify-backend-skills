---
name: fastify-observability
description: "Operability. Use when Fastify logs, metrics, traces, probes, or shutdown need implementation or diagnosis."
---

# Fastify Observability

Design for **operability**: begin with the operational question and choose its smallest useful signal. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Follow the existing instrumentation through the affected operation. Use Fastify's configured request logger and correlation context. Keep errors structured and redact credentials and sensitive data before emission. A caller-provided request identifier is untrusted input, not identity authority; choose its acceptance deliberately.

Metrics describe aggregate behavior, traces explain a path, and logs preserve actionable events. Bound metric dimensions; use route templates instead of raw URLs or user identifiers. Distinguish logical outcomes from retry attempts and HTTP completion from durable business completion.

Choose lifecycle hooks that observe the event being claimed. Avoid duplicating existing request logs or spans. Preserve the telemetry stack and check installed Fastify API support.

Treat probes as control inputs: liveness reflects local progress, readiness reflects ability to serve. Consider how dependency failures change routing or restart behavior.

Follow shutdown through admission, in-flight work, and resource release. Await Fastify closure; release owned clients in the appropriate close hook and handle long-lived connections when relevant. Align draining with the environment's deadline.

Verify emitted signals and the affected lifecycle behavior. Report what was observed, separating local evidence from deployment behavior.
