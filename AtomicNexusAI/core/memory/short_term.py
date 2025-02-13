short_term.py

class ShortTermMemory:
    def __init__(self):
        self.memory = []

    def add(self, data):
        self.memory.append(data)

    def retrieve(self):
        return self.memory[-1] if self.memory else None