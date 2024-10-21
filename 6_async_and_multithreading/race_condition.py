"""
В коде на Java несколько потоков одновременно пытаются изменить значение
переменной counter. Так как операция counter++ не атомарна (она состоит
из нескольких шагов, это может привести к тому, что два потока
одновременно прочитают одно и то же значение, увеличат его и запишут обратно,
что приведёт к неверному результату. Это типичная ошибка "состояние гонки".

Ниже исправленный вариант на Python. Использована блокировка (threading.Lock),
чтобы сделать изменение переменной атомарным и предотвратить состояние гонки.
"""


import threading

counter = 0
lock = threading.Lock()


def increment_counter():
    global counter
    for _ in range(100000):
        with lock:  # Защищаем доступ к общей переменной
            counter += 1


def main():
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=increment_counter)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final counter value: {counter}")


if __name__ == "__main__":
    main()
