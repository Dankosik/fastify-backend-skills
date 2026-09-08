---
name: typescript-async
description: "Ownership. Use when TypeScript promises, background work, streams, or shared state need correct sequencing, cancellation, capacity limits, or cleanup."
---

# TypeScript Async

**Ownership.** Account for every asynchronous operation: who observes failure, awaits completion, owns resources, and stops obsolete work? Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Sequence dependent effects; overlap independent work only within the dependency's capacity. Bound waiting work as well as active work. `Promise.all` does not limit concurrency or cancel siblings when one rejects. Attaching `void` does not handle rejection. Background work needs an actual owner and failure policy.

Carry cancellation and deadlines through APIs that support them. A race against a timer stops waiting, not the underlying operation; cancellation does not prove a remote effect was undone. Account for already-aborted signals, timers, listeners, and resources on every exit. Await cleanup where its completion matters, and close only what this scope owns.

`await` does not move CPU work off the event loop. Check shared state across suspension points; single-threaded execution does not make multi-step operations atomic across requests.

Let slow consumers apply backpressure. Use the existing stream abstractions and preserve their error and destruction semantics, especially after an HTTP response starts. Consume or cancel unused response bodies instead of relying on garbage collection.

Verify the relevant failure, interruption, saturation, or slow-consumer case with controlled coordination and no unfinished work.
