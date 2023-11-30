# This is the template code for the CNE335 Final Project
# Rosa Hulbert
# CNE 335 Fall

import subprocess


class Server:
    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):
        try:
            result = subprocess.check_output(["ping", "-n", "5", self.server_ip], text=True)
            return result
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Rosa Hulbert")


# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()

    # # TODO - Create a Server object
    server_ip = '35.160.182.172'
    server = Server(server_ip)

    # TODO - Call Ping method and print the results
    ping_result = server.ping()
    print(f"Ping result for {server_ip}:")
    print(ping_result)

