import simpy

from porter import Porter
from state import State
from dispatcher import Dispatcher
from job import Job, JobList
from statImport import StatImport
from porterManager import PorterManager
from excelConverter import main as dashOutput
from random import seed, randint
import sys

SIM_TIME = 86400


def main(config):
    # Set the random seed if it is set in the config
    if not config["randomSeed"] is None:
        used_seed = config["randomSeed"]
        seed(used_seed)
    else:
        used_seed = randint(0, 999999999)
        seed(used_seed)
    
    simState = State()
    
    # Initialize the reason to max delay amount look up table
    simState.maxDelayReason = {"Patient Not Ready": config['porterWait'] * 60}
    
    # Import the jobs from the historical job data
    importer = StatImport(config["jobFlow"], config["dayOffset"])
    simState.dispatchTable, simState.jobList = importer.runImport(config["fileLocation"])
    
    simState.env = simpy.Environment()
    
    simState.dispatcher = Dispatcher(config["appFactorValue"], config["wjl"], config["ajb"])
    simState.dispatcher.configData()

    # Initialize the porter manager with the day offset and schedule
    simState.porterManager = PorterManager(config["dayOffset"])
    simState.porterManager.importPorterSched(config["schedule"])
	
    simState.env.process(simState.dispatcher.assignJobs(simState))
    simState.env.process(simState.jobList.jobReleaser(simState))

    # Calculate the simulation duration in seconds
    sim_time = config["simulationDuration"] * 24 * 60 * 60

    simState.env.run(until=sim_time)

    print "*****SIMULATION COMPLETE*****"

    # Create the dashboard output
    dashOutput(simState.jobList.releasedJobList, config["outputLocation"])
    
    print "*****SEED USED: " + str(int(used_seed)) + "*****"

if __name__=='__main__':
	main()

