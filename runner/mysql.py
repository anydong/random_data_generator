import threading
from generator import address
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from runner import schema

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


def insert():
    session = DBSession()
    user = schema.User(
        name=address.street_name()
    )
    session.add(user)
    session.commit()
    session.close()


for num in range(1000):
    t = threading.Thread(target=insert, name='ccc')
    t.start()
    t.join()
    print(num)
