TERMINATION CODES — CANONICAL ENUM
(Exhaustive, Closed Set, No Interpretation)

PURPOSE
Termination codes explain why something was killed, not whether it was “bad.”
They are diagnostic labels, not judgments.
Every automated deletion MUST emit exactly one termination code from this list.
No new codes may be invented without a Structural claim.

⸻

CORE PRINCIPLE

If a candidate cannot survive mechanical scrutiny, it dies.
Human meaning is irrelevant at this stage.

⸻

TERMINATION CODE ENUMERATION

TR-EMPTY
Definition:
Candidate contains no characters after trimming whitespace.

Trigger:
   •   length(raw_text) == 0

Meaning:
Nothing was submitted.

⸻

TR-LOW-SIGNAL
Definition:
Candidate is too short to encode a falsifiable claim.

Trigger:
   •   length(raw_text) < MIN_SIGNAL_LENGTH

Meaning:
Not enough information to even be wrong.

⸻

TR-VIBE
Definition:
Candidate expresses emotion, narrative, opinion, or reaction without a declarative claim.

Trigger (any):
   •   No subject–predicate structure
   •   Contains only feelings, complaints, or storytelling
   •   Cannot be rewritten as a boolean statement

Meaning:
Language without liability.

⸻

TR-UNFALSIFIABLE
Definition:
Candidate makes a statement that cannot be proven true or false in principle.

Trigger (any):
   •   No observable state could ever disconfirm it
   •   Relies on intention, belief, morality, or unverifiable internal states

Meaning:
Immune to reality.

⸻

TR-DUPE
Definition:
Candidate is redundant with existing material.

Trigger (any):
   •   Exact hash match to existing blob
   •   Near-exact semantic duplicate of existing QUARANTINE or CANON content

Meaning:
Adds no new leverage.

⸻

TR-NO-LIABILITY
Definition:
Candidate does not imply any cost for being wrong.

Trigger (any):
   •   No consequence for failure
   •   No stake, embarrassment, loss, or downstream dependency
   •   Pure description with no obligation

Meaning:
Free speech is prohibited.

⸻

TR-NO-PREDICATE
Definition:
Candidate cannot be expressed as a single boolean predicate.

Trigger (any):
   •   Requires multiple unrelated assertions
   •   Depends on vague qualifiers (“generally”, “kind of”, “seems like”)

Meaning:
Not machine-checkable.

⸻

TR-SCOPE-ERROR
Definition:
Candidate asserts authority or scope it does not possess.

Trigger (any):
   •   Attempts to define CANON directly
   •   Attempts to modify invariants
   •   Attempts to speak for entities without standing

Meaning:
Illegal jurisdiction.

⸻

TR-STRUCTURAL-PREMATURE
Definition:
Candidate proposes a structural change without prerequisite evidence.

Trigger (any):
   •   Structural claim without supporting diagnostics
   •   Governance edits without prior Observations

Meaning:
Skipped the ladder.

⸻

TR-SELF-REFERENTIAL
Definition:
Candidate attempts to validate itself or its own correctness.

Trigger (any):
   •   “This is true because I say so” patterns
   •   Internal-only justification

Meaning:
Recursive validation loop detected.

⸻

TR-UNKNOWN
Definition:
Catch-all for explicitly unclassifiable content.

Trigger:
   •   Does not satisfy ANY routing condition
   •   Does not clearly fail any other code

Meaning:
Better to kill than guess.

⸻

ENUM CLOSURE RULE
   •   This list is CLOSED.
   •   Scanner may not emit any other termination code.
   •   Any candidate not explicitly survivable under this enum MUST be killed.

⸻

SUCCESS CONDITION

A healthy intake produces:
   •   High TR-VIBE
   •   High TR-LOW-SIGNAL
   •   Rare survivors

If most candidates survive, the system is failing.

⸻

END OF FILE
