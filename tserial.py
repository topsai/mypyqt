#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2018/12/28
import serial

import serial.tools.list_ports


port_list = list(serial.tools.list_ports.comports())
# print(port_list)

if len(port_list) <= 0:
    print("The Serial port can't find!")

else:
    for i in port_list:
        print(i)
        # port_list_0 = list(port_list[0])
        #
        # port_serial = port_list_0[0]
        #
        # ser = serial.Serial(port_serial, 9600, timeout=60)
        #
        # print("check which port was really used >", ser.name)
        # ser.close()
    try:
        ser = serial.Serial("COM6", 9600, timeout=60)
        print("连接成功")
        print(ser.name)
        ser.close()
    except Exception as e:
        print("连接失败。")
