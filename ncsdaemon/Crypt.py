""" Handles cryptography for the server """
import os
import hashlib

class Crypt(object):
    """ Class that handles cryptographic functions needed by the server """

    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def generate_salt(cls):
        """ Generates a random salt for password encryption """
        return os.urandom(8).encode('hex')

    @classmethod
    def hash_password(cls, plaintext_password, salt):
        """ Hashes a plaintext password and a salt to get a final hashed password """
        return hashlib.sha256(plaintext_password + salt).hexdigest()
