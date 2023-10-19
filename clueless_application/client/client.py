import sys
sys.path.append('../')
import socket
from messaging.message import Message

class CluelessClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))
        print(f"Connected to {self.host}:{self.port}")

    def send_message(self, message):
        self.socket.send(message.encode('utf-8'))
        response = self.socket.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

    def close(self):
        self.socket.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345

    client = CluelessClient(HOST, PORT)
    client.connect()

    while True:
        message = input("Enter a message (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client.send_message(message)

    client.close()