import time
from multiprocessing import Pool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import OperationalError

schema = __import__(''.join(['schemas', '.', 'mysql_user']), fromlist=['schema'])
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


def main():
    main_process_start_time = time.time()
    pool = Pool()

    for i in range(10):
        print(i)
        pool.apply_async(run, (str(i),), error_callback=error_callback)

    pool.close()
    pool.join()

    print('总耗时：', time.time() - main_process_start_time)


if __name__ == "__main__":
    main()
