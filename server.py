import asyncio
import websockets


port = 12345
DEBUG_OUTPUT = True  # Change this to False for silent program

def _print(msg):
    if DEBUG_OUTPUT:
        print(msg)

async def handle_client(websocket):
    try:
        _print("Client connected")
        await websocket.send("Hello, world!")
        _print("Sent data!")

        data = await websocket.recv()
        _print(f"Received: {data}")
        
    except websockets.exceptions.ConnectionClosed:
        _print("Client disconnected")

async def main():
    async with websockets.serve(handle_client, "localhost", port, subprotocols=[]): 
        _print(f"WebSocket server listening on port {port}")
        await asyncio.Future()  # run forever  # run forever

 
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Keyboard interrupt!! Quitting!")
    quit()
