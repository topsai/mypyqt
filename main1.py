# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from myserial import search1, conn_com
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt

model_list = ["Uno", "Nano", "Micra"]


class Ui_MainWindow(object):
    def __init__(self):
        self.com_list = search1()

    def conn(self):
        # 连接信号
        my_com = self.comboBox.currentText()
        print(my_com)
        # 连接
        if self.pushButton.text() == "连接":
            if conn_com(my_com):
                self.label.setText("已连接")
                pe = QPalette()
                self.label.setAutoFillBackground(True)  # 设置背景充满,为设置背景颜色的必要条件
                pe.setColor(QPalette.Window, Qt.green)  # 设置背景颜色
                self.label.setPalette(pe)
                self.pushButton.setText("断开")
            else:
                self.pushButton.setText("连接")
                self.label.setText("未连接")
        # 断开
        else:
            pe = QPalette()
            self.label.setAutoFillBackground(True)  # 设置背景充满,为设置背景颜色的必要条件
            pe.setColor(QPalette.Window, Qt.color0)  # 设置背景颜色
            self.label.setPalette(pe)
            self.pushButton.setText("连接")
            self.label.setText("未连接")

    def refresh(self):
        # 刷新com 端口
        ret = search1()
        if ret != self.com_list:
            self.com_list = ret
            self.comboBox.clear()
            self.comboBox.addItems(self.com_list)
            print('ccc+++', self.comboBox.currentText())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 202)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(70, 70, 348, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.splitter)
        self.comboBox_2.setObjectName("comboBox_2")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.splitter)
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        # self.pushButton.clicked.connect(self.comboBox.clearEditText)
        # self.pushButton.clicked.connect(self.label.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 连接信号
        self.comboBox_2.addItems(model_list)
        self.pushButton_2.clicked.connect(self.refresh)
        self.comboBox.addItems(self.com_list)
        self.pushButton.clicked.connect(self.conn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>啊</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "型号"))
        self.label.setText(_translate("MainWindow", "未连接"))
        self.pushButton.setText(_translate("MainWindow", "连接"))
        self.pushButton_2.setText(_translate("MainWindow", "刷新"))
        self.menu.setTitle(_translate("MainWindow", "打开"))
