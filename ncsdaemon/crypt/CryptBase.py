""" Abstract class for cryptography """
from abc import ABCMeta, abstractmethod

class Crypt(object):
    """ Abstract class that outlines the behavior of the Crypt Class """
    __metaclass__ = ABCMeta

    @abstractmethod
    @classmethod
    def generate_salt(cls):
        """ Generates a random salt for password encryption """
        pass

    @abstractmethod
    @classmethod
    def generate_api_key(cls):
        """ Generates a random api key """
        pass

    @abstractmethod
    @classmethod
    def hash_password(cls, plaintext_password, salt):
        """ Hashes a plaintext password and a salt to get a final hashed password """
        pass
