class State(object):

    def __init__(self, porters, spanningTree, eventList):
        self.porters = porters
        self.sTree = spanningTree
        self.eList = eventList
        self.curTime = 0
        self.jobPool = []
        
    def __repr__(self):
        return "simState"