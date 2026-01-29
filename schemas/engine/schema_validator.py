import json
import jsonschema
from jsonschema import ValidationError
import os
import sys
import hashlib
import datetime
from typing import Tuple, List

# -----------------------------
# CONFIGURATION (WRITE-LOCKED)
# -----------------------------

CANON_SALT = "TESSRAX_CANON_v1"
LEDGER_PATH = "05_LOGS/validation_ledger.jsonl"
FR_LOG_PATH = "05_LOGS/forensic_rejection_log.jsonl"

SCORE_PASS = +1
SCORE_FAIL_MINOR = -3
SCORE_FAIL_MAJOR = -5

# -----------------------------
# UTILITIES
# -----------------------------

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def load_json(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)

def append_jsonl(path: str, record: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(record) + "\n")

def utc_now() -> str:
    return datetime.datetime.utcnow().isoformat() + "Z"

# -----------------------------
# SCHEMA VALIDATOR (FAIL-CLOSED)
# -----------------------------

class SchemaValidator:
    """
    TESSRAX Gate-0 / Gate-1 Validator
    Authority: STRUCTURAL ONLY
    Posture: FAIL-CLOSED, DETERMINISTIC, LEDGERED
    """

    def __init__(self, schema_path: str):
        self.schema_path = schema_path
        self.schema = load_json(schema_path)

    def compute_context_hash(self, document: dict) -> str:
        payload = {
            "schema": self.schema,
            "document": document,
            "canon": CANON_SALT
        }
        return sha256(json.dumps(payload, sort_keys=True).encode())

    def validate(self, document: dict) -> Tuple[bool, List[str], dict]:
        errors = []
        score = 0

        try:
            jsonschema.validate(instance=document, schema=self.schema)
            score += SCORE_PASS
        except ValidationError:
            validator = jsonschema.Draft7Validator(self.schema)
            for err in sorted(validator.iter_errors(document), key=str):
                path = "/".join(map(str, err.path)) if err.path else "root"
                errors.append(f"SCHEMA_VIOLATION: {err.message} (Path: {path})")
            score += SCORE_FAIL_MAJOR

        context_hash = self.compute_context_hash(document)

        ledger_entry = {
            "timestamp": utc_now(),
            "context_hash": context_hash,
            "schema": self.schema_path,
            "score": score,
            "status": "PASS" if score > 0 else "FAIL",
            "gate": "SCHEMA_VALIDATION"
        }

        append_jsonl(LEDGER_PATH, ledger_entry)

        if score <= 0:
            fr_entry = {
                "timestamp": utc_now(),
                "context_hash": context_hash,
                "gate": "SCHEMA_VALIDATION",
                "failure_class": "STRUCTURAL",
                "score": score,
                "errors": errors,
                "determination": "REJECTED"
            }
            append_jsonl(FR_LOG_PATH, fr_entry)
            return False, errors, fr_entry

        return True, [], ledger_entry

# -----------------------------
# CLI ENTRYPOINT
# -----------------------------

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("USAGE: python schema_validator.py <schema.json> <document.json>")
        sys.exit(1)

    schema_path = sys.argv[1]
    document_path = sys.argv[2]

    if not os.path.exists(schema_path):
        print("CRITICAL: Schema not found")
        sys.exit(1)

    if not os.path.exists(document_path):
        print("CRITICAL: Document not found")
        sys.exit(1)

    document = load_json(document_path)

    validator = SchemaValidator(schema_path)
    is_valid, errors, artifact = validator.validate(document)

    if is_valid:
        print(json.dumps({
            "status": "PASS",
            "context_hash": artifact["context_hash"],
            "gate": "SCHEMA_VALIDATION"
        }, indent=2))
        sys.exit(0)
    else:
        print(json.dumps({
            "status": "FAIL",
            "context_hash": artifact["context_hash"],
            "errors": errors
        }, indent=2))
        sys.exit(1)
