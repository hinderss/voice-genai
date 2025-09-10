from pydantic import BaseModel


class Result(BaseModel):
    transcribed_text: str
    answer: str


class TaskResponse(BaseModel):
    task_id: str
    status: str


class TaskResultResponse(BaseModel):
    status: str
    result: Result



