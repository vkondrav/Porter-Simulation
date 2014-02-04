from job import Job

class Porter(object):
    pending = 'pending'
    dispatched = 'dispatched'
    inprogress = 'inprogress'
    complete = 'complete'

    AUTOLOCATION_VALUE = [['LOCATION', 4], ['ZONE', 8], ['UNIT', 7], ['SECTION', 14], ['FLOOR', 10], ['BUILDING', 12], ['BASE', 16]]


    def __init__(self, id, au):
        self.id = id
        self.state = Porter.pending
        self.unit = 0
        self.job = None
        self.origin = None
        self.destination = None
        self.autoLocation = au
        self.clearProc = None

    def configData():
        for i in xrange(0,9):
            AUTOLOCATION_VALUE[i][1] = self.autoLocation[i]
        self.autoLocation = AUTOLOCATION_VALUE
        
    def __repr__(self):
        return "Porter" + str(self.id)

    # porter will no longer be at their completed destination after a specific amout of time
    def clearLocation():
        yield simState.env.timeout(self.autoLocation[0]*60)
        self.unit = 0     
        
    def work(self, simState):
        # dispatch
        if self.clearProc:
            self.clearProc.Interrupt()
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
        self.clearProc = simState.env.process(clearLocation())
