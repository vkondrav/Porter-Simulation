class Job(object):
    
    _jobId = 0

    def __init__(self, creationTime, inProgressTime, completeTime, origin, destination):
        self.creationTime = creationTime
        self.inProgressTime = inProgressTime
        self.completeTime = completeTime
        self.origin = origin
        self.destination = destination
        self.jobStartTime = None
        self.jobCompletionTime = None
        self.jobId = Job._jobId
        Job._jobId += 1
        
    def __repr__(self):
        return "Job%d: %s -> %s" % (self.jobId, self.origin, self.destination)
        
        
class JobList(object):

    def __init__(self):                         
        self.jobList = []
        self.releasedJobList = []
						
    def insert(self, job):
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