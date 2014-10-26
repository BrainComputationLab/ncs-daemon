from __future__ import absolute_import, unicode_literals
from ipaddress import ip_address, AddressValueError

import click
from flask import Flask
from flask.ext.uuid import FlaskUUID
from flask.ext.restful import Api
from flask.ext.basicauth import BasicAuth

from ncsdaemon.views.simulator import SimulatorResource
from ncsdaemon.views.simulation import SimulationResource
from ncsdaemon.views.report import ReportResource
from ncsdaemon.services.user import UserService

# Create new application
app = Flask(__name__)

# set app route
app.config['APPLICATION_ROUTE'] = '/ncs/api'

# enforce basic authentication on all endpoints
app.config['BASIC_AUTH_FORCE'] = True

# restful api
api = Api(app)

# we use HTTP basic auth here
basic_auth = BasicAuth(app)
# tell BasicAuth how to authenticate our user
basic_auth.check_credentials = UserService.authenticate

# allow us to use UUID's in routes
FlaskUUID(app)

# add resources
api.add_resource(SimulatorResource, '/simulator')
api.add_resource(SimulationResource, '/simulation/<uuid:sim_id>')
api.add_resource(ReportResource, '/report/<uuid:report_id>')


@click.command()
@click.option("--host", default="0.0.0.0", help="Host to bind to.")
@click.option("--port", default=6767, help="Port to bind to.")
@click.option("--debug", is_flag=True, help="Start in debug mode.")
def run(host, port, debug):
    """Command to start the ncsdaemon process.

    :param host: The host to bind to.
    :type host: str
    :param port: The port to bind to.
    :type port: int
    :param debug: Start in debug mode.
    :type debug: bool
    """
    # verify the host is valid
    try:
        ip_address(host)
    except AddressValueError:
        raise click.BadParameter(
            "%s is not a valid IPv4 or IPv6 address." % host)
    # set debugging if requested
    if debug:
        app.debug = True
    # run the server
    app.run(host, port)
