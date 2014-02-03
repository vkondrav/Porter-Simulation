#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mockup.ui'
#
# Created: Mon Feb  3 16:12:12 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

import os
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

    appFactorInitial = "1";

    ajbInitial = list()
    wjlInitial = list()
    pmvInitial = list()
    avInitial = list()

    ajb = list()
    wjl = list()
    pmv = list()
    av = list()

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(772, 638)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 358, 57))
        font = QtGui.QFont()
        font.setPointSize(28)

        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 60, 751, 561))
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
        self.startDate.setDateTime(QtCore.QDateTime.currentDateTime())
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
        self.endDate.setDateTime(QtCore.QDateTime.currentDateTime())
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
        self.splitter_11.setGeometry(QtCore.QRect(20, 450, 381, 41))
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName(_fromUtf8("splitter_11"))

        self.resetAllButton = QtGui.QPushButton(self.splitter_11)
        self.resetAllButton.setObjectName(_fromUtf8("resetAllButton"))

        self.simulateButton = QtGui.QPushButton(self.splitter_11)
        self.simulateButton.setObjectName(_fromUtf8("simulateButton"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 20, 711, 491))
        self.groupBox_4.setStyleSheet(_fromUtf8("QGroupBox{\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-width : 1.2px;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QSpinBox,QDateEdit,QComboBox,QDoubleSpinBox\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"}"))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 70, 691, 91))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))

        self.splitter_23 = QtGui.QSplitter(self.groupBox_5)
        self.splitter_23.setGeometry(QtCore.QRect(20, 30, 651, 51))
        self.splitter_23.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_23.setObjectName(_fromUtf8("splitter_23"))
        self.splitter_22 = QtGui.QSplitter(self.splitter_23)
        self.splitter_22.setOrientation(QtCore.Qt.Vertical)
        self.splitter_22.setObjectName(_fromUtf8("splitter_22"))

        self.label_19 = QtGui.QLabel(self.splitter_22)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.splitter_22)
        self.label_20.setObjectName(_fromUtf8("label_20"))

        self.splitter_13 = QtGui.QSplitter(self.splitter_23)
        self.splitter_13.setOrientation(QtCore.Qt.Vertical)
        self.splitter_13.setObjectName(_fromUtf8("splitter_13"))

        self.label_21 = QtGui.QLabel(self.splitter_13)
        self.label_21.setObjectName(_fromUtf8("label_21"))

        self.ajb1 = QtGui.QDoubleSpinBox(self.splitter_13)
        self.ajb1.setObjectName(_fromUtf8("ajb1"))
        self.ajb.append(self.ajb1)

        self.splitter_14 = QtGui.QSplitter(self.splitter_23)
        self.splitter_14.setOrientation(QtCore.Qt.Vertical)
        self.splitter_14.setObjectName(_fromUtf8("splitter_14"))

        self.label_22 = QtGui.QLabel(self.splitter_14)
        self.label_22.setObjectName(_fromUtf8("label_22"))

        self.ajb2 = QtGui.QDoubleSpinBox(self.splitter_14)
        self.ajb2.setObjectName(_fromUtf8("ajb2"))
        self.ajb.append(self.ajb2)

        self.splitter_15 = QtGui.QSplitter(self.splitter_23)
        self.splitter_15.setOrientation(QtCore.Qt.Vertical)
        self.splitter_15.setObjectName(_fromUtf8("splitter_15"))

        self.label_23 = QtGui.QLabel(self.splitter_15)
        self.label_23.setObjectName(_fromUtf8("label_23"))

        self.ajb3 = QtGui.QDoubleSpinBox(self.splitter_15)
        self.ajb3.setObjectName(_fromUtf8("ajb3"))
        self.ajb.append(self.ajb3)

        self.splitter_16 = QtGui.QSplitter(self.splitter_23)
        self.splitter_16.setOrientation(QtCore.Qt.Vertical)
        self.splitter_16.setObjectName(_fromUtf8("splitter_16"))

        self.label_24 = QtGui.QLabel(self.splitter_16)
        self.label_24.setObjectName(_fromUtf8("label_24"))

        self.ajb4 = QtGui.QDoubleSpinBox(self.splitter_16)
        self.ajb4.setObjectName(_fromUtf8("ajb4"))
        self.ajb.append(self.ajb4)

        self.splitter_17 = QtGui.QSplitter(self.splitter_23)
        self.splitter_17.setOrientation(QtCore.Qt.Vertical)
        self.splitter_17.setObjectName(_fromUtf8("splitter_17"))

        self.label_25 = QtGui.QLabel(self.splitter_17)
        self.label_25.setObjectName(_fromUtf8("label_25"))

        self.ajb5 = QtGui.QDoubleSpinBox(self.splitter_17)
        self.ajb5.setObjectName(_fromUtf8("ajb5"))
        self.ajb.append(self.ajb5)

        self.splitter_18 = QtGui.QSplitter(self.splitter_23)
        self.splitter_18.setOrientation(QtCore.Qt.Vertical)
        self.splitter_18.setObjectName(_fromUtf8("splitter_18"))

        self.label_26 = QtGui.QLabel(self.splitter_18)
        self.label_26.setObjectName(_fromUtf8("label_26"))

        self.ajb6 = QtGui.QDoubleSpinBox(self.splitter_18)
        self.ajb6.setObjectName(_fromUtf8("ajb6"))
        self.ajb.append(self.ajb6)

        self.splitter_19 = QtGui.QSplitter(self.splitter_23)
        self.splitter_19.setOrientation(QtCore.Qt.Vertical)
        self.splitter_19.setObjectName(_fromUtf8("splitter_19"))

        self.label_27 = QtGui.QLabel(self.splitter_19)
        self.label_27.setObjectName(_fromUtf8("label_27"))

        self.ajb7 = QtGui.QDoubleSpinBox(self.splitter_19)
        self.ajb7.setObjectName(_fromUtf8("ajb7"))
        self.ajb.append(self.ajb7)

        self.splitter_20 = QtGui.QSplitter(self.splitter_23)
        self.splitter_20.setOrientation(QtCore.Qt.Vertical)
        self.splitter_20.setObjectName(_fromUtf8("splitter_20"))

        self.label_28 = QtGui.QLabel(self.splitter_20)
        self.label_28.setObjectName(_fromUtf8("label_28"))

        self.ajb8 = QtGui.QDoubleSpinBox(self.splitter_20)
        self.ajb8.setObjectName(_fromUtf8("ajb8"))
        self.ajb.append(self.ajb8)

        self.splitter_21 = QtGui.QSplitter(self.splitter_23)
        self.splitter_21.setOrientation(QtCore.Qt.Vertical)
        self.splitter_21.setObjectName(_fromUtf8("splitter_21"))

        self.label_29 = QtGui.QLabel(self.splitter_21)
        self.label_29.setObjectName(_fromUtf8("label_29"))

        self.ajb9 = QtGui.QDoubleSpinBox(self.splitter_21)
        self.ajb9.setObjectName(_fromUtf8("ajb9"))
        self.ajb.append(self.ajb9)

        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 270, 691, 91))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))

        self.splitter_45 = QtGui.QSplitter(self.groupBox_7)
        self.splitter_45.setGeometry(QtCore.QRect(555, 30, 16, 16))
        self.splitter_45.setOrientation(QtCore.Qt.Vertical)
        self.splitter_45.setObjectName(_fromUtf8("splitter_45"))
        self.splitter_46 = QtGui.QSplitter(self.groupBox_7)
        self.splitter_46.setGeometry(QtCore.QRect(561, 30, 16, 16))
        self.splitter_46.setOrientation(QtCore.Qt.Vertical)
        self.splitter_46.setObjectName(_fromUtf8("splitter_46"))
        self.splitter_36 = QtGui.QSplitter(self.groupBox_7)
        self.splitter_36.setGeometry(QtCore.QRect(20, 30, 651, 51))
        self.splitter_36.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_36.setObjectName(_fromUtf8("splitter_36"))
        self.splitter_37 = QtGui.QSplitter(self.splitter_36)
        self.splitter_37.setOrientation(QtCore.Qt.Vertical)
        self.splitter_37.setObjectName(_fromUtf8("splitter_37"))

        self.label_41 = QtGui.QLabel(self.splitter_37)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.label_42 = QtGui.QLabel(self.splitter_37)
        self.label_42.setObjectName(_fromUtf8("label_42"))

        self.splitter_38 = QtGui.QSplitter(self.splitter_36)
        self.splitter_38.setOrientation(QtCore.Qt.Vertical)
        self.splitter_38.setObjectName(_fromUtf8("splitter_38"))

        self.label_43 = QtGui.QLabel(self.splitter_38)
        self.label_43.setObjectName(_fromUtf8("label_43"))

        self.pmv1 = QtGui.QDoubleSpinBox(self.splitter_38)
        self.pmv1.setObjectName(_fromUtf8("pmv1"))
        self.pmv.append(self.pmv1)

        self.splitter_39 = QtGui.QSplitter(self.splitter_36)
        self.splitter_39.setOrientation(QtCore.Qt.Vertical)
        self.splitter_39.setObjectName(_fromUtf8("splitter_39"))

        self.label_44 = QtGui.QLabel(self.splitter_39)
        self.label_44.setObjectName(_fromUtf8("label_44"))

        self.pmv2 = QtGui.QDoubleSpinBox(self.splitter_39)
        self.pmv2.setObjectName(_fromUtf8("pmv2"))
        self.pmv.append(self.pmv2)

        self.splitter_40 = QtGui.QSplitter(self.splitter_36)
        self.splitter_40.setOrientation(QtCore.Qt.Vertical)
        self.splitter_40.setObjectName(_fromUtf8("splitter_40"))

        self.label_45 = QtGui.QLabel(self.splitter_40)
        self.label_45.setObjectName(_fromUtf8("label_45"))

        self.pmv3 = QtGui.QDoubleSpinBox(self.splitter_40)
        self.pmv3.setObjectName(_fromUtf8("pmv3"))
        self.pmv.append(self.pmv3)

        self.splitter_41 = QtGui.QSplitter(self.splitter_36)
        self.splitter_41.setOrientation(QtCore.Qt.Vertical)
        self.splitter_41.setObjectName(_fromUtf8("splitter_41"))

        self.label_46 = QtGui.QLabel(self.splitter_41)
        self.label_46.setObjectName(_fromUtf8("label_46"))

        self.pmv4 = QtGui.QDoubleSpinBox(self.splitter_41)
        self.pmv4.setObjectName(_fromUtf8("pmv4"))
        self.pmv.append(self.pmv4)

        self.splitter_42 = QtGui.QSplitter(self.splitter_36)
        self.splitter_42.setOrientation(QtCore.Qt.Vertical)
        self.splitter_42.setObjectName(_fromUtf8("splitter_42"))

        self.label_47 = QtGui.QLabel(self.splitter_42)
        self.label_47.setObjectName(_fromUtf8("label_47"))

        self.pmv5 = QtGui.QDoubleSpinBox(self.splitter_42)
        self.pmv5.setObjectName(_fromUtf8("pmv5"))
        self.pmv.append(self.pmv5)

        self.splitter_43 = QtGui.QSplitter(self.splitter_36)
        self.splitter_43.setOrientation(QtCore.Qt.Vertical)
        self.splitter_43.setObjectName(_fromUtf8("splitter_43"))

        self.label_48 = QtGui.QLabel(self.splitter_43)
        self.label_48.setObjectName(_fromUtf8("label_48"))

        self.pmv6 = QtGui.QDoubleSpinBox(self.splitter_43)
        self.pmv6.setObjectName(_fromUtf8("pmv6"))
        self.pmv.append(self.pmv6)

        self.splitter_44 = QtGui.QSplitter(self.splitter_36)
        self.splitter_44.setOrientation(QtCore.Qt.Vertical)
        self.splitter_44.setObjectName(_fromUtf8("splitter_44"))

        self.label_49 = QtGui.QLabel(self.splitter_44)
        self.label_49.setObjectName(_fromUtf8("label_49"))

        self.pmv7 = QtGui.QDoubleSpinBox(self.splitter_44)
        self.pmv7.setObjectName(_fromUtf8("pmv7"))

        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 380, 691, 91))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))

        self.splitter_56 = QtGui.QSplitter(self.groupBox_8)
        self.splitter_56.setGeometry(QtCore.QRect(555, 30, 16, 16))
        self.splitter_56.setOrientation(QtCore.Qt.Vertical)
        self.splitter_56.setObjectName(_fromUtf8("splitter_56"))

        self.splitter_57 = QtGui.QSplitter(self.groupBox_8)
        self.splitter_57.setGeometry(QtCore.QRect(561, 30, 16, 16))
        self.splitter_57.setOrientation(QtCore.Qt.Vertical)
        self.splitter_57.setObjectName(_fromUtf8("splitter_57"))

        self.splitter_47 = QtGui.QSplitter(self.groupBox_8)
        self.splitter_47.setGeometry(QtCore.QRect(20, 30, 651, 51))
        self.splitter_47.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_47.setObjectName(_fromUtf8("splitter_47"))

        self.splitter_48 = QtGui.QSplitter(self.splitter_47)
        self.splitter_48.setOrientation(QtCore.Qt.Vertical)
        self.splitter_48.setObjectName(_fromUtf8("splitter_48"))

        self.label_50 = QtGui.QLabel(self.splitter_48)
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.label_51 = QtGui.QLabel(self.splitter_48)
        self.label_51.setObjectName(_fromUtf8("label_51"))

        self.splitter_49 = QtGui.QSplitter(self.splitter_47)
        self.splitter_49.setOrientation(QtCore.Qt.Vertical)
        self.splitter_49.setObjectName(_fromUtf8("splitter_49"))

        self.label_52 = QtGui.QLabel(self.splitter_49)
        self.label_52.setObjectName(_fromUtf8("label_52"))

        self.av1 = QtGui.QDoubleSpinBox(self.splitter_49)
        self.av1.setObjectName(_fromUtf8("av1"))
        self.av.append(self.av1)

        self.splitter_50 = QtGui.QSplitter(self.splitter_47)
        self.splitter_50.setOrientation(QtCore.Qt.Vertical)
        self.splitter_50.setObjectName(_fromUtf8("splitter_50"))

        self.label_53 = QtGui.QLabel(self.splitter_50)
        self.label_53.setObjectName(_fromUtf8("label_53"))

        self.av2 = QtGui.QDoubleSpinBox(self.splitter_50)
        self.av2.setObjectName(_fromUtf8("av2"))
        self.av.append(self.av2)

        self.splitter_51 = QtGui.QSplitter(self.splitter_47)
        self.splitter_51.setOrientation(QtCore.Qt.Vertical)
        self.splitter_51.setObjectName(_fromUtf8("splitter_51"))

        self.label_54 = QtGui.QLabel(self.splitter_51)
        self.label_54.setObjectName(_fromUtf8("label_54"))

        self.av3 = QtGui.QDoubleSpinBox(self.splitter_51)
        self.av3.setObjectName(_fromUtf8("av3"))

        self.splitter_52 = QtGui.QSplitter(self.splitter_47)
        self.splitter_52.setOrientation(QtCore.Qt.Vertical)
        self.splitter_52.setObjectName(_fromUtf8("splitter_52"))

        self.label_55 = QtGui.QLabel(self.splitter_52)
        self.label_55.setObjectName(_fromUtf8("label_55"))

        self.av4 = QtGui.QDoubleSpinBox(self.splitter_52)
        self.av4.setObjectName(_fromUtf8("av4"))
        self.av.append(self.av4)

        self.splitter_53 = QtGui.QSplitter(self.splitter_47)
        self.splitter_53.setOrientation(QtCore.Qt.Vertical)
        self.splitter_53.setObjectName(_fromUtf8("splitter_53"))

        self.label_56 = QtGui.QLabel(self.splitter_53)
        self.label_56.setObjectName(_fromUtf8("label_56"))

        self.av5 = QtGui.QDoubleSpinBox(self.splitter_53)
        self.av5.setObjectName(_fromUtf8("av5"))
        self.av.append(self.av5)

        self.splitter_54 = QtGui.QSplitter(self.splitter_47)
        self.splitter_54.setOrientation(QtCore.Qt.Vertical)
        self.splitter_54.setObjectName(_fromUtf8("splitter_54"))

        self.label_57 = QtGui.QLabel(self.splitter_54)
        self.label_57.setObjectName(_fromUtf8("label_57"))

        self.av6 = QtGui.QDoubleSpinBox(self.splitter_54)
        self.av6.setObjectName(_fromUtf8("av6"))
        self.av.append(self.av6)

        self.splitter_55 = QtGui.QSplitter(self.splitter_47)
        self.splitter_55.setOrientation(QtCore.Qt.Vertical)
        self.splitter_55.setObjectName(_fromUtf8("splitter_55"))

        self.label_58 = QtGui.QLabel(self.splitter_55)
        self.label_58.setObjectName(_fromUtf8("label_58"))

        self.av7 = QtGui.QDoubleSpinBox(self.splitter_55)
        self.av7.setObjectName(_fromUtf8("av7"))
        self.av.append(self.av7)

        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 170, 691, 91))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))

        self.splitter_25 = QtGui.QSplitter(self.groupBox_6)
        self.splitter_25.setGeometry(QtCore.QRect(20, 30, 651, 51))
        self.splitter_25.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_25.setObjectName(_fromUtf8("splitter_25"))
        self.splitter_26 = QtGui.QSplitter(self.splitter_25)
        self.splitter_26.setOrientation(QtCore.Qt.Vertical)
        self.splitter_26.setObjectName(_fromUtf8("splitter_26"))

        self.label_30 = QtGui.QLabel(self.splitter_26)
        self.label_30.setObjectName(_fromUtf8("label_30"))        
        self.label_31 = QtGui.QLabel(self.splitter_26)
        self.label_31.setObjectName(_fromUtf8("label_31"))

        self.splitter_27 = QtGui.QSplitter(self.splitter_25)
        self.splitter_27.setOrientation(QtCore.Qt.Vertical)
        self.splitter_27.setObjectName(_fromUtf8("splitter_27"))

        self.label_32 = QtGui.QLabel(self.splitter_27)
        self.label_32.setObjectName(_fromUtf8("label_32"))

        self.wjl1 = QtGui.QDoubleSpinBox(self.splitter_27)
        self.wjl1.setObjectName(_fromUtf8("wjl1"))
        self.wjl.append(self.wjl1)

        self.splitter_28 = QtGui.QSplitter(self.splitter_25)
        self.splitter_28.setOrientation(QtCore.Qt.Vertical)
        self.splitter_28.setObjectName(_fromUtf8("splitter_28"))

        self.label_33 = QtGui.QLabel(self.splitter_28)
        self.label_33.setObjectName(_fromUtf8("label_33"))

        self.wjl2 = QtGui.QDoubleSpinBox(self.splitter_28)
        self.wjl2.setObjectName(_fromUtf8("wjl2"))
        self.wjl.append(self.wjl2)

        self.splitter_29 = QtGui.QSplitter(self.splitter_25)
        self.splitter_29.setOrientation(QtCore.Qt.Vertical)
        self.splitter_29.setObjectName(_fromUtf8("splitter_29"))

        self.label_34 = QtGui.QLabel(self.splitter_29)
        self.label_34.setObjectName(_fromUtf8("label_34"))

        self.wjl3 = QtGui.QDoubleSpinBox(self.splitter_29)
        self.wjl3.setObjectName(_fromUtf8("wjl3"))
        self.wjl.append(self.wjl3)

        self.splitter_30 = QtGui.QSplitter(self.splitter_25)
        self.splitter_30.setOrientation(QtCore.Qt.Vertical)
        self.splitter_30.setObjectName(_fromUtf8("splitter_30"))

        self.label_35 = QtGui.QLabel(self.splitter_30)
        self.label_35.setObjectName(_fromUtf8("label_35"))

        self.wjl4 = QtGui.QDoubleSpinBox(self.splitter_30)
        self.wjl4.setObjectName(_fromUtf8("wjl4"))
        self.wjl.append(self.wjl4)

        self.splitter_31 = QtGui.QSplitter(self.splitter_25)
        self.splitter_31.setOrientation(QtCore.Qt.Vertical)
        self.splitter_31.setObjectName(_fromUtf8("splitter_31"))

        self.label_36 = QtGui.QLabel(self.splitter_31)
        self.label_36.setObjectName(_fromUtf8("label_36"))

        self.wjl5 = QtGui.QDoubleSpinBox(self.splitter_31)
        self.wjl5.setObjectName(_fromUtf8("wjl5"))
        self.wjl.append(self.wjl5)

        self.splitter_32 = QtGui.QSplitter(self.splitter_25)
        self.splitter_32.setOrientation(QtCore.Qt.Vertical)
        self.splitter_32.setObjectName(_fromUtf8("splitter_32"))

        self.label_37 = QtGui.QLabel(self.splitter_32)
        self.label_37.setObjectName(_fromUtf8("label_37"))

        self.wjl6 = QtGui.QDoubleSpinBox(self.splitter_32)
        self.wjl6.setObjectName(_fromUtf8("wjl6"))
        self.wjl.append(self.wjl6)

        self.splitter_33 = QtGui.QSplitter(self.splitter_25)
        self.splitter_33.setOrientation(QtCore.Qt.Vertical)
        self.splitter_33.setObjectName(_fromUtf8("splitter_33"))

        self.label_38 = QtGui.QLabel(self.splitter_33)
        self.label_38.setObjectName(_fromUtf8("label_38"))

        self.wjl7 = QtGui.QDoubleSpinBox(self.splitter_33)
        self.wjl7.setObjectName(_fromUtf8("wjl7"))
        self.wjl.append(self.wjl7)

        self.splitter_34 = QtGui.QSplitter(self.splitter_25)
        self.splitter_34.setOrientation(QtCore.Qt.Vertical)
        self.splitter_34.setObjectName(_fromUtf8("splitter_34"))

        self.label_39 = QtGui.QLabel(self.splitter_34)
        self.label_39.setObjectName(_fromUtf8("label_39"))

        self.wjl8 = QtGui.QDoubleSpinBox(self.splitter_34)
        self.wjl8.setObjectName(_fromUtf8("wjl8"))
        self.wjl.append(self.wjl8)

        self.splitter_35 = QtGui.QSplitter(self.splitter_25)
        self.splitter_35.setOrientation(QtCore.Qt.Vertical)
        self.splitter_35.setObjectName(_fromUtf8("splitter_35"))

        self.label_40 = QtGui.QLabel(self.splitter_35)
        self.label_40.setObjectName(_fromUtf8("label_40"))

        self.wjl9 = QtGui.QDoubleSpinBox(self.splitter_35)
        self.wjl9.setObjectName(_fromUtf8("wjl9"))
        self.wjl.append(self.wjl9)

        self.resetAllDispatch = QtGui.QPushButton(self.groupBox_4)
        self.resetAllDispatch.setGeometry(QtCore.QRect(580, 20, 111, 28))
        self.resetAllDispatch.setObjectName(_fromUtf8("resetAllDispatch"))

        self.splitter_24 = QtGui.QSplitter(self.groupBox_4)
        self.splitter_24.setGeometry(QtCore.QRect(20, 20, 361, 27))
        self.splitter_24.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_24.setObjectName(_fromUtf8("splitter_24"))

        self.label_13 = QtGui.QLabel(self.splitter_24)
        self.label_13.setObjectName(_fromUtf8("label_13"))

        self.appFactor = QtGui.QSlider(self.splitter_24)
        self.appFactor.setMinimum(10)
        self.appFactor.setMaximum(30)
        self.appFactor.setOrientation(QtCore.Qt.Horizontal)
        self.appFactor.setTickPosition(QtGui.QSlider.TicksAbove)
        self.appFactor.setTickInterval(1)
        self.appFactor.setObjectName(_fromUtf8("appFactor"))

        self.appFactorValue = QtGui.QLabel(self.splitter_24)
        self.appFactorValue.setObjectName(_fromUtf8("appFactorValue"))

        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.hhs = QtGui.QLabel(Dialog)
        self.hhs.setGeometry(QtCore.QRect(630, 10, 131, 61))
        self.hhs.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"border: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(141, 141, 141);\n"
