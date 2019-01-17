# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from myserial import search1, conn_com, flash, my_log
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import subprocess
import os
import threading

model_list = ["Uno", "Nano", "Micra"]


class Ui_MainWindow(object):
    def __init__(self):
        self.com_list = search1()
        # 串口句柄
        self.serial = None
        self.message = None
        self.com = None
        self.cmd = "{}/avrdude -C{}/avrdude.conf -v -patmega328p " \
                   "-carduino -P{} -b115200 -D -Uflash:w:{}/Blink.ino.hex:i"

    def __del__(self):
        if self.serial:
            self.serial.close()

    def conn(self):
        # 连接信号
        my_com = self.comboBox.currentText()
        print(my_com)
        # 连接
        if self.pushButton.text() == "连接":
            self.serial = conn_com(my_com)
            print(self.serial)
            if self.serial:
                self.com = my_com
                self.label.setText("已连接")
                self.comboBox.setDisabled(True)
                pe = QPalette()
                self.label.setAutoFillBackground(True)  # 设置背景充满,为设置背景颜色的必要条件
                pe.setColor(QPalette.Window, Qt.green)  # 设置背景颜色
                self.label.setPalette(pe)
                self.pushButton.setText("断开")
                self.message = "连接" + my_com + "成功"
                self.listWidget.addItem(self.message)
            else:
                self.pushButton.setText("连接")
                self.label.setText("未连接")
                self.listWidget.addItem("连接失败")
        # 断开
        else:
            if self.serial:
                self.serial.close()
                self.serial = None
                print('close ok')
            self.com = None
            self.comboBox.setDisabled(False)
            pe = QPalette()
            self.label.setAutoFillBackground(True)  # 设置背景充满,为设置背景颜色的必要条件
            pe.setColor(QPalette.Window, Qt.color0)  # 设置背景颜色
            self.label.setPalette(pe)
            self.pushButton.setText("连接")
            self.label.setText("未连接")
            self.message = "端口" + my_com + "已断开"
            self.listWidget.addItem(self.message)

    def refresh(self):
        # 刷新com 端口
        ret = search1()
        if ret != self.com_list:
            self.com_list = ret
            self.comboBox.clear()
            self.comboBox.addItems(self.com_list)
            print('ccc+++', self.comboBox.currentText())
        self.message = "COM刷新成功"
        self.listWidget.addItem(self.message)

    def com_chenge(self):
        print(self.comboBox.currentText())
        self.com = self.comboBox.currentText()

    @staticmethod
    def comm(cmd):
        p = subprocess.Popen(cmd, shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # p.stdout.encoding = 'utf8'
        # p.stderr.encoding = 'utf8'
        t = threading.Thread(target=p.stdout.read)
        t.start()
        t.join(timeout=10)
        try:
            data = p.stdout.read()
        except:
            data = None

        if data:
            data = data.decode('gbk')

    def flash_bin(self):
        if self.serial:
            self.serial.close()
        ret = flash(self.comboBox_2.currentText(), self.comboBox.currentText())
        if ret:
            print('ok')

            print(os.path.dirname(__file__))
            base_dir = (os.path.join(os.path.dirname(__file__), "avr"))
            # todo
            cmd = self.cmd.format(base_dir, base_dir, self.com, base_dir)
            print('====>', cmd)

            p = subprocess.Popen(cmd, shell=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            # p.stdout.encoding = 'utf8'
            # p.stderr.encoding = 'utf8'
            t = threading.Thread(target=self.comm, args=(cmd,))
            t.start()
            try:
                data = p.stdout.read()
            except:
                data = None

            if data:
                data = data.decode('gbk')
            # print('--->', data)

            if "bytes of flash verified" in data:
                self.message = "写入固件成功"
                self.listWidget.addItem(self.message)
            else:
                self.message = "写入固件失败"
                self.listWidget.addItem(self.message)
                print('err')

        else:
            self.message = "写入固件失败"
            self.listWidget.addItem(self.message)
            print('err')
        # else:
        #     self.message = "未连接"
        #     self.listWidget.addItem(self.message)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 223)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 80, 72, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 50, 36, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(280, 50, 61, 20))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 110, 72, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(269, 20, 61, 20))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 24, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 140, 71, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 211, 141))
        self.listWidget.setObjectName("listWidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 180, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # self.pushButton.clicked.connect(self.comboBox.clearEditText)
        # self.pushButton.clicked.connect(self.label.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 连接信号
        self.comboBox_2.addItems(model_list)
        self.comboBox.currentIndexChanged.connect(self.com_chenge)
        self.pushButton_2.clicked.connect(self.refresh)
        self.comboBox.addItems(self.com_list)
        self.pushButton.clicked.connect(self.conn)
        self.pushButton_3.clicked.connect(self.flash_bin)
        self.pushButton_4.clicked.connect(self.listWidget.clear)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial"))
        MainWindow.setWindowIcon(QIcon("./my.ico"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>啊</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "连接"))
        self.label.setText(_translate("MainWindow", "未连接"))
        self.pushButton_2.setText(_translate("MainWindow", "刷新"))
        self.label_2.setText(_translate("MainWindow", "型号"))
        self.pushButton_3.setText(_translate("MainWindow", "写入固件"))
        self.label_3.setText(_translate("MainWindow", "日志"))
        self.pushButton_4.setText(_translate("MainWindow", "清空"))
