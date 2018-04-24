#!/usr/bin/env python

"""
	Data Recollection
	This node is in charge of recollection the data  to be used by the 
	learning algorithm to estimate position. 
"""

import rospy
from std_msgs.msg import *
from deepfind_package.msg import EncodersData
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Imu
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry 
import message_filters

"""
	Creates SensorData message and publishes it
"""
def callback(lidar, encoder, pose, imu):
	sensorData = SensorData()
	sensorData.imu = imu;
	sensorData.lidar = lidar
	sensorData.encoder = encoder
	sensorData.pose = pose
	dataPub.publish(sensorData)

"""
	Start data recollection node. Set the data subcribers to accept data when
	messages arrive within a 0.1 second difference of each other.
	Waits for messages for arrive.
"""
def synch_data():
	rospy.init_node('data_recollection')

	imu = message_filters.Subscriber('vn100_yaw', Imu)
	lidar = message_filters.Subscriber('scan', LaserScan)
	encoders = message_filters.Subscriber('encoder', EncodersData)
	pose = message_filters.Subscriber('slam_out_pose', PoseStamped)
	#odom = message_filters.Subscriber('odom', Odometry) 

	ts = message_filters.ApproximateTimeSynchronizer([lidar, encoders, pose, imu], 10, 0.1, allow_headerless=True)
	ts.registerCallback(callback)

	global dataPub
	dataPub = rospy.Publisher('sensor_data', sensor_data, queue_size = 1000)

	rospy.spin()

#Main Function
if __name__ == '__main__':
	synch_data()
	
