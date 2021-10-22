import redis
from redis import StrictRedis

REDIS_LIST_KEY = 'messages'
REDIS_SUB_KEY = 'messages_channel'


def get_redis() -> StrictRedis:
    return redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
