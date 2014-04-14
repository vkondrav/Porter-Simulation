import csv
import time
import calendar
import string
from random import randint
from job import JobList, Job


keys = {
        "TransportJobID": 0,
        "SequenceOrder": 1,
        "Campus": 2,
        "Last_Status": 3,
        "StatusDate": 4,
        "Requester": 5,
        "Origin": 6,
        "Destination": 7,
        "JobPriorityID": 8,
        "OriginalPriorityID": 9,
        "Transporter": 10,
        "AppointmentDT": 11,
        "PendingDT": 12,
        "DispatchedDT": 13,
        "InProgressDT": 14,
        "CompleteDT": 15,
        "DelayMin": 16,
        "DelayReason": 17,
        "DispatchMins": 18,
        "ResponseMins": 19,
        "ArrivalMins": 20,
        "TransactionMins": 21,
        "TripMins": 22,
        "PatientMins": 23,
        "LostPorterMinsOnCancel": 24,
        "PatientTransportFlag": 25,
        "PendWeekendFlag": 26,
        "Created_Status": 27,
        "RequesterType": 28,
        "OriginZone": 29,
        "OriginBuilding": 30,
        "OriginUnit": 31,
        "DestinZone": 32,
        "DestinBuilding": 33,
        "DestinUnit": 34,
        "NumberOfJobsBatched": 35,
        "BatchedToJobID": 36,
        "ModeOfTravel": 37,
        "TotalTransportersRequired": 38,
        "TransportItem": 39,
        "ReasonCodeID": 40,
        "NumberOfPages": 41,
        "UniqueTransportJobID": 42,
        "RejectCount": 43,
        }

attributes = [
        "Last_Status",
        #"StatusDate",
        "Origin",
        "Destination",
        "OriginalPriorityID",
        #"AppointmentDT",
        "PendingDT",
        "DispatchedDT",
        "InProgressDT",
        "CompleteDT",
        "DelayMin",
        "DelayReason",
        # "DispatchMins",
        # "ResponseMins",
        # "ArrivalMins",
        # "TransactionMins",
        # "TripMins",
        # "PatientMins",
        # "LostPorterMinsOnCancel",
        "PatientTransportFlag",
        "Created_Status",
        # "ModeOfTravel"
     ]
             
required_attributes = [
        "Last_Status",
        #"StatusDate",
        "Origin",
        "Destination",
        "OriginalPriorityID",
        #"AppointmentDT",
        "PendingDT",
        "DispatchedDT",
        "InProgressDT",
        "CompleteDT",
        # "DelayMin",
        # "DelayReason",
        # "DispatchMins",
        # "ResponseMins",
        # "ArrivalMins",
        # "TransactionMins",
        # "TripMins",
        # "PatientMins",
        # "LostPorterMinsOnCancel",
        "PatientTransportFlag",
        "Created_Status",
        # "ModeOfTravel"
     ]


class StatImport(object):
    
    def __init__(self, rate, dayOffset):
        self.dispatchTable = {}
        self.statData = StatData(rate, dayOffset)
       
    def runImport(self, fileName):
        with open(fileName, 'rb') as csvFile:
            reader = csv.reader(csvFile, delimiter= ',')

            for row in reader:
                data = {}

                for attr in attributes:
                    if len(row) == len(keys) and row[keys[attr]] != "NULL":
                        data[attr] = row[keys[attr]]
                    
                if "Last_Status" in data and data["Last_Status"] == "Complete" and data["PatientTransportFlag"] == "1":
                    if all(k in data for k in required_attributes):
                        dispatchTimeAbs = strToT(data["DispatchedDT"])
                        dispatchTimeDelta = strToDeltaT(data["InProgressDT"], dispatchTimeAbs)
                        origin = data["Origin"]
                        
                        delayReason = data.get("DelayReason")
                        delayMin = data.get("DelayMin")
                        
                        if delayReason == "Patient Not Ready":
                            if delayMin:
                                dispatchTimeDelta -= int(delayMin) * 60
                                if dispatchTimeDelta < 0:
                                    # Delays are assumed during the dispatch state of a porter
                                    # If the delay is negative, then the assumption is incorrect
                                    # So we ignore that job
                                    continue
                            else:
                                # delay reason but no delay min
                                # discard dispatch time
                                continue
                        
                        self.addDispatchTime(origin, dispatchTimeDelta)
                        self.statData.addToSegment(data)
                    else:
                        print "Invalid CSV Entry:"
                        print data
                        continue
                    
        jobList = self.statData.constructJobList()
        
        return (self.dispatchTable, jobList)
                        
    def addDispatchTime(self, origin, dispatchTime):
        if origin in self.dispatchTable:
            self.dispatchTable[origin].append(dispatchTime)
        else:
            self.dispatchTable[origin] = [dispatchTime]
                        
                        
