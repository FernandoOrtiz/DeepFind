#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from deepfind_package.msg import *
from sensor_msgs.msg import LaserScan, Imu

#----------------------Communication Set Up-----------------#
def init_connections():
	rospy.init_node('system_communication')
	global controlPub
	controlPub = rospy.Publisher('cmd_vel', String, queue_size = 10)

#----------------------Publisher----------------------------#

def send_commnand(command):
	controlPub.publish(command)


#----------------------Subscriber---------------------------#
def get_sensor_data():
	sensorData = sensor_data()
    sensorData.imu = rospy.wait_for_message('vn100_yaw', Imu)
    sensorData.lidar = rospy.wait_for_message('scan', LaserScan)
    sensorData.encoder = rospy.wait_for_message('encoder', encoders_data)
    return sensorData
"""
if __name__ == '__main__':
	get_sensor_data()
"""
