# Claim Status

**Repository:** beyond-repair/AtomicNexusAI  
**Classification:** RESEARCH (Claim-0 runnable sketch)  
**Claim level:** 0  
**Sweep:** 246 (2026-10-06)  
**Pre-head:** `663df6a76400a1c5ef36bc3bceedfd270cca2881`  
**Workflow fix commit:** `45a68454b2b661e38ac4abd728dc2bcf0b8f663b`  

## Allowed statements

- Historical / repaired demo of a modular AI agent framework idea with hybrid local/cloud *stub* execution.
- Runnable entrypoint: `python main.py` / `python -m AtomicNexusAI` after `pip install -e ".[dev]"`.
- Local pytest on the Sweep-242 pre-head: 11 passed (stock Linux, no cloud credentials).
- Deploy workflow run 37492591439 on `663df6a7` failed at `./deploy.sh` with exit 126 after the in-job attack simulator and 11 pytest passed. Cause: Permission denied. `deploy.sh` only echoes.
- Commit `45a68454` changes the job to `bash deploy.sh`. That removes the executable-bit dependency. It is not a production deploy and is not verified until a later Actions run on that commit is observed.
- GitHub `archived` flag is false. Registry "ARCHIVED target" was inherited and is not the GitHub archive flag.

## Forbidden / unsupported

- Shipped IDE, marketplace, or visual builder product.
- Real AWS / Kubernetes / container offload or cost APIs.
- Production authentication, encryption, or security-audit guarantees.
- Profit, live trading, or deployment claims.
- Treating Actions success, if later observed, as product completeness.
- Treating `bash deploy.sh` as a release or as a fix of the deploy workflow until a new run is observed.

## Repair note

Product mutation allowed for Claim-0 runnability: proper `__init__.py` package layout, fixed imports, installable `pyproject.toml`, honest demo/tests/docs. Nested `AtomicNexusAI/` package root preserved. Root orphan dirs left in place as historical leftovers.

Sweep-242 did not delete `utils/`, `security/`, `ecurity/`, `github/`, or `**LICENSE**`. Deletion and the GitHub archive flag remain operator-only.

Sweep-246 did not change `deploy.sh` body and did not set the executable bit. The contents API used here does not expose file mode.
