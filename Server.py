import os


class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        response = os.system(f"ping -n 4 {self.server_ip}")
        # The value of 'response' indicates the success of the ping. 0 means success.
        if response == 0:
            return f"The server {self.server_ip} is reachable."
        else:
            return f"The server {self.server_ip} is not reachable."


# Instantiate the Server class with a server IP
my_server = Server("35.160.182.172")

# Call the ping method and print the result
ping_result = my_server.ping()
print(ping_result)
