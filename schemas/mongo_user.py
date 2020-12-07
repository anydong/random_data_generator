from faker import Faker

fake = Faker(locale='zh_CN')


def url():
    return 'mongodb://admin:123456@localhost:27017/db_test'


def generator():
    return {
        "username": fake.name(),
        "password": fake.lexify(text='????????????????'),
        "nickname": fake.lexify(text='????????????????'),
        "avatar": fake.image_url(),
        "email": fake.email()
    }
