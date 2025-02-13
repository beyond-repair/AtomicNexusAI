# autonomous_agent.py
from .agent_base import AgentBase

class AutonomousAgent(AgentBase):
    def __init__(self, name: str, model: str) -> None:
        super().__init__(name)
        self.model = model

    def execute(self) -> None:
        from utils.logging.execution_logger import log
        log(f"{self.name} executing autonomously with model {self.model}.")