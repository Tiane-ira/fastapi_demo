from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    deleted_at = Column(DateTime, default=datetime.now)

    def to_dict(self):
        data = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.strftime('%Y-%m-%d %H:%M:%S')
        return data


class User(Base):
    __tablename__ = 'cs_user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return "<User(id=%d, name='%s', fullname='%s')>" % (self.id,
                                                            self.name, self.age)
