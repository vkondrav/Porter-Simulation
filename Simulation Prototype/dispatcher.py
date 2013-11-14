from porter import Porter, setStateDispatched
from event import Event

class Dispatcher(object):

    def __init__(self):
        self.simState = None
		
    def assignJob(self, job):
        # generate list of porters who are in a pending state
        pendingPorters = [porter for porter in self.simState.porters if porter.state == Porter.pending]
        print "PendingPorters ", pendingPorters
        
        if not pendingPorters:
            # no porters in pending state, so add the job to the job pool
            self.simState.jobPool.append(job)
            return
            
        closestPorter = None
        minDistance = None
        for porter in pendingPorters:
            if porter.unit == job.origin:
                porter.job = job
                event = Event(setStateDispatched, self.simState, porter)
                timedEvent = [self.simState.curTime, event]
                self.simState.eList.insert(timedEvent)
                return
            
            distance = self.simState.sTree.getTimeBetween(porter.unit, job.origin)
            if minDistance is None:
                minDistance = distance
                closestPorter = porter
            elif distance < minDistance:
                minDistance = distance
                closestPorter = porter
                
        closestPorter.job = job
        event = Event(setStateDispatched, self.simState, closestPorter)
        timedEvent = [self.simState.curTime, event]
        self.simState.eList.insert(timedEvent)
        return
        