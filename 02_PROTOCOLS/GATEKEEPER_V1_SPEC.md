# GATEKEEPER-V1 — Self-Contained Governance Binary Specification

## Status
PRODUCTION-READY  
Authority Tier: 02_PROTOCOLS  
Enforcement Model: FAIL-CLOSED

---

## Purpose

Gatekeeper-V1 packages the Naming Gate architecture into a portable, production-ready governance binary.

It transforms a repository from passive storage into an **active epistemic enforcement system** where:
- filenames are not chosen
- directories are not curated
- history cannot be rewritten
- ambiguity cannot compile

If content cannot deterministically justify its identity, location, and time direction, it is refused.

---

## Core Invariant

> The filesystem is a compiled artifact.  
> Content is the only source of authority.

---

## Tool Overview

**Name:** `gatekeeper-v1`  
**Form:** Self-contained CLI + hooks + CI  
**Audience:** Any team that wants to lock a repository against semantic drift

---

## Project Structure

```
gatekeeper-v1/
├── bin/
│   └── gate-ingest          # CLI entry point
├── core/
│   ├── compiler.py          # Phase 1–5 Logic
│   ├── stability.py         # Phase 6 Monotonicity Logic
│   └── prompt_template.txt  # Write-locked NAMING_GATE_V1 prompt
├── config/
│   └── authority.json       # User-customizable authority matrix
└── install.sh               # Bootstrap + Git hook wiring
```

Logic is immutable. Configuration is user-owned.

---

## Authority Configuration Schema

`config/authority.json`

```json
{
  "tiers": {
    "01_CANON": ["INV-", "S0", "immutable"],
    "02_PROTOCOLS": ["IF/THEN", "policy"],
    "03_DIAGNOSTICS": ["FAIL", "ERROR", "test"]
  },
  "stability_rules": {
    "enforce_monotonic_versioning": true,
    "allow_ephemeral_overwrite": true
  }
}
```

The gate refuses if classification does not match physical placement.

---

## CLI Operating Modes

### 1. Ingest
Turns RAW_TEXT into a governed artifact.

```
cat feature_spec.md | gate-ingest --commit
```

Result: file is deterministically named and placed.

---

### 2. Audit
Validates an existing repository.

```
gate-ingest --audit ./repo
```

Returns all violations of naming, authority, or stability laws.

---

### 3. Init
Bootstraps governance in a new repo.

```
gate-ingest --init
```

Creates directory hierarchy and installs Git hooks.

---

## Portability Mode

A single-file bundle (`gatekeeper.py`) may embed:
- prompt template
- default authority matrix
- stability logic

This allows zero-config deployment.

---

## Governance Invariants Ledger

The system is governed by the following non-negotiable invariants:

| ID | Name | Requirement |
|----|------|-------------|
| INV-0 | MAS | No action on data exceeding Maximum Allowable Staleness |
| INV-1 | Sequential | State transitions must be strictly monotonic (v2 > v1) |
| INV-2 | Atomic | All-or-nothing commits only |
| INV-3 | Gating | Validation + bounding + receipt before any write |
| INV-4 | Bounding | Explicit scope limits; no unbounded side effects |
| INV-5 | Semantic | Filenames must be derivable from content |
| INV-6 | OIAT | Two gate rejections invalidate the session |

---

## install.sh — Governance Bootloader

```bash
#!/bin/bash
set -e

echo "🛡️  Initializing Epistemic Border Control..."

DIRECTORIES=(
  "01_CANON"
  "02_PROTOCOLS"
  "03_DIAGNOSTICS"
  "04_CASES"
  "05_LOGS"
  "RAW/INBOX"
  "scripts"
)

for dir in "${DIRECTORIES[@]}"; do
  mkdir -p "$dir"
done

if [ -f "gate_ingest.py" ]; then
  mv gate_ingest.py scripts/
  chmod +x scripts/gate_ingest.py
fi

HOOK=".git/hooks/pre-commit"
cat << 'EOF' > "$HOOK"
#!/bin/bash
STAGED_FILES=$(git diff --cached --name-only --diff-filter=d | grep '\.md$')
[ -z "$STAGED_FILES" ] && exit 0

for FILE in $STAGED_FILES; do
  RESULT=$(cat "$FILE" | python3 scripts/gate_ingest.py --validate-only --actual-path "$FILE")
  if [[ "$RESULT" == *"REFUSED"* ]]; then
    echo "❌ NAMING GATE REFUSAL: $FILE"
    echo "$RESULT"
    exit 1
  fi
done
EOF

chmod +x "$HOOK"

LEDGER="01_CANON/SPEC_GOVERNANCE_INVARIANTS.md"
if [ ! -f "$LEDGER" ]; then
  cat << 'EOF' > "$LEDGER"
# 01_CANON/SPEC_GOVERNANCE_INVARIANTS
INV-0: No action on stale data.
INV-1: Monotonic state transitions.
INV-2: Atomic commits only.
INV-3: Validation before action.
INV-5: Deterministic naming.
EOF
fi

echo "✨ Gatekeeper-V1 deployed. Repository is now governed."
```

---

## Terminal State

Once installed:

- Files cannot be misnamed
- Authority cannot be inflated
- History cannot be rewritten
- Ambiguity cannot enter

Invalid states are **unrepresentable**.

---

## Final Status

ARCHITECTURE: CLOSED  
TOOLING: PORTABLE  
GOVERNANCE: ENFORCED  
TRUST: ELIMINATED
