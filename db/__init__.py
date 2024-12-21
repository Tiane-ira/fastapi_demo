from sqlalchemy import create_engine, URL

from config import CONF

db = CONF['db']

url = URL.create(
    drivername=f"{db['type']}+{db['driver']}",
    username=db['user'],
    password=db['password'],
    host=db['host'],
    port=db['port'],
    database=db['database'],
    query=CONF['db.params']
)
E = create_engine(url)
