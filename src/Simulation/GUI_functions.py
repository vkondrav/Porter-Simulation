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

#Description: redirects any output to console to the GUI console
class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

#Description: this class is responsible for handling a lot of the GUI functionality
#and passing the configuration variable to the main simulation
class functions():

    ui = None
    Dialog = None
    appFactorInitial = None

    #automatic job priority initial values
    ajbInitial = list()
    #weighted job list initial values
    wjlInitial = list()

    #automatic job priority values
    ajb = list()
    #weighted job list values
    wjl = list()

    schedule = None

    #place holder variable used when doing file name checks
    fileName = None

    #this function stores the automatic job priority and weighted job list GUI variables to their respective arrays
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

    #this function attaches events to GUI elements
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

    #connect the console output to the GUI console
    def connectOutput(self):
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)

    #this function appends the text and refreshes the GUI
    def normalOutputWritten(self, text):
        self.ui.output.append(text)
        QtCore.QCoreApplication.processEvents()

    #main submit button event
    def buttonClicked(self):
            self.ui.output.setText("")

            errorStr = ""

            statFile = self.ui.fileLocation.text()

            #Checking of the Stats File
            if statFile == "":
                errorStr = errorStr + "*****STATISTICAL DATA FILE ERROR*****\n" + "Message: Statistical Data File path is empty\n"
            elif not os.path.isfile(statFile):
                errorStr = errorStr + "*****STATISTICAL DATA FILE ERROR*****\n" + "Message: Statistical Data File does not exist\n"
            elif not statFile[-4:] == ".csv":
                errorStr = errorStr + "*****STATISTICAL DATA FILE ERROR*****\n" + "Message: Statistical Data File is not a .csv file\n"
            else:
                print "Statistical Data File Exists"

            schedFile = self.ui.fileLocation_2.text()

            #Checking of the Schedule Files
            if schedFile == "":
                errorStr = errorStr + "*****SCHEDULE DATA FILE ERROR*****\n" + "Message: Schedule Data File path is empty\n"
            elif not os.path.isfile(schedFile):
                errorStr = errorStr + "*****SCHEDULE DATA FILE ERROR*****\n" + "Message: Schedule Data File does not exist\n"
            elif not schedFile[-4:] == ".csv":
                errorStr = errorStr + "*****SCHEDULE DATA FILE ERROR*****\n" + "Message: Schedule Data File is not a .csv file\n"

            #Checking of the output directory
            s = self.ui.fileLocation_3.text()
            if s == "":
                errorStr = errorStr + "*****OUTPUT FOLDER ERROR*****\n" + "Message: Output Folder path is empty\n"
            elif not os.path.isdir(self.ui.fileLocation_3.text()):
                errorStr = errorStr + "*****OUTPUT FOLDER ERROR*****\n" + "Message: Output Folder path does not exist\n"
            else:
                print "Output Folder Exists"

            #Parsing of the schedule to insure integrity
            if errorStr == "":
                errorStr = errorStr + self.scheduleChecker()

            #If no errors proceed to simulation initilization, otherwise the use is presented with a Message Box lisiting the errors
            if errorStr == "":
                print "Schedule Data File Correct"
                self.assignAndExecute()
            else:
                QtGui.QMessageBox.information(self.Dialog,  'Error',  errorStr,  QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

    #Description: collect all the variables and compile them into a configuration dictionary to be passed to the main function
    def assignAndExecute(self):

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

        #auto pick a file name for the output document
        self.fileName = str(dt.now())

        self.fileName = self.fileName.replace(':', "-")
        self.fileName = self.fileName.replace('.', "-")
        self.fileName = self.fileName.replace(' ', "_")

        self.fileName = self.fileName + ".xlsm"

        #join the generated file name with the specified output path
        fileLocation_3 = os.path.join(str(self.ui.fileLocation_3.text()), self.fileName)
        #float
        appFactorValue = float(self.ui.appFactorValue.text())

        #checking if the user has decided to use the random seed option
        #int
        if self.ui.randSeedCheck.isChecked():
            randomSeed = self.ui.randFactor.value()
        else:
            randomSeed = None

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

        #start_time = time()
        print "*****STARTING SIMULATION*****"

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

    #Statistical Data File Selection dialog
    def fileBrowseButtonClicked(self):
        fname = QtGui.QFileDialog.getOpenFileName(self.Dialog, 'Choose Statistical Data File', os.path.expanduser("~"), "CSV Files (*.csv)")

        self.ui.fileLocation.setText(fname)

    #Schedule data File Selection Dialog
    def fileBrowseButton2Clicked(self):
        fname = QtGui.QFileDialog.getOpenFileName(self.Dialog, 'Choose Schedule Data File', os.path.expanduser("~"), "CSV Files (*.csv)")

        self.ui.fileLocation_2.setText(fname)

    #Output Directory Selection Dialog
    def fileBrowseButton3Clicked(self):

        #fname = QtGui.QFileDialog.getSaveFileName(self.Dialog, 'Save File', fileName, "Excel Macro Enabled Files (*.xlsm)")
        dirName = QtGui.QFileDialog.getExistingDirectory(self.Dialog, 'Directory to Save File', os.path.expanduser("~"))
        self.ui.fileLocation_3.setText(dirName)

    #Controls the appoinment factor float value as pyQt only allows for integer values
    def appFactorChange(self):
        self.ui.appFactorValue.setText(str(float(self.ui.appFactor.value())/100))

    #Storing of the initial Dispatch value to be used in the reset function
    def recordInitialDispatch(self):

        for i in self.ajb:
            self.ajbInitial.append(i.value())

        for i in self.wjl:
            self.wjlInitial.append(i.value())

        self.appFactorInitial = float(self.ui.appFactor.value())/100
        self.randFactorInitial = float(self.ui.randFactor.value())

    #Reseting of all the advanced options values
    def resetAllDispatchClicked(self):
        self.ui.appFactorValue.setText(str(self.appFactorInitial))
        self.ui.appFactor.setProperty("value", self.appFactorInitial*100)
        self.ui.randFactor.setProperty("value", self.randFactorInitial)
        self.ui.randSeedCheck.setChecked(False)
        self.ui.randFactor.setEnabled(False)

        i = 0
        while i < len(self.ajb):
            self.ajb[i].setProperty("value", self.ajbInitial[i])
            i += 1

        i = 0
        while i < len(self.wjl):
            self.wjl[i].setProperty("value", self.wjlInitial[i])
            i += 1

    #Description: this function parses through the schedule and checks for any errors in
    #the file. Outputs a string of errors for any errors found
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

    #Shift verification matches a regular expression to the contents
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

    #matching of a regular expression to the contents of porter ids
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

    #matching of a regular expression to the days contents
    def verifyDays(self, string, cell):

        strError = ""
        if string == "":
            strError += "*****DAY ID ERROR*****\n" + "Please check cell " + cell + " in schedule.\n" + "Message: empty Day ID\n"

        string = string.split(",")
        i = 1
        for c in string:

            if c == "":
                strError += "*****DAY ID ERROR*****\n" + "Please check cell " + cell + " in schedule.\n" + "Message: empty Day ID at position " + str(i) + "\n"
            if not bool(match("^[0-6]$", c)):
                strError += "*****DAY ID ERROR*****\n" + "Please check cell " + cell + " in schedule.\n" + "Message: invalid Day ID at position " + str(i) + "\n"
            i = i + 1

        return strError

    #Description: Actual realignment of the schedule to represent each porter individually
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

    #Some values being assigned to the GUI that are out of the scope of pyQt and QT Designer
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