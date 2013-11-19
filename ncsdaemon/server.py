""" Runs the Flask server for the REST interface """

from flask import Flask, request
from flask.ext.restful import Api
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json

from ncsdaemon.resources import ReportResource
from ncsdaemon.users import UserManager
from ncsdaemon.util import SchemaLoader
from ncsdaemon.util import ServerUtils
from ncsdaemon.sim import Sim

API_PREFIX = '/ncs/api'

def register_resources(api):
    api.add_resource(ReportResource)

def register_routes(app):
    """ Registers routes for the Flask application """

    @app.before_request
    def before_request():
        """ This runs before each request, currently ensures a key is in
        the header for all requests aside from the login request """
        token = None
        # If the requested URL doesn't match any routes
        if request.url_rule == None:
            message = ServerUtils.json_message("Invalid request path")
            return ServerUtils.json_and_status(message, 404)
        # Try to get the auth token from the header
        try:
            token = request.headers['token']
        # Return an error if they didn't provide an auth token
        except KeyError:
            if request.path != API_PREFIX + '/login':
                message = ServerUtils.json_message("Authentication Required")
                return ServerUtils.json_and_status(message, 401)

    @app.route(API_PREFIX + '/login', methods=['POST'])
    def handle_login_request():
        """ Handles requests for auth tokens """
        schema_loader = SchemaLoader()
        user_manager = UserManager()
        js = {}
        # Ensure the request is valid json
        try:
            js = json.loads(request.get_data())
        except ValueError:
            message = "Invalid request, the request should be a json object"
            json_message = ServerUtils.json_message(message)
            return ServerUtils.json_and_status(json_message, 400)
        # see if the schema works
        try:
            validate(js, schema_loader.get_schema('login_post'))
        except ValidationError:
            message = "Improper json format"
            json_message = ServerUtils.json_message(message)
            return ServerUtils.json_and_status(json_message, 400)
        # check user credentials
        is_valid = user_manager.verify_user(js['username'], js['password'])
        # if the credentials are valid, send the key
        if is_valid:
            key = user_manager.get_user_key(js['username'])
            # TODO need a mock user_manager to do this right
            key = "a_key"
            return ServerUtils.json_and_status({ "key": key }, 200)
        # otherwise send a 'Not Authorized'
        else:
            message = "Invalid login credentials"
            json_message = ServerUtils.json_message(message)
            return ServerUtils.json_and_status(json_message, 401)

    @app.route(API_PREFIX + '/sim', methods=['GET', 'POST', 'DELETE'])
    def handle_simulation():
        return ''
        sim = Sim()
        status = sim.get_status()
        # if requesting info about the simulator
        if request.method == 'GET':
            return status
        # if they're trying to run the simulator
        if request.method == 'POST':
            # if theres already a sim running
            if status.status == 'running':
                message = "Simulation currently in progress"
                json_message = ServerUtils.json_message(message)
                ServerUtils.json_and_status(json_message, 409)
            if status.status == 'idle':
                info = sim.run()
                return ServerUtils.json_and_status(info, 200)
        if request.method == 'DELETE':
            if status.status == 'running':
                pass
            if status.status == 'idle':
                message = "No simulation is running"
                json_message = ServerUtils.json_message(message)
                return ServerUtils.json_and_status(json_message, 409)

    @app.route(API_PREFIX + '/sim/<simid>', methods=['GET', 'POST', 'DELETE'])
    def handle_prior_simulation(self):

        pass

class Server(object):
    """ Rest server class """

    def run(self, host, port):
        """ Runs the REST server """
        self.app.run(host, port)

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
