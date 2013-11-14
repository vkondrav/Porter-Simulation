# from InitTaskList import initEventList
# from BinTree import BTree

from porter import Porter
from spanningtree import SpanningTree, constructSampleTree
from event import DetFutureEventList
from state import State
from dispatcher import Dispatcher
from job import Job
		
		
# class FutureEventList(object):

	# def __init__(self):
		# self.eventList = BTree
		
	# def insert(self,data):
		# self.eventList.insert(data)
		
	# def pop(self):
		# return self.eventList.pop()
		
	# def isEmpty(self):
		# return self.eventList.isEmpty()
        
def reportStatistics(jobList):
    numJobs = len(jobList)

    timeToStart = 0
    summedTimeToStart = 0
    shortestTimeToStart = None
    longestTimeToStart = None
    averageTimeToStart = None
    
    timeToComplete = 0
    summedTimeToComplete = 0
    shortestTimeToComplete = None
    longestTimeToComplete = None
    averageTimeToComplete = None
    
    for job in jobList:
        timeToStart = job.startTime - job.creationTime
        summedTimeToStart += timeToStart
        
        if shortestTimeToStart is None:
            shortestTimeToStart = timeToStart
        elif timeToStart < shortestTimeToStart:
            shortestTimeToStart = timeToStart
            
        if longestTimeToStart is None:
            longestTimeToStart = timeToStart
        elif timeToStart > longestTimeToStart:
            longestTimeToStart = timeToStart
            
        
        timeToComplete = job.completionTime - job.creationTime
        summedTimeToComplete += timeToComplete
            
        if shortestTimeToComplete is None:
            shortestTimeToComplete = timeToComplete
        elif timeToComplete < shortestTimeToComplete:
            shortestTimeToComplete = timeToComplete
            
        if longestTimeToComplete is None:
            longestTimeToComplete = timeToComplete
        elif timeToComplete > longestTimeToComplete:
            longestTimeToComplete = timeToComplete
 
            
    averageTimeToStart = summedTimeToStart / float(numJobs)
    averageTimeToComplete = summedTimeToComplete / float(numJobs)
            
    print
    print
    print "Shortest time to start a job: %d" % shortestTimeToStart
    print "Longest time to start a job: %d" % longestTimeToStart
    print "Average time to start a job: %d" % averageTimeToStart
    print
    print "Shortest time to complete a job: %d" % shortestTimeToComplete
    print "Longest time to complete a job: %d" % longestTimeToComplete
    print "Average time to complete a job: %d" % averageTimeToComplete
            
		
def main():
    jobList = []
    jobList.append(Job(0, 0, 1))
    jobList.append(Job(10, 1, 2))
    jobList.append(Job(20, 2, 0))
    jobList.append(Job(30, 1, 0))
    jobList.append(Job(40, 0, 2))
    jobList.append(Job(50, 2, 1))
    jobList.append(Job(60, 0, 2))
    jobList.append(Job(70, 1, 2))
    jobList.append(Job(80, 0, 1))
    jobList.append(Job(90, 2, 1))
    
    while True:
        try:
            numPorters = int(raw_input('Number of porters: '))
            break
        except ValueError:
            print 'Please input an integer'
    
    # Using DetEventList until FutureEventList works correctly
    # EventList = FutureEventList()
    dispatcher = Dispatcher()
    eventList = DetFutureEventList(func=dispatcher.assignJob, jobList=jobList)
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
        
    reportStatistics(jobList)
		
main()