""))
        self.hhs.setText(_fromUtf8(""))
        self.hhs.setPixmap(QtGui.QPixmap(os.getcwd() + "/hhs.png"))
        self.hhs.setScaledContents(True)
        self.hhs.setObjectName(_fromUtf8("hhs"))

        self.retranslateUi(Dialog)
        self.recordInitialDispatch()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        ####EVENTS####
        self.simulateButton.clicked.connect(self.buttonClicked)
        self.resetAllButton.clicked.connect(self.resetAllButtonClicked)
        self.fileBrowseButton.clicked.connect(self.fileBrowseButtonClicked)
        self.resetAllDispatch.clicked.connect(self.resetAllDispatchClicked)
        self.appFactor.valueChanged[int].connect(self.appFactorChange)

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
        self.groupBox_4.setTitle(_translate("Dialog", "Dispatcher", None))
        self.groupBox_5.setTitle(_translate("Dialog", "Automatic Job Priority Values", None))
        self.label_19.setText(_translate("Dialog", "Job Priority", None))
        self.label_20.setText(_translate("Dialog", "Minutes", None))
        self.label_21.setText(_translate("Dialog", "1", None))
        self.label_22.setText(_translate("Dialog", "2", None))
        self.label_23.setText(_translate("Dialog", "3", None))
        self.label_24.setText(_translate("Dialog", "4", None))
        self.label_25.setText(_translate("Dialog", "5", None))
        self.label_26.setText(_translate("Dialog", "6", None))
        self.label_27.setText(_translate("Dialog", "7", None))
        self.label_28.setText(_translate("Dialog", "8", None))
        self.label_29.setText(_translate("Dialog", "9", None))
        self.groupBox_7.setTitle(_translate("Dialog", "Proximity Match Value", None))
        self.label_41.setText(_translate("Dialog", "Section", None))
        self.label_42.setText(_translate("Dialog", "Weight", None))
        self.label_43.setText(_translate("Dialog", "Location", None))
        self.label_44.setText(_translate("Dialog", "Zone", None))
        self.label_45.setText(_translate("Dialog", "Unit", None))
        self.label_46.setText(_translate("Dialog", "Section", None))
        self.label_47.setText(_translate("Dialog", "Floor", None))
        self.label_48.setText(_translate("Dialog", "Building", None))
        self.label_49.setText(_translate("Dialog", "Campus", None))
        self.groupBox_8.setTitle(_translate("Dialog", "Autolocation Values", None))
        self.label_50.setText(_translate("Dialog", "Section", None))
        self.label_51.setText(_translate("Dialog", "Weight", None))
        self.label_52.setText(_translate("Dialog", "Location", None))
        self.label_53.setText(_translate("Dialog", "Zone", None))
        self.label_54.setText(_translate("Dialog", "Unit", None))
        self.label_55.setText(_translate("Dialog", "Section", None))
        self.label_56.setText(_translate("Dialog", "Floor", None))
        self.label_57.setText(_translate("Dialog", "Building", None))
        self.label_58.setText(_translate("Dialog", "Campus", None))
        self.groupBox_6.setTitle(_translate("Dialog", "Weighted Job List", None))
        self.label_30.setText(_translate("Dialog", "Job Priority", None))
        self.label_31.setText(_translate("Dialog", "Weight", None))
        self.label_32.setText(_translate("Dialog", "1", None))
        self.label_33.setText(_translate("Dialog", "2", None))
        self.label_34.setText(_translate("Dialog", "3", None))
        self.label_35.setText(_translate("Dialog", "4", None))
        self.label_36.setText(_translate("Dialog", "5", None))
        self.label_37.setText(_translate("Dialog", "6", None))
        self.label_38.setText(_translate("Dialog", "7", None))
        self.label_39.setText(_translate("Dialog", "8", None))
        self.label_40.setText(_translate("Dialog", "9", None))
        self.resetAllDispatch.setText(_translate("Dialog", "Reset All", None))
        self.label_13.setText(_translate("Dialog", "Apointment Factor", None))

        self.appFactorValue.setText(_translate("Dialog", "0", None))
        self.appFactorInitial = self.appFactorValue.text()

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Advanced Settings", None))

    def buttonClicked(self):
        print (self.jobDistribution.currentText())

    def resetAllButtonClicked(self):
        self.numberOfPorters.setProperty("value", 10)
        self.startDate.setDateTime(QtCore.QDateTime.currentDateTime())
        self.endDate.setDateTime(QtCore.QDateTime.currentDateTime())
        self.jobDistribution.setItemText(0, _translate("Dialog", "Data Based", None))
        self.jobIntensity.setItemText(0, _translate("Dialog", "High", None))
        self.correctEquipment.setProperty("value", 80.0)
        self.patientReadiness.setProperty("value", 80.0)
        self.porterWait.setProperty("value", 5.0)
        self.fileLocation.setText("")

    def fileBrowseButtonClicked(self):
        fname = QtGui.QFileDialog.getOpenFileName(Dialog, 'Open file', os.getcwd(), "CSV Files (.csv)")
                
        self.fileLocation.setText(fname)

    def appFactorChange(self,value):
        self.appFactorValue.setText(str(value/100))

    def recordInitialDispatch(self):
        
        for i in self.ajb:
            self.ajbInitial.append(i.value())

        for i in self.wjl:
            self.wjlInitial.append(i.value())

        for i in self.pmv:
            self.pmvInitial.append(i.value())

        for i in self.av:
            self.avInitial.append(i.value())

    def resetAllDispatchClicked(self):
        self.appFactorValue.setText(self.appFactorInitial)

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



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
