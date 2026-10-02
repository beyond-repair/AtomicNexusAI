# collaborative_agent.py
from .agent_base import AgentBase
from ...utils.logging.execution_logger import log


class CollaborativeAgent(AgentBase):
    def __init__(self, name: str, partners: list[str] | None = None) -> None:
        super().__init__(name)
        self.partners = partners or []

    def execute(self) -> str:
        partners_str = ", ".join(self.partners) if self.partners else "no partners"
        message = f"{self.name} collaborating with {partners_str}."
        log(message)
        return message
