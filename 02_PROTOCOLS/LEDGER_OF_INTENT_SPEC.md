# Ledger of Intent — Specification

## Purpose
Provide a printable, causal anchor for system state.

## Format Requirements
- Fixed-width text
- CSV or Markdown table
- No nested structures
- A4 printable
- Monotonic timestamps

## Required Fields
- Timestamp
- Actor_ID
- Action_Type
- Evidence_Hash (short)
- Gate_Status
- Risk_Delta
- Invariant_Protected

## Prohibited
- JSON
- Binary blobs
- Opaque IDs
- System-only semantics

## Rule
If a human cannot understand a line in under 30 seconds,
the line is invalid.
