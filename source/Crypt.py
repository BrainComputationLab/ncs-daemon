""" Handles cryptograpy for the server """
import os
import hashlib

class Crypt(object):
    """ Class that handles cryptographic functions needed by the server """

    def __init__(self):
        pass

    @classmethod
    def generate_salt(self):
        """ Generates a random salt for password encryption """
        return os.urandom(8)

    @classmethod
    def hash_password(self, plaintext_password, salt):
        """ Hashes a plaintext password and a salt to get a final hashed password """
        return hashlib.sha256(plaintext_password + salt)
