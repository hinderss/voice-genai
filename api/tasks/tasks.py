import os

import openai

from api.config import GPT_API_BASE_URL, GPT_API_KEY, GPT_MODEL, VOICE_MODEL, PROMPT
from api.core.celery_worker import celery_app
from api.schemas.task import Result

openai.base_url = GPT_API_BASE_URL
openai.api_key = GPT_API_KEY


@celery_app.task(bind=True)
def process_audio_task(self, file_path: str):
    with open(file_path, "rb") as audio_file:
        transcription = openai.audio.transcriptions.create(
            model=VOICE_MODEL,
            file=audio_file
        )

    text = transcription.text

    response = openai.chat.completions.create(
        model=GPT_MODEL,
        messages=PROMPT,
        temperature=0.7,
        max_tokens=500,
    )

    answer = response.choices[0].message.content.strip()

    os.remove(file_path)

    return Result(transcribed_text=text, answer=answer).json()
