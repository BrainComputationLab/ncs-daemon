""" Runs the Flask server for the REST interface """
from flask import Flask

def registerRoutes(app):
    @app.route('/auth/requestToken')
    def handleAuthTokenRequest(self):
        """ Handles requests for auth tokens """
        return ''

class Server(object):
    """ Rest server class """
    def run(self):
        """ Runs the REST server """
        self.app.run()

    def __init__(self):
        # Create new application
        self.app = Flask(__name__)
        # Debugging is okay for now
        self.app.debug = True
        # Register application routes
        registerRoutes(self.app)
