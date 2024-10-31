import unittest
from decimal import Decimal
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self) -> None:
        # Инициализация начального состояния
        self.initial_balance = Decimal("1000.00")
        self.account = BankAccount.create(self.initial_balance)

    def test_initial_balance(self) -> None:
        # Проверка начального баланса
        self.assertEqual(self.account.get_balance(), self.initial_balance)

    def test_deposit(self) -> None:
        # Тестируем корректное пополнение
        new_account = self.account.deposit(Decimal("500.00"))
        self.assertEqual(new_account.get_balance(), Decimal("1500.00"))

    def test_withdraw(self) -> None:
        # Тестируем корректное снятие
        new_account = self.account.withdraw(Decimal("300.00"))
        self.assertEqual(new_account.get_balance(), Decimal("700.00"))

    def test_deposit_negative_amount(self) -> None:
        # Тестируем исключение при попытке внести отрицательный депозит
        with self.assertRaises(ValueError, msg="Сумма депозита должна быть положительной."):
            self.account.deposit(Decimal("-100.00"))

    def test_withdraw_negative_amount(self) -> None:
        # Тестируем исключение при попытке снять отрицательную сумму
        with self.assertRaises(ValueError, msg="Сумма снятия должна быть положительной."):
            self.account.withdraw(Decimal("-50.00"))

    def test_withdraw_insufficient_funds(self) -> None:
        # Тестируем исключение при недостатке средств
        with self.assertRaises(ValueError, msg="Недостаточно средств на счете."):
            self.account.withdraw(Decimal("1500.00"))


if __name__ == "__main__":
    unittest.main()
