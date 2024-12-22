from redis import Redis

from config import CONF

default_ttl = 60 * 30


def redis():
    """
    Returns a Redis connection instance.
    """
    return Redis(host=CONF['redis']['host'],
                 port=CONF['redis']['port'],
                 db=CONF['redis']['db'],
                 password=CONF['redis']['password']
                 )


def get(key: str) -> str:
    """
    Returns a value from the Redis cache.
    """
    return redis().get(key)


def setTTL(key: str, value: str, expire: int = default_ttl) -> None:
    """
    Sets a value in the Redis
    """
    redis().set(key, value, expire)
