# This is the template code for the CNE335 Final Project
# Justin Ellis
# CNE 335 Fall
from Server import Server
def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Your Name")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    server = Server("34.219.58.195")
    is_reachable = server.ping()
    print(f"Server {server.server_ip} is {'reachable' if is_reachable else 'not reachable'}.")

    # TODO - Create a Server object
    # TODO - Call Ping method and print the results
