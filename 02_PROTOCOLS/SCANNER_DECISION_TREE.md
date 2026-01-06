SCANNER DECISION TREE
(Deterministic, Fail-Closed, Bias-for-Deletion)

PURPOSE
This defines the only legal routing logic for automated intake.
The scanner does not “classify for usefulness.”
It disqualifies aggressively.

Anything not explicitly allowed is destroyed or quarantined.

⸻

GLOBAL INVARIANTS
   •   Scanner has NO WRITE ACCESS to:
      •   01_CANON/
      •   02_PROTOCOLS/
      •   03_DIAGNOSTICS/
   •   Scanner MAY:
      •   READ everything
      •   WRITE ONLY to:
         •   QUARANTINE/**
         •   QUARANTINE/KILLED/**
         •   RAW/ARCHIVE/**
   •   Scanner CANNOT:
      •   Edit files
      •   Rename files
      •   Merge files
      •   Interpret intent
      •   Decide truth

It only routes or kills.

⸻

INPUT SURFACE

All automation operates ONLY on:

RAW/INBOX/DROP.md

Assumptions:
   •   This file is append-only
   •   Content is untrusted
   •   Content may be garbage
   •   Content may be gold
   •   Scanner treats both the same

⸻

STEP 0 — SNAPSHOT & ISOLATION

On trigger (push or schedule):
	1.	Copy RAW/INBOX/DROP.md to an immutable blob:
RAW/BLOBS/_.md
	2.	Clear RAW/INBOX/DROP.md (truncate to empty)
	3.	Scanner operates ONLY on the blob copy

This prevents race conditions and partial writes.

⸻

STEP 1 — SPLIT INTO CANDIDATES

For each logical block in the blob (paragraph or delimiter-separated):

Create CANDIDATE[i] with:
   •   raw_text
   •   source_blob_hash
   •   timestamp

No parsing yet. No judgment yet.

⸻

STEP 2 — HARD DISQUALIFICATION (KILL FAST)

For each CANDIDATE:

IF raw_text is empty → KILL(TR-EMPTY)

IF length < N characters → KILL(TR-LOW-SIGNAL)

IF contains no declarative content
(e.g. only emotion, venting, narrative)
→ KILL(TR-VIBE)

IF cannot possibly be rewritten as a boolean claim
→ KILL(TR-UNFALSIFIABLE)

IF duplicates existing content (hash or near-exact)
→ KILL(TR-DUPE)

Killed candidates are written to:

QUARANTINE/KILLED/_.md

with:
   •   raw_text
   •   termination_code
   •   source_blob_hash

⸻

STEP 3 — STRUCTURAL ELIGIBILITY CHECK

Surviving candidates must pass ALL:
	1.	Can be expressed as ONE of:
      •   Observation
      •   Prediction
      •   Structural claim
	2.	Can accept LIABILITY:
      •   Someone could be wrong
      •   Someone could be embarrassed
      •   Someone could lose leverage
	3.	Could theoretically earn or lose budget

IF ANY FAIL → KILL(TR-NO-LIABILITY)

⸻

STEP 4 — ROUTING DECISION

For each remaining candidate:

IF it asserts something about reality, causality, or governance
→ ROUTE TO: QUARANTINE/CLAIMS/

IF it is a factual assertion needing verification
(numbers, dates, quotes, prices, laws)
→ ROUTE TO: QUARANTINE/FACTS/

IF it is an object, proof, or primary material
→ ROUTE TO: QUARANTINE/ARTIFACTS/

NO OTHER DESTINATIONS EXIST.

⸻

STEP 5 — FILE EMISSION RULES

When emitting a file to QUARANTINE:
   •   Filename: _.md
   •   Content is IMMUTABLE
   •   Scanner NEVER edits after write
   •   Scanner NEVER merges entries

Each emitted file must include:
   •   SOURCE (blob hash)
   •   RAW_TEXT (verbatim)
   •   ROUTE_REASON
   •   STATUS: pending

⸻

STEP 6 — ABSOLUTE PROHIBITIONS

The scanner MUST NOT:
   •   Promote anything to CANON
   •   Rewrite content
   •   Summarize content
   •   Explain content
   •   Decide importance
   •   Decide truth
   •   “Help”

If it’s not clearly allowed → kill it.

⸻

SUCCESS METRIC

A healthy system has:
   •   90%+ of RAW content killed
   •   Small QUARANTINE
   •   Tiny CANON
   •   High signal density
   •   Slow growth
   •   High confidence

If QUARANTINE grows fast, the scanner is too permissive.

⸻

END OF DECISION TREE
