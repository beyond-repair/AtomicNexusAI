# agent_base.py
from typing import Any

class AgentBase:
    def __init__(self, name: str) -> None:
        """
        Initialize an agent with a name.
        """
        self.name = name

    def execute(self) -> None:
        """
        Execute the agent's task. Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the execute method.")