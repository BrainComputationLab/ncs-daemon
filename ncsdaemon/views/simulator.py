from __future__ import absolute_import, unicode_literals

from flask import jsonify
from flask.ext.restful import Resource

from ncsdaemon.services.simulator import SimulatorService


class SimulatorResource(Resource):
    """This resource represents the current state of the simulator."""

    def get(self):
        """Return information about the status of the simulator."""
        info = SimulatorService.get_info()
        return jsonify(info=info)

    def delete(self):
        """Stop the simulator from executing it's current simulation."""
        SimulatorService.stop_simulation()
        res = jsonify({})
        res.status_code = 202
        return res
