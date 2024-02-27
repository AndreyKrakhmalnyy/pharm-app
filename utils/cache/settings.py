import os
from dotenv import load_dotenv 

load_dotenv()

REDIS_HOST = os.getenv('REDIS_HOST') #'localhost' 
REDIS_PORT = os.getenv('REDIS_PORT') #6379 
CACHE_TTL = 60 * 15
REDIS_USER = os.getenv('REDIS_USER')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/1', # 'redis://127.0.0.1:6379'
        'OPTIONS': {
            'db': '1',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}