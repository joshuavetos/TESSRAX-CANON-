FILE: README_QUICKSTART.md

# Forensic Probe v0 — Quick Start (CYA Compliance Manager)

This tool produces a **point-in-time, cryptographically verifiable snapshot** of a system’s raw state.
It is designed to create **career-safe evidence**, not dashboards.

---

## What You Get (In 60 Seconds)
- A `snapshot.json` of raw system signals
- A `snapshot.sha256` hash you can verify with standard tools
- An optional Ed25519 signature proving who captured it
- A directory you can hand to Audit, Legal, or your Boss

---

## Step 0 — Copy the Binary
Upload the single static binary to the target machine.

```bash
scp forensic-probe-static user@server:/tmp/forensic-probe
ssh user@server
cd /tmp
chmod +x forensic-probe
```

No install. No daemon. No config.

---

## Step 1 — (Optional) Create a Signing Key
Do this once, on a trusted machine.

```bash
forensic-probe keygen --out auditor.key
```

This creates:
- `auditor.key` (private — KEEP SAFE)
- `auditor.pub` (public — safe to share)

---

## Step 2 — Capture a Snapshot
Run on the system you need evidence for.

Unsigned capture:
```bash
./forensic-probe capture
```

Signed capture:
```bash
./forensic-probe capture --sign auditor.key
```

Output:
```
forensic_snapshot_<SESSION_ID>/
├── snapshot.json
├── snapshot.sha256
└── snapshot.sig        (only if signed)
```

You may now delete the binary if desired.

---

## Step 3 — Verify Integrity (Anyone, Anytime)
Verification does **not** require the original machine.

Hash verification:
```bash
./forensic-probe verify forensic_snapshot_<SESSION_ID>
```

Signature verification:
```bash
./forensic-probe verify forensic_snapshot_<SESSION_ID> --pub auditor.pub
```

Possible results:
- `AUTHENTIC` — hash and signature valid
- `HASH MISMATCH` — file was altered
- `SIGNATURE INVALID` — forgery or wrong key

---

## Step 4 — Hand It Off
Give the **entire directory** to:
- Internal Audit
- External Auditors
- Legal / Forensics
- Your Manager

They can independently verify without trusting you.

---

## Step 5 — Know the Boundary (IMPORTANT)
This artifact proves:
- What the system state **was** at the timestamp
- That it has **not been altered**
- That it was captured by a known key (if signed)

It does NOT prove:
- What happened before or after
- That the kernel was not malicious
- That future behavior is safe

Read `THREAT_MODEL.md`.

---

## One-Sentence Truth
> “This is the signed kernel-level state of the machine at this exact time.”

That sentence is why this exists.

END.
