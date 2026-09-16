---
name: typescript-performance
description: "Use to audit or improve Node.js latency, throughput, CPU, memory, or startup behavior, or to design and run a requested benchmark."
---

# TypeScript Performance

**Evidence.** Identify the affected workload, metric, runtime, and resource limit. Honor the requested outcome and preserve settled choices outside the requested change. For an audit without runtime evidence, separate code-supported properties from bottleneck hypotheses and propose discriminating measurements; do not require a profiling environment merely to provide an analysis.

Distinguish time spent executing JavaScript from time spent waiting for dependencies, worker pools, queues, or the network. Choose diagnostics for the hypothesis: CPU profiles for computation, retained-object evidence for leaks, and event-loop measurements for responsiveness. Event-loop utilization is not CPU utilization, and rising RSS alone does not establish a JavaScript heap leak. Account for diagnostic overhead and sensitive data in captures.

When optimizing, establish comparable conditions and measure what separates plausible causes. Remove demonstrated waste before adding caches, parallelism, worker threads, or tuning flags speculatively. Workers can help CPU-heavy JavaScript; moving ordinary asynchronous I/O into workers rarely solves its bottleneck. Implement an explicitly requested mechanism without reopening that decision, but do not claim a speedup without evidence.

Match measurement to the claim. Service claims need representative load, including relevant payload sizes, errors, concurrency, and saturation. Keep the load generator from becoming the hidden limit. Compare latency distributions and throughput, not only averages. For isolated operations, control warmup, repeated samples, input shape, and observable results; a microbenchmark gain does not prove an endpoint gain.

For analysis, return supported findings and hypotheses without editing. For requested implementation, preserve correctness and resource bounds; report the intervention, actual before-and-after evidence, and its limits. If evidence is unavailable or inconclusive, say so rather than claiming a speedup or adding speculative complexity.
