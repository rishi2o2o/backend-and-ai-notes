import asyncio
from websockets.asyncio.client import connect

async def get_user_input():
    # Runs the blocking terminal input in a separate thread
    return await asyncio.to_thread(input, "Type a message to send (or Ctrl+C to quit): ")

async def send_messages():
    uri = "ws://localhost:8765"
    async with connect(uri) as websocket:
        print(f"Connected to server at {uri}")
        while True:
            # Replaced blocking input() with non-blocking async wrapper
            user_message = await get_user_input() 
            await websocket.send(user_message)
            response = await websocket.recv()
            print(f"Server replied: {response}")

if __name__ == "__main__":
    try:
        asyncio.run(send_messages())
    except (KeyboardInterrupt, asyncio.exceptions.CancelledError):
        print("\nDisconnected.")

