import unittest
import random


class TestNumeric(unittest.TestCase):

    def test_numeric(self):
        for _ in range(9):
            print('----------------------------------------------------------------')
            print('随机整数（min ～ max）：', random.randint(0, 9))
            print('随机整数（min ～ max，步进 step）', random.randrange(0, 100, 2))
            print('随机浮点数（0 ～ 1）：', random.random())
            print('随机浮点数（min ～ max）：', random.uniform(0, 9))
