'''
В этом примере используем ProcessPoolExecutor для параллельной обработки,
что будет аналогом ForkJoinPool в Java.
'''

import random
from concurrent.futures import ProcessPoolExecutor

SIZE = 1000000
data = [random.randint(0, 99) for _ in range(SIZE)]


def partial_sum(args):
    """Функция для вычисления суммы части массива."""
    start, end = args
    return sum(data[start:end])


chunk_size = SIZE // 4  # Разделяем данные на 4 части
ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(4)]

with ProcessPoolExecutor() as executor:
    # Передаем список кортежей в partial_sum напрямую
    results = list(executor.map(partial_sum, ranges))

total_sum = sum(results)
print("Sum of all elements:", total_sum)
