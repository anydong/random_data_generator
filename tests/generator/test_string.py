import unittest
import random
import string


class TestString(unittest.TestCase):

    def test_string(self):
        letters = string.ascii_letters + string.digits
        for _ in range(9):
            print('----------------------------------------------------------------')
            print('随机字符：', random.sample(letters, 10))
            print('随机字符串：', ''.join(random.choice(letters) for _ in range(10)))
            print('随机枚举值：', random.choice(letters))
            print('随机打乱：', ''.join(random.sample(letters, len(letters))))
