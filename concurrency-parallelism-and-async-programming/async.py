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



