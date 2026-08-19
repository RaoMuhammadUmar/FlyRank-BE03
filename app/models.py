from pydantic import BaseModel


class Task(BaseModel):
    task: str


class AuthRequest(BaseModel):
    email: str
    password: str