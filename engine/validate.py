#!/usr/bin/env python3
"""
TESSRAX VALIDITY ENGINE
Deterministic claim validator. Emits receipts only.
"""

import json
import sys
import datetime
from jsonschema import validate, ValidationError

# -----------------------------
# Schema loading (local files)
# -----------------------------
def load_schema(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

CLAIM_SCHEMA   = load_schema("schemas/claim.schema.json")
ARTIFACT_SCHEMA = load_schema("schemas/artifact.schema.json")
VERDICT_SCHEMA = load_schema("schemas/verdict.schema.json")

# -----------------------------
# Canonical constants
# -----------------------------
MAX_ARTIFACT_STALENESS_DAYS = 365

# -----------------------------
# Utilities
# -----------------------------
def utcnow():
    return datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

def emit_verdict(claim_id, status, violations=None, bounded_scope=None):
    verdict = {
        "claim_id": claim_id,
        "status": status,
        "timestamp": utcnow(),
        "invariant_violations": violations or []
    }
    if bounded_scope is not None:
        verdict["bounded_scope"] = bounded_scope

    # Structural self-check (no prose allowed)
    validate(instance=verdict, schema=VERDICT_SCHEMA)
    print(json.dumps(verdict, indent=2))
    return verdict

def parse_dt(ts):
    return datetime.datetime.fromisoformat(ts.rstrip("Z"))

# -----------------------------
# Engine
# -----------------------------
class TessraxValidator:
    def validate(self, claim, artifacts):
        claim_id = claim.get("claim_id", "UNKNOWN")
        violations = []

        # 1) Structural validation (hard gate)
        try:
            validate(instance=claim, schema=CLAIM_SCHEMA)
        except ValidationError as e:
            return emit_verdict(
                claim_id,
                "NERF",
                [f"SCHEMA_VIOLATION: {e.message}"]
            )

        # 2) Artifact validation (structure + linkage)
        verified = []
        claim_hashes = set(claim["artifact_hashes"])

        for art in artifacts:
            try:
                validate(instance=art, schema=ARTIFACT_SCHEMA)
            except ValidationError as e:
                violations.append(f"INVALID_ARTIFACT_STRUCTURE: {e.message}")
                continue

            if art["hash"] in claim_hashes:
                verified.append(art)

        if not verified:
            return emit_verdict(
                claim_id,
                "NERF",
                ["INV-STRAND-0: NO_MATCHING_ARTIF
