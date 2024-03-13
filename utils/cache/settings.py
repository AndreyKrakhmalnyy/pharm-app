import os
from dotenv import load_dotenv 

load_dotenv()

REDIS_HOST = os.getenv('REDIS_HOST') 
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_USER = os.getenv('REDIS_USER')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1', #f'redis://{REDIS_HOST}:{REDIS_PORT}/1'
        'OPTIONS': {
            'db': 1,
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
