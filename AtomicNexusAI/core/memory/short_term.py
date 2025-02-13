# short_term.py

class ShortTermMemory:
    def __init__(self) -> None:
        self.memory = []

    def add(self, data: any) -> None:
        self.memory.append(data)

    def retrieve(self) -> any:
        return self.memory[-1] if self.memory else None