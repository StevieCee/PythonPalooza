import websockets
import json
import asyncio


async def echo(websocket):
    async for message in websocket:
        try:
            data = json.loads(message)
            print(f"Received: {data}")
            response_data = {"message": f"You sent: {data}"}
            await websocket.send(json.dumps(response_data))
        except json.JSONDecodeError:
            print(f"Received non-JSON message: {message}")
            await websocket.send(f"Invalid message format: {message}")


async def main():
    async with websockets.serve(echo,"localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())