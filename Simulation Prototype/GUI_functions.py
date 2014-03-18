import os
from PyQt4 import QtCore, QtGui
import csv
import dateutil.parser as parser
import datetime as dt
import pprint
from portersim import main as portermain
import sys
import time

class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

class functions():

    ui = None
    Dialog = None
    appFactorInitial = None

    ajbInitial = list()
    wjlInitial = list()
    pmvInitial = list()
    avInitial = list()

    ajb = list()
    wjl = list()
    pmv = list()
    av = list()

    def appendDispatchLists(self):

        self.ajb.append(self.ui.ajb1)
        self.ajb.append(self.ui.ajb2)
        self.ajb.append(self.ui.ajb3)
        self.ajb.append(self.ui.ajb4)
        self.ajb.append(self.ui.ajb5)
        self.ajb.append(self.ui.ajb6)
        self.ajb.append(self.ui.ajb7)
        self.ajb.append(self.ui.ajb8)
        self.ajb.append(self.ui.ajb9)

        self.pmv.append(self.ui.pmv1)
        self.pmv.append(self.ui.pmv2)
        self.pmv.append(self.ui.pmv3)
        self.pmv.append(self.ui.pmv4)
        self.pmv.append(self.ui.pmv5)
        self.pmv.append(self.ui.pmv6)
        self.pmv.append(self.ui.pmv7)

        self.av.append(self.ui.av1)
        self.av.append(self.ui.av2)
        self.av.append(self.ui.av3)
        self.av.append(self.ui.av4)
        self.av.append(self.ui.av5)
        self.av.append(self.ui.av6)
        self.av.append(self.ui.av7)

        self.wjl.append(self.ui.wjl1)
        self.wjl.append(self.ui.wjl2)
        self.wjl.append(self.ui.wjl3)
        self.wjl.append(self.ui.wjl4)
        self.wjl.append(self.ui.wjl5)
        self.wjl.append(self.ui.wjl6)
        self.wjl.append(self.ui.wjl7)
        self.wjl.append(self.ui.wjl8)
        self.wjl.append(self.ui.wjl9)

    def assignEvents(self):

        ####EVENTS#############################################################
        self.ui.simulateButton.clicked.connect(self.buttonClicked)
        self.ui.resetAllButton.clicked.connect(self.resetAllButtonClicked)
        self.ui.fileBrowseButton.clicked.connect(self.fileBrowseButtonClicked)
        self.ui.fileBrowseButton_2.clicked.connect(self.fileBrowseButton2Clicked)
        self.ui.fileBrowseButton_3.clicked.connect(self.fileBrowseButton3Clicked)
        self.ui.resetAllDispatch.clicked.connect(self.resetAllDispatchClicked)
        self.ui.appFactor.valueChanged[int].connect(self.appFactorChange)
        self.ui.jobDistribution.currentIndexChanged[int].connect(self.jobDistChange)
        ########################################################################

    def connectOutput(self):
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)

    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        #cursor = self.ui.output.textCursor()
        #cursor.movePosition(QtGui.QTextCursor.End)
        #cursor.insertText(text)
        #self.ui.output.setTextCursor(cursor)
        #self.ui.output.ensureCursorVisible()
        self.ui.output.append(text)

    def buttonClicked(self):

            ex = True
            errorStr = ""

            if self.ui.startDate.date() > self.ui.endDate.date():
                ex = False
                errorStr = errorStr + "Start Date cannot be more than the End Date.\n"

            if not os.path.isfile(self.ui.fileLocation.text()):
                ex = False
                errorStr = errorStr + "Statistical Data File does not exist.\n"

            if not os.path.isfile(self.ui.fileLocation_2.text()):
                ex = False
                errorStr = errorStr + "Schedule Data File does not exist.\n"

            s = self.ui.fileLocation_3.text()
            if not s[-5:] == ".xlsm":
                ex = False
                errorStr = errorStr + "Output File must end with (.xlsm)"

            if ex:
                self.assignAndExecute()
            else:
                QtGui.QMessageBox.information(self.Dialog,  'Error',  errorStr,  QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

    def assignAndExecute(self):
        self.ui.output.setText("")
        print "*****STARTING SIMULATION*****"
        #float
        numberOfPorters = self.ui.numberOfPorters.value()
        #float
        simDuration = self.ui.simDuration.value()
        #date
        startDate = self.ui.startDate.date()
        startDay = startDate.dayOfWeek()
        startDate = startDate.toPyDate()
        startDate = str(startDate) + " 00:00:00"
        #date
        endDate = self.ui.endDate.date()
        endDay = endDate.dayOfWeek()
        endDate = endDate.toPyDate()
        endDate = str(endDate) + " 00:00:00"
        #int
        jobDistribution = self.ui.jobDistribution.currentIndex()
        #float
        correctEquipment = self.ui.correctEquipment.value()
        #float
        patientReadiness = self.ui.patientReadiness.value()
        #float
        porterWait = self.ui.porterWait.value()
        #float
        jobCancel = self.ui.jobCancel.value()
        #string
        fileLocation = self.ui.fileLocation.text()
        #string
        fileLocation_2 = self.ui.fileLocation_2.text()
        #string
        fileLocation_3 = self.ui.fileLocation_3.text()
        #float
        appFactorValue = float(self.ui.appFactorValue.text())
        #list of float
        ajb = list()

        i = 0
        while i < len(self.ajb):
            ajb.append(self.ajb[i].value())
            i += 1
        #list of float
        i = 0
        wjl = list()
        while i < len(self.wjl):
            wjl.append(self.wjl[i].value())
            i += 1
        #list of float
        i = 0
        pmv = list()
        while i < len(self.pmv):
            pmv.append(self.pmv[i].value())
            i += 1
        #list of float
        i = 0
        av = list()
        while i < len(self.av):
            av.append(self.av[i].value())
            i += 1

        #Dictionary
        inputDict = dict()
        inputDict["numberOfPorters"] = numberOfPorters
        inputDict["simulationDuration"] = simDuration
        inputDict["startDate"] = startDate
        inputDict["endDate"] = endDate
        inputDict["startDay"] = startDay
        inputDict["endDay"] = endDay
        inputDict["jobDistribution"] = jobDistribution
        inputDict["correctEquipment"] = correctEquipment
        inputDict["patientReadiness"] = patientReadiness
        inputDict["porterWait"] = porterWait
        inputDict["jobCancel"] = jobCancel
        inputDict["fileLocation"] = fileLocation
        inputDict["appFactorValue"] = appFactorValue
        inputDict["ajb"] = ajb
        inputDict["wjl"] = wjl
        inputDict["pmv"] = pmv
        inputDict["av"] = av
        inputDict["schedule"] = self.scheduleParser()
        inputDict["outputLocation"] = fileLocation_3

        #for i in inputDict:
        #    print(i + " : " + str(inputDict[i]))

        start_time = time.time()

        portermain(inputDict)

        print "Process Complete in " + str(time.time() - start_time) + "seconds"

    def resetAllButtonClicked(self):
        self.ui.numberOfPorters.setProperty("value", 10)
        self.ui.startDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2013, 7, 22), QtCore.QTime(0, 0, 0)))
        self.ui.endDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2013, 7, 23), QtCore.QTime(0, 0, 0)))
        self.ui.jobDistribution.setCurrentIndex(0)
        self.ui.correctEquipment.setProperty("value", 80.0)
        self.ui.patientReadiness.setProperty("value", 80.0)
        self.ui.porterWait.setProperty("value", 5.0)
        self.ui.fileLocation.setText("")
        self.ui.fileLocation_2.setText("")
        self.ui.fileLocation_3.setText("")

    def fileBrowseButtonClicked(self):
        fname = QtGui.QFileDialog.getOpenFileName(self.Dialog, 'Open file', os.getcwd(), "CSV Files (*.csv)")

        self.ui.fileLocation.setText(fname)

    def fileBrowseButton2Clicked(self):
        fname = QtGui.QFileDialog.getOpenFileName(self.Dialog, 'Open file', os.getcwd(), "CSV Files (*.csv)")

        self.ui.fileLocation_2.setText(fname)

    def fileBrowseButton3Clicked(self):
        fileName = str(dt.datetime.now())

        fileName = fileName.replace(':', "-")
        fileName = fileName.replace('.', "-")
        fileName = fileName.replace(' ', "_")

        fileName = fileName + ".xlsm"

        fname = QtGui.QFileDialog.getSaveFileName(self.Dialog, 'Save File', fileName, "Excel Macro Enabled Files (*.xlsm)")
        self.ui.fileLocation_3.setText(fname)


    def appFactorChange(self):
        self.ui.appFactorValue.setText(str(float(self.ui.appFactor.value())/100))

    def recordInitialDispatch(self):

        for i in self.ajb:
            self.ajbInitial.append(i.value())

        for i in self.wjl:
            self.wjlInitial.append(i.value())

        for i in self.pmv:
            self.pmvInitial.append(i.value())

        for i in self.av:
            self.avInitial.append(i.value())

        self.appFactorInitial = float(self.ui.appFactor.value())/100

    def resetAllDispatchClicked(self):
        self.ui.appFactorValue.setText(str(self.appFactorInitial))
        self.ui.appFactor.setProperty("value", self.appFactorInitial*100)

        i = 0
        while i < len(self.ajb):
            self.ajb[i].setProperty("value", self.ajbInitial[i])
            i += 1

        i = 0
        while i < len(self.wjl):
            self.wjl[i].setProperty("value", self.wjlInitial[i])
            i += 1

        i = 0
        while i < len(self.pmv):
            self.pmv[i].setProperty("value", self.pmvInitial[i])
            i += 1

        i = 0
        while i < len(self.av):
            self.av[i].setProperty("value", self.avInitial[i])
            i += 1

    def jobDistChange(self):
        if self.ui.jobDistribution.currentIndex() == 0:
            self.ui.fileLocation.setEnabled(True)
            self.ui.fileBrowseButton.setEnabled(True)
            self.ui.startDate.setEnabled(True)
            self.ui.endDate.setEnabled(True)
        else:
            self.ui.fileLocation.setEnabled(False)
            self.ui.fileBrowseButton.setEnabled(False)
            self.ui.startDate.setEnabled(False)
            self.ui.endDate.setEnabled(False)

    def initFileLocations(self):
        self.ui.fileLocation.setText("C:/Users/Vitaliy/Documents/GitHub/Porter-Simulation/Simulation Prototype/data.csv")
        self.ui.fileLocation_2.setText("C:/Users/Vitaliy/Documents/GitHub/Porter-Simulation/Simulation Prototype/Schedule.csv")

    def scheduleParser(self):

        with open(self.ui.fileLocation_2.text(), 'r') as f:
            reader = csv.reader(f)

            next(reader)
            parsedSchedule = []
            for row in reader:
                startTime = parser.parse(row[1])
                startTime = (startTime.hour * 3600) + (startTime.minute * 60)
                endTime = parser.parse(row[2])
                endTime = (endTime.hour * 3600) + (endTime.minute * 60)
                parsedSchedule.append((row[0], startTime, endTime, row[3].split(','), row[4].split(',')))

        reformattedSchedule = {}

        for ps in parsedSchedule:
            for pid in ps[3]:

                if str(pid) not in reformattedSchedule:
                    reformattedSchedule[str(pid)] = []

                for day in ps[4]:
                    reformattedSchedule[str(pid)].append((ps[0], ps[1], ps[2], day))

        #pprint.pprint(reformattedSchedule, None, 1, 80, 3)

        return reformattedSchedule

class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))