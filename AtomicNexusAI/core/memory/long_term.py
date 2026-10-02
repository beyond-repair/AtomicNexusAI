# long_term.py
from typing import Any, List


class LongTermMemory:
    def __init__(self) -> None:
        self.memory: List[Any] = []

    def add(self, data: Any) -> None:
        self.memory.append(data)

    def retrieve_all(self) -> list:
        return list(self.memory)
