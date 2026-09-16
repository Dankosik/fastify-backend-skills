---
name: fastify-security
description: "Use for Fastify access control, tenant isolation, credential verification, request protections, and browser or proxy trust."
---

# Fastify Security

**Authorization.** Identify the subject, action, resource, and trusted context on the affected path. Authentication establishes identity; resource access still needs its own decision. Honor the requested outcome and preserve settled choices outside the requested change.

Follow the actual plugin scope and hook order before changing security behavior. Place header-based authentication before body parsing when it needs no body. Register cookie parsing before hooks that consume cookies. Ensure a rejection stops the protected operation; preserve each route's intended access.

Use the established identity integration and compatible plugins. Verify tokens through their verification API, preserving signature, algorithm, issuer, audience, and lifetime requirements. Decoding claims does not make them trusted. Enforce ownership and tenant scope where the protected operation executes; caller-supplied identifiers or claims are not permission.

When browser credentials are involved, reason separately about automatically attached credentials. Cookie attributes, CSRF defenses, and credentialed CORS must fit the actual client contract. CORS does not authorize a request. Match protections to actual exposure.

When proxy or request protections are affected, trust forwarding headers only through the known proxy boundary. Relate body limits, timeouts, and rate-limit identity and storage to the actual deployment. A receive timeout does not cancel application work. Do not turn a local permission change into an unrelated deployment audit.

For review, connect attacker-controlled input to a reachable protected operation and identify the missing or ineffective guard without editing. Check actual hook scope and existing enforcement; distinguish a demonstrated access defect from a hardening hypothesis. Never present an untested exploit as observed. For implementation, exercise the real security path and the denial that would expose the flaw; assert that no protected effect occurred alongside the relevant successful case. Report the boundary exercised and any missing evidence, not a broader security guarantee.
