class BankAccount:
    def __init__(self, initial_balance: float) -> None:
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.__balance: float = initial_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств на счете для снятия")
        self.__balance -= amount

    def get_balance(self) -> float:
        return self.__balance


if __name__ == "__main__":
    try:
        account = BankAccount(1000.0)
        print(f"Начальный баланс: {account.get_balance()}")  # 1000.0

        # Вносим депозит 500
        account.deposit(500.0)
        print(f"Баланс после депозита: {account.get_balance()}")  # 1500.0

        # Снимаем 300
        account.withdraw(300.0)
        print(f"Баланс после снятия: {account.get_balance()}")  # 1200.0

        # Попробуем внести отрицательный депозит (ожидается ошибка)
        account.deposit(-100.0)
    except ValueError as e:
        print(f"Ошибка депозита: {e}")

    try:
        # Попробуем снять больше средств, чем на балансе (ожидается ошибка)
        account.withdraw(2000.0)
    except ValueError as e:
        print(f"Ошибка снятия: {e}")

    try:
        # Попробуем снять отрицательную сумму (ожидается ошибка)
        account.withdraw(-50.0)
    except ValueError as e:
        print(f"Ошибка снятия отрицательной суммы: {e}")

    print(f"Итоговый баланс: {account.get_balance()}")  # 1200.0
