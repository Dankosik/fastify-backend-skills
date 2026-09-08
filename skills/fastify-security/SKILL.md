---
name: fastify-security
description: "Authorization. Use when Fastify authentication, resource permissions, tenancy, browser credentials, proxy trust, or request protections cross a security boundary."
---

# Fastify Security

**Authorization.** Identify the subject, action, resource, and trusted context. Authentication establishes identity; resource access still needs its own decision. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Follow the actual plugin scope and hook order before changing security behavior. Place header-based authentication before body parsing when it needs no body. Register cookie parsing before hooks that consume cookies. Ensure a rejection stops the protected operation; preserve each route's intended access.

Use the established identity integration and compatible plugins. Verify tokens through their verification API, preserving signature, algorithm, issuer, audience, and lifetime requirements. Decoding claims does not make them trusted. Enforce ownership and tenant scope where the protected operation executes; caller-supplied identifiers or claims are not permission.

Reason separately about automatically attached browser credentials. Cookie attributes, CSRF defenses, and credentialed CORS must fit the actual client contract. CORS does not authorize a request. Match protections to actual exposure.

Trust forwarding headers only through the known proxy boundary. Relate body limits, timeouts, and rate-limit identity and storage to the actual deployment. A receive timeout does not cancel application work.

Exercise the denial that would expose the flaw and assert that no protected effect occurred, alongside the relevant successful case.
