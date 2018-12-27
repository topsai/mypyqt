# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
import serial

import serial.tools.list_ports


class Ui_MainWindow(object):
    def Action(self):
        port_list = list(serial.tools.list_ports.comports())

        if len(port_list) <= 0:
            print("The Serial port can't find!")

        else:
            port_list_0 = list(port_list[0])

            port_serial = port_list_0[0]

            ser = serial.Serial(port_serial, 9600, timeout=60)

            print("check which port was really used >", ser.name)

        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.open()

        ser.write("testing")
        try:
            while 1:
                response = ser.readline()
                print(response)
        except KeyboardInterrupt:
            ser.close()

        if self.pushButton.text() == "未连接":

            self.pushButton.setText("连接")
            self.pushButton.setStyleSheet("background: rgb(0,255,0)")
            self.label.setText("连接")
        else:
            self.pushButton.setText("未连接")
            self.label.setText("未连接")
            self.pushButton.setStyleSheet("background: rgb(255,255,255)")


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Action)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 9, 60, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>啊</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "未连接"))
        self.label.setText(_translate("MainWindow", "no connect"))

