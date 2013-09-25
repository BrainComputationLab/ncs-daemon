""" Stuff related to users """

class User(object):
    """ Class that contains data and operations related to a user """

    def __init__(self, username, first_name, last_name, email, hashed_password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hashed_password = hashed_password

    def to_dictionary(self):
        """ Returns the user as a dictionary for easy write to JSON """
        return { 'username' : self.username,
                 'first_name': self.first_name,
                 'last_name': self.last_name,
                 'email': self.email,
                 'hashed_password': self.hashed_password }
