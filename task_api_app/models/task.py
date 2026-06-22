from dataclasses import dataclass

@dataclass
class Task:
    id: int = None
    title = str
    priority: str

