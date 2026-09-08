---
name: typescript-integrations
description: "Delivery semantics. Use when TypeScript outbound calls, retries, messages, jobs, or caches must remain correct across delay, duplication, failure, or restart."
---

# TypeScript Integrations

**Delivery semantics.** Determine what can repeat, disappear, or remain unknown at each process boundary. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Trace intent through effect to acknowledgement. A connection lost after a write can leave success unknown. Tie safe replay to a stable operation identity and equivalent request meaning; preserve uncertainty until the integration's actual contract resolves it.

Budget attempts, total time, active work, queued work, and response consumption together. Put retry policy where effect semantics are known. Propagate cancellation through supported client APIs and observe actual termination; racing a promise against a timer only settles the race. Consume or cancel response bodies so abandoned requests do not exhaust connection capacity.

For messages and jobs, follow commit, publication, acknowledgement, redelivery, and process death. Choose durability and coordination to match the promised outcome. A detached promise or in-process event does not survive a restart. Broker guarantees do not automatically cover database or HTTP effects.

For caches, identify the authority, key identity, freshness contract, and invalidation owner. Consider concurrent stale refill and origin load during failure. A measured need should justify the cache.

Challenge the most consequential interruption point and observe the actual effect. Finish when that path has bounded recovery and evidence appropriate to the client, database, or broker involved.
