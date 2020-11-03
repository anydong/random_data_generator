import unittest
from faker import Faker

fake = Faker(locale='zh_CN')


class TestDatetime(unittest.TestCase):

    def test_datetime(self):
        print('时间字符串：', fake.date_time())
        print('时间戳(end_time ~ start_time)：', fake.unix_time())
        print('年：', fake.year())
        print('月：', fake.month())
        print('日：', fake.day_of_month())
        print('日期：', fake.date())
        print('时间：', fake.time())
