# This is the template code for the CNE335 Final Project
# Rosa Hulbert
# CNE 335 Fall
from Server import Server


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

