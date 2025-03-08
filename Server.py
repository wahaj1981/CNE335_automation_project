import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):

        # TODO -
        self.server_ip = server_ip
    def ping(self):
        # TODO - Use os module to ping the server
        response = os.system(f"ping -c 5 {self.server_ip}" if os.name != "nt" else f"ping -n 5 {self.server_ip}")
        return response == 0
