import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from schemas import table_user

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://homestead:secret@127.0.0.1:33060/homestead', pool_size=20, max_overflow=10)

# 创建 Session:
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def run():
    start_time = time.time()
    session = Session()

    for _ in range(100):
        users = []
        for _ in range(1000):
            users.append(table_user.generator())
        session.add_all(users)

    session.commit()
    Session.remove()
    print(time.time() - start_time)


if __name__ == "__main__":
    start_time = time.time()
    for i in range(100):
        print(i)
        run()
    print('time:', time.time() - start_time)
