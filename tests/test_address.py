import unittest
from faker import Faker

fake = Faker(locale='zh_CN')


class TestAddress(unittest.TestCase):

    def test_address(self):
        print('完整通信地址（含邮编）：', fake.address())
        print('----------------国家----------------')
        print('国家：', fake.country())
        print('国家代号：', fake.country_code())
        print('----------------省----------------')
        print('省：', fake.province())
        print('----------------市----------------')
        print('市：', fake.city())
        print('城市后缀：', fake.city_suffix())
        print('----------------区----------------')
        print('区：', fake.district())
        print('----------------街道----------------')
        print('街道名称：', fake.street_name())
        print('街道后缀：', fake.street_suffix())
        print('建筑门牌号：', fake.building_number())
        print('街道地址：', fake.street_address())
        print('----------------邮编----------------')
        print('邮编：', fake.postcode())
