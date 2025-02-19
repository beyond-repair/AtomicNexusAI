# AtomicNexusAI/core/agents/autonomous_agent.py

from .agent_base import AgentBase
from AtomicNexusAI/core/models/adaptive_selector import AdaptiveSelector

class AutonomousAgent(AgentBase):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model
        self.selector = AdaptiveSelector()  # Initialize adaptive selector
        self.execution_context = {}  # Memory for tracking execution context

    def execute(self):
        # Dynamically select best model for the current task
        selected_model = self.selector.select_model(self.model)
        self.execution_context['selected_model'] = selected_model
        print(f"{self.name} executing autonomously with model {selected_model}.")
        return f"{self.name} executed using {selected_model}."