import websocket


# works (needs to have websocket-client package installed)
if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.create_connection("ws://echo.websocket.events/")
    ws.recv()
    print("Sending 'Hello, World'...")
    ws.send("Hello, World")
    print("Sent")
    print("Receiving...")
    result = ws.recv()
    print(f"Received '{result}'")
    ws.close()