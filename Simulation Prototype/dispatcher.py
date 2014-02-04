from porter import Porter
from job import Job

APPOINTMENT_FACTOR = 1.2
AUTOMATIC_UPGRADE = [[1, None], [2, 14], [3, 8], [4, 8], [5,5], [6,5], [7, 25], [8, 30], [9,40]]
PRIORITY_WEIGHT = [[1, 20], [2, 11], [3, 7], [4,5], [5,4], [6,3], [7,2], [8,1], [9,0]]
PROXMITY_WEIGHT = [['LOCATION', 11], ['ZONE', 7], ['UNIT', 7], ['SECTION', 2], ['FLOOR', 5], ['BUILDING', 3], ['CAMPUS', 1]]
AUTOLOCATION_VALUE = [['LOCATION', 4], ['ZONE', 8], ['UNIT', 7], ['SECTION', 14], ['FLOOR', 10], ['BUILDING', 12], ['BASE', 16]]

class Dispatcher(object):

    def __init__(self, af=APPOINTMENT_FACTOR, au=AUTOMATIC_UPGRADE, pw=PRIORITY_WEIGHT, pm=PROXIMITY_WEIGHT, av=AUTOLOCATION_VALUE):
        self.pending_jobs = []
        self.appointmentFactor = af
        self.automaticUpgrade = au
        self.priorityWeight = pw
        self.proximityWeight = pm
        self.autolocationValue = av

    # get the priority weight
    def getJobPriorityWeight(priority):
        for pw in self.priorityWeight:
            if pw[0] == priority:
                return pw[1]

    # check to see if porter is at the job's origin
    def getProximityMatchValue(origin):
        for porter in pendingPorter:
            if porter.unit == origin
                return self.proximityWeight[1][2]
        return 0

    # return the appointment factor
    def getAppointmentFactor(appointment):
        if appointment:
            return self.appointmentFactor
        else:
            return 1

    # get the next job to be assigned to a porter
    def getNextJob():
        nextJob = None
        nextDV = 0
        for job in self.pending_jobs:
            pmv = getProximityMatchValue(job.origin)
            pw = getJobPriorityWeight(job.priority)
            af = getAppointmentFactor(job.appointment)
            # calculate the dispatch value for all the jobs
            dv = pmv + pw * af
            # store the job with the highest dispatch value
            if dv > nextDV:
                nextJob = job
        return nextJob
                    
    def addJob(self, job):
        # start updating a job's priority
        job.autoProc = simState.env.Process(autoUpdateProcess())
        self.pending_jobs.append(job)
		
    def assignJobs(self, simState):
        while not simState.jobList.isEmpty() or self.pending_jobs:
            yield simState.env.timeout(1)
            job = None  
            if self.pending_jobs:
                job = getNextJob()
                # stop updating a job's priority
                job.autoProc.Interrupt()
            else:
                continue
            
            # generate list of porters who are in a pending state
            pendingPorters = [porter for porter in simState.porters if porter.state == Porter.pending]
            
            if not pendingPorters:
                # no porters in pending state, so add the job to the job pool
                self.pending_jobs.append(job)
                continue
                
            closestPorter = None
            minDistance = None
            for porter in pendingPorters:
                if porter.unit == job.origin:
                    porter.job = job
                    simState.env.process(porter.work(simState))
                    break
                
                distance = simState.sGraph.getTimeBetween(porter.unit, job.origin)
                if minDistance is None:
                    minDistance = distance
                    closestPorter = porter
                elif distance < minDistance:
                    minDistance = distance
                    closestPorter = porter
                    
            if not porter.job:
                closestPorter.job = job
                simState.env.process(closestPorter.work(simState))
