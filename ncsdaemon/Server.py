""" Runs the Flask server for the REST interface """
from flask import Flask
from flask.ext.restful import Api
import resources

def register_resources(api):
    api.add_resource(resources.Model)

def register_routes(app):
    @app.route('/auth/requestToken')
    def handle_auth_token_request(self):
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
        # Create the REST API
        self.api = Api(self.app)
        # Register application resources
        register_resources(self.api)
        # Register application routes
        register_routes(self.app)
