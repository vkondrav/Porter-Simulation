import unittest
from mock import Mock
from porter import Porter

class TestPorter(unittest.TestCase):

    def setUp(self):
        self.porter = Porter(1)

    ## This function goes through all the porter states returning to pending once complete ##
    def test_work(self):
        simState = Mock()
        simState.env.timout(return_value=20)
        self.assertEqual(self.porter.state,Porter.pending)
        self.porter.work(simState)
        self.assertEqual(self.porter.state,Porter.pending)

if __name__ == '__main__':
    unittest.main()
