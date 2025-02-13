autonomous_agent.py
from .agent_base import AgentBase

class AutonomousAgent(AgentBase):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

    def execute(self):
        print(f"{self.name} executing autonomously with model {self.model}."