import serial
import time
import threading


ser = serial.Serial('COM21',9600,timeout=0.5)


print("test")
ser.close()

