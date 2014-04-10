import unittest
from mock import Mock
from dispatcher import Dispatcher
from job import Job


## Use Default Values ##
AUTOMATIC_UPGRADE = [[0, None], [1, 14], [2, 8], [3, 8], [4,5], [5,5], [6, 25], [7, 30], [8,40]]
PRIORITY_WEIGHT = [[0, 20], [1, 11], [2, 7], [3,5], [4,4], [5,3], [6,2], [7,1], [8,0]]
PROXIMITY_WEIGHT = [['LOCATION', 11], ['ZONE', 7], ['UNIT', 7], ['SECTION', 2], ['FLOOR', 5], ['BUILDING', 3], ['CAMPUS', 1]]
AUTOLOCATION_VALUE = [['LOCATION', 4], ['ZONE', 8], ['UNIT', 7], ['SECTION', 14], ['FLOOR', 10], ['BUILDING', 12], ['BASE', 16]]
APPOINTMENT_FACTOR = 1.2

class TestDispatcher(unittest.TestCase):

    ## Setup the dispatcher ##
    def setUp(self):
        self.dispatcher = Dispatcher(APPOINTMENT_FACTOR, PRIORITY_WEIGHT,PROXIMITY_WEIGHT,AUTOMATIC_UPGRADE,AUTOLOCATION_VALUE)

    ## This function should return default values from PRIORITY_WEIGHT ##
    def test_getJobPriorityWeight(self):
        for i in xrange(0,9):
            self.assertEqual(self.dispatcher.getJobPriorityWeight(i), PRIORITY_WEIGHT[i][1])

    ## This function should return AppointmentFactor if passed True ##
    def test_getAppointmentFactor(self):
        self.assertEqual(self.dispatcher.getAppointmentFactor(True), APPOINTMENT_FACTOR)
        self.assertEqual(self.dispatcher.getAppointmentFactor(False), 1)

    ## This function should add a job to the pending list ##
    def test_addJob(self):
        simState = Mock()
        simState.env.process(return_value=None)
        tmpJob = Job('1','2','3','4','5','6','7')
        pendingLen = len(self.dispatcher.pending_jobs)
        self.dispatcher.addJob(tmpJob,simState)
        self.assertEqual(len(self.dispatcher.pending_jobs), pendingLen+1)

      
if __name__ == '__main__':
    unittest.main()
