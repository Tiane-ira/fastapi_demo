from fastapi import APIRouter

from db.db import db, redis
from model.user import User

router = APIRouter()


@router.get("/db")
def db():
    users = db().query(User).all()
    result = []
    for user in users:
        result.append(user.to_dict())
    return result


@router.get("/redis")
def test():
    c = redis()
    c.set("/redis", "123")
    return c.get("/redis")
