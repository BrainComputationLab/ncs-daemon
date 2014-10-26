from __future__ import absolute_import, unicode_literals

from flask.ext.restful import Resource


class SimulationResource(Resource):
    """This resource represents the current state of the simulator."""

    def get(self, report_id):
        pass

    def put(self, report_id):
        pass

    def delete(self, report_id):
        pass
