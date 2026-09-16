---
name: typescript-integrations
description: "Delivery semantics. Use when TypeScript outbound calls, retries, messages, jobs, or caches must remain correct across delay, duplication, failure, or restart."
---

# TypeScript Integrations

**Delivery semantics.** Determine what can repeat, disappear, or remain unknown at the affected boundary. Honor the requested outcome and preserve settled choices outside the requested change.

For outbound calls, trace intent through effect to acknowledgement. A connection lost after a write can leave success unknown. Tie safe replay to a stable operation identity and equivalent request meaning; preserve uncertainty until the integration's actual contract resolves it.

Budget attempts, total time, active work, queued work, and response consumption together. Put retry policy where effect semantics are known. Propagate cancellation through supported client APIs and observe actual termination; racing a promise against a timer only settles the race. Consume or cancel response bodies so abandoned requests do not exhaust connection capacity.

For messages and jobs, follow commit, publication, acknowledgement, redelivery, and process death. Choose durability and coordination to match the promised outcome. A detached promise or in-process event does not survive a restart. Broker guarantees do not automatically cover database or HTTP effects.

For caches, identify the authority, key identity, freshness contract, and invalidation owner. Consider concurrent stale refill and origin load during failure. Do not introduce a cache as an unmeasured performance remedy. When a cache is explicitly required, implement its agreed semantics without reopening that decision; do not claim an unmeasured speedup.

For analysis, explain the affected boundary and uncertainty without editing. For implementation, challenge the consequential failure for that boundary: response loss or replay, message redelivery, or stale cache refill. Finish with bounded recovery or freshness behavior and evidence appropriate to the claim, not checks of every integration category. State unavailable evidence and preserve required project checks.
