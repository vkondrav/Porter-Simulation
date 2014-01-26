class State(object):

    def __init__(self, env, porterList, spanningGraph, dispatcher, jobList):
        self.env = env
        self.porters = porterList
        self.sGraph = spanningGraph
        self.dispatcher = dispatcher
        self.jobList = jobList
        self.curTime = 0
        self.jobPool = []
        
    def __repr__(self):
        return "simState"