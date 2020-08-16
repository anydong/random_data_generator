import unittest
from generator import address


class TestAddress(unittest.TestCase):

    def test_address(self):
        self.assertIsInstance(address.address(), str)

    def test_building_number(self):
        self.assertIsInstance(address.building_number(), str)

    def test_city(self):
        self.assertIsInstance(address.city(), str)

    def test_city_suffix(self):
        self.assertIsInstance(address.city_suffix(), str)
