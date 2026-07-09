from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    priority: int

class TaskUpdate(BaseModel):
    
    title: str
    priority: int
    