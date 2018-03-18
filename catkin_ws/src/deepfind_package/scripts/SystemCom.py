#!/usr/bin/env pythonS

import rospy
from std_msgs.msg import *
from deepfind_package.msg import *
from sensor_msgs.msg import LaserScan

#----------------------Communication Set Up-----------------#
def initConnections():
	rospy.init_node('SystemCommunication')
	global controlPub
	controlPub = rospy.Publisher('cmd_vel', String, queue_size = 10)

#----------------------Publisher----------------------------#

def sendCommnand(command):
	controlPub.publish(command)


#----------------------Subscriber---------------------------#
def getSensorData():
	sensorData = sensor_data()
    sensorData.imu = rospy.wait_for_message('imu', imu_data)
    sensorData.lidar = rospy.wait_for_message('lidar', LaserScan)
    sensorData.encoder = rospy.wait_for_message('encoder', String)
    return sensorData