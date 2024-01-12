import uvicorn
import socketio
from fastapi import FastAPI

# Create a Socket.IO server
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

# Create a FastAPI application
app = FastAPI()

# Socket.IO events
@sio.on("connect")
async def connect(sid, env):
    print("Client connected:", sid)

@sio.on("disconnect")
async def disconnect(sid):
    print("Client disconnected:", sid)

@sio.on("message_from_client")
async def message_from_client(sid, data):
    print("Message from client:", data)
    await sio.emit("message_from_server", f"From Server: Received: {data}")

# Create a Socket.IO ASGI app
socket_app = socketio.ASGIApp(sio)

# Mount the Socket.IO ASGI app on the FastAPI app
app.mount("/", socket_app)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
