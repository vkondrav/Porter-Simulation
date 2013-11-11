from event import Event

class Porter(object):
    
    pending = 'pending'
    dispatched = 'dispatched'
    inprogress = 'inprogress'
    complete = 'complete'

    def __init__(self):
        self.state = Porter.pending
        self.unit = 0
        self.origin = None
        self.destination = None

def setStatePending(porter):
    porter.state = Porter.pending
    
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
    event = Event(setStateComplete, porter)
    timedEvent = [simState.curTime + delay, event]
    simState.eList.insert(timedEvent)
            
def setStateComplete(porter):
    porter.state = Porter.complete
    porter.unit = porter.destination
    porter.origin = None
    porter.destination = None