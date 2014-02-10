class Job(object):
    _jobId = 0

    def __init__(self, creationTime, inProgressTime, completeTime, origin, destination, priority, appointment):
        self.creationTime = creationTime
        self.inProgressTime = inProgressTime
        self.completeTime = completeTime
        self.origin = origin
        self.destination = destination
        self.jobStartTime = None
        self.jobCompletionTime = None
        self.startTime = None
        self.completionTime = None
        self.priority = priority
        self.appointment = appointment
        self.autoProc = None
        self.jobId = Job._jobId
        Job._jobId += 1
        
    def __repr__(self):
        return "Job%d: %s -> %s" % (self.jobId, self.origin, self.destination)

    # process to update the job's priority
    def autoUpdateProcess(self, au):
        # continue updating until priority is 1 or it is interrupted by the dispatcher
        while self.priority != 0:
            # find the matching priority and wait X minutes before lowering the job's priority
            for upgrade in au:
                if upgrade[0] == self.priority and self.priority != 0:
                    try:
                        yield simState.env.timeout(upgrade[1] * 60)
                    except:
                        self.autoProc = None
                    self.priority = self.priority - 1
                    break
        self.autoProc = None
        
class JobList(object):

    def __init__(self, au):                         
        self.jobList = []
        self.releasedJobList = []
        self.automaticUpgrade = au
						
    def insert(self, job):
        job.automaticUpgrade = self.automaticUpgrade
        self.jobList.append(job)
        self.jobList = sorted(self.jobList, key=self._jobListKey, reverse=True)
        
    def _jobListKey(self, job):
        return job.creationTime
        
    def isEmpty(self):
        return not bool(self.jobList)
        
    def jobReleaser(self, simState):
        while self.jobList:
            # peek at the end of the job list to ensure atomicity of job lists
            job = self.jobList[-1]
            print job
            yield simState.env.timeout(job.creationTime - simState.env.now)
            self.releasedJobList.append(self.jobList.pop())
            simState.dispatcher.addJob(job)
            
