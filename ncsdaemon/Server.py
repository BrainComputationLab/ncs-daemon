""" Runs the Flask server for the REST interface """
from flask import Flask, request, make_response
from flask.ext.restful import Api
from ncsdaemon.resources import Report
from ncsdaemon.UserManager import UserManager
from jsonschema import validate as validate_json
from jsonschema.exceptions import ValidationError
from ncsdaemon.SchemaLoader import SchemaLoader

API_PREFIX = '/ncs/api'

def register_resources(api):
    api.add_resource(Report)

def register_routes(app):
    """ Registers routes for the Flask application """

    @app.before_request
    def before_request():
        """ This runs before each request, currently ensures a key is in
        the header for all requests aside from the login request """
        if request.path != API_PREFIX + '/login':
            return make_response({"message": "Authentication required"}, 401)

    @app.route(API_PREFIX + '/login', methods=['POST'])
    def handle_login_request(self):
        """ Handles requests for auth tokens """
        login_request = request.get_json()
        schema_loader = SchemaLoader()
        user_manager = UserManager()
        try:
            validate_json(login_request, schema_loader['login_post'])
        except ValidationError as e:
            return make_response({ "message": e.message }, 400)
        valid_user = user_manager.verify_user(login_request['username'],
                                              login_request['password'])
        if valid_user:
            key = user_manager.get_user_key(login_request['username'])
            return make_response({"key": key}, 200)
        return make_response({"message": "Bad user or password"}, 401)

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
