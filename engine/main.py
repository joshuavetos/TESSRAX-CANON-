import json
import sys
import os
from datetime import datetime, timezone
from jsonschema import Draft202012Validator

# Structural Change: Logic is separated from the IO runner
from engine.validator import TessraxValidator

ENGINE_VERSION = "v0.1.0"
SCHEMA_PATH = "schemas/claim_and_artifact.schema.json"

def emit_receipt(verdict, violations, nonce=None):
    """Canonical Forensic Log Emission (JSON FR-v0.1)"""
    receipt = {
        "engine_version": ENGINE_VERSION,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "verdict": verdict,
        "nonce": nonce,
        "violations": violations,
    }
    print(json.dumps(receipt, indent=2))

def main():
    # 1. Input Validation (CLI Gate)
    if len(sys.argv) != 3:
        emit_receipt("HALT", ["USAGE_ERROR: Required <claim> <artifact>"])
        sys.exit(64) # EX_USAGE

    claim_path, art_path = sys.argv[1], sys.argv[2]

    # 2. Sequential Data Load (INV-1)
    try:
        if not os.path.exists(SCHEMA_PATH):
            raise FileNotFoundError(f"Missing schema: {SCHEMA_PATH}")
            
        with open(SCHEMA_PATH) as s, open(claim_path) as c, open(art_path) as a:
            schema = json.load(s)
            claim = json.load(c)
            artifact = json.load(a)
    except Exception as e:
        emit_receipt("HALT", [f"IO_FAILURE: {str(e)}"])
        sys.exit(74) # EX_IOERR

    # 3. Schema Enforcement (The First Gate)
    payload = {"claim_data": claim, "artifact": artifact}
    validator_schema = Draft202012Validator(schema)
    errors = sorted(validator_schema.iter_errors(payload), key=lambda e: e.path)

    if errors:
        violations = [f"SCHEMA_FAIL at '{'.'.join(map(str, e.path))}': {e.message}" for e in errors]
        emit_receipt("REJECT", violations, nonce=claim.get("nonce"))
        sys.exit(1)

    # 4. Logic Enforcement (The Second Gate)
    # Uses the TessraxValidator for v1.3 Authority/FSM checks
    engine = TessraxValidator()
    verdict, violations = engine.enforce_mve(claim, artifact)

    # 5. Final State Commitment
    emit_receipt(verdict, violations, nonce=claim.get("nonce"))
    
    if verdict != "PASS":
        sys.exit(1)

if __name__ == "__main__":
    main()
