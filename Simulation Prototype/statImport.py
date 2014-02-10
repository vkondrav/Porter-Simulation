import csv
import time
import calendar
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
    
    def __init__(self):
        self.dispatchTable = {}
       
    def runImport(self, fileName, jobList, startTimeStr, endTimeStr):
        startTimeAbs = strToT(startTimeStr)
        endTimeAbs = strToT(endTimeStr)
        
        with open(fileName, 'rb') as csvFile:
            reader = csv.reader(csvFile, delimiter= ',')

            for row in reader:
                data = {}

                for attr in attributes:
                    if len(row) == len(keys) and row[keys[attr]] != "NULL":
                        data[attr] = row[keys[attr]]
                    
                if "Last_Status" in data and data["Last_Status"] == "Complete" and data["PatientTransportFlag"] == "1": # time filter goes here
                    pendingTimeAbs = strToT(data["PendingDT"])
                    pendingTime = pendingTimeAbs - startTimeAbs
                    
                    if pendingTimeAbs >= startTimeAbs and pendingTimeAbs <= endTimeAbs:
                        
                        #print pendingTime
                        if all(k in data for k in attributes):
                            dispatchTime = strToDeltaT(data["DispatchedDT"], pendingTimeAbs)
                            inProgressTime = strToDeltaT(data["InProgressDT"], pendingTimeAbs)
                            completeTime = strToDeltaT(data["CompleteDT"], pendingTimeAbs)
                            origin = data["Origin"]
                            destination = data["Destination"]
                            priority = int(data["OriginalPriorityID"])
                            appointment = 1 if data["Created_Status"] == "Appointment" else 0
                            jobList.insert(Job(pendingTime, inProgressTime, completeTime, origin, destination, priority, appointment))
                            self.addDispatchTime(origin, dispatchTime)
                        else:
                            print "Invalid CSV Entry:"
                            print Data
                            continue
                        
                        #print data
                        
        
        return self.dispatchTable
                        
    def addDispatchTime(self, origin, dispatchTime):
        if origin in self.dispatchTable:
            self.dispatchTable[origin].append(dispatchTime)
        else:
            self.dispatchTable[origin] = [dispatchTime]
                        

def strToT(timeString):
    return calendar.timegm(time.strptime(timeString , "%Y-%m-%d %H:%M:%S"))
    
    
def strToDeltaT(timeString, refTime):
    return strToT(timeString) - refTime


if __name__=='__main__':
    a = StatImport()
    print a.runImport('data.csv', JobList(), "2013-10-31 8:00:00", "2013-10-31 20:00:00")
            
