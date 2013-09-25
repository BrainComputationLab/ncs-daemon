""" Handles NCS users """
import os
import json
import logging
from source.User import User

class UserManagement(object):
    """ Class that handles users """

    USERS_FILENAME = 'users.json'

    def __init__(self):
        self.users = []
        user_dict = load_users_file(USERS_FILENAME)

    def create_user():
        pass

    def load_users_file(self, filename):
        """ Loads the JSON formatted users file and returns a dictionary that contains the data """
        try:
            with open(filename).read() as f:
                try:
                    return json.loads(f)
                except ValueError:
                    logging.error('Users file not found or poorly formatted')
        except IOError:
            logging.warning('Users file not found, creating new one')

    def save_users_file(self):
        try:
            with open(filename, 'w') as f:
                self.users.
        except IOError:
            logging.error('Couldn\'t write to users file')

    def convert_users_dict(self, user_dict):
        try:
            for user in user_dict.users:
                self.users.push(User(user['username']))
        except KeyError:
            logging.error('Attribute validation of users object failed, check the file')
