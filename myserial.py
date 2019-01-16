#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/1/16
import serial.tools.list_ports


class MySerial:
    pass


def search1():
    port_list = list(serial.tools.list_ports.comports())
    ret_list = []
    if len(port_list) <= 0:
        print("The Serial port can't find!")
    else:
        for i in port_list:
            ret_list.append(i[0])
            print(i[0])
    return ret_list


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


