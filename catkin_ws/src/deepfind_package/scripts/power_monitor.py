#!/usr/bin/env python

import rospy
import os
import time



def get_input_voltage():
	with open("/sys/bus/i2c/devices/0-0040/iio_device/in_voltage0_input",'r') as i:
		line = next(i)
	voltage = int(line[0]+line[1])
	voltageDecimal = int(line[3])
	if voltage <= 11 and voltageDecimal <= 5:
		#todo: save data
		os.system("rosnode kill -a")
		os.system("shutdown now")		
    

if __name__ == '__main__':
	rospy.init_node('voltage_monitor')
	while(1):
		get_input_voltage()
		time.sleep(10)

