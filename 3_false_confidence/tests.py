import unittest

from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(1000.0)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 1000.0)

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.get_balance(), 1500.0)

    def test_withdraw(self):
        self.account.withdraw(200.0)
        self.assertEqual(self.account.get_balance(), 800.0)

    def test_negative_withdraw(self):
        with self.assertRaises(ValueError, msg="Недостаточно средств на счете для снятия"):
            self.account.withdraw(1200.0)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError, msg="Сумма депозита должна быть положительной"):
            self.account.deposit(-500.0)

    def test_negative_withdraw_amount(self):
        with self.assertRaises(ValueError, msg="Сумма снятия должна быть положительной"):
            self.account.withdraw(-100.0)


if __name__ == "__main__":
    unittest.main()
