from fastapi import APIRouter, HTTPException
from task_api_app.schemas.task_schema import TaskCreate, TaskUpdate
from task_api_app.services.task_service import create_task, get_all_tasks, get_task, update_tasks, delete_task, get_stats

router = APIRouter()

@router.post("/tasks")
def add_task(task:TaskCreate):
    return create_task(task.title, task.priority)
   

@router.get("/tasks")
def list_tasks():
    return get_all_tasks()

@router.get("/tasks/{task_id}")
def get_single_task(task_id:int):
    task = get_task(task_id)
    return task

@router.put("/tasks/{task_id}")
def edit_task(task_id: int, task: TaskUpdate):
    return update_tasks(task_id, task.title, task.priority)

@router.get("/stats")
def stats():
    return get_stats()

@router.delete("/tasks/{task_id}")
def remove_task(task_id:int):
    return delete_task(task_id)
