from fastapi import APIRouter

from common.req import UserAddReq
from common.resp import success
from db.db import session, paginate
from db.redis import setTTL, get
from model.user import User

router = APIRouter()


@router.get("/list")
def add(page: int = 1, size: int = 10, order_by: str = ''):
    s = session()
    page = paginate(s.query(User), page=page, size=size, order_by=order_by)
    s.close()
    return success(data=page)


@router.post("/add")
def add(user: UserAddReq):
    u = User(name=user.name, age=user.age)
    s = session()
    s.add(u)
    s.commit()
    s.close()
    return success()


@router.get("/redis")
def test():
    setTTL("test", "123456")
    return get("test")
