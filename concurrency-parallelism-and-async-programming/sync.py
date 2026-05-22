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

