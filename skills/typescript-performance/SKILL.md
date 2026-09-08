---
name: typescript-performance
description: "Evidence. Use for a reported Node.js latency, throughput, CPU, memory, or startup problem, or a requested backend benchmark."
---

# TypeScript Performance

**Evidence.** Identify the affected workload, metric, runtime, and resource limit. Establish comparable conditions. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Distinguish time spent executing JavaScript from time spent waiting for dependencies, worker pools, queues, or the network. Use a CPU profile for computation, retained-object evidence for leaks, and event-loop measurements for responsiveness. Event-loop utilization is not CPU utilization, and rising RSS alone does not establish a JavaScript heap leak. Account for diagnostic overhead and sensitive data in captures.

Form a falsifiable hypothesis and measure what separates plausible causes. Remove demonstrated waste before adding caches, parallelism, worker threads, or tuning flags. Workers can help CPU-heavy JavaScript; moving ordinary asynchronous I/O into workers rarely solves its bottleneck.

Measure service behavior under representative load, including payload sizes, errors, concurrency, and saturation. Keep the load generator from becoming the hidden limit. Compare latency distributions and throughput, not only averages. For isolated operations, control warmup, repeated samples, input shape, and observable results; a microbenchmark gain does not prove an endpoint gain.

Preserve correctness and resource bounds while optimizing. Report the measured cause, intervention, before-and-after result, and remaining uncertainty. If the evidence is inconclusive, keep the simpler correct implementation rather than claiming a speedup.
