import datetime
from faker import Faker
from sqlalchemy import Column, BigInteger, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func, text

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(BigInteger(), primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now(), default=datetime.datetime.now)
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                        default=datetime.datetime.now, onupdate=True)
    deleted_at = Column(TIMESTAMP, nullable=False, server_default='0000-00-00 00:00:00')


fake = Faker(locale='zh_CN')


def generator():
    return User(
        name=fake.name()
    )
