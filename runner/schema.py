from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, String, create_engine, TIMESTAMP
from sqlalchemy.sql import func, text
import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(BigInteger(), primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now(), default=datetime.datetime.now)
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                        default=datetime.datetime.now, onupdate=True)
    deleted_at = Column(TIMESTAMP, nullable=False, server_default='0000-00-00 00:00:00')


# 初始化数据库连接:
# engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test')
# 创建表
# Base.metadata.create_all(engine)
