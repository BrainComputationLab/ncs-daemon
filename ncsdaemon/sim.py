""" Module for interaction between ncs-daemon and the ncs simulator """
#from ncs import Simulation

class SimBase(object):
    """ Abstract base for the sim object """

    def get_status(cls):
        """ Gets the status of the simulator """
        pass

    def run(cls):
        """ Tells the simulator to run with the current configureation """
        pass

class SimDummy(SimBase):
    """ Dummy sim class for testing """

    def get_status(cls):
        return { 'status': 'idle' }

    def run(cls):
        pass

class Sim(SimBase):
    """ This class handles interaction with the NCS simulator """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Sim, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def get_status(cls):
        status = {
            "status": "running",
            "user": "njordan",
            "started": "11/10/2013 5:30PM PST",
            "sim_id": "fjdklsaj90sjfidja0asdf",
        }
        return status

    def run(cls):
        #simulation = Simulation()
        #simulation.step(500)
        info = {
            "status": "running",
            "user": "dtanna",
            "started": "11/10/2013 5:30PM PST",
            "sim_id": "fjdklsaj90sjfidja0asdf",
        }
        return info
