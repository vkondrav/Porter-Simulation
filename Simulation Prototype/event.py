from operator import itemgetter

class Event(object):
    
    def __init__(self, func, *args):
        self.func = func
        self.args = args
    
    def trigger(self):
        self.func(*self.args)
        
    def log(self):
        print self.func, self.args
        
     
class DetFutureEventList(object):

    def __init__(self, func=None, jobList=None):                         
        self.detEventList = []
        for job in jobList:
            self.detEventList.append([job.creationTime, Event(func, job)])
                            
        self.detEventList = sorted(self.detEventList, key=itemgetter(0), reverse=True)
						
    def insert(self, event):
        self.detEventList.append(event)
        self.detEventList = sorted(self.detEventList, key=itemgetter(0), reverse=True)
        
    def pop(self):
        return self.detEventList.pop()
        
    def isEmpty(self):
        return not bool(self.detEventList)