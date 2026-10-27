import Pyro4

uri = input("Enter the Server URI: ")

server = Pyro4.Proxy(uri)

filename = input("Enter file name: ")

result = server.get_file_info(filename)

print("\nFile Information:")
print(result)