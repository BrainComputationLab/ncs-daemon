from __future__ import absolute_import, unicode_literals
from threading import Thread

from ncsdaemon.services.model import ModelService


class SimulationNotRunningException(Exception):
    pass


class SimInitFailedException(Exception):
    pass


class SimThread(Thread):
    """Thread that contains the running simulation."""

    def run(self):
        while self.step <= self.max_steps:
            # Run the simulation
            self.sim.step(1)
            # increment stop counter
            self.step += 1
        # TODO Figure out whats going on here, MPI_INIT is being called twice
        # for some reason
        del self.sim


class SimulatorService(object):
    """This class handles interaction with the NCS simulator."""

    def get_info(self):
        """Get information about the simulator and its state."""
        pass

    def run(self, simulation):
        """Run a simulation."""
        # create a new sim object
        ncs_simulation = object()
        # ncs_simulation = ncs.Simulation()
        # TODO move this out of here
        neuron_group_map = {}
        # generate the sim stuff
        ModelService.process_model(
            ncs_simulation,
            simulation.model,
            neuron_group_map,
        )
        # try to init the simulation
        if not ncs_simulation.init([]):
            raise SimInitFailedException
        # after the init, we can add stims and reports
        ModelService.add_stims_and_reports(
            ncs_simulation,
            simulation.model,
            neuron_group_map,
        )
        # create a new thread for the simulation
        sim_thread = SimThread(self, self.simulation, 5)
        # start running the simulation
        sim_thread.start()

    def stop(self):
        """Stop the simulation."""
        pass
