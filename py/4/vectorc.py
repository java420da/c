import socket
import threading

HOST = "127.0.0.1"
PORT = 5008

name = input("Process name: ").strip()

client = socket.socket()
client.connect((HOST, PORT))
client.sendall(name.encode())

peers = []
vector = {name: 0}
lock = threading.Lock()

def receive():
    global peers, vector

    while True:
        try:
            data = client.recv(4096).decode()
            if not data:
                break

            for msg in data.splitlines():

                if msg.startswith("PEERS|"):
                    peers = sorted(
                        set(filter(None, msg.split("|", 1)[1].split(",")))
                    )

                    with lock:
                        for p in peers:
                            vector.setdefault(p, 0)

                    print("\nProcesses:", peers)

                elif msg.startswith("EVENT|"):
                    _, sender, values, text = msg.split("|", 3)

                    received = {
                        p: int(v)
                        for p, v in (
                            item.split(":")
                            for item in values.split(",")
                        )
                    }

                    with lock:
                        for p in set(vector) | set(received):
                            vector[p] = max(
                                vector.get(p, 0),
                                received.get(p, 0)
                            )

                        vector[name] += 1
                        current = dict(vector)

                    print(
                        f"\nReceived from {sender}: {text}"
                        f"\nVector Clock: {current}"
                    )

        except OSError:
            break

threading.Thread(target=receive, daemon=True).start()

while True:
    text = input("Enter message (quit to stop): ")

    if text.lower() == "quit":
        break

    with lock:
        vector[name] += 1
        values = ",".join(
            f"{p}:{vector[p]}" for p in sorted(vector)
        )
        current = dict(vector)

    message = f"EVENT|{name}|{values}|{text}\n"
    client.sendall(message.encode())

    print("Sent with Vector Clock:", current)

client.close()