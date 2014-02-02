# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mockup.ui'
#
# Created: Sun Feb  2 09:39:26 2014
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
        Dialog.resize(640, 480)
        self.formLayout = QtGui.QFormLayout(Dialog)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(50)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.groupBox)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_2 = QtGui.QLabel(self.splitter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.splitter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.splitter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.splitter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.splitter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 5, 1)
        self.startDate = QtGui.QDateEdit(self.groupBox)
        self.startDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.startDate.setCalendarPopup(True)
        self.startDate.setCurrentSectionIndex(0)
        self.startDate.setObjectName(_fromUtf8("startDate"))
        self.gridLayout.addWidget(self.startDate, 1, 1, 1, 1)
        self.numberOfPorters = QtGui.QSpinBox(self.groupBox)
        self.numberOfPorters.setObjectName(_fromUtf8("numberOfPorters"))
        self.gridLayout.addWidget(self.numberOfPorters, 0, 1, 1, 1)
        self.endDate = QtGui.QDateEdit(self.groupBox)
        self.endDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.endDate.setCalendarPopup(True)
        self.endDate.setCurrentSectionIndex(0)
        self.endDate.setObjectName(_fromUtf8("endDate"))
        self.gridLayout.addWidget(self.endDate, 2, 1, 1, 1)
        self.jobIntensity = QtGui.QComboBox(self.groupBox)
        self.jobIntensity.setObjectName(_fromUtf8("jobIntensity"))
        self.jobIntensity.addItem(_fromUtf8(""))
        self.jobIntensity.addItem(_fromUtf8(""))
        self.jobIntensity.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.jobIntensity, 4, 1, 1, 1)
        self.jobDistribution = QtGui.QComboBox(self.groupBox)
        self.jobDistribution.setObjectName(_fromUtf8("jobDistribution"))
        self.jobDistribution.addItem(_fromUtf8(""))
        self.jobDistribution.addItem(_fromUtf8(""))
        self.jobDistribution.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.jobDistribution, 3, 1, 1, 1)
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.groupBox)
        self.simulateButton = QtGui.QPushButton(Dialog)
        self.simulateButton.setObjectName(_fromUtf8("simulateButton"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.simulateButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Porter Simulation", None))
        self.groupBox.setTitle(_translate("Dialog", "Basic Settings", None))
        self.label_2.setText(_translate("Dialog", "Number of Porters", None))
        self.label_3.setText(_translate("Dialog", "Start Date", None))
        self.label_4.setText(_translate("Dialog", "End Date", None))
        self.label_5.setText(_translate("Dialog", "Job Distribution", None))
        self.label_6.setText(_translate("Dialog", "Job Intensity", None))
        self.startDate.setDisplayFormat(_translate("Dialog", "dd-MM-yyyy", None))
        self.endDate.setDisplayFormat(_translate("Dialog", "dd-MM-yyyy", None))
        self.jobIntensity.setItemText(0, _translate("Dialog", "High", None))
        self.jobIntensity.setItemText(1, _translate("Dialog", "Moderate", None))
        self.jobIntensity.setItemText(2, _translate("Dialog", "Low", None))
        self.jobDistribution.setItemText(0, _translate("Dialog", "Data Based", None))
        self.jobDistribution.setItemText(1, _translate("Dialog", "Poisson Distribution", None))
        self.jobDistribution.setItemText(2, _translate("Dialog", "Lagrange Distribution", None))
        self.simulateButton.setText(_translate("Dialog", "Simulate", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