class StatData(object):

    secondsInDay = 86400
    secondsInHour = 3600
    secondsInMin = 60

    def __init__(self, rate, dayOffset):
        self.numSegments = 6
        self.segmentSize = 4
        self.statData = []
        self.rate = rate
        self.dayOffset = dayOffset
        
        for i in range(7):
            self.statData.append([])
            for j in range(self.numSegments):
                self.statData[i].append({})
        
    def addToSegment(self, data):
        timeStruct = time.strptime(data["PendingDT"] , "%Y-%m-%d %H:%M:%S")
        day = (timeStruct.tm_wday + (7 - self.dayOffset)) % 7
        segment = timeStruct.tm_hour / self.segmentSize;
        key = string.split(data["PendingDT"])[0]
        
        if self.statData[day][segment].has_key(key):
            self.statData[day][segment][key].append(data)
        else:
            self.statData[day][segment][key] = [data]
        
    def constructJobList(self):
        jobList = JobList()
        for day in self.statData:
            for segment in day:
                # keys = segment.keys()
                # key = keys[randint(0, len(keys) - 1)]
                
                # activeSegment = segment[key]
                activeSegment = self.segmentSelector(segment)
                
                for data in activeSegment:
                    delayReason = data.get("DelayReason")
                    delayTime = data.get("DelayMin")
                    
                    if not delayTime:
                        delayTime = 0
                        
                    delayTime = int(delayTime) * 60
                    
                    pendingTimeAbs = self.strToS(data["PendingDT"])
                    inProgressTimeDelta = strToT(data["InProgressDT"]) - strToT(data["DispatchedDT"])
                    completeTimeDelta = strToT(data["CompleteDT"]) - strToT(data["InProgressDT"])
                        
                    origin = data["Origin"]
                    destination = data["Destination"]
                    priority = int(data["OriginalPriorityID"])
                    appointment = 1 if data["Created_Status"] == "Appointment" else 0

                    jobList.insert(Job(pendingTimeAbs, inProgressTimeDelta, completeTimeDelta, origin, destination, priority, appointment, delayReason, delayTime))
                    
        return jobList
                    
    def segmentSelector(self, segment):
        sorted_keys = sorted(segment, key=lambda k: len(segment[k]))
        
        size = len(sorted_keys)
        third = (size - 1) / 3
        modulus = (size - 1) % 3
        offset = self.rate * third
        key = sorted_keys[randint(offset, offset + third + modulus)]
        
        return segment[key]

    def strToS(self, timeString):
        timeStruct = time.strptime(timeString , "%Y-%m-%d %H:%M:%S")
        day = (timeStruct.tm_wday + (7 - self.dayOffset)) % 7
        hour = timeStruct.tm_hour
        min = timeStruct.tm_min
        sec = timeStruct.tm_sec
        return (day * StatData.secondsInDay
                + hour * StatData.secondsInHour
                + min * StatData.secondsInMin
                + sec)


def strToT(timeString):
    return calendar.timegm(time.strptime(timeString , "%Y-%m-%d %H:%M:%S"))
    
    
def strToDeltaT(timeString, refTime):
    return strToT(timeString) - refTime


if __name__=='__main__':
    a = StatImport()
    jobList = JobList()
    print a.runImport('data.csv', jobList)
    print
    print jobList.jobList
    
# pendingTimeAbs = strToT(data["PendingDT"])
# pendingTime = pendingTimeAbs - startTimeAbs

# if pendingTimeAbs >= startTimeAbs and pendingTimeAbs <= endTimeAbs:
    
    # #print pendingTime
    # if all(k in data for k in attributes):
        # dispatchTime = strToDeltaT(data["DispatchedDT"], pendingTimeAbs)
        # inProgressTime = strToDeltaT(data["InProgressDT"], pendingTimeAbs)
        # completeTime = strToDeltaT(data["CompleteDT"], pendingTimeAbs)
        # origin = data["Origin"]
        # destination = data["Destination"]
        # priority = int(data["OriginalPriorityID"])
        # appointment = 1 if data["Created_Status"] == "Appointment" else 0
        # jobList.insert(Job(pendingTime, inProgressTime, completeTime, origin, destination, priority, appointment))
        # self.addDispatchTime(origin, dispatchTime)
    # else:
        # print "Invalid CSV Entry:"
        # print Data
        # continue
    
    # #print data
            
