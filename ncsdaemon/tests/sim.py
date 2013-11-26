""" This module tests the  simulator integration """

from ncsdaemon.sim import SimHelper
import unittest
import json

class SimTestCase(unittest.TestCase):
    """ Test case used for all simulator interaction """

    def setUp(self):
        pass

class SimRunTest(SimTestCase):
    """ Case for running simulations """

    def test_empty_sim(self):
        sim = SimHelper()
        sim.run('njordan', {})

