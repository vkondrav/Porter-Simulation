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

    def __init__(self, func=None):
        self.detEventList = [[0, Event(func, 0, 1)],
							[100, Event(func, 1, 2)],
							[200, Event(func, 2, 0)],
							[300, Event(func, 1, 0)],
							[400, Event(func, 0, 2)],
							[500, Event(func, 2, 1)],
							[600, Event(func, 0, 2)],
							[700, Event(func, 1, 2)],
							[800, Event(func, 0, 1)],
							[900, Event(func, 2, 1)]]
                            
        sorted(self.detEventList, key=itemgetter(0), reverse=True)
						
    def insert(self, event):
        self.detEventList.append(event)
        sorted(self.detEventList, key=itemgetter(0), reverse=True)
        
    def pop(self):
        self.curTime, event = self.detEventList.pop()
        return event
        
    def isEmpty(self):
        return not bool(self.detEventList)