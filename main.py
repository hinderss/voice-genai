from fastapi import FastAPI

from api.endpoints import tasks

app = FastAPI(title="Voice Processing API")

app.include_router(tasks.router, prefix="/api")
