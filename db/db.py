from redis import Redis
from sqlalchemy.orm import Session

from config import CONF
from . import E


def db():
    """
    Returns a SQLAlchemy session instance.
    """
    return Session(E)


def redis():
    """
    Returns a Redis connection instance.
    """
    return Redis(host=CONF['redis']['host'],
                 port=CONF['redis']['port'],
                 db=CONF['redis']['db'],
                 password=CONF['redis']['password']
                 )
