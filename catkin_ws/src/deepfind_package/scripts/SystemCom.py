#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from deepfind_package.msg import *
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

sensorData = sensor_data()

#-----------------------Callback Functions-------------------#

def imu_callback(data):
	sensorData.imu = data
#	print(sensorData.imu)

def lidar_callback(data):
	sensorData.lidar = data

def encoder_callback(data):
	sensorData.encoder = data


#----------------------Communication Set Up-----------------#
def run():
	global sensorData
	sensorData = sensor_data()
	rospy.init_node('system_communication')
	global controlPub
	controlPub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
	imuSub = rospy.Subscriber('vn100_yaw', imu_data, imu_callback)
	lidarSub = rospy.Subscriber('scan', LaserScan, lidar_callback)
	encoderSub = rospy.Subscriber('encoder', encoders_data, encoder_callback)
	print(sensorData)
	rospy.spin()

#----------------------Publisher----------------------------#

def send_commnand(command):
	controlPub.publish(command)


#----------------------Subscriber---------------------------#
def get_sensor_data():
	print(sensorData)
	return sensorData

if __name__ == '__main__':
	run()
