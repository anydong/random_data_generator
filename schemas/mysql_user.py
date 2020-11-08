import datetime
from faker import Faker
from sqlalchemy import Column, BigInteger, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func, text

Base = declarative_base()


def url():
    return 'mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8mb4'


class User(Base):
    __tablename__ = 'user'

    id = Column(BigInteger(), primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    nickname = Column(String(255), nullable=False)
    avatar = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                        default=datetime.datetime.now, onupdate=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now(), default=datetime.datetime.now)


fake = Faker(locale='zh_CN')


def generator():
    return User(
        username=fake.name(),
        password=fake.lexify(text='????????????????'),
        nickname=fake.lexify(text='????????????????'),
        avatar=fake.image_url(),
        email=fake.email()
    )
