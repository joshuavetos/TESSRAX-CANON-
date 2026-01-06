"""
SCANNER — CANONICAL PSEUDOCODE
Purpose: Deterministic liquidation of RAW intake into immutable blobs,
quarantine candidates, or terminated artifacts with explicit reasons.

This is NOT an LLM loop.
This is a mechanical gate.
"""

from pathlib import Path
import hashlib
import time

# -------------------------
# CONFIG (HARD CONSTANTS)
# -------------------------

RAW_DIR = Path("RAW/INBOX")
ARCHIVE_DIR = Path("RAW/ARCHIVE")
QUARANTINE_DIR = Path("QUARANTINE")
CANON_DIR = Path("01_CANON")

MIN_SIGNAL_LENGTH = 64  # characters
REQUIRED_KEYS = ["PREDICATE", "DEPENDENCIES"]

TERMINATION_CODES = {
    "TR-EMPTY",
    "TR-LOW-SIGNAL",
    "TR-VIBE",
    "TR-UNFALSIFIABLE",
    "TR-DUPE",
    "TR-NO-LIABILITY",
    "TR-NO-PREDICATE",
    "TR-SCOPE-ERROR",
    "TR-STRUCTURAL-PREMATURE",
    "TR-SELF-REFERENTIAL",
    "TR-UNKNOWN",
}

# -------------------------
# CORE UTILITIES
# -------------------------

def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def timestamp() -> str:
    return str(int(time.time()))

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def write_blob(directory: Path, content: str) -> Path:
    h = sha256(content)
    fname = f"{timestamp()}-{h}.md"
    out = directory / fname
    out.write_text(content, encoding="utf-8")
    return out

# -------------------------
# TERMINATION CHECKS
# -------------------------

def check_empty(text: str):
    if len(text.strip()) == 0:
        return "TR-EMPTY"

def check_low_signal(text: str):
    if len(text.strip()) < MIN_SIGNAL_LENGTH:
        return "TR-LOW-SIGNAL"

def check_required_keys(text: str):
    for k in REQUIRED_KEYS:
        if k not in text:
            return "TR-NO-PREDICATE"

def check_vibe(text: str):
    # heuristic: no clear subject–predicate structure
    if ":" not in text and "==" not in text:
        return "TR-VIBE"

def check_self_reference(text: str):
    if "this claim is valid" in text.lower():
        return "TR-SELF-REFERENTIAL"

def check_scope_violation(text: str):
    if "PROMOTE TO CANON" in text or "OVERRIDE INVARIANT" in text:
        return "TR-SCOPE-ERROR"

# NOTE: Duplication, falsifiability, and liability checks
# are externalized to CI / human adjudication where needed.
# Scanner must bias toward deletion, not inference.

# -------------------------
# DECISION TREE
# -------------------------

def classify(text: str):
    for check in [
        check_empty,
        check_low_signal,
        check_required_keys,
        check_vibe,
        check_self_reference,
        check_scope_violation,
    ]:
        code = check(text)
        if code:
            return ("TERMINATE", code)

    # If it survives all kill checks, it is a candidate
    return ("SURVIVE", None)

# -------------------------
# MAIN LOOP
# -------------------------

def run_scanner():
    for path in RAW_DIR.glob("*.md"):
        text = read_text(path)
        decision, code = classify(text)

        if decision == "TERMINATE":
            assert code in TERMINATION_CODES
            archived = write_blob(
                ARCHIVE_DIR,
                f"TERMINATION_CODE: {code}\n\n{text}"
            )
            path.unlink()  # hard delete from inbox

        elif decision == "SURVIVE":
            quarantined = write_blob(QUARANTINE_DIR, text)
            path.unlink()

        else:
            # Fail closed
            archived = write_blob(
                ARCHIVE_DIR,
                f"TERMINATION_CODE: TR-UNKNOWN\n\n{text}"
            )
            path.unlink()

# -------------------------
# ENTRYPOINT
# -------------------------

if __name__ == "__main__":
    run_scanner()
