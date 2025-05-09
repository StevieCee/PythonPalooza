import asyncio
import websocket


ws = websocket.WebSocket()
ws.connect("ws://echo.websocket.events/")

async def connect_and_interact():
    name = input("What's your name? ")
    await websocket.send(name)
    print(f">>> {name}")
    greeting = await websocket.recv()
    print(f"<<< {greeting}")

if __name__ == "__main__":
    asyncio.run(connect_and_interact())
