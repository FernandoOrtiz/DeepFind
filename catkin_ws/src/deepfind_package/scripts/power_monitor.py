#!/usr/bin/env python

"""
Power Monitor 
The purpose of this file is to monitor the comouter's voltage and current input
at all times and act accordingly in order to portect the hardware
"""

import rospy
import os
import time

sudoPassword = 'nvidia'
command = 'sudo shutdown now'

#Monitors the voltage and current input
#Shuts down Jetson when voltage reaches 11.5V
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
	print("Voltage = " + str( voltage) + "." + str(voltageDecimal))
	if voltage <= 10 and voltageDecimal < 5 and enable == 1:
		print('shutting down')
		os.system('echo %s|sudo -S %s' % (sudoPassword, command))	
	
		

    
#Main function:
#Responsible for starting the ros node 
#and monitoring the power every 5 seconds
if __name__ == '__main__':
	rospy.init_node('power_monitor')
	enable = 0
	while(1):
		get_input_power()
		enable = 1
		time.sleep(5)

