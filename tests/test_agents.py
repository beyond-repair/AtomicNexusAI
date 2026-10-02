from AtomicNexusAI.core.agents.autonomous_agent import AutonomousAgent
from AtomicNexusAI.core.agents.collaborative_agent import CollaborativeAgent
from AtomicNexusAI.core.agents.agent_base import AgentBase
import pytest


def test_agent_base_requires_execute():
    with pytest.raises(NotImplementedError):
        AgentBase("x").execute()


def test_autonomous_agent_selects_model():
    agent = AutonomousAgent("explorer", "hint")
    result = agent.execute()
    assert "default_model" in result
    assert agent.execution_context["selected_model"] == "default_model"


def test_collaborative_agent():
    agent = CollaborativeAgent("coord", partners=["a", "b"])
    result = agent.execute()
    assert "collaborating" in result
    assert "a" in result
