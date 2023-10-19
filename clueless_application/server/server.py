import sys
import socket
import threading
import pickle

class CluelessServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def validateMove(self):
        print("Validating Move")
    
    def validateSuggestion(self):
        print("Validating Suggestion")
    
    def validateAccusation(self):
        print("Validating Accusation")

    def validateDisprove(self):
        print("Validating Disprove")

    def updateGameBoard(self):
        print("Update Game Board")

    def determineGameWinner(self):
        print("Determining if Their is a Game Winner")
    
    def endGame(self):
        print("Winner Determined, Exiting Game")

    """
    Switch-Case to Trigger Methods Based on Message Contents
    """
    def processMessage(self, message):
        print(f"Processing Message: {message}")

        if message == 'move':
            self.validateMove()
        elif message == 'suggestion':
            self.validateSuggestion()
        elif message == 'accusation':
            self.validateAccusation()
        elif message == 'disprove':
            self.validateDisprove()
        else:
            print("Processing Failed: Unknown Message")
    
    """
    Starts Server Listening for Client Connections
    """
    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"Server is listening on {self.host}:{self.port}")

        while True:
            client, addr = self.socket.accept()
            print(f"Accepted connection from {addr}")
            self.clients.append(client)

            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()
    
    """
    When Client Sends Message, New Thread is Opened to Process the Message
    """
    def handle_client(self, client):
        while True:
            try:
                data = client.recv(1024)
                if not data:
                    break

                message = data.decode('utf-8')
                print(f"Received: {message}")

                self.processMessage(message)

                response = f"You said: {message}"
                client.send(response.encode('utf-8'))

            except Exception as e:
                print(f"Error: {e}")
                break

        client.close()
        self.clients.remove(client)

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345

    server = CluelessServer(HOST, PORT)
    server.start()