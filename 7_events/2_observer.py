import time


class Observable:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)


class Observer:
    def update(self, message):
        print(f"Received event: {message}")


observable = Observable()
observer = Observer()
observable.register(observer)

time.sleep(2)  # Имитируем событие через некоторое время
observable.notify_observers("Event occurred!")
