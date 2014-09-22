""" Runs the Flask server for the REST interface """

from flask import Flask, request
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json

from ncsdaemon.users import UserManager
from ncsdaemon.util import ServerUtils
from ncsdaemon.simhelper import SimHelper

class Server(object):
    """ Rest server class """

    def run(self, host, port):
        """ Runs the REST server """
        self.app.run(host, port)

    def __init__(self):
        # Create new application
        self.app = Flask(__name__)
        # set app route
        self.app.config['APPLICATION_ROUTE'] = '/ncs/api'
        # Debugging is okay for now
        self.app.debug = True
        # Register application routes
        self.register_routes()
        # create a user manager
        self.user_manager = UserManager()

    def register_routes(self):
        """ Registers routes for the Flask application """

        @self.app.before_request
        def before_request():
            """ This runs before each request, currently ensures a key is in
            the header for all requests aside from the login request """
            user_manager = UserManager()
            token = None
            # If the requested URL doesn't match any routes
            if request.url_rule is None:
                message = ServerUtils.json_message("Invalid request path")
                return ServerUtils.json_and_status(message, 404)
            # If they're trying to login, send them through
            if request.path == self.app.config['APPLICATION_ROUTE'] + '/login':
                return
            # Try to get the auth token from the header
            try:
                token = request.headers['token']
            # Return an error if they didn't provide an auth token
            except KeyError:
                if request.path != self.app.config['APPLICATION_ROUTE'] + '/login':
                    message = ServerUtils.json_message("Authentication Required")
                    return ServerUtils.json_and_status(message, 401)
            # check that the token is valid
            try:
                user = user_manager.get_user_from_token(token)
                # add the user to the request object
                request.user = user
            # if the token is not valid return a 401
            except KeyError:
                message = ServerUtils.json_message("Invalid auth token")
                return ServerUtils.json_and_status(message, 401)

        @self.app.route('/login', methods=['POST'])
        def login_route():
            """ Handles requests for auth tokens """
            js = request.json
            # check user credentials
            is_valid = self.user_manager.verify_user(js['username'], js['password'])
            # if the credentials are valid, send the token
            if is_valid:
                token = self.user_manager.get_user_token(js['username'])
                return ServerUtils.json_and_status({"token": token}, 200)
            # otherwise send a 'Not Authorized'
            else:
                message = "Invalid login credentials"
                json_message = ServerUtils.json_message(message)
                return ServerUtils.json_and_status(json_message, 401)

        @self.app.route('/simulator', methods=['GET', 'POST', 'DELETE'])
        def simulator_route():
            """ Method to deal with running/querying/stopping a simulation """
            sim = SimHelper()
            status = sim.get_status()
            # if requesting info about the simulator
            if request.method == 'GET':
                return ServerUtils.json_and_status(status, 200)
            # if they're trying to run the simulator
            if request.method == 'POST':
                # if theres already a sim running
                if status['status'] == 'running':
                    message = "Simulation currently in progress"
                    json_message = ServerUtils.json_message(message)
                    ServerUtils.json_and_status(json_message, 409)
                # if theres no sim currently running, start one
                if status['status'] == 'idle':
                    # get the json model
                    try:
                        js = json.loads(request.get_data())
                    except ValueError:
                        message = """Invalid request, the request should be a valid
                                    json object"""
                        json_message = ServerUtils.json_message(message)
                        return ServerUtils.json_and_status(json_message, 400)
                    # get the user from their token
                    info = sim.run(request.user.username, js)
                    return ServerUtils.json_and_status(info, 200)
            # if they're trying to stop a simulation
            if request.method == 'DELETE':
                # if a sim is running
                if status['status'] == 'running':
                    # if the user requesting is the same that ran the sim
                    if status['user'] == request.user.username:
                        res = sim.stop()
                        ServerUtils.json_and_status(res, 200)
                    # otherwise they are not authorized
                    else:
                        message = """You are not authorized to terminate the
                                    current simulation"""
                        json_message = ServerUtils.json_message(message)
                        return ServerUtils.json_and_status(json_message, 401)
                # if theres no sim running, return a conflict message
                if status['status'] == 'idle':
                    message = "No simulation is running"
                    json_message = ServerUtils.json_message(message)
                    return ServerUtils.json_and_status(json_message, 409)

        @self.app.route('/simulation/<simid>', methods=['GET', 'POST', 'DELETE'])
        def simulation_route():
            return ''


if __name__ == '__main__':
    server = Server()
    server.run('localhost', 8000)
