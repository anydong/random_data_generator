from faker import Faker
import config

fake = Faker(locale=config.locale)
if config.seed:
    Faker.seed(config.seed)


def address():
    """
    :return: 一个字符串地址，形如：山西省红梅市牧野济南街n座 885605

    """
    return fake.address()


def building_number():
    return fake.building_number()


def city():
    return fake.city()


def city_suffix():
    return fake.city_suffix()


def country():
    return fake.country()


def country_code():
    return fake.country_code()


def postcode():
    return fake.postcode()


def street_address():
    return fake.street_address()


def street_name():
    return fake.street_name()


def street_suffix():
    return fake.street_suffix()
