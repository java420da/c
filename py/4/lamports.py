import socket
import threading

HOST = "127.0.0.1"
PORT = 5007
clients = {}
lock = threading.Lock()

def handle(conn):
    name = conn.recv(1024).decode().strip()

    with lock:
        clients[name] = conn

    print("Connected:", name)

    while True:
        try:
            data = conn.recv(4096)
            if not data:
                break

            print("Received:", data.decode().strip())

            with lock:
                for peer, c in clients.items():
                    if peer != name:
                        c.sendall(data)

        except OSError:
            break

    with lock:
        clients.pop(name, None)

    conn.close()

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print("Lamport Clock Server Started")

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle, args=(conn,), daemon=True).start()