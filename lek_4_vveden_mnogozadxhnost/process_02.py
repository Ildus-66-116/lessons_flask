import multiprocessing
import time


def worker(num):
    print(f"Запущен процесс {num}")
    time.sleep(3)
    print(f"Завершён процесс {num}")


if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)

    for p in processes:
        p.start()  # по очереди запускаются ничем не отличается от синхронного выполнения
        p.join()

    print("Все процессы завершили работу")
