from porter import Porter, setStateDispatched
from event import Event

class Dispatcher(object):

    def __init__(self):
        self.simState = None
		
    def assignTask(self, origin, destination):
        # generate list of porters who are in a pending state
        pendingPorters = [porter for porter in self.simState.porters if porter.state == Porter.pending]
        print "PendingPorters ", pendingPorters
        
        if not pendingPorters:
            # no porters in pending state, so add the job to the job pool
            self.simState.jobPool.append((origin, destination))
            return
            
        closestPorter = None
        minDistance = None
        for porter in pendingPorters:
            if porter.unit == origin:
                event = Event(setStateDispatched, self.simState, porter, origin, destination)
                timedEvent = [self.simState.curTime, event]
                self.simState.eList.insert(timedEvent)
                return
            
            distance = self.simState.sTree.getTimeBetween(porter.unit, origin)
            if not minDistance:
                minDistance = distance
                closestPorter = porter
            elif distance < minDistance:
                minDistance = distance
                closestPorter = porter
                
        event = Event(setStateDispatched, self.simState, closestPorter, origin, destination)
        timedEvent = [self.simState.curTime, event]
        self.simState.eList.insert(timedEvent)
        return
        