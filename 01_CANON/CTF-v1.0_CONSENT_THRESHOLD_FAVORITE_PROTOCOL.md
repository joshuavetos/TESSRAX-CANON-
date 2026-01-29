01_CANON/CTF-v1.0_CONSENT_THRESHOLD_FAVORITE_PROTOCOL.md

PROTOCOL SPECIFICATION: CTF-v1.0
Alias: Consent-Threshold Favorite
Class: Two-Round System / Single-Ballot / Hybrid Cardinal-Ordinal
Status: CANONICAL
Scope: Deterministic Social Choice // Single-Winner Elections
Objective: Maximize favorability among broadly acceptable candidates while eliminating strategic vote-splitting (“Predator’s Dilemma”) and post-hoc parameter manipulation.

────────────────────────────────────────────────────────
	1.	SYSTEM INTENT
────────────────────────────────────────────────────────

CTF-v1.0 is a deterministic voting protocol designed to satisfy the following hard requirements:

• Eliminate vote-splitting between ideologically similar candidates
• Minimize incentives for strategic dishonesty (approval truncation)
• Preserve a cognitively simple ballot usable without technical literacy
• Enforce fail-closed behavior under ambiguity or malformed input
• Lock all outcome-relevant parameters prior to ballot ingestion
• Produce results that are fully auditable, reproducible, and recount-safe

CTF-v1.0 explicitly rejects narrative reconciliation, probabilistic arbitration, and discretionary tie-breaking beyond pre-committed rules.

────────────────────────────────────────────────────────
2. PARAMETER LAW (DETERMINISTIC LOCK)
────────────────────────────────────────────────────────

All parameters in this section MUST be fixed, published, and cryptographically locked before any ballot is cast. No post-hoc adjustment is permitted.

2.1 Finalist Cap (M)

M defines the maximum number of candidates allowed to advance beyond the Viability Gate.

• Executive offices (Mayor / Governor / President):
M = 3

• Legislative or Council (Single-Seat):
M = 4

• At-Large or Multi-Winner Contexts:
M = 6

2.2 Viability Threshold (T)

T defines the minimum approval percentage required for a candidate to qualify.

• T₀ (Default Threshold): 20.00% of valid ballots
• T_min (Floor): 8.00%
• Δ (Decrement Step): 2.00 percentage points

Fallback Protocol:

• If fewer than 2 candidates meet T₀, reduce T by Δ iteratively
• Stop when at least 2 candidates qualify OR T = T_min
• Emergency Path:
If T = T_min and fewer than 2 candidates qualify, ignore T and select the Top-2 candidates by raw Approval count

This emergency path exists solely to guarantee liveness and does not alter incentives under normal conditions.

────────────────────────────────────────────────────────
3. BALLOT SYNTAX & SANITATION
────────────────────────────────────────────────────────

3.1 Ballot Structure

Each ballot permits two independent markings per candidate:

• [Approve] — indicates acceptability
• [Favorite] — indicates strongest preference

3.2 Sanitation Rules (Fail-Closed)

• A voter MAY mark any number of [Approve]
• A voter MAY mark at most ONE [Favorite]

Coherency Rule:
• If a [Favorite] is marked without a corresponding [Approve], the system SHALL auto-fill [Approve]
Rationale: Intent is unambiguous; punishing clerical errors violates voter safety

Overvote (Favorite):
• If more than one [Favorite] is marked:
– Void ALL [Favorite] marks on that ballot
– Preserve ALL valid [Approve] marks

Undervote (Favorite):
• If zero [Favorite] marks are present:
– Count [Approve] marks only
– Ballot contributes no weight in the Final Decision phase

Malformed Ballots:
• Ballots with ambiguous or unreadable markings are rejected in full and logged

────────────────────────────────────────────────────────
4. TABULATION LOGIC
────────────────────────────────────────────────────────

4.1 Phase 1 — Viability Gate (Audit Step A)

• Count total [Approve] marks for each candidate
• Compute Approval Percentage = Approvals / Total Valid Ballots
• Define Qualifier Set Q = { candidates where Approval ≥ T }

4.2 Cap Enforcement (if |Q| > M)

If the number of qualifiers exceeds M:

• Sort Q by [Favorite] count in descending order
• Retain the top M candidates
• Discard remaining qualifiers

Rationale:
• Cap resolution uses the decision-aligned signal ([Favorite]) rather than the gate signal ([Approve])
• This prevents strategic truncation from influencing cap survival

4.3 Phase 2 — Final Decision (Audit Step B)

• Discard all non-qualifying candidates
• Tally [Favorite] marks for candidates in Q
• Winner = candidate with maximum [Favorite] count

Tie-Break Order:
	1.	Higher Approval count
	2.	Pre-published deterministic candidate ordering

────────────────────────────────────────────────────────
5. INCENTIVE STRUCTURE & STRATEGIC SAFETY
────────────────────────────────────────────────────────

Voter Safety Invariant:

Approving an additional acceptable candidate CANNOT reduce the probability that the voter’s Favorite wins.

Proof Sketch:

• Qualification depends solely on each candidate’s own approval count
• Approving a backup candidate does not raise T or lower another candidate’s approval
• Cap enforcement is determined by [Favorite] counts, not approvals
• Therefore, approval truncation provides no dominant strategic advantage

Result:
• Honest approval of all acceptable candidates is weakly dominant
• “Bullet voting” is strictly risk-increasing except in degenerate edge cases

────────────────────────────────────────────────────────
6. KNOWN EDGE CASE
────────────────────────────────────────────────────────

SF-CTF-01: Cap Saturation Edge Case

If a very large number of candidates surpass T simultaneously and |Q| > M, cap enforcement occurs.

Mitigation:
• Favorite-based cap sorting aligns survival with decisive preference
• Truncating approvals does not increase Favorite counts and thus does not improve outcomes

This edge case does not reintroduce the Predator’s Dilemma.

────────────────────────────────────────────────────────
7. AUDIT & RECOUNT PROCEDURE
────────────────────────────────────────────────────────

To certify a result, the following worksheet MUST be reproducible at precinct or aggregate level.

Worksheet CTF-01:

• Total Ballots Cast (N): ________
• Initial Threshold T₀ = 0.20 × N
• Final Threshold Used: ________

Phase 1:
• Candidate A: Approvals ___ (Pass / Fail) | Favorites ___
• Candidate B: Approvals ___ (Pass / Fail) | Favorites ___
• …

Cap Check:
• |Q| = ____
• Is |Q| > M? (Y/N)
• If YES: retain top M by Favorite count

Phase 2:
• Winner = argmax(Favorite) among finalists

All intermediate values MUST be preserved in an append-only audit log.

────────────────────────────────────────────────────────
8. IMPLEMENTATION NOTE
────────────────────────────────────────────────────────

CTF-v1.0 is designed to be unignorable by construction:

• Parameters are locked pre-election
• All logic is monotonic and deterministic
• No discretionary interpretation exists at any stage
• Strategic exploits are neutralized structurally, not behaviorally

The protocol is suitable for legislative codification, standards adoption, and hostile recount environments.

END OF FILE![A8FD5271-BE94-42A5-A947-19F9D5A6903B](https://github.com/user-attachments/assets/23b3a97a-0070-4819-8d37-c0e660004921)
