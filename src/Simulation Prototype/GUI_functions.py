import os
import sys
from PyQt4 import QtCore, QtGui
from csv import reader as csvreader
import dateutil.parser as parser
from datetime import datetime as dt
from time import time
from re import match
from portersim import main as portermain
import pprint

class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

class functions():

    ui = None
    Dialog = None
    appFactorInitial = None

    #automatic job priority
    ajbInitial = list()
    #weighted job list
    wjlInitial = list()

    ajb = list()
    wjl = list()

    schedule = None

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
        ########################################################################

    def connectOutput(self):
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)

    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        self.ui.output.append(text)

    def buttonClicked(self):
            self.ui.output.setText("")

            errorStr = ""

            if self.ui.fileLocation.text() == "":
                errorStr = errorStr + "*****STATISTICAL DATA FILE ERROR*****\n" + "Message: Statistical Data File path is empty\n"
            elif not os.path.isfile(self.ui.fileLocation.text()):
                errorStr = errorStr + "*****STATISTICAL DATA FILE ERROR*****\n" + "Message: Statistical Data File does not exist\n"
            else:
                self.ui.output.append("Statistical Data File Exists")
                QtCore.QCoreApplication.processEvents()



            if self.ui.fileLocation_2.text() == "":
                errorStr = errorStr + "*****SCHEDULE DATA FILE ERROR*****\n" + "Message: Schedule Data File path is empty\n"
            elif not os.path.isfile(self.ui.fileLocation_2.text()):
                errorStr = errorStr + "*****SCHEDULE DATA FILE ERROR*****\n" + "Message: Schedule Data File does not exist\n"

            s = self.ui.fileLocation_3.text()
            if s == "":
                errorStr = errorStr + "*****OUTPUT FILE ERROR*****\n" + "Message: Output File path is empty\n"
            elif not s[-5:] == ".xlsm":
                errorStr = errorStr + "*****OUTPUT FILE ERROR*****\n" + "Message: Output File must end with (.xlsm)\n"
            else:
                self.ui.output.append("Output File Exists")
                QtCore.QCoreApplication.processEvents()

            if errorStr == "":
                errorStr = errorStr + self.scheduleChecker()

            if errorStr == "":
                self.ui.output.append("Schedule Data File Correct")
                QtCore.QCoreApplication.processEvents()
                self.assignAndExecute()
            else:
                QtGui.QMessageBox.information(self.Dialog,  'Error',  errorStr,  QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

    def assignAndExecute(self):
        self.ui.output.append("*****STARTING SIMULATION*****")
        QtCore.QCoreApplication.processEvents()

        #float
        simDuration = self.ui.simDuration.value()
        #float
        porterWait = self.ui.porterWait.value()
        #int
        jobFlow = self.ui.jobFlow.currentIndex()
        #float
        #jobCancel = self.ui.jobCancel.value()
        #string
        fileLocation = self.ui.fileLocation.text()
        #string
        fileLocation_2 = self.ui.fileLocation_2.text()
        #string
        fileLocation_3 = self.ui.fileLocation_3.text()
        #float
        appFactorValue = float(self.ui.appFactorValue.text())
        #int
        randomSeed = self.ui.randFactor.value()
        #int
        dayOffset = self.ui.dayOffset.currentIndex()


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

        #Dictionary
        inputDict = dict()
        inputDict["simulationDuration"] = simDuration
        inputDict["porterWait"] = porterWait
        inputDict["jobFlow"] = jobFlow
        inputDict["fileLocation"] = fileLocation
        inputDict["appFactorValue"] = appFactorValue
        inputDict["ajb"] = ajb
        inputDict["wjl"] = wjl
        inputDict["schedule"] = self.scheduleParser()
        inputDict["outputLocation"] = fileLocation_3
        inputDict["randomSeed"] = randomSeed
        inputDict["dayOffset"] = dayOffset

        start_time = time()

        portermain(inputDict)

        #print "Process Complete in " + str(time() - start_time) + " seconds"

        QtGui.QMessageBox.information(self.Dialog,  'Success',  "Simulation Complete",  QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

    def resetAllButtonClicked(self):
        self.ui.simDuration.setProperty("value", 1.0)
        self.ui.porterWait.setProperty("value", 5.0)
        self.ui.jobFlow.setCurrentIndex(1)
        self.ui.dayOffset.setCurrentIndex(0)
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
        fileName = str(dt.now())

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

        self.appFactorInitial = float(self.ui.appFactor.value())/100
        self.randFactorInitial = float(self.ui.randFactor.value())

    def resetAllDispatchClicked(self):
        self.ui.appFactorValue.setText(str(self.appFactorInitial))
        self.ui.appFactor.setProperty("value", self.appFactorInitial*100)
        self.ui.randFactor.setProperty("value", self.randFactorInitial)

        i = 0
        while i < len(self.ajb):
            self.ajb[i].setProperty("value", self.ajbInitial[i])
            i += 1

        i = 0
        while i < len(self.wjl):
            self.wjl[i].setProperty("value", self.wjlInitial[i])
            i += 1

    def scheduleChecker(self):
        with open(self.ui.fileLocation_2.text(), 'r') as f:
            reader = csvreader(f)

            next(reader)

            strError = ""
            i = 2

            for row in reader:

                cell = "Row: " + str(i) + " Column: 1"

                try:
                    strError = strError + self.verifyShiftID(row[0], cell)
                except:
                    strError = strError + "Incorrect Syntax in Schedule File. Check " + cell + "\n"

                cell = "Row: " + str(i) + " Column: 2"
                try:
                    strError = strError + self.verifyStartTime(row[1], cell)
                except:
                    strError = strError + "Incorrect Syntax in Schedule File. Check " + cell + "\n"

                cell = "Row: " + str(i) + " Column: 3"
                try:
                    strError = strError + self.verifyEndTime(row[2], cell)
                except:
                    strError = strError + "Incorrect Syntax in Schedule File. Check " + cell + "\n"

                cell = "Row: " + str(i) + " Column: 4"
                try:
                    strError = strError + self.verifyPorterID(row[3], cell)
                except:
                    strError = strError + "Incorrect Syntax in Schedule File. Check " + cell + "\n"

                cell = "Row: " + str(i) + " Column: 5"
                try:
                    strError = strError + self.verifyDays(row[4], cell)
                except:
                    strError = strError + "Incorrect Syntax in Schedule File. Check " + cell + "\n"

                i = i + 1

                if strError != "":
                    break

            f.close()

        if strError == "":
            return strError
        else:
            strError = "*****SCHEDULE DATA FILE ERROR*****\n" + strError
            return strError

    def verifyShiftID(self, string, cell):

        strError = ""
        if string == "":
            strError += "*****SHIFT ID ERROR*****\n", "Please check cell " + cell + " in schedule.\n", "Message: empty shift ID at position\n"
        if not bool(match("^[A-Za-z0-9 ]*$", string)):
            strError += "*****SHIFT ID ERROR*****\n", "Please check cell " + cell + " in schedule.\n", "Message: invalid shift ID at position\n"

        return strError

    def verifyStartTime(self, string, cell):

        strError = ""

        try:
            if string == "":
                strError = strError + "*****START TIME ERROR*****\n" + "Please check " + cell + " in the schedule.\n" + "Message: empty start time\n"
            startTime = parser.parse(string)

        except ValueError as e:
            strError =  strError + "*****START TIME ERROR*****\n" + "Please check " + cell + " in the schedule.\n" +  "Message: " + str(e.message) + "\n"
            pass
        except TypeError as e:
            strError = strError + "*****START TIME ERROR*****\n" + "Please check " + cell + " in the schedule.\n" + "Message: " + str(e.message) + "\n"
            pass
        except:
            e = sys.exc_info()[0]
            strError = strError + "*****START TIME ERROR*****\n" + "Man, you must have done something special to get this. Check " + cell + "\n" + "Message: " + str(e) + "\n"
            pass

        return strError

    def verifyEndTime(self, string, cell):

        strError = ""

        try:
            if string == "":
                strError = strError + "*****END TIME ERROR*****\n" + "Please check " + cell + " in schedule.\n" + "Message: empty start time\n"
            endTime = parser.parse(string)

        except ValueError as e:
            strError =  strError + "*****END TIME ERROR*****\n" + "Please check cell " + cell + " in the schedule.\n" + "Message: " + e.message + "\n"
            pass
        except TypeError as e:
            strError = strError + "*****END TIME ERROR*****\n" + "Please check cell " + cell + " in the schedule.\n" + "Message: " + e.message + "\n"
            pass
        except:
            e = sys.exc_info()[0]
            strError = strError + "*****END TIME ERROR*****\n" + "Man, you must have done something special to get this. Check " + cell + "\n" + "Message: " + str(e) + "\n"
            pass

        return strError


    def verifyPorterID(self, string, cell):

        strError = ""

        if string == "":
            strError += "*****PORTER ID ERROR*****\n" + "Please check cell " + cell + " in schedule.\n" + "Message: empty porter ID\n"

        string = string.split(",")
        i = 1

        for c in string:
            if c == "":
                strError += "*****PORTER ID ERROR*****\n" + "Please check cell " + cell + " in schedule.\n" + "Message: empty porter ID at position " + str(i) + "\n"
            if not bool(match("^[A-Za-z0-9 ]*$", c)):
                strError += "*****PORTER ID ERROR*****\n" + "Please check cell " + cell + " in schedule.\n" + "Message: invalid porter ID at position " + str(i) + "\n"
            i = i + 1

        return strError

    def verifyDays(self, string, cell):

        strError = ""
        if string == "":
            strError += "*****DAY ID ERROR*****\n" + "Please check cell " + cell + " in schedule.\n" + "Message: empty Day ID\n"

        string = string.split(",")
        i = 1
        for c in string:

            if c == "":
                strError += "*****DAY ID ERROR*****\n" + "Please check cell " + cell + " in schedule.\n" + "Message: empty Day ID at position " + str(i) + "\n"
            if not bool(match("^[0-4]$", c)):
                strError += "*****DAY ID ERROR*****\n" + "Please check cell " + cell + " in schedule.\n" + "Message: invalid Day ID at position " + str(i) + "\n"
            i = i + 1

        return strError


    def scheduleParser(self):

        with open(self.ui.fileLocation_2.text(), 'r') as f:
            reader = csvreader(f)

            next(reader)
            parsedSchedule = []

            for row in reader:

                startTime = parser.parse(row[1])

                startTime = (startTime.hour * 3600) + (startTime.minute * 60)

                endTime = parser.parse(row[2])

                endTime = (endTime.hour * 3600) + (endTime.minute * 60)

                parsedSchedule.append((row[0], startTime, endTime, row[3].split(','), row[4].split(',')))

            f.close()
        reformattedSchedule = {}

        for ps in parsedSchedule:
            for pid in ps[3]:

                if str(pid) not in reformattedSchedule:
                    reformattedSchedule[str(pid)] = []

                for day in ps[4]:
                    reformattedSchedule[str(pid)].append((ps[0], ps[1], ps[2], day))

        return reformattedSchedule

    def assignNewValues(self):

        #window Title
        self.Dialog.setWindowTitle("Porter Simulation")

        #window properties
        self.Dialog.setFixedSize(766, 625)
        self.Dialog.setWindowFlags(self.Dialog.windowFlags() | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowMinimizeButtonHint)

        #output box config
        self.ui.output.setReadOnly(True)
        self.ui.output.setGeometry(QtCore.QRect(10, 340, 731, 181))

        #load logo
        pixmap = QtGui.QPixmap(os.getcwd() + "/hhs.png")
        self.ui.hhs.setPixmap(pixmap)