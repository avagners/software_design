'''
Используем threading.Lock для синхронизации доступа к counter.
Блокировка гарантирует, что в любой момент времени только один
поток выполняет инкремент.

Программа гарантированно выведет ожидаемый результат: "Counter: 2000".
'''

import threading

# Глобальный счётчик и объект блокировки
counter = 0
lock = threading.Lock()


def task():
    global counter
    for _ in range(1000):
        # Используем блокировку для синхронизации доступа к счётчику
        with lock:
            counter += 1


# Создаем потоки
thread1 = threading.Thread(target=task)
thread2 = threading.Thread(target=task)

# Запускаем потоки
thread1.start()
thread2.start()

# Ждём завершения потоков
thread1.join()
thread2.join()

print("Counter:", counter)  # Counter: 2000
