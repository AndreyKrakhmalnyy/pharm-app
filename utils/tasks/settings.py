import os
from dotenv import load_dotenv 

load_dotenv()

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
CELERY_TIMEZONE = os.getenv('CELERY_TIMEZONE')
CELERY_TASK_TRACK_STARTED = os.getenv('CELERY_TASK_TRACK_STARTED')
CELERY_TASK_TIME_LIMIT = os.getenv('CELERY_TASK_TIME_LIMIT')
CELERY_CACHE_BACKEND = os.getenv('CELERY_CACHE_BACKEND')

# FLOWER http://127.0.0.1:5555/