import sys
from client.client import CluelessClient
from server.server import CluelessServer
from client.character import Character

def main():

    test_client = CluelessClient("client_test")
    clueless_server = CluelessServer('127.0.0.1', 12345)

    clueless_server.start()

if __name__ == "__main__":
    main()