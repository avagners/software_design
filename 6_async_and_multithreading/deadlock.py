"""
В примере на Java два потока пытаются захватить два ресурса (замка) в разном
порядке. Поток 1 захватывает lock1 и ждёт lock2, в то время как поток 2 
захватывает lock2 и ждёт lock1. Это приводит к взаимной блокировке, поскольку
оба потока ждут освобождения ресурсов друг другом, что никогда не произойдёт.

Ниже исправленный вариант на Python. Использован порядок захвата блокировок,
гарантируя, что оба потока всегда захватывают замки в одном порядке.
"""

import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def thread1_func():
    with lock1:
        print("Thread 1 acquired lock1")
        time.sleep(0.05)  # Задержка, чтобы второй поток успел захватить lock2
        with lock2:
            print("Thread 1 acquired lock2")


def thread2_func():
    with lock1:  # Изменили порядок захвата замков (сначала lock1)
        print("Thread 2 acquired lock1")
        time.sleep(0.05)  # Задержка, чтобы первый поток успел захватить lock1
        with lock2:
            print("Thread 2 acquired lock2")


def main():
    thread1 = threading.Thread(target=thread1_func)
    thread2 = threading.Thread(target=thread2_func)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Finished")


if __name__ == "__main__":
    main()
