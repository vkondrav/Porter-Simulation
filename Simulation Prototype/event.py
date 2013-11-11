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
							[10, Event(func, 1, 2)],
							[20, Event(func, 2, 0)],
							[30, Event(func, 1, 0)],
							[40, Event(func, 0, 2)],
							[50, Event(func, 2, 1)],
							[60, Event(func, 0, 2)],
							[70, Event(func, 1, 2)],
							[80, Event(func, 0, 1)],
							[90, Event(func, 2, 1)]]
                            
        self.detEventList = sorted(self.detEventList, key=itemgetter(0), reverse=True)
						
    def insert(self, event):
        self.detEventList.append(event)
        self.detEventList = sorted(self.detEventList, key=itemgetter(0), reverse=True)
        
    def pop(self):
        return self.detEventList.pop()
        
    def isEmpty(self):
        return not bool(self.detEventList)