import simpy

from porter import Porter
from state import State
from dispatcher import Dispatcher
from job import Job, JobList
from statImport import StatImport


SIM_TIME = None

  
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
        timeToStart = job.jobStartTime - job.creationTime
        summedTimeToStart += timeToStart
        
        if shortestTimeToStart is None:
            shortestTimeToStart = timeToStart
        elif timeToStart < shortestTimeToStart:
            shortestTimeToStart = timeToStart
            
        if longestTimeToStart is None:
            longestTimeToStart = timeToStart
        elif timeToStart > longestTimeToStart:
            longestTimeToStart = timeToStart
            
        
        timeToComplete = job.jobCompletionTime - job.creationTime
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
    #name of input dictionary
    configDict = None
    
    jobList = JobList(configDict['ajb'])
    jobList.configData()
    
    importer = StatImport()
    jobList = JobList()
    dispatchTable = importer.runImport('data.csv', jobList, "2013-10-31 8:00:00", "2013-10-31 20:00:00")
    
    env = simpy.Environment()
    
    while True:
        try:
            numPorters = int(raw_input('Number of porters: '))
            break
        except ValueError:
            print 'Please input an integer'

    
    dispatcher = Dispatcher(inputDict['appFactorValue'],inputDict['wjl'],inputDict['pmv'])
    dispatcher.configData()

    
    porterList = []
    for i in range(numPorters):
        newPorter = Porter(inputDict['av'])
        newPorter.configData()
        porterList.append(newPorter)
	
    simState = State(env, porterList, dispatchTable, dispatcher, jobList)
	
    env.process(dispatcher.assignJobs(simState))
    env.process(jobList.jobReleaser(simState))
    
    env.run(until=SIM_TIME)
        
    reportStatistics(jobList.releasedJobList)

    
main()
