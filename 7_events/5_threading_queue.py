import threading
from queue import Queue
import time


def producer(event_queue):
    """Этот поток будет генерировать события и помещать их в очередь."""
    for i in range(3):
        time.sleep(2)  # Имитируем работу
        event = f"Event {i}"
        print(f"Produced: {event}")
        event_queue.put(event)

    event_queue.put(None)  # Специальный сигнал для завершения


def consumer(event_queue):
    """Этот поток будет получать события из очереди и обрабатывать их."""
    while True:
        event = event_queue.get()
        if event is None:  # Проверка на специальный сигнал
            break
        print(f"Consumed: {event}")


# Создаем очередь для передачи событий
event_queue = Queue()

# Запускаем потоки
producer_thread = threading.Thread(target=producer, args=(event_queue,))
consumer_thread = threading.Thread(target=consumer, args=(event_queue,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("Event processing completed.")
