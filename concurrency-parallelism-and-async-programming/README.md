# Concurrency and Async Programming

Concurrency is the broader concept of dealing with multiple tasks at the same time, while Asynchronous programming is a specific coding technique used to achieve concurrency. It prevents blocking the main thread by pausing a task while waiting for an external response, allowing other operations to continue.


## 1. Concurrency (Dealing with Many Things)

Concurrency is about structure. It refers to an application’s ability to manage multiple tasks simultaneously. It means tasks are in progress at the same time, but they don't necessarily execute at the exact same physical instant.

* How it works: Think of a chef making a complex meal. They might chop vegetables, put a pot of water on the stove, and marinate meat. They switch between these tasks (juggling) so that multiple things are in progress, but they are likely only doing one physical action at a time.

* Goal: Improve the overall efficiency and responsiveness of a system.


## 2. Asynchronous Programming (Non-Blocking Execution)

Asynchronous programming is an implementation method of concurrency. It allows the program to initiate a long-running operation (like a network request or database query) and immediately move on to do other work, rather than freezing to wait for a response.

* How it works: Using keywords like async and await, your program tells the operating system or environment to execute a slow task in the background. When the background task finishes, a callback or event handles the result.

* Real-world example: In a web application, requesting user data from a database might take 200 milliseconds. Synchronous code freezes the entire app during that time. Async code allows the app to serve other users while that data loads in the background.


## The Core Difference

* Concurrency describes what your system is doing (managing multiple tasks).

* Asynchrony describes how your system handles tasks (pausing them while waiting instead of blocking the thread).

*Note: Neither concept is the same as Parallelism. While concurrency deals with multiple tasks at once, parallelism means physically executing multiple tasks at the exact same time using multi-core hardware.*


# How Parallelism differs from Concurrency and Async Programming

## Concurrency
It manages multiple tasks by making progress on them during the same time period. It doesn't mean they run at the same millisecond; rather, the system switches between them so fast it feels simultaneous. Think of a waiter serving three different tables—he isn't literally at all three at once, but he's managing all of them concurrently.

## Parallelism
This is true simultaneous execution. It requires multiple CPU cores where each core handles a separate task independently at the exact same moment. Think of three different waiters, each assigned to one table, all working at the same time.

## Asynchronous (Async) Programming
A non-blocking model where a task can start an operation (like a database call) and then step aside so the program can do other work. When the result is ready, the task resumes. It is a way to achieve concurrency, often on a single thread.


# Does Multithreading Achieve Concurrency or Parallelism?

It can achieve both, depending on your hardware:

* Concurrency: On a single-core processor, multithreading achieves concurrency via time-slicing. The CPU switches between threads so quickly that it creates the illusion of simultaneous progress.

* Parallelism: On a multi-core processor, multithreading can achieve true parallelism. The operating system assigns different threads to different physical cores, allowing them to execute at the exact same instant.

*Tip: Use Async for I/O-bound tasks (network requests, disk reading) to keep your app responsive without wasting threads. Use Multithreading for CPU-bound tasks (video rendering, heavy math) to get true parallel speed boosts.*


# Demo of Async Programming in Python

In Python, the asyncio library is the standard way to handle asynchronous tasks. The goal is to avoid sitting idle while waiting for slow operations like network requests or timers.

## The Breakfast Analogy

* In a synchronous world, you would start brewing coffee and wait for it to finish (2 seconds) and then start the toast and wait for it to finish (1 second). This would take 3 seconds total. 

* While, in an asynchronous world, you would start the coffee, and while the coffee machine is running (2 seconds), you would immediately start the toast (1 second). This way, the entire process would take max(2,1) = 2 seconds total.


## Synchronous version of code

```python
import time

def brew_coffee():
    print("  [Coffee] Starting the machine...")
    time.sleep(2)  # Pauses here, waits for it to finish
    print("  [Coffee] Coffee is ready!")
    return "Hot Coffee"

def toast_bread():
    print("  [Toast] Putting bread in toaster...")
    time.sleep(1)  # Pauses here, waits for it to finish
    print("  [Toast] Toast popped up!")
    return "Crispy Toast"

def main():
    start_time = time.perf_counter()

    results = brew_coffee() + ", " + toast_bread()

    end_time = time.perf_counter()
    print(f"Result: {results}")
    print(f"Total time: {end_time - start_time:.2f} seconds")

main()
```

## Asynchronous version of code

```python
import asyncio
import time

async def brew_coffee():
    print("  [Coffee] Starting the machine...")
    await asyncio.sleep(2)  # Pauses here, yielding control
    print("  [Coffee] Coffee is ready!")
    return "Hot Coffee"

async def toast_bread():
    print("  [Toast] Putting bread in toaster...")
    await asyncio.sleep(1)  # Pauses here, yielding control
    print("  [Toast] Toast popped up!")
    return "Crispy Toast"

async def main():
    start_time = time.perf_counter()

    # asyncio.gather runs tasks concurrently
    results = await asyncio.gather(brew_coffee(), toast_bread())

    end_time = time.perf_counter()
    print(f"Result: {results}")
    print(f"Total time: {end_time - start_time:.2f} seconds")

asyncio.run(main())
```

## Why this works

* async def: Marks a function as a "coroutine." It doesn't run immediately when called; it returns a coroutine object.

* await: The "magic" keyword. It tells the program: "This will take a while. You can go do other things, and come back to me when this is done."

* asyncio.gather(): Bundles multiple coroutines together and tells the event loop to manage them all at once.

* The Event Loop: A single-threaded manager that keeps track of all awaiting tasks. It switches between them whenever one is "waiting."

The Result: Even though the total work time is 3 seconds (2+1), the script finishes in 2 seconds because the tasks overlapped.

