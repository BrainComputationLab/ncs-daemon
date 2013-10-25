""" Dummy cryptography module for testing """
import CryptBase

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
