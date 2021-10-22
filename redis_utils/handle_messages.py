from redis_utils.redis_config import REDIS_LIST_KEY, get_redis


def save_message_to_redis(message: str) ->None:
    """
    Save the posted message into the defined REDIS_LIST_KEY
    :param message: the message to be saved
    :return: None
    """
    r = get_redis()
    # push the message into the defined redis list, REDIS_LIST_KEY
    r.rpush(REDIS_LIST_KEY, message)

def query_all_messages() -> list[str]:
    """
    Query the redis_utils database for all the strings stored in REDIS_LIST_KEY.
    :return: list of all posted strings
    """
    r = get_redis()

    # query the whole redis list in a single command
    words = r.lrange(REDIS_LIST_KEY, 0, -1)
    return words


def worker_save_message(message:str) -> None:
    """
    This the function passed to the worker by the queue.
    In this implementation we save the message into redis_utils list.

    :param message: the message to be saved
    :return: None
    """
    save_message_to_redis(message)


