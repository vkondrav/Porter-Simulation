class State(object):

    def __init__(self, env=None, porterManager=None, dispatchTable=None, dispatcher=None, jobList=None):
        self.env = env
        self.porterManager = porterManager
        self.dispatchTable = dispatchTable
        self.dispatcher = dispatcher
        self.jobList = jobList
        maxDelayReason = {}
        
    def __repr__(self):
        return "simState"
