---
name: fastify-routes
description: "Contract. Use when Fastify routes, validation, serialization, hooks, or errors change observable HTTP behavior."
---

# Fastify Routes

**Contract.** Start from accepted input, status, headers, response shape, and failure behavior. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Keep runtime validation and TypeScript inference aligned through the project's existing schema library, compiler, and type provider. A type assertion does not validate a request. Treat compiled schemas as trusted application code; caller-supplied schemas cannot safely enter that compilation path.

Reason about what the validator actually does: coercion, defaults, unknown properties, and absent versus null values affect the contract. Ensure validation covers the content types the parser accepts. Keep database lookups and other business checks after structural validation, outside schema compilation and initial validation.

Return intentional public data and use response schemas where the contract calls for them. Serialization can filter or transform output; it does not replace authorization. Preserve the established error format and appropriate status; conceal internal exception details.

Choose hooks by when their inputs exist and what remains changeable. Keep one owner for sending the response. Use the scoped error handler for translation; `onError` observes failures and cannot send a replacement response.

Exercise the changed route through Fastify, including meaningful invalid input or failure. Inspect serialization and application effects; a direct handler call cannot prove the HTTP contract.
