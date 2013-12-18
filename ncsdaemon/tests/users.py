""" Testing for user management """
from ncsdaemon.users import UserManager

class FakeUserManager(UserManager):
    """ Mock user management object that sets static test data """

    def __init__(self):
        users_dict = { "users": [
            {
                "username": "bobjones",
                "first_name": "Bob",
                "last_name": "Jones",
                "email": "bobjones@bobjones.com",
                "salt": "9bbec67b94cc432f",
                # password = password
                "hashed_password": "727a082e0a8380c509f4579471ce92add9bb55cae7316200ad21124c5f81f2bc",
                "token": "a_token"
            },
            {
                "username": "janedoe",
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "janedoe@janedoe.com",
                "salt": "bb1ac1f3d601bcf0",
                # password = another_password
                "hashed_password": "50bf344d94f5e5441a42079f390b15d54ecf0e29e3c5cc5471f434e514bb8626",
                "token": "another_token"
            }
        ] }
        self.users = self.convert_users_dict(users_dict)

