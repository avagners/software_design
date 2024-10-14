from typing import List


class AverageCalculator:

    @staticmethod
    def calculate_average(numbers: List[int]) -> float:
        if not numbers:
            raise ValueError("List of numbers is empty")
        return sum(numbers) / len(numbers)


if __name__ == "__main__":
    calculator = AverageCalculator()

    # Примеры покрытые тестами
    numbers1 = [10, 20, 30, 40]
    print(f"Среднее от {numbers1}:", calculator.calculate_average(numbers1))
    numbers2 = [-10, -20, -30, -40]
    print(f"Среднее от {numbers2}:", calculator.calculate_average(numbers2))

    try:
        print("Среднее от []:", calculator.calculate_average([]))
    except ValueError as e:
        print("Ошибка:", e)

    # Пример с некорректными данными, который не покрыт тестами
    numbers3 = [10, None, 20]
    try:
        print(f"Среднее от {numbers3}:", calculator.calculate_average(numbers3))
    except TypeError as e:
        print("Ошибка (TypeError):", e)

    # Еще один случай, когда могут возникнуть ошибки:
    # список содержит строку, вместо целого числа
    numbers4 = [10, '20', 30]
    try:
        print(f"Среднее от {numbers4}:", calculator.calculate_average(numbers4))
    except TypeError as e:
        print("Ошибка (TypeError):", e)
