from faker import Faker

fake = Faker(locale='zh_CN')


def url():
    return {
        "host": 'localhost',
        "port": 27017,
        "name": 'root',
        "password": '123456',
        "database": 'test',
        "collection": "user"
    }


def generator():
    return {
        "username": fake.name(),
        "password": fake.lexify(text='????????????????'),
        "nickname": fake.lexify(text='????????????????'),
        "avatar": fake.image_url(),
        "email": fake.email()
    }
