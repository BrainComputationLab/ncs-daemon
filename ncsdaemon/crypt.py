""" Handles cryptography for the server """
import os
import hashlib

class CryptBase(object):
    """ Abstract class that outlines the behavior of the Crypt Class """

    @classmethod
    def generate_salt(cls):
        """ Generates a random salt for password encryption """
        pass

    @classmethod
    def generate_api_key(cls):
        """ Generates a random api key """
        pass

    @classmethod
    def hash_password(cls, plaintext_password, salt):
        """ Hashes a plaintext password and a salt to get a final hashed password """
        pass

class Crypt(CryptBase):
    """ Class that handles cryptographic functions needed by the server """

    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def generate_salt(cls):
        """ Generates a random salt for password encryption """
        return os.urandom(8).encode('hex')

    @classmethod
    def generate_api_key(cls):
        """ Generates a random api key """
        return os.urandom(8).encode('hex')

    @classmethod
    def hash_password(cls, plaintext_password, salt):
        """ Hashes a plaintext password and a salt to get a final hashed password """
        return hashlib.sha256(plaintext_password + salt).hexdigest()

class CryptDummy(CryptBase):
    """ Class that handles cryptographic functions needed by the server """

    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def generate_salt(cls):
        """ Generates a random salt for password encryption """
        return 'abc123'

    @classmethod
    def generate_api_key(cls):
        """ Generates a random api key """
        return 'apikey'

    @classmethod
    def hash_password(cls, plaintext_password, salt):
        """ Hashes a plaintext password and a salt to get a final hashed password """
        return 'password'