"""Handles cryptography for the server"""
from __future__ import absolute_import, unicode_literals
import os

import bcrypt


class Crypt(object):
    """ Class that handles cryptographic functions needed by the server """

    @classmethod
    def generate_salt(cls):
        """Generate a random salt for password encryption.

        :returns: str
        """
        return bcrypt.gensalt()

    @classmethod
    def generate_user_token(cls):
        """Generate a user token for their session.

        :returns: str
        """
        return os.urandom(32).encode('hex')

    @classmethod
    def hash_password(cls, plaintext_password, salt):
        """Hash a plaintext password and a salt to create a secure password.

        :param plaintext_password: The password to be encrypted
        :type plaintext_password: str
        :param salt: The salt to hash the password with.
        :type salt: str
        :returns: str -- The hashed password as a string.
        """
        return bcrypt.hashpw(plaintext_password, salt)

    @classmethod
    def generate_sim_id(cls):
        """Generate an ID for simulation.

        :returns: str
        """
        return os.urandom(32).encode('hex')
