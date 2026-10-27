import socket
import os

HOST = "127.0.0.1"
PORT = 5002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("Server listening on port", PORT)

while True:
    conn, addr = server.accept()

    with conn:
        print("Connected:", addr)

        filename = conn.recv(4096).decode().strip()

        if os.path.isfile(filename):
            size = os.path.getsize(filename)

            with open(filename, "r") as file:
                lines = len(file.readlines())

            response = (
                f"File name: {filename}\n"
                f"File size: {size} bytes\n"
                f"Number of lines: {lines}"
            )
        else:
            response = "File not found."

        conn.sendall(response.encode())