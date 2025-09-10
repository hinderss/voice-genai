import os

SHARED_DIR = os.getenv("SHARED_DIR", "/shared")
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", CELERY_BROKER_URL)

GPT_API_KEY = os.getenv("GPT_API_KEY")
GPT_API_BASE_URL = os.getenv("GPT_API_BASE_URL")
GPT_MODEL = os.getenv("GPT_MODEL")
VOICE_MODEL = os.getenv("VOICE_MODEL")

PROMPT = "You are an assistant that answers questions."
