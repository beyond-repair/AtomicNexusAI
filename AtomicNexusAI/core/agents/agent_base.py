agent_base.py

class AgentBase:
    def __init__(self, name):
        self.name = name

    def execute(self):
        raise NotImplementedError("Subclasses must implement the execute method.")