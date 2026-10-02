# Claim Status

**Repository:** beyond-repair/AtomicNexusAI  
**Classification:** RUNNABLE SKETCH (Claim-0)  
**Claim level:** 0  

## Allowed statements

- Historical / repaired demo of a modular AI agent framework idea with hybrid local/cloud *stub* execution.
- Runnable entrypoint: `python main.py` / `python -m AtomicNexusAI` after `pip install -e ".[dev]"`.
- Clean-clone verified: install, pytest, and demo smoke on a stock Linux Python environment (no cloud credentials).

## Forbidden / unsupported

- Shipped IDE, marketplace, or visual builder product.
- Real AWS / Kubernetes / container offload or cost APIs.
- Production authentication, encryption, or security-audit guarantees.
- Profit, live trading, or deployment claims.

## Repair note

Product mutation allowed for Claim-0 runnability: proper `__init__.py` package layout, fixed imports, installable `pyproject.toml`, honest demo/tests/docs. Nested `AtomicNexusAI/` package root preserved. Root orphan dirs left in place as historical leftovers.
