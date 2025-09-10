from fastapi import APIRouter, UploadFile, File
from uuid import uuid4
import os
from api.config import SHARED_DIR
from api.core.celery_worker import celery_app
from api.schemas.task import TaskResponse, TaskResultResponse
from api.tasks.tasks import process_audio_task

router = APIRouter()


@router.post("/voice-to-answer", response_model=TaskResponse)
async def voice_to_answer(file: UploadFile = File(...)):
    file_name = f"{uuid4()}.wav"
    file_path = os.path.join(SHARED_DIR, file_name)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    task = process_audio_task.delay(file_path)
    return TaskResponse(task_id=task.id, status="processing")


@router.get("/tasks/{task_id}", response_model=TaskResultResponse)
async def get_task(task_id: str):
    result = celery_app.AsyncResult(task_id)
    if result.ready():
        return TaskResultResponse(status="done", result=result.result)
    else:
        return TaskResultResponse(status="processing")
