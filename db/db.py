from sqlalchemy import desc, asc
from sqlalchemy.orm import Session, Query

from common.page import Page
from . import E


def session():
    """
    Returns a SQLAlchemy session instance.
    """
    return Session(E)


def paginate(query: Query, page: int = 1, size: int = 10, order_by: str = '') -> Page:
    if page < 1:
        page = 1
    if page > 100:
        page = 100
    if size < 1:
        size = 10
    if size > 200:
        size = 200
    # 获取总记录数
    total = query.count()
    # 计算偏移量
    offset_value = (page - 1) * size
    # 排序
    sorts = order_by.split(";")
    for sort in sorts:
        if sort.endswith("-"):
            query = query.order_by(desc(sort[:-1]))
        else:
            query = query.order_by(asc(sort))
    # 查询分页后的数据
    items = query.offset(offset_value).limit(size).all()
    # 构造分页结果
    page = Page(items=items, total=total, currentPage=page, size=size)
    return page
