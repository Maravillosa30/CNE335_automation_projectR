import subprocess


class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):

        try:

            result = subprocess.run(['ping', '-n', '4', self.server_ip], capture_output=True, text=True, check=True)

            ping_output = result.stdout

            return ping_output
        except subprocess.CalledProcessError as e:
            # Handle errors, if any
            return f"Error: {e}"


server_ip = "35.160.182.172"
my_server = Server(server_ip)
ping_result = my_server.ping()
print(ping_result)


