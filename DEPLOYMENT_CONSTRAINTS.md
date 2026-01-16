Deployment Constraints — TESSRAX v0.1.0

1. NO PERSISTENCE  
   Must be deployed to a read-only or ephemeral file system.
   No request data, artifacts, or receipts may be written to disk.

2. NO LOGGING  
   Do not log request payloads (Claims/Artifacts).
   Permitted logs are limited to:
   - timestamp
   - verdict enum (PASS / PARTIAL / NERF)
   - request latency

   No identifiers, hashes, source URLs, or derived fields may be logged.

3. NO RETRIES  
   500 errors (Wrapper Faults) must not be automatically retried by load balancers,
   job queues, or orchestration layers.

4. SINGLE PROCESS  
   Run as a single worker process.
   Do not enable multi-worker, auto-scaling, or concurrent execution modes.

5. ISOLATION  
   No outbound internet access is required or permitted.
   The engine is self-contained and must not depend on external services.

6. NO AGGREGATION  
   Requests and receipts must not be aggregated, correlated, replayed,
   or analyzed outside the immediate execution context.

Status: READY TO FREEZE
