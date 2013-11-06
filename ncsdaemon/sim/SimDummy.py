""" Handles interaction with the NCS Simulator """
import SimBase

class Sim(SimBase):
    """ This class handles interaction with the NCS simulator """

    @classmethod
    def get_status(cls):
        """ Gets the status of the simulator """
        return { 'status': 'idle' }

    @classmethod
    def run(cls):
        """ Tells the simulator to run with the current configureation """
        pass
