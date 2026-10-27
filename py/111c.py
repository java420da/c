import socket

HOST = "127.0.0.1"
PORT = 5002

filename = input("Enter file name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(filename.encode())

response = client.recv(4096).decode()
print("Server:\n", response)

client.close()