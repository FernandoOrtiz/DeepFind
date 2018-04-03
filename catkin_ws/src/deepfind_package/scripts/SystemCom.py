#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from deepfind_package.msg import *
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

global imuData
imuData = imu_data()

#-----------------------Callback Functions-------------------#

def imu_callback(data):
	imuData = data
	print(imuData)

def lidar_callback(data):
	global lidarData
	lidarData = data

def encoder_callback(data):
	global encoderData
	encoderData = data


#----------------------Communication Set Up-----------------#
def run():
#	global sensorData
#	sensorData = sensor_data()
	rospy.init_node('system_communication')
	global controlPub
	controlPub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
	imuSub = rospy.Subscriber('vn100_yaw', imu_data, imu_callback)
	lidarSub = rospy.Subscriber('scan', LaserScan, lidar_callback)
	encoderSub = rospy.Subscriber('encoder', encoders_data, encoder_callback)
#	print(sensorData)
#	sensorData = sensor_data()
#	sensorData.imu = imuData
#	sensorData.lidar = lidarData
#	sensorData.encoder = encoderData
	rospy.spin()

#----------------------Publisher----------------------------#

def send_commnand(command):
	controlPub.publish(command)


#-----------------------------------------------------------#
def get_sensor_data():
	print(imuData)
	return imuData

if __name__ == '__main__':
	run()
