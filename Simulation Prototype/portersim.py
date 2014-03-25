import simpy

from porter import Porter
from state import State
from dispatcher import Dispatcher
from job import Job, JobList
from statImport import StatImport
from porterManager import PorterManager
from excelConverter import main as dashOutput

SIM_TIME = 86400

  
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
        if not job.jobStartTime:
            print "Negative start time on %s by %s of %s" % (job.jobId, job.jobCompletionPorterID, job.jobStartTime)
            continue
        if not job.jobCompletionTime:
            print "Negative completion time on %s by %s of %s" % (job.jobId, job.jobCompletionPorterID, job.jobStartTime)
            continue
    
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


def main(config):
    jobList = JobList()
    # jobList.insert(Job(0, 0, 1))
    # jobList.insert(Job(10, 1, 2))
    # jobList.insert(Job(20, 2, 0))
    # jobList.insert(Job(30, 1, 0))
    # jobList.insert(Job(40, 0, 2))
    # jobList.insert(Job(50, 2, 1))
    # jobList.insert(Job(60, 0, 2))
    # jobList.insert(Job(70, 1, 2))
    # jobList.insert(Job(80, 0, 1))
    # jobList.insert(Job(90, 2, 1))
    
    importer = StatImport()
    jobList = JobList()
    dispatchTable = importer.runImport(config["fileLocation"], jobList)
    
    env = simpy.Environment()
    
    # while True:
        # try:
            # numPorters = int(raw_input('Number of porters: '))
            # break
        # except ValueError:
            # print 'Please input an integer'
     
    dispatcher = Dispatcher(config["appFactorValue"], config["wjl"], config["pmv"], config["ajb"], config["av"])
    dispatcher.configData()

    #porterManager = PorterManager(config["startDay"])
    porterManager = PorterManager(0)
    porterManager.importPorterSched(config["schedule"])
	
    simState = State(env, porterManager, dispatchTable, dispatcher, jobList)
	
    env.process(dispatcher.assignJobs(simState))
    env.process(jobList.jobReleaser(simState))

    sim_time = config["simulationDuration"] * 24 * 60 * 60
    print sim_time
    env.run(until=sim_time)

    print "*****SIMULATION COMPLETE*****"
    #reportStatistics(jobList.releasedJobList)

    dashOutput(jobList.releasedJobList, config["outputLocation"])

if __name__=='__main__':
	main()

