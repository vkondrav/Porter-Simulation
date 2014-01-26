from job import Job

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
        done_in = simState.sGraph.getTimeBetween(self.unit, self.job.origin)
        yield simState.env.timeout(done_in)
        
        # in progress
        print "%s is in-progress %s" % (self, self.job)
        self.state = Porter.inprogress
        self.unit = self.job.origin
        self.job.startTime = simState.env.now
        done_in = simState.sGraph.getTimeBetween(self.job.origin, self.job.destination)
        yield simState.env.timeout(done_in)
        
        # complete
        print "%s is complete %s" % (self, self.job)
        self.state = Porter.complete
        self.unit = self.job.destination
        self.job.completionTime = simState.env.now
        self.job = None
        done_in = 0
        yield simState.env.timeout(done_in)
        
        # pending
        print "%s is pending" % (self)
        self.state = Porter.pending