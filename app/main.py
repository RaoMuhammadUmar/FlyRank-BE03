from fastapi import FastAPI
from app.route import router
from app.supabase_client import supabase

app = FastAPI()

app.include_router(router)