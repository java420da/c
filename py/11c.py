#ipc

import socket
import pickle

HOST = "127.0.0.1"
PORT = 5002

name = input("Enter object name: ")
values = [int(x) for x in input("Enter values separated by spaces: ").split()]
data_object = {"name": name, "values": values}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(pickle.dumps(data_object))

print("Server:", client.recv(4096).decode())
client.close()
