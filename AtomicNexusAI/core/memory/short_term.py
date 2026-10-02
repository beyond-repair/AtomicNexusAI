# short_term.py
from typing import Any, List, Optional


class ShortTermMemory:
    def __init__(self) -> None:
        self.memory: List[Any] = []

    def add(self, data: Any) -> None:
        self.memory.append(data)

    def retrieve(self) -> Optional[Any]:
        return self.memory[-1] if self.memory else None

    def clear(self) -> None:
        self.memory.clear()
