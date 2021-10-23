import redis
import os

REDIS_LIST_KEY = 'messages'
REDIS_SUB_KEY = 'messages_channel'


def get_redis_url() -> str:
    local_env = os.getenv("LOCAL_ENV_TYPE")
    if local_env == "DOCKER":
        return 'redis'
    elif local_env == "VENV":
        return 'localhost'
    else:
        raise AttributeError('envriorment variable LOCAL_ENV_TYPE was not set correctly')


def get_redis() -> redis.StrictRedis:
    return redis.StrictRedis(get_redis_url(), 6379, charset="utf-8", decode_responses=True)
