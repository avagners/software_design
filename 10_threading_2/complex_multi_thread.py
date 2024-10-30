import threading
import random

SIZE = 1000000  # Размер массива
THREADS = 4

data = [random.randint(0, 100) for _ in range(SIZE)]  # Заполняем массив случайными числами
sum_result = 0
lock = threading.Lock()  # Блокировка для синхронизации доступа


def partial_sum(start, end):
    global sum_result
    local_sum = sum(data[start:end])

    # Синхронизация при доступе к общей переменной
    with lock:
        sum_result += local_sum


# Определяем размер части массива для каждого потока
chunk_size = SIZE // THREADS
threads = []

# Создаем и запускаем потоки
for i in range(THREADS):
    start = i * chunk_size
    end = SIZE if i == THREADS - 1 else (i + 1) * chunk_size
    thread = threading.Thread(target=partial_sum, args=(start, end))
    threads.append(thread)
    thread.start()

# Ждем завершения всех потоков
for thread in threads:
    thread.join()

print("Sum of all elements:", sum_result)
