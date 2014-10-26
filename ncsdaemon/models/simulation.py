from __future__ import absolute_import, unicode_literals
from datetime import datetime

from mongoengine import Document
from mongoengine.fields import (
    UUIDField,
    DateTimeField,
    ReferenceField,
    EmbeddedDocumentField,
)

from ncsdaemon.models.user import User
from ncsdaemon.models.model import Model


class Simulation(Document):
    """Mongo document representing a simulation."""
    _id = UUIDField(primary_key=True)
    user = ReferenceField(User)
    created_time = DateTimeField(default=datetime.now())
    began_time = DateTimeField(default=datetime.now())
    ended_time = DateTimeField(default=datetime.now())
    model = EmbeddedDocumentField(Model)


class SimulationQueue(Document):
    """Mongo document representing a queued simulation."""
    simulation = ReferenceField(Simulation)
    queued_time = DateTimeField(default=datetime.now())
