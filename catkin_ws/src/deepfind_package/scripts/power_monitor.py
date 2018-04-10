#!/usr/bin/env python

import rospy
import os
import time



def get_input_power():
	with open("/sys/bus/i2c/devices/0-0040/iio_device/in_current0_input",'r') as i:
		current = next(i)
	file = open ("current_consumption",'w')
	file.write(current)
	file.close()

	with open("/sys/bus/i2c/devices/0-0040/iio_device/in_voltage0_input",'r') as i:
		line = next(i)
	voltage = int(line[0]+line[1])
	voltageDecimal = int(line[3])
	if voltage <= 11 and voltageDecimal <= 5:
		#todo: save data
		os.system("rosnode kill -a")
		os.system("shutdown now")		
    

if __name__ == '__main__':
	rospy.init_node('power_monitor')
	while(1):
		get_input_power()
		time.sleep(10)

