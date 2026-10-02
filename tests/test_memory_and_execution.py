from AtomicNexusAI.core.memory.short_term import ShortTermMemory
from AtomicNexusAI.core.memory.long_term import LongTermMemory
from AtomicNexusAI.core.agents.autonomous_agent import AutonomousAgent
from AtomicNexusAI.execution.execution_manager import ExecutionManager


def test_memory_roundtrip():
    st = ShortTermMemory()
    lt = LongTermMemory()
    assert st.retrieve() is None
    st.add("a")
    st.add("b")
    assert st.retrieve() == "b"
    lt.add(1)
    lt.add(2)
    assert lt.retrieve_all() == [1, 2]


def test_execution_manager_local_path():
    # Default stub pricing: cloud=10, local=8 → cost_diff > 1 → local
    mgr = ExecutionManager()
    agent = AutonomousAgent("local-demo", "default_model")
    out = mgr.execute_task(agent)
    assert out["mode"] == "local"
    assert "default_model" in (out["result"] or "")
