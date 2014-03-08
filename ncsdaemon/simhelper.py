""" Module for interaction between ncs-daemon and the ncs simulator """
import ncs
import os
from ncsdaemon.crypt import Crypt
from datetime import datetime
import json
from threading import Thread
from ncsdaemon.util import WriteRedirect
from ncsdaemon.util import SchemaLoader
import jsonschema.validate
from jsonschema.exceptions import ValidationError

SIM_DATA_DIRECTORY = '/var/ncs/sims/'

class SimThread(Thread):
    """ Thread that contains the running simulation """

    helper = None
    sim = None
    step = None

    def __init__(self, helper, sim, step):
        # call the superstructor for the Thread class, otherwise demons emerge
        super(SimThread, self).__init__()
        self.sim = sim
        self.step = step
        self.helper = helper

    def run(self):
        # Run the simulation
        self.sim.step(self.step)
        # Once it's done, change the helper's status
        self.helper.is_running = False


class SimHelperBase(object):
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

class SimHelper(SimHelperBase):
    """ This class handles interaction with the NCS simulator """

    _instance = None
    sim_status = None
    is_running = False
    simulation = None
    most_recent_sim_info = None

    def __new__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super(SimHelper, self).__new__(
                                self, *args, **kwargs)
        return self._instance

    def __init__(self):
        if not os.path.exists(SIM_DATA_DIRECTORY):
            os.makedirs(SIM_DATA_DIRECTORY)

    def get_status(self):
        """ Get the status of the simulation """
        # if the sim is running, send info about the currently running sim
        if self.is_running:
            return self.most_recent_sim_info
        # otherwise say its idle
        else:
            info = {
                "status": "idle"
            }
            return info

    def run(self, user, model):
        """ Runs a simulation """
        # create a new sim object
        self.simulation = ncs.Simulation()
        # generate the sim stuff
        errors = ModelHelper.process_model(self.simulation, model)
        #check for errors
        if len(errors):
            # do something here
            pass
        # try to init the simulation
        if not self.simulation.init([]):
            info = {
                "status": "error",
                "message": "Failed to initialize simulation"
            }
            return info
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
        # create a new thread for the simulation
        sim_thread = SimThread(self, self.simulation, 5)
        # start running the simulation
        sim_thread.start()
        # set the sim to running
        self.is_running = True
        return info

    def stop(self):
        """ Stop the simulation """
        # if there was a simulation running, shut it down
        if self.simulation.shutdown():
            # set current status to stopped
            self.sim_status['status'] = 'idle'
            return self.sim_status
        # otherwise indicate that
        else:
            info = {
                "status": "error",
                "message": "No simulation was running"
            }
            return info


class ModelHelper(object):

    @classmethod
    def process_model(cls, sim, model):
        # create a list of errors to output if neccessary
        errors = []
        # schemaloader
        schema_loader = SchemaLoader()
        # see if the schema works
        try:
            jsonschema.validate(model,
                                schema_loader.get_schema('transfer_schema'))
        # if it doesn't pass validation, return a bad request error
        except ValidationError:
            error = "Improper json format"
        sim_model = model['model']
        neurons = model['neurons']
        synapses = model['synapses']
        stimuli = model['stimuli']
        reports = model['reports']
        groups = model['groups']
        model = model['model']
        # add neurons to sim
        for neuron in neurons:
            # TODO: Validate neuron spec
            pass
            # Get neuron type from the model
            neuron_type = neuron['specification']['type']
            sim.addNeuron(neuron['_id'], neuron_type, spec)
        for synapse in synapses:
            # TODO: Validate synapse spec
            pass
            # Get synapse type from the model
            synapse_type = synapse['specification']['type']
            sim.addSynapse(synapse['_id'], synapse_type, spec)
        for stimulus in stimuli:
            # TODO: Validate stimulus spec
            pass
            # Get stimulus type from the model
            stimulus_type = stimulus['specification']['type']
            prob = stimulus['specification']['probability']
            time_start = stimulus['specification']['time_start']
            time_end = stimulus['specification']['time_end']
            # TODO what to do about groups...
            sim.addSynapse(stimulus_type, spec, [], prob, time_start, time_end)
        for report in reports:
            # TODO: Validate report spec
            pass
            # Get report type from the model
            report_type = report['specification']['report_type']['type']
            report_target = stimulus['specification']['report_target']
            probability = stimulus['specification']['probability']
            time_start = stimulus['specification']['time_start']
            time_end = stimulus['specification']['time_end']
            # TODO what to do about targets...
            sim.addReport([], target_type, report_type, probability,
                          time_start, time_end)
        # time for the groups :(
        for group in groups:
            pass


    def create_ncs_normal(cls, params):
        return ncs.Normal(params['mean'], params['std_dev'])

    def create_ncs_uniform(cls, params):
        return ncs.Uniform(params['lower_bound'], params['upper_bound'])

    def create_ncs_exact(cls, params):
        return params['value']
