from typing import final
from typing import NamedTuple
from decimal import Decimal


@final
class BankAccount(NamedTuple):
    balance: Decimal

    @staticmethod
    def create(initial_balance: Decimal) -> 'BankAccount':
        # Проверка на положительный начальный баланс
        if initial_balance < Decimal('0'):
            raise ValueError("Начальный баланс должен быть неотрицательным.")
        return BankAccount(initial_balance)

    def deposit(self, amount: Decimal) -> 'BankAccount':
        # Проверка на положительную сумму депозита
        if amount <= Decimal('0'):
            raise ValueError("Сумма депозита должна быть положительной.")
        # Возвращаем новый объект BankAccount с обновленным балансом
        return BankAccount(self.balance + amount)

    def withdraw(self, amount: Decimal) -> 'BankAccount':
        # Проверка на положительную сумму снятия и на достаточность средств
        if amount <= Decimal('0'):
            raise ValueError("Сумма снятия должна быть положительной.")
        if self.balance < amount:
            raise ValueError("Недостаточно средств на счете.")
        # Возвращаем новый объект BankAccount с обновленным балансом
        return BankAccount(self.balance - amount)

    def get_balance(self) -> Decimal:
        return self.balance

    def __str__(self) -> str:
        return f"BankAccount(balance={self.balance})"


if __name__ == "__main__":
    # Создаем новый объект BankAccount
    account = BankAccount.create(Decimal("1000.00"))
    print("Начальный баланс:", account)

    # Вносим депозит и получаем новый объект
    account = account.deposit(Decimal("500.00"))
    print("Баланс после депозита:", account)

    # Снимаем средства и получаем новый объект
    account = account.withdraw(Decimal("300.00"))
    print("Баланс после снятия:", account)
