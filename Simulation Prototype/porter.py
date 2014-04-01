from job import Job
from random import randint


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

        if self.job.delayReason == "Patient Not Ready":
            maxDelay = simState.maxDelayReason.get(self.job.delayReason)
            if self.job.delayTime <= maxDelay:
                done_in += self.job.delayTime
            else:
                done_in += maxDelay
                self.job.cancelled = True
                #self.state = Porter.pending
        
        yield simState.env.timeout(done_in)
        
        if self.job.cancelled:
            creationTime = self.job.creationTime + self.job.delayTime - maxDelay
            inProgressTime = self.job.inProgressTime
            completeTime = self.job.completeTime
            origin = self.job.origin
            destination = self.job.destination
            priority = self.job.originalPriority
            appointment = 0
            delayReason = None
            delayTime = None
            
            self.job = None
            rescheduledJob = Job(creationTime, inProgressTime, completeTime, origin, destination, priority, appointment, delayReason, delayTime)
            simState.jobList.insert(rescheduledJob)
            self.state = Porter.pending

        
        # in progress
        if self.state == Porter.dispatched:
            print "%s is in-progress %s" % (self, self.job)
            self.state = Porter.inprogress
            self.unit = self.job.origin
            self.job.jobStartTime = simState.env.now
            done_in = self.job.inProgressTime
            yield simState.env.timeout(done_in)
        
        # complete
        if self.state == Porter.inprogress:
            print "%s is complete %s" % (self, self.job)
            self.state = Porter.complete
            self.unit = self.job.destination
            self.job.jobCompletionTime = simState.env.now
            done_in = self.job.completeTime
            self.job.jobCompletionPorterID = self.id
            self.job = None
            yield simState.env.timeout(done_in)
        
        # pending
        print "%s is pending" % (self)
        self.state = Porter.pending
