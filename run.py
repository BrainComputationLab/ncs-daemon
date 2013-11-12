""" Runs the REST server interface """
from ncsdaemon.Server import Server

# Run the server if this file is run directly
if __name__ == '__main__':
    server = Server()
    server.run()
