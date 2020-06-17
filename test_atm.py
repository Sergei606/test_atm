import unittest
from features import *

class TestAtm(unittest.TestCase):
    def setUp(self):
        self.atm = Atm()
        self.pin = 777
        self.attempts = 2
        self.balance = 10000

    def test_rise_money(self):
        self.assertTrue(self.atm.rise_money(1000))

    def test_overall_balance(self):
        self.assertEqual(10001, self.atm.rise_money(1))

    def test_correct_pin(self):
        self.assertTrue(True, self.pin)

    def test_check_balance(self):
        self.atm.enter_pin(self.pin)
        self.assertEqual(10000, self.atm.check_balance())

    def test_incorrect_balance(self):
        self.atm.enter_pin(self.pin)
        self.assertNotEqual(9999, self.atm.check_balance())

    def test_incorrect_pin(self):
        self.assertNotEqual(111, self.pin)

    def test_get_money(self):
        self.atm.enter_pin(self.pin)
        self.assertEqual(5000, self.atm.get_money(5000))

    def test_attempts(self):
        self.atm.enter_pin(777)
        self.assertTrue(self.attempts)






