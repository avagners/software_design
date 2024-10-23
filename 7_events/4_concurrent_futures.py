from concurrent.futures import ThreadPoolExecutor, wait
import time


def worker():
    time.sleep(2)
    print("Worker finished")


with ThreadPoolExecutor() as executor:
    futures = [executor.submit(worker) for _ in range(2)]
    print("Waiting for workers to finish...")
    wait(futures)  # Ждём завершения всех задач
    print("All workers done")
