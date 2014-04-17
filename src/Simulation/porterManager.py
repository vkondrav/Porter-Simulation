import math
from state import State
from porter import Porter

SECONDS_IN_DAY = 86400

class PorterManager(object):

    def __init__(self, startDay):
        self.porterList = []
        self.schedule = None
        self.startDay = startDay


    def importPorterSched(self, porterSchedule):
        self.schedule = porterSchedule
        #Initialize all the porters found in the porterSchedule
        for i in porterSchedule:
            newPorter = Porter(i)
            self.porterList.append(newPorter)

    def getPendingPorters(self, creationTime):
        ## First get a list of porters who are working ##
        workingList = []
        for porterID, shifts in self.schedule.items():
            for shift in shifts:
                #Get the porters if the simulation is only on the first day
                if int(creationTime) < SECONDS_IN_DAY:
                    if int(shift[3]) == self.startDay and int(shift[1]) <= creationTime and int(shift[2]) >= creationTime:
                        workingList.append(porterID)
                else:
                    #Get the number of days since the first day
                    numDays = int(math.floor(int(creationTime) / SECONDS_IN_DAY))
                    #Get the current day of the week
                    if (self.startDay + numDays) > 6:
                        currentDay = (self.startDay + numDays) - 7
                    else:
                        currentDay = self.startDay + numDays
                    #Get the time based on the number of days passed
                    creationTimeDay = creationTime / (numDays * SECONDS_IN_DAY)
                    if int(shift[3]) == currentDay and int(shift[1]) <= int(creationTimeDay) and int(shift[2]) >= int(creationTimeDay):
                        workingList.append(porterID)

        # Create a list of porters that are available and do not currently have jobs
        pendingList = []
        for porter in self.porterList:
            if porter.id in workingList and porter.state == Porter.pending:
                pendingList.append(porter)

        return pendingList
                    
