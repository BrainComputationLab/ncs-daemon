""" Handles interaction with the NCS Simulator """
from abc import ABCMeta, abstractmethod

class Sim(object):
    """ This class handles interaction with the NCS simulator """
    __metaclass__ = ABCMeta

    @abstractmethod
    @classmethod
    def get_status(cls):
        """ Gets the status of the simulator """
        pass

    @abstractmethod
    @classmethod
    def run(cls):
        """ Tells the simulator to run with the current configureation """
        pass
