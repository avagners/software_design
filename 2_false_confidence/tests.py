import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(1000.0)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 1000.0, "Начальный баланс должен быть 1000")

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.get_balance(), 1500.0, "Баланс должен быть 1500 после депозита 500")

    def test_withdraw(self):
        self.account.withdraw(200.0)
        self.assertEqual(self.account.get_balance(), 800.0, "Баланс должен быть 800 после снятия 200")

    def test_negative_withdraw(self):
        self.account.withdraw(1200.0)  # Баланс уйдет в минус
        self.assertEqual(self.account.get_balance(), -200.0, "Баланс должен быть -200 после снятия 1200")

    def test_negative_deposit(self):
        self.account.deposit(-500.0)  # Отрицательная сумма
        self.assertEqual(self.account.get_balance(), 500.0, "Баланс должен быть 500 после депозита -500")

    def test_negative_withdraw_amount(self):
        self.account.withdraw(-100.0)  # Отрицательная сумма на снятие
        self.assertEqual(self.account.get_balance(), 1100.0, "Баланс должен быть 1100 после снятия -100")


if __name__ == "__main__":
    unittest.main()
