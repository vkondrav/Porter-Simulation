import simpy

from porter import Porter
from state import State
from dispatcher import Dispatcher
from job import Job, JobList
from statImport import StatImport
from porterManager import PorterManager
from excelConverter import main as dashOutput
from random import seed

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
    seed(0)
    
    simState = State()
    
    simState.maxDelayReason = {"Patient Not Ready": config['porterWait'] * 60}
    
    importer = StatImport(config["jobFlow"]) # This should be fetched from the config
    simState.dispatchTable, simState.jobList = importer.runImport(config["fileLocation"])
    
    simState.env = simpy.Environment()
     
    simState.dispatcher = Dispatcher(config["appFactorValue"], config["wjl"], config["ajb"])
    simState.dispatcher.configData()

    #porterManager = PorterManager(config["startDay"])
    simState.porterManager = PorterManager(0)
    simState.porterManager.importPorterSched(config["schedule"])
	
    simState.env.process(simState.dispatcher.assignJobs(simState))
    simState.env.process(simState.jobList.jobReleaser(simState))

    sim_time = config["simulationDuration"] * 24 * 60 * 60
    print sim_time
    simState.env.run(until=sim_time)

    print "*****SIMULATION COMPLETE*****"

    dashOutput(simState.jobList.releasedJobList, config["outputLocation"])

if __name__=='__main__':
	main()

