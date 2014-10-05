from __future__ import absolute_import, unicode_literals
import datetime

from mongoengine import Document


class Session(Document):
    """Mongo document representing a users session."""
    username = StringField()
    ip = StringField()
