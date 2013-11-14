class Job(object):

    def __init__(self, creationTime, origin, destination):
        self.creationTime = creationTime
        self.origin = origin
        self.destination = destination
        self.startTime = None
        self.completionTime = None
        
    def __repr__(self):
        return "Job: %d -> %d" % (self.origin, self.destination)