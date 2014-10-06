from __future__ import absolute_import, unicode_literals

from mongoengine import Document
from mongoengine.fields import (
    StringField,
)


class User(Document):
    """Mongo document representing a user."""
    username = StringField(required=True, primary_key=True)
    first_name = StringField()
    last_name = StringField()
    email = StringField()
    institution = StringField()
    password = StringField(required=True)
    salt = StringField(required=True)
