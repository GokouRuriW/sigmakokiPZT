# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial
import tkinter as tk
import time
import sys

ser = None

class PZTstages:
    def __init__(self,port):
        global ser
        self.port = port
        ser = serial.Serial(self.port)
        ser.baudrate=38400
        ser.BYTESIZES=serial.EIGHTBITS
        ser.PARITIES=serial.PARITY_NONE
        ser.STOPBITS=serial.STOPBITS_ONE
        ser.timeout=5
        ser.rtscts=True

    def click_Origin(self):
        global ser
        if ser == None:
            return
        rtn = 1
        axis = str(rtn)
        wdata = 'H:' + axis + '\r\n' 
        ser.write(wdata.encode())
        rdata = ser.readline()
        return rdata
    
    def click_MoveAbs(self,sss):
        global ser
        if ser == None:
            return
        value = int(sss)
        ssss = str(sss)
        if value > 0:
            direction = '+'
        else:
            direction = '-'
        rtn = 1
        axis = str(rtn)
        wdata = 'A:'+ axis + direction + 'P' + ssss + '\r\n'
        ser.write(wdata.encode())
        rdata = ser.readline()

        time.sleep(0.01)
        wdata = 'G:\r\n'
        ser.write(wdata.encode())
        rdata = ser.readline()
        return rdata
    
    def click_Status(self):
        global ser
        if ser == None:
            return
        wdata = 'Q:' + '\r\n' 
        ser.write(wdata.encode())
        rdata = ser.readline().decode()
        sss = rdata[0:10]
        return sss
    
    def click_Exit(self):
        global ser
        time.sleep(1)
        ser.close()

