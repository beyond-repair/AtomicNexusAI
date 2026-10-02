# autonomous_agent.py
from .agent_base import AgentBase
from ..models.adaptive_selector import AdaptiveSelector


class AutonomousAgent(AgentBase):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model
        self.selector = AdaptiveSelector()
        self.execution_context = {}

    def execute(self):
        selected_model = self.selector.select_model(self.model)
        self.execution_context["selected_model"] = selected_model
        result = f"{self.name} executed using {selected_model}."
        print(f"{self.name} executing autonomously with model {selected_model}.")
        return result
