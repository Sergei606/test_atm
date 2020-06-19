import unittest
from features import *

class TestAtm(unittest.TestCase):
    def setUp(self):
        self.atm = Atm()
        self.attempts = 2
        self.balance = 10000

    def test_client_can_get_money(self):
        self.assertFalse(self.atm.client_can_get_money)

    def test_balance(self):
        self.assertEqual(10000, self.balance)

    def test_overall_balance(self):
        self.assertEqual(self.balance + 1000, self.atm.rise_money(1000))

    def test_two_recharge(self):
        self.rise = 1000
        self.assertEqual(13000, self.atm.rise_money(2000) + self.rise)

    def test_not_replenish(self):
        self.assertEqual(self.balance, self.atm.rise_money(0))

    def test_negative_replenishment(self):
        self.assertEqual(self.balance - 10001, self.atm.rise_money(-10001))

    def test_get_money(self):
        self.assertEqual(1, self.atm.get_money(1))

    def test_get_nothing(self):
        self.assertEqual(self.balance, self.atm.get_money(0))

    def test_get_negative_sum(self):
        self.assertFalse(self.atm.get_money(-10))

    def test_check_balance(self):
        self.assertEqual(10000, self.atm.check_balance())










