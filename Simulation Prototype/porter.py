from job import Job
from random import randint, seed

# maintain determinism
seed(0)

class Porter(object):
    pending = 'pending'
    dispatched = 'dispatched'
    inprogress = 'inprogress'
    complete = 'complete'

    def __init__(self, id):
        self.id = id
        self.state = Porter.pending
        self.unit = 0
        self.job = None
        self.origin = None
        self.destination = None
        
    def __repr__(self):
        return "Porter" + str(self.id)  
        
    def work(self, simState):
        # dispatch
        print "%s is dispatched %s" % (self, self.job)
        self.state = Porter.dispatched
        dispatchTimes = simState.dispatchTable[self.job.origin]
        done_in = dispatchTimes[randint(0, len(dispatchTimes) - 1)]
        yield simState.env.timeout(done_in)
        
        # in progress
        print "%s is in-progress %s" % (self, self.job)
        self.state = Porter.inprogress
        self.unit = self.job.origin
        self.job.jobStartTime = simState.env.now
        done_in = self.job.inProgressTime
        yield simState.env.timeout(done_in)
        
        # complete
        print "%s is complete %s" % (self, self.job)
        self.state = Porter.complete
        self.unit = self.job.destination
        self.job.jobCompletionTime = simState.env.now
		jobCompletionPorterID = self.id
        done_in = self.job.completeTime
        self.job = None
        yield simState.env.timeout(done_in)
        
        # pending
        print "%s is pending" % (self)
        self.state = Porter.pending
