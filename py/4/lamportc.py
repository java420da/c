import socket
import threading

HOST = "127.0.0.1"
PORT = 5007

name = input("Process name: ").strip()
clock = 0

client = socket.socket()
client.connect((HOST, PORT))
client.sendall(name.encode())

def receive():
    global clock

    while True:
        try:
            data = client.recv(4096).decode()
            if not data:
                break

            for msg in data.splitlines():
                if msg.startswith("EVENT|"):
                    _, sender, timestamp, text = msg.split("|", 3)

                    clock = max(clock, int(timestamp)) + 1

                    print(
                        f"\nReceived from {sender}: {text}"
                        f"\nLamport Clock: {clock}"
                    )
        except OSError:
            break

threading.Thread(target=receive, daemon=True).start()

while True:
    text = input("Enter message (quit to stop): ")

    if text.lower() == "quit":
        break

    clock += 1

    message = f"EVENT|{name}|{clock}|{text}\n"
    client.sendall(message.encode())

    print("Sent with Lamport timestamp:", clock)

client.close()