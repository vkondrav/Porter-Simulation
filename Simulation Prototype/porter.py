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
        self.origin = None
        self.destination = None
        
    def __repr__(self):
        return "Porter" + str(self.id)

        
def setStatePending(simState, porter):
    porter.state = Porter.pending
    
    if simState.jobPool:
        # time to go from pending to dispatched
        delay = 0
        origin, destination = simState.jobPool.pop()
        event = Event(setStateDispatched, simState, porter, origin, destination)
        timedEvent = [simState.curTime + delay, event]
        simState.eList.insert(timedEvent)
    
def setStateDispatched(simState, porter, origin, destination):
    porter.state = Porter.dispatched
    porter.origin = origin
    porter.destination = destination
    
    # time to go from dispatched to inprogress
    delay = simState.sTree.getTimeBetween(porter.unit, porter.origin)
    event = Event(setStateInProgress, simState, porter)
    timedEvent = [simState.curTime + delay, event]
    simState.eList.insert(timedEvent)
    
def setStateInProgress(simState, porter):
    porter.state = Porter.inprogress
    porter.unit = porter.origin
    
    # time to go from dispatched to inprogress
    delay = simState.sTree.getTimeBetween(porter.origin, porter.destination)
    event = Event(setStateComplete, simState, porter)
    timedEvent = [simState.curTime + delay, event]
    simState.eList.insert(timedEvent)
            
def setStateComplete(simState, porter):
    porter.state = Porter.complete
    porter.unit = porter.destination
    porter.origin = None
    porter.destination = None
    
    # time to go from complete to pending
    delay = 0
    event = Event(setStatePending, simState, porter)
    timedEvent = [simState.curTime + delay, event]
    simState.eList.insert(timedEvent)