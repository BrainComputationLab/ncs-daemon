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
        # Monkey patch the sim
        import ncs
        ncs.Simulation = FakeSim
        from ncsdaemon.simhelper import SimHelper
        self.sim_helper = SimHelper()
        return

class SimRunTest(SimTestCase):
    """ Case for running simulations """

    def test_no_username(self):
        self.sim_helper.run(None, {})

    def test_bad_username(self):
        self.sim_helper.run('not_a_user', {})

    def test_empty_sim(self):
        self.sim_helper.run('njordan', {})

if __name__ == "__main__":
    unittest.main()
