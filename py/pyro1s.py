import Pyro4
import os

@Pyro4.expose
class FileInfo:

    def get_file_info(self, filename):
        if not os.path.isfile(filename):
            return "File not found."

        size = os.path.getsize(filename)

        with open(filename, "r") as file:
            lines = len(file.readlines())

        return (
            f"File name: {filename}\n"
            f"File size: {size} bytes\n"
            f"Number of lines: {lines}"
        )

daemon = Pyro4.Daemon()
uri = daemon.register(FileInfo())

print("Server Started")
print("Server URI:", uri)

daemon.requestLoop()