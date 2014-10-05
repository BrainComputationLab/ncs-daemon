from __future__ import absolute_import, unicode_literals

from mongoengine import (
    Document,
    StringField,
)


class User(Document):
    """Mongo document representing a user."""
    username = StringField()
    first_name = StringField()
    last_name = StringField()
    email = StringField()
    institution = StringField()
    password = StringField()
    salt = StringField()
