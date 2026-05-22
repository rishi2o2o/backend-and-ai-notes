import threading
import time

def worker():
    print("Thread starting...")
    time.sleep(2)  # Simulating a network request or I/O
    print("Thread finished!")

# Create two threads
t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)

t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()

