import asyncio
from websockets.asyncio.server import serve


# This function handles incoming connections
async def echo(websocket):
    print("A client connected!")

    # Keep listening for incoming real-time messages
    async for message in websocket:
        print(f"Received from client: {message}")

        # Send the exact message back to the client
        await websocket.send(message)


async def main():
    async with serve(echo, "localhost", 8765) as server:
        print("WebSocket Server running on ws://localhost:8765")
        await asyncio.Future()  # Keeps the server running indefinitely


if __name__ == "__main__":
    asyncio.run(main())



