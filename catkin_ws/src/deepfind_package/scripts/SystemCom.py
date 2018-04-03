#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from deepfind_package.msg import *
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist



class SysCom(object):
	def __init__(self):
		self.sensorData = sensor_data()
		# self.imuData = imu_data()
		# self.lidarData = LaserScan()
		# self.encoderData = encoders_data()

		rospy.Subscriber('vn100_yaw', imu_data, self.imu_callback)
		rospy.Subscriber('scan', LaserScan, self.lidar_callback)
		rospy.Subscriber('encoder', encoders_data, self.encoder_callback)

		# self.controlPub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)

	def imu_callback(self, data):
		self.sensorData.imu = data

	def lidar_callback(self, data):
		self.sensorData.lidar = data	

	def encoder_callback(self, data):
		self.sensorData.encoder = data


	def start():
		rospy.spin()


	def get_sensor_data():
		return self.sensorData


if __name__ == '__main__':
	rospy.init_node('system_communication')
	sys_com = SysCom()
	sys_com.start()
