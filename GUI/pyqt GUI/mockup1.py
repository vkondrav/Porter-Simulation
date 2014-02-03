# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mockup.ui'
#
# Created: Mon Feb  3 00:14:41 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(681, 549)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 358, 57))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 60, 661, 481))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(_fromUtf8("background-color: rgb(216, 216, 216);"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 381, 190))
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox{\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-width : 1.2px;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QSpinBox,QDateEdit,QComboBox\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"}"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.splitter_6 = QtGui.QSplitter(self.groupBox)
        self.splitter_6.setGeometry(QtCore.QRect(30, 20, 331, 161))
        self.splitter_6.setStyleSheet(_fromUtf8(""))
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName(_fromUtf8("splitter_6"))
        self.splitter_5 = QtGui.QSplitter(self.splitter_6)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.label_2 = QtGui.QLabel(self.splitter_5)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.numberOfPorters = QtGui.QSpinBox(self.splitter_5)
        self.numberOfPorters.setStyleSheet(_fromUtf8(""))
        self.numberOfPorters.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numberOfPorters.setMaximum(1000)
        self.numberOfPorters.setProperty("value", 10)
        self.numberOfPorters.setObjectName(_fromUtf8("numberOfPorters"))
        self.splitter_4 = QtGui.QSplitter(self.splitter_6)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.label_3 = QtGui.QLabel(self.splitter_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.startDate = QtGui.QDateEdit(self.splitter_4)
        self.startDate.setStyleSheet(_fromUtf8(""))
        self.startDate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.startDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.startDate.setCalendarPopup(True)
        self.startDate.setCurrentSectionIndex(0)
        self.startDate.setObjectName(_fromUtf8("startDate"))
        self.splitter_3 = QtGui.QSplitter(self.splitter_6)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.label_4 = QtGui.QLabel(self.splitter_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.endDate = QtGui.QDateEdit(self.splitter_3)
        self.endDate.setStyleSheet(_fromUtf8(""))
        self.endDate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.endDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.endDate.setCalendarPopup(True)
        self.endDate.setCurrentSectionIndex(0)
        self.endDate.setObjectName(_fromUtf8("endDate"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_6)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.label_5 = QtGui.QLabel(self.splitter_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.jobDistribution = QtGui.QComboBox(self.splitter_2)
        self.jobDistribution.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.jobDistribution.setStyleSheet(_fromUtf8(""))
        self.jobDistribution.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.jobDistribution.setObjectName(_fromUtf8("jobDistribution"))
        self.jobDistribution.addItem(_fromUtf8(""))
        self.jobDistribution.addItem(_fromUtf8(""))
        self.jobDistribution.addItem(_fromUtf8(""))
        self.splitter = QtGui.QSplitter(self.splitter_6)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_6 = QtGui.QLabel(self.splitter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.jobIntensity = QtGui.QComboBox(self.splitter)
        self.jobIntensity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.jobIntensity.setStyleSheet(_fromUtf8(""))
        self.jobIntensity.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.jobIntensity.setObjectName(_fromUtf8("jobIntensity"))
        self.jobIntensity.addItem(_fromUtf8(""))
        self.jobIntensity.addItem(_fromUtf8(""))
        self.jobIntensity.addItem(_fromUtf8(""))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 210, 381, 141))
        self.groupBox_2.setStyleSheet(_fromUtf8("QGroupBox{\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-width : 1.2px;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QDoubleSpinBox\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"}"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.splitter_10 = QtGui.QSplitter(self.groupBox_2)
        self.splitter_10.setGeometry(QtCore.QRect(30, 30, 311, 91))
        self.splitter_10.setStyleSheet(_fromUtf8(""))
        self.splitter_10.setOrientation(QtCore.Qt.Vertical)
        self.splitter_10.setObjectName(_fromUtf8("splitter_10"))
        self.splitter_7 = QtGui.QSplitter(self.splitter_10)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName(_fromUtf8("splitter_7"))
        self.label_7 = QtGui.QLabel(self.splitter_7)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.correctEquipment = QtGui.QDoubleSpinBox(self.splitter_7)
        self.correctEquipment.setStyleSheet(_fromUtf8(""))
        self.correctEquipment.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.correctEquipment.setMaximum(100.0)
        self.correctEquipment.setProperty("value", 80.0)
        self.correctEquipment.setObjectName(_fromUtf8("correctEquipment"))
        self.splitter_8 = QtGui.QSplitter(self.splitter_10)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName(_fromUtf8("splitter_8"))
        self.label_8 = QtGui.QLabel(self.splitter_8)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.patientReadiness = QtGui.QDoubleSpinBox(self.splitter_8)
        self.patientReadiness.setStyleSheet(_fromUtf8(""))
        self.patientReadiness.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.patientReadiness.setMaximum(100.0)
        self.patientReadiness.setProperty("value", 80.0)
        self.patientReadiness.setObjectName(_fromUtf8("patientReadiness"))
        self.splitter_9 = QtGui.QSplitter(self.splitter_10)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName(_fromUtf8("splitter_9"))
        self.label_9 = QtGui.QLabel(self.splitter_9)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.porterWait = QtGui.QDoubleSpinBox(self.splitter_9)
        self.porterWait.setStyleSheet(_fromUtf8(""))
        self.porterWait.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.porterWait.setMaximum(1000.0)
        self.porterWait.setProperty("value", 5.0)
        self.porterWait.setObjectName(_fromUtf8("porterWait"))
        self.splitter_12 = QtGui.QSplitter(self.groupBox_2)
        self.splitter_12.setGeometry(QtCore.QRect(350, 30, 21, 91))
        self.splitter_12.setStyleSheet(_fromUtf8(""))
        self.splitter_12.setOrientation(QtCore.Qt.Vertical)
        self.splitter_12.setObjectName(_fromUtf8("splitter_12"))
        self.label_11 = QtGui.QLabel(self.splitter_12)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_10 = QtGui.QLabel(self.splitter_12)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_12 = QtGui.QLabel(self.splitter_12)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 360, 381, 80))
        self.groupBox_3.setStyleSheet(_fromUtf8("QGroupBox{\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-width : 1.2px;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"}"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.fileLocation = QtGui.QLineEdit(self.groupBox_3)
        self.fileLocation.setGeometry(QtCore.QRect(30, 30, 291, 21))
        self.fileLocation.setStyleSheet(_fromUtf8(""))
        self.fileLocation.setObjectName(_fromUtf8("fileLocation"))
        self.fileBrowseButton = QtGui.QPushButton(self.groupBox_3)
        self.fileBrowseButton.setGeometry(QtCore.QRect(330, 30, 31, 21))
        self.fileBrowseButton.setStyleSheet(_fromUtf8(""))
        self.fileBrowseButton.setObjectName(_fromUtf8("fileBrowseButton"))
        self.splitter_11 = QtGui.QSplitter(self.tab)
        self.splitter_11.setGeometry(QtCore.QRect(420, 270, 221, 171))
        self.splitter_11.setOrientation(QtCore.Qt.Vertical)
        self.splitter_11.setObjectName(_fromUtf8("splitter_11"))
        self.resetAllButton = QtGui.QPushButton(self.splitter_11)
        self.resetAllButton.setObjectName(_fromUtf8("resetAllButton"))
        self.simulateButton = QtGui.QPushButton(self.splitter_11)
        self.simulateButton.setObjectName(_fromUtf8("simulateButton"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Porter Simulation", None))
        self.groupBox.setTitle(_translate("Dialog", "Basic Settings", None))
        self.label_2.setText(_translate("Dialog", "Number of Porters", None))
        self.label_3.setText(_translate("Dialog", "Start Date", None))
        self.startDate.setDisplayFormat(_translate("Dialog", "dd-MM-yyyy", None))
        self.label_4.setText(_translate("Dialog", "End Date", None))
        self.endDate.setDisplayFormat(_translate("Dialog", "dd-MM-yyyy", None))
        self.label_5.setText(_translate("Dialog", "Job Distribution", None))
        self.jobDistribution.setItemText(0, _translate("Dialog", "Data Based", None))
        self.jobDistribution.setItemText(1, _translate("Dialog", "Poisson Distribution", None))
        self.jobDistribution.setItemText(2, _translate("Dialog", "Lagrange Distribution", None))
        self.label_6.setText(_translate("Dialog", "Job Intensity", None))
        self.jobIntensity.setItemText(0, _translate("Dialog", "High", None))
        self.jobIntensity.setItemText(1, _translate("Dialog", "Moderate", None))
        self.jobIntensity.setItemText(2, _translate("Dialog", "Low", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Compliance", None))
        self.label_7.setText(_translate("Dialog", "Correct Equipment Usage", None))
        self.label_8.setText(_translate("Dialog", "Patient Readiness", None))
        self.label_9.setText(_translate("Dialog", "Porter Wait Times", None))
        self.label_11.setText(_translate("Dialog", "%", None))
        self.label_10.setText(_translate("Dialog", "%", None))
        self.label_12.setText(_translate("Dialog", "min", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Data Source", None))
        self.fileBrowseButton.setText(_translate("Dialog", "...", None))
        self.resetAllButton.setText(_translate("Dialog", "Reset All", None))
        self.simulateButton.setText(_translate("Dialog", "Simulate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Basic Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Advanced Settings", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

