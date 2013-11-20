""" Module for interaction between ncs-daemon and the ncs simulator """
#from ncs import Simulation

class SimBase(object):
    """ Abstract base for the sim object """

    def get_status(self):
        """ Gets the status of the simulator """
        pass

    def run(self):
        """ Tells the simulator to run with the current configureation """
        pass

    def stop(self):
        """ Tells the simulator to stop """
        pass

class SimDummy(SimBase):
    """ Dummy sim class for testing """

    def get_status(self):
        return { 'status': 'idle' }

    def run(self):
        pass

    def stop(self):
        pass

class Sim(SimBase):
    """ This class handles interaction with the NCS simulator """

    _instance = None

    def __new__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super(Sim, self).__new__(
                                self, *args, **kwargs)
        return self._instance

    def get_status(self):
        status = {
            "status": "running",
            "user": "njordan",
            "started": "11/10/2013 5:30PM PST",
            "sim_id": "fjdklsaj90sjfidja0asdf",
        }
        return status

    def run(self):
        #simulation = Simulation()
        #simulation.step(500)
        info = {
            "status": "running",
            "user": "dtanna",
            "started": "11/10/2013 5:30PM PST",
            "sim_id": "fjdklsaj90sjfidja0asdf",
        }
        return info

    def stop(self):
        info = {
            "status": "stopped",
            "user": "dtanna",
            "started": "11/10/2013 5:30PM PST",
            "sim_id": "fjdklsaj90sjfidja0asdf",
        }
        return info

