import asyncio


class ReactiveStream:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    async def publish(self, event):
        for subscriber in self.subscribers:
            await subscriber(event)


async def subscriber1(event):
    print(f"Subscriber 1 received: {event}")


async def subscriber2(event):
    print(f"Subscriber 2 received: {event}")


stream = ReactiveStream()
stream.subscribe(subscriber1)
stream.subscribe(subscriber2)


async def main():
    await stream.publish("Event 1")
    await stream.publish("Event 2")

asyncio.run(main())
