from fastapi import FastAPI
from pydantic import BaseModel
from app.supabase_client import supabase

app = FastAPI()

tasks = []


class Task(BaseModel):
    task: str


@app.get("/")
def root():
    return {"message": "Hello, FlyRank!"}


@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task.task)
    return {
        "message": "Task created successfully",
        "task": task.task
    }


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    if 0 <= task_id < len(tasks):
        tasks[task_id] = task.task
        return {
            "message": "Task updated successfully",
            "task": task.task
        }
    return {"error": "Task not found"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if 0 <= task_id < len(tasks):
        deleted_task = tasks.pop(task_id)
        return {
            "message": "Task deleted successfully",
            "task": deleted_task
        }
    return {"error": "Task not found"}