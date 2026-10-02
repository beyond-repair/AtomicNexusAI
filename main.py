#!/usr/bin/env python3
"""Atomic Nexus AI — Claim-0 runnable sketch entrypoint."""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from AtomicNexusAI.config.logging_config import setup_logging
from AtomicNexusAI.config.config_manager import load_config
from AtomicNexusAI.core.agents.autonomous_agent import AutonomousAgent
from AtomicNexusAI.core.agents.collaborative_agent import CollaborativeAgent
from AtomicNexusAI.core.workflows.dag_orchestrator import DAGOrchestrator
from AtomicNexusAI.core.memory.short_term import ShortTermMemory
from AtomicNexusAI.core.memory.long_term import LongTermMemory
from AtomicNexusAI.execution.execution_manager import ExecutionManager
from AtomicNexusAI.security.audit.anomaly_detector import AnomalyDetector

setup_logging()
logger = logging.getLogger(__name__)

DEFAULT_CONFIG = Path(__file__).resolve().parent / "AtomicNexusAI" / "config" / "default_settings.yaml"


def run_demo(config: dict) -> int:
    app = config.get("app", {})
    mode = "debug" if app.get("debug") else "production"
    logger.info(
        "Starting %s version %s in %s mode (Claim-0 sketch).",
        app.get("name", "Atomic Nexus AI"),
        app.get("version", "?"),
        mode,
    )

    demo = config.get("demo", {})
    memory_short = ShortTermMemory()
    memory_long = LongTermMemory()
    orchestrator = DAGOrchestrator()
    executor = ExecutionManager()
    detector = AnomalyDetector()

    explorer = AutonomousAgent("explorer", "default_model")
    coordinator = CollaborativeAgent("coordinator", partners=["explorer"])

    orchestrator.add_task(explorer)
    orchestrator.add_task(coordinator, preconditions=[explorer])
    logger.info("DAG nodes=%d", orchestrator.execution_graph.number_of_nodes())
    orchestrator.execute()

    exec_result = executor.execute_task(explorer)
    memory_short.add({"agent": explorer.name, "context": explorer.execution_context})
    memory_long.add(exec_result)

    logs = demo.get("sample_logs") or [
        "All good",
        "Error: something failed",
        "Warning: check system",
    ]
    anomalies = detector.detect(logs)

    print("--- Atomic Nexus AI Claim-0 demo ---")
    print(f"app: {app.get('name')} v{app.get('version')} ({mode})")
    print(f"dag_path: {[type(n).__name__ for n in orchestrator.optimize_path()]}")
    print(f"execution: {exec_result}")
    print(f"short_term: {memory_short.retrieve()}")
    print(f"long_term_count: {len(memory_long.retrieve_all())}")
    print(f"anomalies: {anomalies}")
    logger.info("Atomic Nexus AI demo finished.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Atomic Nexus AI (Claim-0 runnable sketch)"
    )
    parser.add_argument(
        "--config",
        type=str,
        default=str(DEFAULT_CONFIG),
        help="Path to configuration YAML",
    )
    args = parser.parse_args()
    try:
        config = load_config(args.config)
    except Exception as e:
        logger.error("Error loading configuration: %s", e)
        sys.exit(1)
    if not isinstance(config, dict) or "app" not in config:
        logger.error("Configuration missing required 'app' section.")
        sys.exit(1)
    sys.exit(run_demo(config))


if __name__ == "__main__":
    main()
