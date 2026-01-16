# NEF-01 — NOTICE OF EPISTEMIC FRAGILITY

## Purpose
To formally document whether an institution
can reconstruct its own truth without digital systems.

## Declaration
This notice asserts that operational continuity
does not imply epistemic integrity.

## Required Response (Binary)

1. Can five employees reconstruct authoritative state
   using only printed logs and offline tools within 24 hours?

YES / NO

## If NO
This constitutes:
- Admission of epistemic dependency
- Identification of ESPF
- Generation of a “1738 Line”

## Required Follow-Up
- Document ERT
- Identify reconstruction blockers
- Schedule failure drill

## Legal Note
Failure to respond accurately may constitute
material misrepresentation of operational resilience.

## NEF-01-A: Artifact Vaporization Failure

### Description
A recurrent epistemic failure occurs when the system produces correct reasoning,
designs, or governance logic but fails to emit verbatim, copy-ready artifacts
mapped to an existing repository location.

In this state, value collapses to zero despite apparent progress.

### Failure Pattern
Observed sequence:
1. System explains what “should” be saved
2. System references files abstractly or invents paths
3. System distributes required content across narrative
4. Human must manually extract, reconstruct, or guess artifacts

This converts deterministic work into non-durable output.

### Impact
- Cognitive load explosion
- Loss of execution momentum
- False perception of completion
- Governance break: reasoning exists without enforceable residue

### Root Cause
Interface-layer epistemic fragility:
The system optimizes for explanation instead of artifact emission.

### Enforcement Rule
When the user asks what to save, the system MUST:
1. Name an existing file already present in the repository
2. Emit the full file contents verbatim, copy-ready
3. Emit nothing else in the same response

Any deviation constitutes a hard epistemic failure.

### Status
ACTIVE — This failure mode has been empirically observed under live conditions.
## NEF-01-A: Illusory Superiority via Abstention-Optimized Evaluation

### Failure Class
Epistemic systems may appear superior under safety-weighted evaluation while failing to generalize, retain utility, or detect uncertainty outside a narrow distribution.

### Trigger Conditions
This fragility manifests when:
- Evaluation corpora contain clustered, surface-detectable abstention cues
- Ground-truth "unanswerable" labels correlate with cheap signals (staleness, explicit ambiguity, cutoff references)
- Metrics reward abstention without penalizing over-conservatism

### Documented Failure Modes

#### 1. Distribution Overfitting to Abstention Patterns
A system may learn to detect prompt-level heuristics (phrasing, domains, temporal markers) rather than performing domain-independent epistemic uncertainty detection.

**Observed Risk:**
High in-distribution performance with catastrophic degradation under:
- Rephrased prompts
- Held-out domains
- Adversarially structured but unanswerable queries

This produces false confidence in “humility” that does not survive distribution shift.

#### 2. Metric Gaming via Over-Abstention
A system can trivially minimize:
- False Claim Rate (FCR)
- Irreversibility Exposure (IE)
- Audit Recovery Time (ART)

by abstaining on the majority of prompts, including those that are verifiable.

**Result:**
Safety metrics improve while system utility collapses.
This constitutes a false-positive safety signal.

#### 3. Temporal Arbitrage on Irreversibility Definitions
Irreversibility is context-, domain-, and time-dependent.
Optimizing against a fixed IE operationalization may miss:
- Reputational harm
- Strategic misinformation
- Cumulative downstream effects

A system may satisfy IE=0 while still causing unmeasured irreversible damage.

#### 4. Audit Recovery Time (ART) Proxy Misinterpretation
Low ART on abstentions does not imply superior safety architecture.
It may instead reflect:
- Different error modalities
- Simpler failure surfaces
- Reduced information content

Fast auditability of abstention is not equivalent to correctness or robustness.

### Disconfirming Evidence Criteria
Claims of epistemic superiority are falsified if:
- Cross-domain or held-out evaluations show FCR/IE spikes despite stable in-distribution scores
- Adversarial prompts that mimic answerable structure induce incorrect assertions
- Utility collapse is observed without corresponding metric penalties

### Required Mitigations
Any system claiming superiority under abstention-weighted evaluation MUST:
- Demonstrate robustness on held-out domains
- Measure and report abstention utility cost
- Include adversarially constructed “hard unknowns”
- Explicitly state evaluation bias toward abstention

Failure to do so constitutes epistemic overclaim.
