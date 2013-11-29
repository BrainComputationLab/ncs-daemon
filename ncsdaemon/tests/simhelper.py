""" This module tests the  simulator integration """

import unittest

class FakeSim(object):
    """ A fake simulation object for testing """

    def init(self, argv):
        return True

    def step(self, steps=1):
        return

    def shutdown(self):
        return True

class SimTestCase(unittest.TestCase):
    """ Test case used for all simulator interaction """

    def setUp(self):
        import ncs
        ncs.Simulator = FakeSim
        from ncsdaemon.simhelper import SimHelper
        self.sim_helper = SimHelper()
        return

class SimRunTest(SimTestCase):
    """ Case for running simulations """

    def test_empty_sim(self):
        self.sim_helper.run('njordan', {})
