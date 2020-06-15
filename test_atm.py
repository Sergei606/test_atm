import unittest
from features import *

class TestAtm(unittest.TestCase):
    def setUp(self):
        self.atm = Atm()
        self.pin = self.atm.enter_pin(777)

    def test_pin(self):
        self.assertTrue(self.pin)

    def test_rise_money(self):
        self.assertTrue(self.atm.rise_money(1000))

    def test_overall_balance(self):
        self.assertEqual(10001, self.atm.rise_money(1))

    def test_correct_pin(self):
        self.assertTrue(True, self.pin)

    def test_check_balance(self):
        self.assertEqual(10000, self.atm.check_balance())\

    def test_incorrect_balance(self):
        self.assertNotEqual(99999, self.atm.check_balance())

    def test_incorrect_pin(self):
        self.assertNotEqual(111, self.pin)

    def test_get_money(self):
        self.assertEqual(5000, self.atm.get_money(5000))

    
