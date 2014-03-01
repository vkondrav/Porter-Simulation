import cPickle
import pprint
import xlwt
import tempfile
import os
import win32com.client

from datetime import datetime, timedelta
from time import sleep

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

class converter():

    timeRef = datetime(2014,1,1,8)

    jobList = None

    def getList(self):

        with open(r"output.pickle", "rb") as input_file:
            self.jobList = cPickle.load(input_file)

    def write(self):

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

        i = 1
        for j in self.jobList:

            crT = self.timeRef + timedelta(seconds=j.creationTime)
            cpT = self.timeRef + timedelta(seconds=j.completeTime)
            jsT = self.timeRef + timedelta(seconds=j.jobStartTime)
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

            i += 1

        book.save('output.xls')
        book.save(tempfile.TemporaryFile())

        xl=win32com.client.Dispatch("Excel.Application")

        path = os.getcwd() + "\dashboard.xlsm"

        xl.Workbooks.Open(Filename=path,ReadOnly=1)
        xl.Application.Run("main")

        sleep(5)
        os.startfile(path)

def main():
    c = converter()
    c.getList()
    c.write()

if __name__=='__main__':
	main()