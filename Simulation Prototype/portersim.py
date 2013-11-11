# from InitTaskList import initEventList
# from BinTree import BTree

from porter import Porter
from spanningtree import SpanningTree, constructSampleTree
from event import DetFutureEventList
from state import State
from dispatcher import Dispatcher
		
		
# class FutureEventList(object):

	# def __init__(self):
		# self.eventList = BTree
		
	# def insert(self,data):
		# self.eventList.insert(data)
		
	# def pop(self):
		# return self.eventList.pop()
		
	# def isEmpty(self):
		# return self.eventList.isEmpty()
	
		
def main():
    numPorters = 3
    
    # Using DetEventList until FutureEventList works correctly
    # EventList = FutureEventList()
    dispatcher = Dispatcher()
    eventList = DetFutureEventList(func=dispatcher.assignTask)
    spanTree = SpanningTree()
    constructSampleTree(spanTree)
    
    porterList = []
    for i in range(numPorters):
        newPorter = Porter(i)
        porterList.append(newPorter)
	
    simState = State(porterList, spanTree, eventList)
    
    dispatcher.simState = simState
	
    while not eventList.isEmpty():
        curTime, event = eventList.pop()
        simState.curTime = curTime
        print '\nCurrent Time: ', curTime
        print 'Job Pool:', simState.jobPool
        event.log()
        event.trigger()
        
		
main()