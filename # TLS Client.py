# TLS Client
# Author: Connor

from socket import *
import ssl

SERVER_NAME = '10.243.58.228' # Localhost
SERVER_PORT = 12000

def start_client():
    # 1. Create TCP Socket
    client_socket = socket(AF_INET, SOCK_STREAM)

    # 2. Create SSL Context
    # Note: We disable hostname checking because we are using a self-signed cert
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # 3. Wrap the socket
    tls_client = context.wrap_socket(client_socket, server_hostname=SERVER_NAME)

    try:
        # 4. Connect
        tls_client.connect((SERVER_NAME, SERVER_PORT))
        print(f"Connected securely to {SERVER_NAME}")

        # 5. Send Data
        msg = input("Enter message: ")
        tls_client.send(msg.encode('utf-8'))
        
        # 6. Receive Reply
        response = tls_client.recv(1024)
        print("Server replied:", response.decode('utf-8'))

    finally:
        tls_client.close()

if __name__ == "__main__":
    start_client()