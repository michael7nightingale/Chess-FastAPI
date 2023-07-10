import redis
from contextlib import contextmanager

from config import get_app_settings_by_keys


@contextmanager
def get_redis_pool():

    host, port = get_app_settings_by_keys("REDIS_HOST", "REDIS_PORT")
    pool = None
    try:
        pool = redis.ConnectionPool(host=host, port=port)
        yield pool
    finally:
        if pool is not None:
            pool.disconnect()


with get_redis_pool() as pool:
    redis_session = redis.Redis(connection_pool=pool)
