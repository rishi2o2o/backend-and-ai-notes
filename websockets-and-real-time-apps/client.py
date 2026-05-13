import asyncio
from websockets.asyncio.client import connect

async def send_messages():
    uri = "ws://localhost:8765"
    async with connect(uri) as websocket:
        print(f"Connected to server at {uri}")
        while True:
            user_message = input("Type a message to send (or Ctrl+C to quit): ")
            await websocket.send(user_message)
            response = await websocket.recv()
            print(f"Server replied: {response}")

if __name__ == "__main__":
    try:
        asyncio.run(send_messages())
    except KeyboardInterrupt:
        print("\nDisconnected.")


