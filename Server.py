import subprocess


class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):

        try:

            result = subprocess.run(['ping', '-n', '6', self.server_ip], capture_output=True, text=True, check=True)

            ping_output = result.stdout

            return ping_output
        except subprocess.CalledProcessError as e:
            # Handle errors, if any
            return f"Error: {e}"





