from event import Event

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

        
def setStatePending(simState, porter):
    porter.state = Porter.pending
    
    if simState.jobPool:
        # time to go from pending to dispatched
        delay = 0
        porter.job = simState.jobPool.pop(0)
        event = Event(setStateDispatched, simState, porter)
        timedEvent = [simState.curTime + delay, event]
        simState.eList.insert(timedEvent)
    
def setStateDispatched(simState, porter):
    porter.state = Porter.dispatched
    
    # time to go from dispatched to inprogress
    delay = simState.sTree.getTimeBetween(porter.unit, porter.job.origin)
    event = Event(setStateInProgress, simState, porter)
    timedEvent = [simState.curTime + delay, event]
    simState.eList.insert(timedEvent)
    
def setStateInProgress(simState, porter):
    porter.state = Porter.inprogress
    porter.unit = porter.job.origin
    porter.job.startTime = simState.curTime
    
    # time to go from dispatched to inprogress
    delay = simState.sTree.getTimeBetween(porter.job.origin, porter.job.destination)
    event = Event(setStateComplete, simState, porter)
    timedEvent = [simState.curTime + delay, event]
    simState.eList.insert(timedEvent)
            
def setStateComplete(simState, porter):
    porter.state = Porter.complete
    porter.unit = porter.job.destination
    porter.job.completionTime = simState.curTime
    porter.job = None
    
    # time to go from complete to pending
    delay = 0
    event = Event(setStatePending, simState, porter)
    timedEvent = [simState.curTime + delay, event]
    simState.eList.insert(timedEvent)