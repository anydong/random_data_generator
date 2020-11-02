import datetime
import time
from faker import Faker
from sqlalchemy import Column, BigInteger, String, create_engine, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import func, text

fake = Faker(locale='zh_CN')

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(BigInteger(), primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now(), default=datetime.datetime.now)
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                        default=datetime.datetime.now, onupdate=True)
    deleted_at = Column(TIMESTAMP, nullable=False, server_default='0000-00-00 00:00:00')


# 创建表
# Base.metadata.create_all(engine)


# 初始化数据库连接:
engine = create_engine('mysql+pymysql://homestead:secret@127.0.0.1:33060/homestead', pool_size=20, max_overflow=10)
# 创建DBSession类型:


session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def run():
    start_time = time.time()
    session = Session()

    for _ in range(100):
        users = []
        for _ in range(1000):
            users.append(User(
                name=fake.name()
            ))
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
