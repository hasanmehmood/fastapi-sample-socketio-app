# Simple Socket.IO Chat App

This is a simple chat application using Socket.IO with FastAPI as the backend and a basic HTML page as the frontend. It allows users to send messages from the client, which are then echoed back by the server.

## Requirements

- Python 3.6+
- FastAPI
- python-socketio
- uvicorn

## Installation

1. Clone this repository or download the source code.

2. Install the required Python packages:

   ```bash
   pip install fastapi "python-socketio[asgi]" uvicorn
   ```

## Running the Application

1. Navigate to the directory containing app.py.

2. Run the application using uvicorn:

   ```bash
   uvicorn app:app --reload
   ```

The server will be accessible at http://localhost:8000.

3. Open index.html in your browser inorder to access the client side of the application.

## Usage

- Type a message in the input box on the webpage and click Send.
- The message is sent to the server, and the server echoes it back to the client.
- The sent message and the server's response are displayed on the webpage.

## Features

- Simple client-server communication using WebSockets.
- Server-side: FastAPI with Socket.IO for real-time communication.
- Client-side: Basic HTML with Socket.IO client to send and receive messages.

## Contributing

Feel free to fork this repository and submit a pull request if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)

