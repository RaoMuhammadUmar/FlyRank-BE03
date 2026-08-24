from fastapi import FastAPI

from app.route import router as task_router
from app.auth import router as auth_router


app = FastAPI()


app.include_router(auth_router)
app.include_router(task_router)