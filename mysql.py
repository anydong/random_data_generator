import time
from multiprocessing import Pool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from schemas import mysql_user

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://homestead:secret@127.0.0.1:33060/homestead?charset=utf8mb4', pool_size=20,
                       max_overflow=10)

# 创建 Session:
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def run(name):
    child_process_start_time = time.time()
    session = Session()

    for _ in range(10):
        users = []
        for _ in range(1000):
            users.append(mysql_user.generator())
        session.add_all(users)

    session.commit()
    Session.remove()
    print(name, '耗时：', time.time() - child_process_start_time)


if __name__ == "__main__":
    main_process_start_time = time.time()
    pool = Pool()

    for i in range(100):
        print(i)
        pool.apply_async(run, (str(i),))

    pool.close()
    pool.join()

    print('总耗时：', time.time() - main_process_start_time)
