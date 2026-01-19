# --------------------------------------------------
# TESSRAX EGaaS — FROZEN EXECUTION ENVIRONMENT
# --------------------------------------------------
# Intent:
# - Deterministic
# - Stateless
# - Fail-closed
# - No advisory surface
# - No mutable state
# --------------------------------------------------
# Base runtime: stable, widely supported, governance-safe
FROM python:3.10-slim

# --------------------------------------------------
# Runtime invariants
# --------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# --------------------------------------------------
# Non-root execution (liability + safety)
# --------------------------------------------------
RUN useradd --create-home --shell /usr/sbin/nologin tessrax
WORKDIR /app

# --------------------------------------------------
# Dependency install (explicit + minimal)
# --------------------------------------------------
# Only what EGaaS requires:
# - fastapi: HTTP boundary
# - uvicorn[standard]: ASGI server
# - jsonschema: enforcement gate dependency
#
# Versions are pinned for absolute reproducibility.
# Upgrades REQUIRE a version bump.
# --------------------------------------------------
RUN pip install --no-cache-dir pip==24.0 && \
    pip install --no-cache-dir \
    "fastapi==0.118.0" \
    "uvicorn[standard]==0.22.0" \
    "jsonschema==4.20.0"

# --------------------------------------------------
# Copy canonical enforcement code
# --------------------------------------------------
COPY engine /app/engine
COPY schemas /app/schemas
COPY api_wrapper.py /app/api_wrapper.py

# --------------------------------------------------
# Lock permissions
# --------------------------------------------------
RUN chown -R tessrax:tessrax /app
USER tessrax

# --------------------------------------------------
# Network surface
# --------------------------------------------------
EXPOSE 8000

# --------------------------------------------------
# Execution
# --------------------------------------------------
# No reload
# No workers auto-scaling
# No dynamic config
# One process = one authority
# --------------------------------------------------
CMD ["uvicorn", "api_wrapper:app", "--host", "0.0.0.0", "--port", "8000"]
