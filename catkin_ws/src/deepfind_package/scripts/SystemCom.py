#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from deepfind_package.msg import *
from sensor_msgs.msg import LaserScan, Imu
from geometry_msgs.msg import Twist


#----------------------Communication Set Up-----------------#
def init_connections():
	rospy.init_node('system_communication')
	global controlPub
	controlPub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)

#----------------------Publisher----------------------------#

def send_commnand(command):
	controlPub.publish(command)


#----------------------Subscriber---------------------------#
def get_sensor_data():
    sensorData = sensor_data()
    sensorData.imu = rospy.wait_for_message('vn100_yaw', imu_data)
    sensorData.lidar = rospy.wait_for_message('scan', LaserScan)
    sensorData.encoder = rospy.wait_for_message('encoder', encoders_data)
    return sensorData

if __name__ == '__main__':
    print(get_sensor_data())

