# This is the code for the CNE335 Final Project
# Wahaj Al Obid
# CNE 335 Winter 2025

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Your Name")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()

    # TODO - Create a Server object
    server = Server("34.219.58.195")

    # TODO - Call Ping method and print the results
    is_reachable = server.ping()
    print(f"Server {server.server_ip} is {'reachable' if is_reachable else 'not reachable'}.")
