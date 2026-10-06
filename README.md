<div align="center">

```
╔═════════════════════════════════════════════════════════════╗
║   ATOMIC DREAM LABS  ·  BEYOND-REPAIR                        ║
╚═════════════════════════════════════════════════════════════╝
```

# Atomic Nexus AI

### Claim-0 modular agent / hybrid-execution sketch — not a shipped framework

[![Lifecycle](https://img.shields.io/badge/%E2%97%8F_RESEARCH_SKETCH-22c55e?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/Claim_0-22c55e?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)
[![Governance](https://img.shields.io/badge/ADL--Governance-7c3aed?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)

```
LIFECYCLE   RESEARCH / RUNNABLE SKETCH (Claim-0)
CLAIM       0
NOT CLAIMED IDE product · live cloud offload · K8s/AWS runners · profit
```

</div>

---

## Status

**RESEARCH — RUNNABLE SKETCH — NOT A COMPLETE PRODUCT.**

Historical archive-queue layout repaired so a stranger can clone, install, run a local demo, and pass pytest. The README feature list below was always aspirational; this Claim-0 surface is a **mock modular agent + DAG + hybrid execution decision** path only.

Sweep-242 (2026-10-06): classification corrected from inherited "ARCHIVED target" to RESEARCH. GitHub archive flag remains false. Local pytest on pre-head `e5434837` was 11 passed. CI workflow aligned to Python 3.11 and `pytest -q`. Actions success is not yet observed and is not a completeness claim.

---

## What works (Claim-0)

| Surface | Behavior |
| --- | --- |
| `python main.py` | Load YAML config, run autonomous + collaborative agents on a NetworkX DAG, hybrid local/cloud *stub* decision, memory + anomaly-detect demo |
| `python -m AtomicNexusAI` | Same demo via package `__main__` |
| Package `AtomicNexusAI` | Installable; `config`, `core` (agents/memory/models/workflows), `execution` stubs, `security.audit.anomaly_detector` |
| `pytest` | Repo-root suite covering config, agents, DAG, models, memory/execution, anomaly, main smoke |

## What is **not** claimed

- Full IDE / visual builder / debugger / tool marketplace
- Real AWS, Kubernetes, or container runners
- Production security (OAuth, encryption, attack simulation)
- Profit, deployment readiness, or live trading

Orphaned root trees (`utils/`, `security/`, `ecurity/`, `github/`) are historical leftovers; the installable package lives under `AtomicNexusAI/`.

---

## Quick start (stranger clone)

```bash
git clone https://github.com/beyond-repair/AtomicNexusAI.git
cd AtomicNexusAI
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python main.py
pytest -q
```

Optional AES helper (not required for demo/tests):

```bash
pip install -e ".[crypto]"
```

---

## Layout

```
AtomicNexusAI/                 ← repo root
├── main.py                    ← Claim-0 demo entrypoint
├── pyproject.toml
├── requirements.txt
├── tests/                     ← maintained pytest suite
└── AtomicNexusAI/             ← installable package
    ├── config/                ← YAML + logging
    ├── core/                  ← agents, memory, models, workflows
    ├── execution/             ← local/cloud stubs + offload decision
    ├── security/audit/        ← anomaly detector used by demo
    ├── ide/                   ← historical stubs (not Claim-0 surface)
    └── utils/                 ← logging / interfaces / optimizers stubs
```

---

## See also

- [CLAIM_STATUS.md](CLAIM_STATUS.md) — allowed / forbidden statements
- [ARCHIVED.md](ARCHIVED.md) — historical archive note (sketch repaired for Claim-0)
- [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · [Claim levels 0–5](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

---

<div align="center">

**REWRITE · BUILD · TRANSCEND**

**William (Brian) Ware** · [Atomic Dream Labs](https://github.com/beyond-repair)

</div>
