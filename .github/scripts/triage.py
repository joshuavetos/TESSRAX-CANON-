import hashlib
import pathlib
import sys
import time

RAW = pathlib.Path("RAW")
QUAR = pathlib.Path("QUARANTINE")
ARCHIVE = RAW / "archive"

ARCHIVE.mkdir(parents=True, exist_ok=True)

def hash_file(p):
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()

def terminate(p, reason):
    ts = int(time.time())
    h = hash_file(p)
    out = ARCHIVE / f"{ts}-{h}.md"
    out.write_text(
        f"# TERMINATED\n\n"
        f"Reason: {reason}\n"
        f"Source: {p}\n"
    )
    p.unlink()

def is_falsifiable(text):
    return "PREDICATE:" in text and "DEPENDENCIES:" in text

for p in RAW.glob("**/*.md"):
    if "archive" in p.parts:
        continue

    text = p.read_text()

    if not is_falsifiable(text):
        terminate(p, "TR-VIBE")
        continue

    # Passed minimal gate — move to quarantine
    QUAR.mkdir(exist_ok=True)
    p.rename(QUAR / p.name)
