""" Handles cryptography for the server """
import bcrypt
import os


class Crypt(object):
    """ Class that handles cryptographic functions needed by the server """

    @classmethod
    def generate_salt(cls):
        """ Generates a random salt for password encryption """
        return bcrypt.gensalt()

    @classmethod
    def generate_user_token(cls):
        return os.urandom(32).encode('hex')

    @classmethod
    def hash_password(cls, plaintext_password, salt):
        """ Hashes a plaintext password and a salt to get a final hashed password """
        return bcrypt.hashpw(plaintext_password, salt)

    @classmethod
    def generate_sim_id(cls):
        """ Generates and ID for a new simulation """
        return os.urandom(32).encode('hex')
