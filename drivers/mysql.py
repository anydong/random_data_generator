import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import OperationalError
import global_var as gl

schema = __import__(''.join(['schemas', '.', gl.get_value('schema')]), fromlist=['schema'])
# 初始化数据库连接:
engine = create_engine(schema.url(), pool_size=20,
                       max_overflow=10)

# 创建 Session:
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def run(name):
    child_process_start_time = time.time()
    session = Session()

    for _ in range(10):
        rows = []
        for _ in range(1000):
            rows.append(schema.generator())
        session.add_all(rows)

    session.commit()
    Session.remove()
    print(name, '耗时：', time.time() - child_process_start_time)


def error_callback(res):
    if isinstance(res, OperationalError):
        print('数据库错误：', res)
    else:
        print(res)
