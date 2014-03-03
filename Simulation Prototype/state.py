class State(object):

    def __init__(self, env, porterManager, dispatchTable, dispatcher, jobList):
        self.env = env
        self.porterManager = porterManager
        self.dispatchTable = dispatchTable
        self.dispatcher = dispatcher
        self.jobList = jobList
        self.curTime = 0
        self.jobPool = []
        
    def __repr__(self):
        return "simState"
