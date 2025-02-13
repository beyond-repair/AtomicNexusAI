# long_term.py

class LongTermMemory:
    def __init__(self) -> None:
        self.memory = []

    def add(self, data: any) -> None:
        self.memory.append(data)

    def retrieve_all(self) -> list:
        return self.memory