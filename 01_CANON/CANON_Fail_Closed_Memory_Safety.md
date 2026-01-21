CANON — FAIL-CLOSED MEMORY SAFETY INVARIANT

Invariant:
All memory access must be provably safe by construction. Any operation whose safety cannot be statically proven is forbidden from execution.

Enforcement:
Safety proof is a precondition of existence. Code that cannot demonstrate memory safety at compile time must not produce a runnable artifact.

Fail-Closed Condition:
If memory safety cannot be proven, the system must refuse to build.

Scope:
This invariant applies to all execution paths, including foreign interfaces, abstractions, and optimizations. No exception exists without an explicit, isolated safety boundary that prevents undefined behavior from propagating beyond it.

Irreversibility:
Undefined behavior is treated as an unrecoverable integrity breach. Once introduced, it invalidates all downstream correctness claims.

Authority:
This invariant supersedes performance, convenience, and compatibility concerns. Any mechanism that violates this rule is invalid regardless of utility.
