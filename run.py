""" Runs the REST server interface """
from source import Server

# Run the server if this file is run directly
if __name__ == '__main__':
    server = Server.Server()
    server.run()
