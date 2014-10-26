from __future__ import absolute_import, unicode_literals

from ncsdaemon.models.simulation import Simulation


class SimulationService(object):
    """Handles interaction with Simulation objects."""

    @classmethod
    def get(cls, id):
        """Retrieves simulation by id."""
        try:
            return Simulation.objects.get(id)
        except Simulation.DoesNotExist:
            return None
