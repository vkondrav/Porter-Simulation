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
        # Get the dispatch time from the look up table which is based 
        # off the origin of the job
        dispatchTimes = simState.dispatchTable[self.job.origin]
        done_in = dispatchTimes[randint(0, len(dispatchTimes) - 1)]
        
        # Checks for a delay in the job
        if self.job.delayReason == "Patient Not Ready":
            # Queries the delay reason look up table for the max amount delay allowed
            maxDelay = simState.maxDelayReason.get(self.job.delayReason)
            
            # The delay is acceptable and the porter keeps doing the job
            if self.job.delayTime <= maxDelay:
                done_in += self.job.delayTime
            # The delay is unacceptable and the porter cancels the job
            else:
                done_in += maxDelay
                self.job.cancelled = True
        
        yield simState.env.timeout(done_in)
        
        # Reschedule the job as it was cancelled because of porter wait times
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
