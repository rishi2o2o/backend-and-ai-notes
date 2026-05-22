import multiprocessing
import time

def heavy_math(n):
    print(f"Process calculating for {n}...")
    time.sleep(2)  # Simulating heavy CPU work
    print(f"Process {n} done!")

if __name__ == "__main__":  # Required for multiprocessing to work safely
    p1 = multiprocessing.Process(target=heavy_math, args=(1,))
    p2 = multiprocessing.Process(target=heavy_math, args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

