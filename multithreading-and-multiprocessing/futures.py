from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def task(n):
    time.sleep(1)
    return f"Task {n} is complete"

if __name__ == "__main__":

    # 1. Using Threads (Best for I/O)
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(task, [1, 2, 3])

        for r in results:
            print(r)

    # 2. Using Processes (Best for CPU)
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(task, [4, 5, 6])

        for r in results:
            print(r)

            