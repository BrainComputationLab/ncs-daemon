from __future__ import absolute_import, unicode_literals

from mongoengine import EmbeddedDocument
from mongoengine.fields import (
    UUIDField,
    DictField,
)


class Model(EmbeddedDocument):
    """Document representing the simulation model to be run."""
    top_group = UUIDField()
    neurons = DictField()
    synapses = DictField()
    stimuli = DictField()
    reports = DictField()
    groups = DictField()
    neuron_aliases = DictField()
    synapse_aliases = DictField()
