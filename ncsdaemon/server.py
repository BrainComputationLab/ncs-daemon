""" Runs the Flask server for the REST interface """

from flask import Flask, request
from flask.ext.restful import Api
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from ncsdaemon.resources import ReportResource
from ncsdaemon.users import UserManager
from ncsdaemon.util import SchemaLoader
from ncsdaemon.util import ServerUtils

API_PREFIX = '/ncs/api'

def register_resources(api):
    api.add_resource(ReportResource)

def register_routes(app):
    """ Registers routes for the Flask application """

    @app.before_request
    def before_request():
        """ This runs before each request, currently ensures a key is in
        the header for all requests aside from the login request """
        if request.path != API_PREFIX + '/login':
            return ServerUtils.json_and_status(
                ServerUtils.json_message('Authentication required'), 401)

    @app.route(API_PREFIX + '/login', methods=['POST'])
    def handle_login_request():
        """ Handles requests for auth tokens """
        login_request = request.get_json()
        schema_loader = SchemaLoader()
        user_manager = UserManager()
        try:
            validate(login_request,
                    schema_loader.get_schema('login_post')
                    )
        except ValidationError as e:
            return ServerUtils.json_and_status(
                        ServerUtils.json_message(str(e)), 400)
        valid_user = user_manager.verify_user(login_request['username'],
                                              login_request['password'])
        if valid_user:
            key = user_manager.get_user_key(login_request['username'])
            return ServerUtils.json_and_status({ "key": key }, 200)
        return ServerUtils.json_and_status(
            ServerUtils.json_message('Username or password were invalid'), 401)

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
