# server.py
import asyncio
import websockets

# https://websockets.readthedocs.io/en/stable/howto/upgrade.html#
# websockets 15.0.1

async def echo(websocket):
    async for message in websocket:
        await websocket.send(f"Server received: {message}")

async def main():
    async with websockets.server.serve(echo, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())