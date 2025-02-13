long_term.py

class LongTermMemory:
    def __init__(self):
        self.memory = []

    def add(self, data):
        self.memory.append(data)

    def retrieve_all(self):
        return self.memory