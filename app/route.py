from fastapi import APIRouter
from app.models import Task

router = APIRouter()

from app.database import cursor, connection


@router.get("/")
def root():
    return {"message": "Hello, FlyRank!"}


@router.get("/tasks")
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return {"tasks": tasks}


@router.post("/tasks")
def create_task(task: Task):
    cursor.execute(
        "INSERT INTO tasks (task) VALUES (?)",
        (task.task,)
    )
    connection.commit()

    return {
        "message": "Task created successfully",
        "task": task.task
    }

@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    cursor.execute(
        "UPDATE tasks SET task = ? WHERE id = ?",
        (task.task, task_id)
    )
    connection.commit()

    if cursor.rowcount == 0:
        return {"error": "Task not found"}

    return {
        "message": "Task updated successfully",
        "task": task.task
    }


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    cursor.execute("SELECT task FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()

    if task is None:
        return {"error": "Task not found"}

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()

    return {
        "message": "Task deleted successfully",
        "task": task[0]
    }