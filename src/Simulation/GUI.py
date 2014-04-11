#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mockup.ui'
#
# Created: Thu Apr 10 20:28:49 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import GUI_functions as guif
import os
import sys

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

    fun = guif.functions()

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(772, 638)

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 358, 57))
        font = QtGui.QFont()
        font.setPointSize(28)

        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.notUsed = QtGui.QTabWidget(Dialog)
        self.notUsed.setEnabled(True)
        self.notUsed.setGeometry(QtCore.QRect(10, 60, 751, 561))
        self.notUsed.setAutoFillBackground(False)
        self.notUsed.setStyleSheet(_fromUtf8("background-color: rgb(216, 216, 216);"))
        self.notUsed.setObjectName(_fromUtf8("notUsed"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 321, 271))
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox{\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-width : 1.2px;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QSpinBox,QDateEdit,QComboBox,QLineEdit,QDoubleSpinBox\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"}"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.splitter_6 = QtGui.QSplitter(self.groupBox)
        self.splitter_6.setGeometry(QtCore.QRect(50, 90, 241, 51))
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName(_fromUtf8("splitter_6"))
        self.splitter_5 = QtGui.QSplitter(self.splitter_6)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.label_6 = QtGui.QLabel(self.splitter_5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_9 = QtGui.QLabel(self.splitter_5)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.splitter_4 = QtGui.QSplitter(self.splitter_6)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_4)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.simDuration = QtGui.QDoubleSpinBox(self.splitter_2)
        self.simDuration.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.simDuration.setDecimals(2)
        self.simDuration.setMinimum(1.0)
        self.simDuration.setMaximum(7.0)
        self.simDuration.setObjectName(_fromUtf8("simDuration"))
        self.porterWait = QtGui.QDoubleSpinBox(self.splitter_2)
        self.porterWait.setEnabled(True)
        self.porterWait.setStyleSheet(_fromUtf8(""))
        self.porterWait.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.porterWait.setMinimum(0.0)
        self.porterWait.setMaximum(60.0)
        self.porterWait.setProperty("value", 5.0)
        self.porterWait.setObjectName(_fromUtf8("porterWait"))
        self.splitter_3 = QtGui.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.label_15 = QtGui.QLabel(self.splitter_3)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_12 = QtGui.QLabel(self.splitter_3)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.splitter_8 = QtGui.QSplitter(self.groupBox)
        self.splitter_8.setGeometry(QtCore.QRect(50, 150, 241, 51))
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName(_fromUtf8("splitter_8"))
        self.splitter_7 = QtGui.QSplitter(self.splitter_8)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName(_fromUtf8("splitter_7"))
        self.label_2 = QtGui.QLabel(self.splitter_7)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.splitter_7)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.splitter = QtGui.QSplitter(self.splitter_8)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.jobFlow = QtGui.QComboBox(self.splitter)
        self.jobFlow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.jobFlow.setObjectName(_fromUtf8("jobFlow"))
        self.jobFlow.addItem(_fromUtf8(""))
        self.jobFlow.addItem(_fromUtf8(""))
        self.jobFlow.addItem(_fromUtf8(""))
        self.dayOffset = QtGui.QComboBox(self.splitter)
        self.dayOffset.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.dayOffset.setObjectName(_fromUtf8("dayOffset"))
        self.dayOffset.addItem(_fromUtf8(""))
        self.dayOffset.addItem(_fromUtf8(""))
        self.dayOffset.addItem(_fromUtf8(""))
        self.dayOffset.addItem(_fromUtf8(""))
        self.dayOffset.addItem(_fromUtf8(""))
        self.dayOffset.addItem(_fromUtf8(""))
        self.dayOffset.addItem(_fromUtf8(""))
        self.splitter_11 = QtGui.QSplitter(self.tab)
        self.splitter_11.setGeometry(QtCore.QRect(160, 290, 381, 41))
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName(_fromUtf8("splitter_11"))
        self.resetAllButton = QtGui.QPushButton(self.splitter_11)
        self.resetAllButton.setObjectName(_fromUtf8("resetAllButton"))
        self.simulateButton = QtGui.QPushButton(self.splitter_11)
        self.simulateButton.setObjectName(_fromUtf8("simulateButton"))
        self.groupBox_9 = QtGui.QGroupBox(self.tab)
        self.groupBox_9.setGeometry(QtCore.QRect(350, 10, 381, 271))
        self.groupBox_9.setStyleSheet(_fromUtf8("QGroupBox{\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-width : 1.2px;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QSpinBox,QDateEdit,QComboBox,QLineEdit\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"}"))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.fileLocation = QtGui.QLineEdit(self.groupBox_9)
        self.fileLocation.setEnabled(True)
        self.fileLocation.setGeometry(QtCore.QRect(20, 90, 291, 21))
        self.fileLocation.setStyleSheet(_fromUtf8(""))
        self.fileLocation.setObjectName(_fromUtf8("fileLocation"))
        self.fileBrowseButton = QtGui.QPushButton(self.groupBox_9)
        self.fileBrowseButton.setEnabled(True)
        self.fileBrowseButton.setGeometry(QtCore.QRect(320, 90, 31, 21))
        self.fileBrowseButton.setStyleSheet(_fromUtf8(""))
        self.fileBrowseButton.setObjectName(_fromUtf8("fileBrowseButton"))
        self.label_18 = QtGui.QLabel(self.groupBox_9)
        self.label_18.setGeometry(QtCore.QRect(20, 70, 141, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.fileLocation_2 = QtGui.QLineEdit(self.groupBox_9)
        self.fileLocation_2.setEnabled(True)
        self.fileLocation_2.setGeometry(QtCore.QRect(20, 140, 291, 21))
        self.fileLocation_2.setStyleSheet(_fromUtf8(""))
        self.fileLocation_2.setObjectName(_fromUtf8("fileLocation_2"))
        self.fileBrowseButton_2 = QtGui.QPushButton(self.groupBox_9)
        self.fileBrowseButton_2.setGeometry(QtCore.QRect(320, 140, 31, 21))
        self.fileBrowseButton_2.setStyleSheet(_fromUtf8(""))
        self.fileBrowseButton_2.setObjectName(_fromUtf8("fileBrowseButton_2"))
        self.label_60 = QtGui.QLabel(self.groupBox_9)
        self.label_60.setGeometry(QtCore.QRect(20, 120, 141, 16))
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.fileLocation_3 = QtGui.QLineEdit(self.groupBox_9)
        self.fileLocation_3.setEnabled(True)
        self.fileLocation_3.setGeometry(QtCore.QRect(20, 190, 291, 21))
        self.fileLocation_3.setStyleSheet(_fromUtf8(""))
        self.fileLocation_3.setObjectName(_fromUtf8("fileLocation_3"))
        self.label_63 = QtGui.QLabel(self.groupBox_9)
        self.label_63.setGeometry(QtCore.QRect(20, 170, 141, 16))
        self.label_63.setObjectName(_fromUtf8("label_63"))
        self.fileBrowseButton_3 = QtGui.QPushButton(self.groupBox_9)
        self.fileBrowseButton_3.setGeometry(QtCore.QRect(320, 190, 31, 21))
        self.fileBrowseButton_3.setStyleSheet(_fromUtf8(""))
        self.fileBrowseButton_3.setObjectName(_fromUtf8("fileBrowseButton_3"))
        self.output = QtGui.QTextEdit(self.tab)
        self.output.setGeometry(QtCore.QRect(10, 340, 731, 181))
        self.output.setStyleSheet(_fromUtf8("QTextEdit\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"}"))
        self.output.setObjectName(_fromUtf8("output"))
        self.notUsed.addTab(self.tab, _fromUtf8(""))
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
        self.groupBox_5.setGeometry(QtCore.QRect(10, 140, 691, 91))
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
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName(_fromUtf8("label_21"))

        self.ajb1 = QtGui.QDoubleSpinBox(self.splitter_13)
        self.ajb1.setObjectName(_fromUtf8("ajb1"))

        self.splitter_14 = QtGui.QSplitter(self.splitter_23)
        self.splitter_14.setOrientation(QtCore.Qt.Vertical)
        self.splitter_14.setObjectName(_fromUtf8("splitter_14"))

        self.label_22 = QtGui.QLabel(self.splitter_14)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName(_fromUtf8("label_22"))

        self.ajb2 = QtGui.QDoubleSpinBox(self.splitter_14)
        self.ajb2.setProperty("value", 14.0)
        self.ajb2.setObjectName(_fromUtf8("ajb2"))

        self.splitter_15 = QtGui.QSplitter(self.splitter_23)
        self.splitter_15.setOrientation(QtCore.Qt.Vertical)
        self.splitter_15.setObjectName(_fromUtf8("splitter_15"))

        self.label_23 = QtGui.QLabel(self.splitter_15)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName(_fromUtf8("label_23"))

        self.ajb3 = QtGui.QDoubleSpinBox(self.splitter_15)
        self.ajb3.setProperty("value", 8.0)
        self.ajb3.setObjectName(_fromUtf8("ajb3"))

        self.splitter_16 = QtGui.QSplitter(self.splitter_23)
        self.splitter_16.setOrientation(QtCore.Qt.Vertical)
        self.splitter_16.setObjectName(_fromUtf8("splitter_16"))

        self.label_24 = QtGui.QLabel(self.splitter_16)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName(_fromUtf8("label_24"))

        self.ajb4 = QtGui.QDoubleSpinBox(self.splitter_16)
        self.ajb4.setProperty("value", 8.0)
        self.ajb4.setObjectName(_fromUtf8("ajb4"))

        self.splitter_17 = QtGui.QSplitter(self.splitter_23)
        self.splitter_17.setOrientation(QtCore.Qt.Vertical)
        self.splitter_17.setObjectName(_fromUtf8("splitter_17"))

        self.label_25 = QtGui.QLabel(self.splitter_17)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName(_fromUtf8("label_25"))

        self.ajb5 = QtGui.QDoubleSpinBox(self.splitter_17)
        self.ajb5.setProperty("value", 5.0)
        self.ajb5.setObjectName(_fromUtf8("ajb5"))

        self.splitter_18 = QtGui.QSplitter(self.splitter_23)
        self.splitter_18.setOrientation(QtCore.Qt.Vertical)
        self.splitter_18.setObjectName(_fromUtf8("splitter_18"))

        self.label_26 = QtGui.QLabel(self.splitter_18)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName(_fromUtf8("label_26"))

        self.ajb6 = QtGui.QDoubleSpinBox(self.splitter_18)
        self.ajb6.setProperty("value", 5.0)
        self.ajb6.setObjectName(_fromUtf8("ajb6"))

        self.splitter_19 = QtGui.QSplitter(self.splitter_23)
        self.splitter_19.setOrientation(QtCore.Qt.Vertical)
        self.splitter_19.setObjectName(_fromUtf8("splitter_19"))

        self.label_27 = QtGui.QLabel(self.splitter_19)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName(_fromUtf8("label_27"))

        self.ajb7 = QtGui.QDoubleSpinBox(self.splitter_19)
        self.ajb7.setProperty("value", 25.0)
        self.ajb7.setObjectName(_fromUtf8("ajb7"))

        self.splitter_20 = QtGui.QSplitter(self.splitter_23)
        self.splitter_20.setOrientation(QtCore.Qt.Vertical)
        self.splitter_20.setObjectName(_fromUtf8("splitter_20"))

        self.label_28 = QtGui.QLabel(self.splitter_20)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName(_fromUtf8("label_28"))

        self.ajb8 = QtGui.QDoubleSpinBox(self.splitter_20)
        self.ajb8.setProperty("value", 30.0)
        self.ajb8.setObjectName(_fromUtf8("ajb8"))

        self.splitter_21 = QtGui.QSplitter(self.splitter_23)
        self.splitter_21.setOrientation(QtCore.Qt.Vertical)
        self.splitter_21.setObjectName(_fromUtf8("splitter_21"))

        self.label_29 = QtGui.QLabel(self.splitter_21)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName(_fromUtf8("label_29"))

        self.ajb9 = QtGui.QDoubleSpinBox(self.splitter_21)
        self.ajb9.setProperty("value", 40.0)
        self.ajb9.setObjectName(_fromUtf8("ajb9"))
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 250, 691, 91))
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
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName(_fromUtf8("label_32"))

        self.wjl1 = QtGui.QDoubleSpinBox(self.splitter_27)
        self.wjl1.setProperty("value", 20.0)
        self.wjl1.setObjectName(_fromUtf8("wjl1"))

        self.splitter_28 = QtGui.QSplitter(self.splitter_25)
        self.splitter_28.setOrientation(QtCore.Qt.Vertical)
        self.splitter_28.setObjectName(_fromUtf8("splitter_28"))

        self.label_33 = QtGui.QLabel(self.splitter_28)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName(_fromUtf8("label_33"))

        self.wjl2 = QtGui.QDoubleSpinBox(self.splitter_28)
        self.wjl2.setProperty("value", 11.0)
        self.wjl2.setObjectName(_fromUtf8("wjl2"))

        self.splitter_29 = QtGui.QSplitter(self.splitter_25)
        self.splitter_29.setOrientation(QtCore.Qt.Vertical)
        self.splitter_29.setObjectName(_fromUtf8("splitter_29"))

        self.label_34 = QtGui.QLabel(self.splitter_29)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName(_fromUtf8("label_34"))

        self.wjl3 = QtGui.QDoubleSpinBox(self.splitter_29)
        self.wjl3.setProperty("value", 7.0)
        self.wjl3.setObjectName(_fromUtf8("wjl3"))

        self.splitter_30 = QtGui.QSplitter(self.splitter_25)
        self.splitter_30.setOrientation(QtCore.Qt.Vertical)
        self.splitter_30.setObjectName(_fromUtf8("splitter_30"))

        self.label_35 = QtGui.QLabel(self.splitter_30)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName(_fromUtf8("label_35"))

        self.wjl4 = QtGui.QDoubleSpinBox(self.splitter_30)
        self.wjl4.setProperty("value", 5.0)
        self.wjl4.setObjectName(_fromUtf8("wjl4"))

        self.splitter_31 = QtGui.QSplitter(self.splitter_25)
        self.splitter_31.setOrientation(QtCore.Qt.Vertical)
        self.splitter_31.setObjectName(_fromUtf8("splitter_31"))

        self.label_36 = QtGui.QLabel(self.splitter_31)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName(_fromUtf8("label_36"))

        self.wjl5 = QtGui.QDoubleSpinBox(self.splitter_31)
        self.wjl5.setProperty("value", 4.0)
        self.wjl5.setObjectName(_fromUtf8("wjl5"))

        self.splitter_32 = QtGui.QSplitter(self.splitter_25)
        self.splitter_32.setOrientation(QtCore.Qt.Vertical)
        self.splitter_32.setObjectName(_fromUtf8("splitter_32"))

        self.label_37 = QtGui.QLabel(self.splitter_32)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName(_fromUtf8("label_37"))

        self.wjl6 = QtGui.QDoubleSpinBox(self.splitter_32)
        self.wjl6.setProperty("value", 3.0)
        self.wjl6.setObjectName(_fromUtf8("wjl6"))

        self.splitter_33 = QtGui.QSplitter(self.splitter_25)
        self.splitter_33.setOrientation(QtCore.Qt.Vertical)
        self.splitter_33.setObjectName(_fromUtf8("splitter_33"))

        self.label_38 = QtGui.QLabel(self.splitter_33)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName(_fromUtf8("label_38"))

        self.wjl7 = QtGui.QDoubleSpinBox(self.splitter_33)
        self.wjl7.setProperty("value", 2.0)
        self.wjl7.setObjectName(_fromUtf8("wjl7"))

        self.splitter_34 = QtGui.QSplitter(self.splitter_25)
        self.splitter_34.setOrientation(QtCore.Qt.Vertical)
        self.splitter_34.setObjectName(_fromUtf8("splitter_34"))

        self.label_39 = QtGui.QLabel(self.splitter_34)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName(_fromUtf8("label_39"))

        self.wjl8 = QtGui.QDoubleSpinBox(self.splitter_34)
        self.wjl8.setProperty("value", 1.0)
        self.wjl8.setObjectName(_fromUtf8("wjl8"))

        self.splitter_35 = QtGui.QSplitter(self.splitter_25)
        self.splitter_35.setOrientation(QtCore.Qt.Vertical)
        self.splitter_35.setObjectName(_fromUtf8("splitter_35"))

        self.label_40 = QtGui.QLabel(self.splitter_35)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName(_fromUtf8("label_40"))

        self.wjl9 = QtGui.QDoubleSpinBox(self.splitter_35)
        self.wjl9.setObjectName(_fromUtf8("wjl9"))

        self.resetAllDispatch = QtGui.QPushButton(self.groupBox_4)
        self.resetAllDispatch.setGeometry(QtCore.QRect(610, 40, 81, 31))
        self.resetAllDispatch.setObjectName(_fromUtf8("resetAllDispatch"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_2.setGeometry(QtCore.QRect(470, 40, 131, 81))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.randSeedCheck = QtGui.QCheckBox(self.groupBox_2)
        self.randSeedCheck.setGeometry(QtCore.QRect(10, 40, 16, 20))
        self.randSeedCheck.setChecked(False)
        self.randSeedCheck.setObjectName(_fromUtf8("randSeedCheck"))
        self.randFactor = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.randFactor.setEnabled(False)
        self.randFactor.setGeometry(QtCore.QRect(30, 40, 91, 26))
        self.randFactor.setDecimals(0)
        self.randFactor.setMinimum(0.0)
        self.randFactor.setMaximum(999999999.0)
        self.randFactor.setSingleStep(1.0)
        self.randFactor.setProperty("value", 0.0)
        self.randFactor.setObjectName(_fromUtf8("randFactor"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 40, 451, 80))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.appFactor = QtGui.QSlider(self.groupBox_3)
        self.appFactor.setGeometry(QtCore.QRect(80, 40, 351, 27))
        self.appFactor.setMinimum(100)
        self.appFactor.setMaximum(300)
        self.appFactor.setSingleStep(3)
        self.appFactor.setProperty("value", 120)
        self.appFactor.setOrientation(QtCore.Qt.Horizontal)
        self.appFactor.setTickPosition(QtGui.QSlider.TicksAbove)
        self.appFactor.setTickInterval(3)
        self.appFactor.setObjectName(_fromUtf8("appFactor"))
        self.appFactorValue = QtGui.QLabel(self.groupBox_3)
        self.appFactorValue.setGeometry(QtCore.QRect(30, 40, 41, 16))
        self.appFactorValue.setAlignment(QtCore.Qt.AlignCenter)
        self.appFactorValue.setObjectName(_fromUtf8("appFactorValue"))
        self.notUsed.addTab(self.tab_2, _fromUtf8(""))
        self.hhs = QtGui.QLabel(Dialog)
        self.hhs.setGeometry(QtCore.QRect(630, 10, 131, 61))
        self.hhs.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"border: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(141, 141, 141);\n"
""))

        self.hhs.setText(_fromUtf8(""))
        self.hhs.setPixmap(QtGui.QPixmap(_fromUtf8("hhs.png")))
        self.hhs.setScaledContents(True)
        self.hhs.setObjectName(_fromUtf8("hhs"))

        self.retranslateUi(Dialog)
        self.notUsed.setCurrentIndex(0)
        self.jobFlow.setCurrentIndex(1)
        self.dayOffset.setCurrentIndex(0)
        QtCore.QObject.connect(self.randSeedCheck, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.randFactor.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Porter Simulation", None))
        self.groupBox.setTitle(_translate("Dialog", "Basic Settings", None))
        self.label_6.setText(_translate("Dialog", "Simulation Duration", None))
        self.label_9.setText(_translate("Dialog", "Porter Wait Times", None))
        self.simDuration.setToolTip(_translate("Dialog", "Choose the number of days to simulate", None))
        self.porterWait.setToolTip(_translate("Dialog", "maximum time a porter waits for patient before abandoning job (0 - 60)", None))
        self.label_15.setText(_translate("Dialog", "days", None))
        self.label_12.setText(_translate("Dialog", "min", None))
        self.label_2.setText(_translate("Dialog", "Job Flow", None))
        self.label_3.setText(_translate("Dialog", "Start Day", None))
        self.jobFlow.setToolTip(_translate("Dialog", "choose the rate of job generation", None))

        self.jobFlow.setItemText(0, _translate("Dialog", "Low", None))
        self.jobFlow.setItemText(1, _translate("Dialog", "Normal", None))
        self.jobFlow.setItemText(2, _translate("Dialog", "High", None))
        self.dayOffset.setToolTip(_translate("Dialog", "starting day of the simulation", None))

        self.dayOffset.setItemText(0, _translate("Dialog", "Monday", None))
        self.dayOffset.setItemText(1, _translate("Dialog", "Tuesday", None))
        self.dayOffset.setItemText(2, _translate("Dialog", "Wednesday", None))
        self.dayOffset.setItemText(3, _translate("Dialog", "Thursday", None))
        self.dayOffset.setItemText(4, _translate("Dialog", "Friday", None))
        self.dayOffset.setItemText(5, _translate("Dialog", "Saturday", None))
        self.dayOffset.setItemText(6, _translate("Dialog", "Sunday", None))
        self.resetAllButton.setText(_translate("Dialog", "Reset All", None))
        self.simulateButton.setText(_translate("Dialog", "Simulate", None))
        self.groupBox_9.setTitle(_translate("Dialog", "Data Source", None))
        self.fileLocation.setToolTip(_translate("Dialog", "Excel File with Data", None))
        self.fileBrowseButton.setToolTip(_translate("Dialog", "browse files", None))
        self.fileBrowseButton.setText(_translate("Dialog", "...", None))
        self.label_18.setText(_translate("Dialog", "Statisitical Data Source:", None))
        self.fileLocation_2.setToolTip(_translate("Dialog", "CSV file with schedule", None))
        self.fileBrowseButton_2.setToolTip(_translate("Dialog", "browse files", None))
        self.fileBrowseButton_2.setText(_translate("Dialog", "...", None))
        self.label_60.setText(_translate("Dialog", "Schedule Data Source", None))
        self.fileLocation_3.setToolTip(_translate("Dialog", "File to write to dashboard to", None))
        self.label_63.setText(_translate("Dialog", "Output Location", None))
        self.fileBrowseButton_3.setToolTip(_translate("Dialog", "browse files", None))
        self.fileBrowseButton_3.setText(_translate("Dialog", "...", None))
        self.notUsed.setTabText(self.notUsed.indexOf(self.tab), _translate("Dialog", "Basic Settings", None))
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
        self.groupBox_2.setTitle(_translate("Dialog", "Random Seed", None))
        self.randSeedCheck.setText(_translate("Dialog", "CheckBox", None))
        self.randFactor.setToolTip(_translate("Dialog", "Choose the a specific seed to use. 0 for True Random", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Appointment Factor", None))
        self.appFactorValue.setText(_translate("Dialog", "1.2", None))
        self.notUsed.setTabText(self.notUsed.indexOf(self.tab_2), _translate("Dialog", "Advanced Settings", None))

        self.assignGUIfunctions(Dialog)

    def assignGUIfunctions(self, Dialog):

        self.fun.ui = self
        self.fun.Dialog = Dialog
        self.fun.appendDispatchLists()
        self.fun.assignEvents()
        self.fun.recordInitialDispatch()
        self.fun.assignNewValues()
        #self.fun.connectOutput()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

