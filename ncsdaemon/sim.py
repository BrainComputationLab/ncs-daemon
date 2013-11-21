""" Module for interaction between ncs-daemon and the ncs simulator """
#from ncs import Simulation
import os
from ncsdaemon.crypt import Crypt
from datetime import datetime
import json

SIM_DATA_DIRECTORY = '/var/ncs/sims/'

class SimBase(object):
    """ Abstract base for the sim object """

    def get_status(self):
        """ Gets the status of the simulator """
        pass

    def run(self, user, model):
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
    most_recent_sim_info = None
    is_running = False

    def __new__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super(Sim, self).__new__(
                                self, *args, **kwargs)
        return self._instance

    def __init__(self):
        if not os.path.exists(SIM_DATA_DIRECTORY):
            os.makedirs(SIM_DATA_DIRECTORY)

    def get_status(self):
        return self.most_recent_sim_info

    def run(self, user, model):
        """ Runs a simulation """
        # TODO get the sim stuff working
        #simulation = Simulation()
        #simulation.step(500)
        # generate a new ID for the ism
        sim_id = Crypt.generate_sim_id()
        #create the directory for sim information like reports
        os.makedirs(SIM_DATA_DIRECTORY + '/' + sim_id)
        # get a timestamp
        now = datetime.now()
        # get a formatted string of the timestamp
        time_string = now.strftime("%d/%m/%Y %I:%M:%S %p %Z")
        # info object to be sent back to the user
        info = {
            "status": "running",
            "user": user,
            "started": time_string,
            "sim_id": sim_id
        }
        # meta object for the sim directory
        meta = {
            "user": user,
            "started": time_string,
            "sim_id": sim_id
        }
        # write the status info to the directory
        with open(SIM_DATA_DIRECTORY + '/' + sim_id + '/meta.json', 'w') as fil:
            fil.write(json.dumps(meta))
        # store the info as the most recent sim info
        self.most_recent_sim_info = info
        return info

    def stop(self):
        #stop sim
        # TODO get the sim stuff working
        # set current status to stopped
        self.most_recent_sim_info['status'] = 'stopped'
        return self.most_recent_sim_info

