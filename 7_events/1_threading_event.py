import threading
import time


def worker(event):
    print("Thread started. Waiting for event...")
    event.wait()  # Ждём сигнала
    print("Event fired, thread resumes!")


event = threading.Event()
thread = threading.Thread(target=worker, args=(event,))
thread.start()

time.sleep(2)  # Имитируем работу
print("Event is fired!")
event.set()  # Запуск события
thread.join()
