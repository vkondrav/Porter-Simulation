import xlwt
import os
import win32com.client

from datetime import datetime, timedelta
import pythoncom

#jobList attributes#

#creationTime
#inProgressTime
#completeTime
#origin
#destination
#jobStartTime
#jobCompletionTime
#startTime
#completionTime
#priority
#appointment
#autoProc
#jobId
#jobCompletionPorterID

#This class takes the output from the simulation, writes it to an excel document and activates dashboard macros
class converter(object):

    timeRef = datetime(2014,1,1,0)

    def __init__(self,jobList, outputLocation):
        self.jobList = jobList
        self.outputLocation = outputLocation

    def write(self):

        print "*****WRITING OUTPUT*****"
        book = xlwt.Workbook()
        sheet1 = book.add_sheet('Sheet 1')

        sheet1.write(0, 0, "Creation Time")
        sheet1.write(0, 1, "In Progress Time")
        sheet1.write(0, 2, "Complete Time")
        sheet1.write(0, 3, "Origin")
        sheet1.write(0, 4, "Destination")
        sheet1.write(0, 5, "Job Start Time")
        sheet1.write(0, 6, "Job Completion Time")
        sheet1.write(0, 7, "Start Time")
        sheet1.write(0, 8, "Completion Time")
        sheet1.write(0, 9, "Priority")
        sheet1.write(0, 10, "Appoinment")
        sheet1.write(0, 11, "Auto Process")
        sheet1.write(0, 12, "Job ID")
        sheet1.write(0, 13, "Completed by Porter")

        i = 1
        for j in self.jobList:

            if j.creationTime == None:
                crT = -1
            else:
                crT = self.timeRef + timedelta(seconds=j.creationTime)

            if j.completeTime == None:
                cpT = -1
            else:
                cpT = self.timeRef + timedelta(seconds=j.completeTime)

            if j.jobStartTime == None:
                jsT = -1
            else:
                jsT = self.timeRef + timedelta(seconds=j.jobStartTime)

            if j.jobCompletionTime == None:
                jcT = -1
            else:
                jcT = self.timeRef + timedelta(seconds=j.jobCompletionTime)

            sheet1.write(i, 0, crT)
            sheet1.write(i, 1, j.inProgressTime)
            sheet1.write(i, 2, cpT)
            sheet1.write(i, 3, j.origin)
            sheet1.write(i, 4, j.destination)
            sheet1.write(i, 5, jsT)
            sheet1.write(i, 6, jcT)
            sheet1.write(i, 7, j.startTime)
            sheet1.write(i, 8, j.completionTime)
            sheet1.write(i, 9, j.priority)
            sheet1.write(i, 10, j.appointment)
            sheet1.write(i, 11, j.autoProc)
            sheet1.write(i, 12, j.jobId)
            sheet1.write(i, 13, j.jobCompletionPorterID)
            i += 1

        print "*****SAVING OUTPUT*****"
        book.save('output.xls')

        print "*****BUILDING DASHBOARD*****"
        ol = str(self.outputLocation)
        ol = ol.replace("/","\\")

        try:
            xl=win32com.client.Dispatch("Excel.Application")
        except pythoncom.com_error as error:
            print "*****EXCEL DISPATCH FAILURE*****"
            return

        path = os.getcwd() + "\dashboard.xlsm"

        xl.Workbooks.Open(Filename=path)

        try:
            xl.Application.Run("main", ol)
        except pythoncom.com_error as error:
            print "*****DASHBOARD COMPLETE*****"

        print "*****DASHBOARD COMPLETE*****"
        xl.Quit()

def main(jobList, outputLocation):
    c = converter(jobList, outputLocation)
    c.write()