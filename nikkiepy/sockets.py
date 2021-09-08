import socket
import os

def connection_test(host, port):
    host = host
    port = port
    s = socket.socket()
    get_client_addr = socket.gethostname()
    client_addr = socket.gethostbyname(get_client_addr)
    client_name = os.environ["COMPUTERNAME"]

    print(f"CONNECTING TO {host}:{port}")
    try:
        s.connect((host, port))  # Connects you to your server address (host) at the (port) you set
        print("[+] CONNECTED")
        s.send(f"Succesfull connection from: {client_addr}@{client_name}".encode())  # Sends a message to the server, confirming the connection
        s.close()  # Disconnects from the server
        print("[-] DISCONNECTED")
        print("[*]TEST SUCCESSFULL")
    except TimeoutError:
        print(f"Couldn't connect to {host} on port {port}")  # A connection couldn't be made to the server