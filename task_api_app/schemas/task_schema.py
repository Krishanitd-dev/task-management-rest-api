from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    priority: int

class TaskUpdate(BaseModel):
    id: int
    title: str
    priority: int
    