# Diagnostics

This directory contains validation artifacts that enforce schema integrity
across all claimant-addressable liability surfaces.

No ingestion code may bypass these diagnostics.

If diagnostics fail:
- Automation halts
- NERF must be emitted
- Manual audit required
