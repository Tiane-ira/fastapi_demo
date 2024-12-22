from pydantic import BaseModel


class Req(BaseModel):
    pass


class UserAddReq(Req):
    name: str
    age: int
