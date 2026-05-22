# Multithreading and Multiprocessing

Multithreading and multiprocessing are techniques operating systems use to achieve multitasking. Multithreading runs multiple lightweight threads within a single process, sharing the same memory. Multiprocessing runs multiple independent processes across multiple CPU cores, each with its own memory space.


## Multithreading

What it is: A single program is divided into multiple independent pathways of execution (threads).

* Memory: Threads share the same memory space and resources of their parent process.

* Use Cases: Ideal for I/O-bound tasks (e.g., waiting for downloads, reading files, or handling user interface clicks) because a thread can work on something else while another is waiting.

* Pros/Cons: Lightweight and fast to create, but highly vulnerable—if one thread crashes, the entire program can go down.


## Multiprocessing

What it is: The operating system assigns entirely separate tasks to different CPU processors or cores.

* Memory: Each process has its own isolated memory and resources. To communicate, they must use inter-process communication (IPC).

* Use Cases: Ideal for heavy CPU-bound tasks (e.g., video rendering, machine learning, and heavy mathematical calculations) because it bypasses single-core limits.

* Pros/Cons: Highly robust—if one process crashes, the others remain unaffected. However, it takes more time and system resources to initialize.


## Differences

| Feature      | Multithreading                          | Multiprocessing                              |
| ------------ | --------------------------------------- | -------------------------------------------- |
| Execution    | Multiple threads within one process     | Multiple independent processes               |
| Hardware Use | Usually runs on a single CPU core       | Distributes work across multiple CPU cores   |
| Memory       | All threads share the same memory       | Each process has its own memory space        |
| Best For     | I/O-bound tasks (waiting for web, disk) | CPU-bound tasks (heavy calculations)         |
| Overhead     | Low (easy to create and manage)         | High (requires more system memory and setup) |


## Demo

In Python, the threading module handles threads, and the multiprocessing module handles processes. While the syntax looks similar, they behave very differently under the hood.

### Multithreading Code

This is best for waiting on external events (like a website response).

```python
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
```

* Key Behavior: Both threads run inside the same memory.

* The Catch: Python has a Global Interpreter Lock (GIL), which prevents multiple threads from executing Python code at the exact same time on different cores. This is why it’s only good for I/O, not math.


### Multiprocessing Code

This is best for heavy calculations because it creates a new instance of the Python interpreter for each process.

```python
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
```

* Key Behavior: Each process gets its own CPU core and its own memory.

* The Catch: Because memory isn't shared, it's harder to send data between processes (you have to use special tools like Queue or Pipe).


### Which one should you use?

* Use Multithreading if you are building a web scraper or a chat app where the program spends most of its time waiting for the internet.

* Use Multiprocessing if you are doing image processing, data science, or complex simulations that make your computer fans spin fast.

If you'd like, I can show you how to share data between these threads or processes, or we can look at the concurrent.futures module, which is a newer, cleaner way to write this code. Would you like to see the modern approach?


## concurrent.futures module

concurrent.futures is a high-level Python module that provides a unified interface for running tasks asynchronously. It acts as a wrapper around both the threading and multiprocessing modules, allowing you to switch between them by changing just one line of code. 

### What's the New Thing It Does?

Before this module, you had to write very different code for threads versus processes. concurrent.futures introduces several modern features: 

* Unified API: You use the same submit() and map() methods regardless of whether you are using threads or processes.

* The Future Object: When you start a task, it returns a Future object - a promise that the result will be available later. You can check if it's done or cancel it easily.

* Automatic Cleanup: Using it as a Context Manager (with statement) ensures that all threads or processes are shut down automatically when the tasks finish.

* Simplified Mapping: It can automatically split a large list of data across multiple workers and return the results in order.


### Code Example

Here is how you run the same task using the two different Executors.

```python
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
```


### Key Advantages Over the Old Way

| Old Way (threading/multiprocessing) | New Way (concurrent.futures) |
|---|---|
| You manually manage start() and join(). | The with block manages execution and cleanup. |
| Getting return values is tricky (needs Queues). | Functions simply return values to the Future. |
| Different syntax for threads vs. processes. | Identical syntax; easy to swap for testing. |
| Harder to handle errors inside the worker. | Exceptions are captured and raised when you ask for the result. |

According to the official Python Documentation, this module is the recommended way to handle parallel execution unless you need very low-level control. You can also see practical benchmarks on sites like Real Python to see which executor performs better for your specific task.


