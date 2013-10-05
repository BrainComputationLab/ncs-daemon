""" User class """

class User(object):
    """ Class that contains data and operations related to a user """

    def __init__(self, username, first_name, last_name, email, salt, hashed_password, apiKey):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salt = salt
        self.hashed_password = hashed_password
        self.apiKey = apiKey

    def to_dictionary(self):
        """ Returns the user as a dictionary for easy write to JSON """
        return { 'username' : self.username,
                 'first_name': self.first_name,
                 'last_name': self.last_name,
                 'email': self.email,
                 'salt': self.salt,
                 'apiKey': self.apiKey,
                 'hashed_password': self.hashed_password }