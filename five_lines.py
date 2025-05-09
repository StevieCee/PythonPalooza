import websocket


# working
# https://websocket.org/tools/websocket-echo-server
ws = websocket.WebSocket()
ws.connect("ws://echo.websocket.events/")
ws.send("Hello, Server")
print(ws.recv())
ws.close()