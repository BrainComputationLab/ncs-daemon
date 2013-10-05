""" Handles NCS users """
import json
import logging
from ncsdaemon.User import User
from ncsdaemon.Crypt import Crypt

class UserManager(object):
    """ Class that handles users """

    USERS_FILENAME = 'users.json'

    def __init__(self):
        user_dict = self.load_users_file(self.USERS_FILENAME)
        self.users = self.convert_users_dict(user_dict)

    def load_users_file(self, filename):
        """ Loads the JSON formatted users file and
        returns a dictionary that contains the data """
        try:
            with open(filename) as f:
                try:
                    data = f.read()
                    return json.loads(data)
                except ValueError:
                    logging.error('Users file not found or poorly formatted')
        except IOError:
            logging.warning('Users file not found, creating new one')
            user_dict = { 'users': [] }
            with open(filename, 'w') as f:
                f.write(json.dumps(user_dict))
            return user_dict

    def create_user(self, username, first_name, last_name, email, password):
        salt = Crypt.generate_salt()
        hashed_password = Crypt.hash_password(password, salt)
        user = User(username, first_name, last_name, email, salt, hashed_password)
        self.users.append(user)
        self.save_users_file(self.USERS_FILENAME)

    def verify_user(self, username, password):
        for user in self.users:
            if user.username == username:
                hashed_password = Crypt.hash_password(password, user.salt)
                if hashed_password == user.hashed_password:
                    return True
                else:
                    return False
        return False

    def save_users_file(self, filename):
        try:
            with open(filename, 'w') as f:
                users = []
                for user in self.users:
                    users.append(user.to_dictionary())
                user_dict = { 'users': users }
                f.write(json.dumps(user_dict))
        except IOError:
            logging.error('Couldn\'t write to users file')

    def convert_users_dict(self, user_dict):
        users = []
        try:
            for user in user_dict['users']:
                users.append(User(user['username'], user['first_name'], user['last_name'], user['email'], user['salt'], user['hashed_password']))
            return users
        except KeyError:
            logging.error('Attribute validation of users object failed, check the file')
