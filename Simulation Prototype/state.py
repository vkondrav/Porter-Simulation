class State(object):

    def __init__(self, env, porterList, dispatchTable, dispatcher, jobList):
        self.env = env
        self.porters = porterList
        self.dispatchTable = dispatchTable
        self.dispatcher = dispatcher
        self.jobList = jobList
        self.curTime = 0
        self.jobPool = []
        
    def __repr__(self):
        return "simState"