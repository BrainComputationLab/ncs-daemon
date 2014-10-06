from __future__ import absolute_import, unicode_literals

from ncsdaemon.models.user import User
from ncsdaemon.util.crypt import Crypt


class UserService(object):
    """Service for managing users."""

    @staticmethod
    def read(username):
        """Read the user object from the database.

        :param username: The username of the user to be returned.
        :type username: str
        """
        try:
            return User.objects.get(username=username)
        # if it can't find it, it's not authentic
        except User.DoesNotExist:
            return None

    @staticmethod
    def create(**kwargs):
        """Create a new user."""
        # get the new users parameters
        username = kwargs.get('username')
        password = kwargs.get('password')
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        email = kwargs.get('email')
        institution = kwargs.get('institution')
        # generate a new salt
        salt = Crypt.generate_salt()
        # hash the provided password with a salt
        password = Crypt.hash_password(password, salt)
        # create the new user``
        user = User(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            institution=institution,
            salt=salt,
        )
        # save them to the database
        user.save()

    @staticmethod
    def authenticate(username, password):
        """Authenticate a user given a username and plaintext password.

        :param username: The username to be authenticated.
        :type username: str
        :param password: The password supplied.
        :type password: str
        :returns: bool -- If the users credentials are authentic.
        """
        # get the user from the database based on their username
        try:
            user = User.objects.get(username=username)
        # if it can't find it, it's not authentic
        except User.DoesNotExist:
            return False
        # hash the password with the salt from the user
        hashed_pw = Crypt.hash_password(password, user.salt)
        # return if the passwords match
        return hashed_pw == user.password
