#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from deepfind_package.msg import *
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist



class SysCom(object):
	def __init__(self):
		self.sensorData = sensor_data()

		rospy.Subscriber('vn100_yaw', imu_data, self.imu_callback)
		rospy.Subscriber('scan', LaserScan, self.lidar_callback)
		rospy.Subscriber('encoder', encoders_data, self.encoder_callback)

		self.dataPub = rospy.Publisher('sensor_data', sensor_data, queue_size = 10)
		self.rate = rospy.Rate(7.1)


	def imu_callback(self, data):
		self.sensorData.imu = data

	def lidar_callback(self, data):
		self.sensorData.lidar = data

	def encoder_callback(self, data):
		self.sensorData.encoder = data

	def get_sensor_data(self):
		return self.sensorData

	def start(self):
		while not rospy.is_shutdown():
			self.dataPub.publish(self.sensorData)
			self.rate.sleep()


if __name__ == '__main__':
	rospy.init_node('system_communication')
	sys_com = SysCom()
	sys_com.start()
