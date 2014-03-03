from porter import Porter
from job import Job

AUTOMATIC_UPGRADE = [[0, None], [1, 14], [2, 8], [3, 8], [4,5], [5,5], [6, 25], [7, 30], [8,40]]
PRIORITY_WEIGHT = [[0, 20], [1, 11], [2, 7], [3,5], [4,4], [5,3], [6,2], [7,1], [8,0]]
PROXIMITY_WEIGHT = [['LOCATION', 11], ['ZONE', 7], ['UNIT', 7], ['SECTION', 2], ['FLOOR', 5], ['BUILDING', 3], ['CAMPUS', 1]]
AUTOLOCATION_VALUE = [['LOCATION', 4], ['ZONE', 8], ['UNIT', 7], ['SECTION', 14], ['FLOOR', 10], ['BUILDING', 12], ['BASE', 16]]

class Dispatcher(object):

    def __init__(self, af, pw, pm, amu, al):
        self.pending_jobs = []
        self.appointmentFactor = af
        self.priorityWeight = pw
        self.proximityWeight = pm
        self.automaticUpgrade = amu
        self.autoLocation = al

    def configData(self):
        for i in xrange(0,9):
            PRIORITY_WEIGHT[i][1] = self.priorityWeight[i]
            AUTOMATIC_UPGRADE[i][1] = self.automaticUpgrade[i]

        for i in xrange(0,6):
            AUTOLOCATION_VALUE[i][1] = self.autoLocation[i]
            PROXIMITY_WEIGHT[i][1] = self.proximityWeight[i]

        self.autoLocation = AUTOLOCATION_VALUE
        self.automaticUpgrade = AUTOMATIC_UPGRADE
        self.priorityWeight = PRIORITY_WEIGHT
        self.proximityWeight = PROXIMITY_WEIGHT

    # get the priority weight
    def getJobPriorityWeight(self, priority):
        for pw in self.priorityWeight:
            if pw[0] == priority:
                return pw[1]

    # return the appointment factor
    def getAppointmentFactor(self, appointment):
        if appointment:
            return self.appointmentFactor
        else:
            return 1

    # get the next job to be assigned to a porter
    def getNextJob(self):
        nextJob = None
        nextDV = 0
        for job in self.pending_jobs:
            #pmv = getProximityMatchValue(job.origin)
            pw = self.getJobPriorityWeight(job.priority)
            af = self.getAppointmentFactor(job.appointment)
            # calculate the dispatch value for all the jobs
            dv = pw * af
            # store the job with the highest dispatch value
            if dv > nextDV:
                nextJob = job
        self.pending_jobs.remove(nextJob)
        return nextJob
                    
    def addJob(self, job, simState):
        # start updating a job's priority
        job.autoProc = simState.env.process(job.autoUpdateProcess(simState, self.automaticUpgrade))
        self.pending_jobs.append(job)
		
    def assignJobs(self, simState):
        while not simState.jobList.isEmpty() or self.pending_jobs:
            yield simState.env.timeout(1)
            job = None  
            if self.pending_jobs:
                job = self.getNextJob()
                # stop updating a job's priority
                if job.autoProc:
                    job.autoProc.interrupt()
            else:
                continue
            
            # generate list of porters who are in a pending state
            pendingPorters = simState.porterManager.getPendingPorters(job.creationTime)
            if not pendingPorters:
                # no porters in pending state, so add the job to the job pool
                self.pending_jobs.append(job)
                continue
                
            for porter in pendingPorters:
                if porter.unit == job.origin:
                    porter.job = job
                    simState.env.process(porter.work(simState))
                    break
                    
            if not porter.job:
                porter = pendingPorters[0]
                porter.job = job
                simState.env.process(porter.work(simState))
