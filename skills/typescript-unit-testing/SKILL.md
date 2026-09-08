---
name: typescript-unit-testing
description: "Behavior. Use for TypeScript backend unit tests, assertions, mocks and deterministic fixtures with Node.js test runner, Vitest or Jest."
---

# TypeScript Unit Testing

**Behavior first.** Find the observable promise. Choose cases that distinguish correct behavior from a plausible defect; derive expected results independently. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Read existing tests, runtime, module system and commands. Preserve the testing stack. Executing TypeScript through a transformer or type stripping does not establish type correctness; identify the project's compiler check.

Exercise functions and components directly. Prefer real values and fixtures. Mock a collaborator when its responses or effects define the scenario; verify calls when those calls are the requirement. Avoid broad module mocks and casts that hide an impossible fixture.

Await asynchronous assertions, nested tests and cleanup. Make rejection tests fail when the operation unexpectedly succeeds. Control time and randomness when relevant; advance promise-driven timers deliberately and bound completion without arbitrary sleeps.

Treat clearing call history, resetting implementations, restoring spies and clearing module caches as different operations. Check the runner's semantics and import timing before relying on isolation. Restore changed globals, environment and clocks; avoid concurrent tests sharing those mutations.

Challenge each test: could the defect survive it, or would harmless refactoring break it? Run tests and type checks, confirm discovery, and state any boundary left untested.
