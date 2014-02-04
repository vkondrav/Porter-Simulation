from porter import Porter
from job import Job

class Dispatcher(object):

    def __init__(self):
        self.pending_jobs = []
        
    def addJob(self, job):
        self.pending_jobs.append(job)
		
    def assignJobs(self, simState):
        while not simState.jobList.isEmpty() or self.pending_jobs:
            yield simState.env.timeout(1)
            job = None  
            if self.pending_jobs:
                job = self.pending_jobs.pop()
            else:
                continue
            
            # generate list of porters who are in a pending state
            pendingPorters = [porter for porter in simState.porters if porter.state == Porter.pending]
            
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