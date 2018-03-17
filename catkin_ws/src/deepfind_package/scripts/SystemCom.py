#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from deepfind_package.msg import *
from sensor_msgs.msg import LaserScan

#----------------------Communication Set Up-----------------#
def initConnections():
	rospy.init_node('SystemCommunication', anonymous = True)
	global controlPub
	controlPub = rospy.Publisher('control', String, queue_size = 10)

#----------------------Publisher----------------------------#

def sendCommnand(command):
	controlPub.publish(command)


#----------------------Subscriber---------------------------#
def getSensorData():
    
    imuData = rospy.wait_for_message('imu', imu_data)
    lidarData = rospy.wait_for_message('lidar', LaserScan)
    encoderData = rospy.wait_for_message('encoder', String)
    sensorData.imu = imuData
    sensorData.lidar = lidarData
    sensorData.encoder = encoderData
    return sensorData