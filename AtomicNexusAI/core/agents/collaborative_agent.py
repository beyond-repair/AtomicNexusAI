collaborative_agent.py
from .agent_base import AgentBase

class CollaborativeAgent(AgentBase):
    def __init__(self, name, partners=None):
        super().__init__(name)
        self.partners = partners or []

    def execute(self):
        partners_str = ', '.join(self.partners) if self.partners else 'no partners'
        print(f"{self.name} collaborating with {partners_str}.")