import unittest
from features import *

class TestAtm(unittest.TestCase):
    def setUp(self):
        self.atm = Atm()
        self.pin = self.atm.enter_pin(777)

    def test_pin(self):
        self.assertTrue(self.atm.enter_pin(777))

    def test_rise_money(self):
        self.assertTrue(self.atm.rise_money(10000))