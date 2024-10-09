class BankAccount:
    def __init__(self, initial_balance: float) -> None:
        self.__balance: float = initial_balance

    def deposit(self, amount: float) -> None:
        # Нет проверки на отрицательную сумму
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        # Нет проверки на отрицательную сумму
        # Баланс может уйти в минус
        self.__balance -= amount

    def get_balance(self) -> float:
        return self.__balance


if __name__ == "__main__":
    account = BankAccount(1000.0)
    account.deposit(500.0)
    print(f"Баланс после депозита: {account.get_balance()}")  # 1500

    account.withdraw(2000.0)
    print(f"Баланс после снятия: {account.get_balance()}")  # -500

    account.deposit(-100.0)
    print(f"Баланс после отрицательного депозита: {account.get_balance()}")  # Ожидается -600

    account.withdraw(-50.0)
    print(f"Баланс после отрицательного снятия: {account.get_balance()}")  # Ожидается -550
