from fastapi import APIRouter, Depends, HTTPException

from app.models import Task
from app.database import cursor, connection
from app.dependencies import get_current_user

router = APIRouter()


# -------------------------
# ROOT
# -------------------------

@router.get("/")
def root():
    return {
        "message": "Hello, FlyRank!"
    }


# -------------------------
# GET TASKS
# PROTECTED
# -------------------------

@router.get("/tasks")
def get_tasks(
    current_user=Depends(get_current_user)
):
    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    return {
        "tasks": tasks
    }


# -------------------------
# CREATE TASK
# PROTECTED
# -------------------------

@router.post("/tasks")
def create_task(
    task: Task,
    current_user=Depends(get_current_user)
):
    cursor.execute(
        "INSERT INTO tasks (task) VALUES (%s)",
        (task.task,)
    )

    connection.commit()

    return {
        "message": "Task created successfully",
        "task": task.task
    }


# -------------------------
# UPDATE TASK
# PROTECTED
# -------------------------

@router.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    task: Task,
    current_user=Depends(get_current_user)
):
    cursor.execute(
        "UPDATE tasks SET task = %s WHERE id = %s",
        (task.task, task_id)
    )

    connection.commit()

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task updated successfully",
        "task": task.task
    }


# -------------------------
# DELETE TASK
# PROTECTED
# -------------------------

@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    current_user=Depends(get_current_user)
):
    cursor.execute(
        "SELECT task FROM tasks WHERE id = %s",
        (task_id,)
    )

    task = cursor.fetchone()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    cursor.execute(
        "DELETE FROM tasks WHERE id = %s",
        (task_id,)
    )

    connection.commit()

    return {
        "message": "Task deleted successfully",
        "task": task[0]
    }