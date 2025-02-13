# collaborative_agent.py
from .agent_base import AgentBase

class CollaborativeAgent(AgentBase):
    def __init__(self, name: str, partners: list[str] | None = None) -> None:
        super().__init__(name)
        self.partners = partners or []

    def execute(self) -> None:
        from utils.logging.execution_logger import log
        partners_str = ', '.join(self.partners) if self.partners else 'no partners'
        log(f"{self.name} collaborating with {partners_str}.")