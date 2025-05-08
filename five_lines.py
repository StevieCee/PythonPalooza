import websocket

# https://websocket.org/tools/websocket-echo-server
ws = websocket.WebSocket()
ws.connect("https://echo.websocket.org/")
ws.send("Hello, Server")
print(ws.recv())
ws.close()