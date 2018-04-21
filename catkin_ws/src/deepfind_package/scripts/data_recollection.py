#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from deepfind_package.msg import *
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Imu
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry 
import message_filters


def callback(lidar, encoder, pose, imu):
	sensorData = sensor_data()
	sensorData.imu = imu;
	sensorData.lidar = lidar
	sensorData.encoder = encoder
	sensorData.pose = pose
	dataPub.publish(sensorData)
	
def synch_data():
	rospy.init_node('data_recollection')

	imu = message_filters.Subscriber('vn100_yaw', Imu)
	lidar = message_filters.Subscriber('scan', LaserScan)
	encoders = message_filters.Subscriber('encoder', encoders_data)
	pose = message_filters.Subscriber('slam_out_pose', PoseStamped)
	#odom = message_filters.Subscriber('odom', Odometry) 

	ts = message_filters.ApproximateTimeSynchronizer([lidar, encoders, pose, imu], 10, 0.1, allow_headerless=True)
	ts.registerCallback(callback)

	global dataPub
	dataPub = rospy.Publisher('sensor_data', sensor_data, queue_size = 1000)

	rospy.spin()


if __name__ == '__main__':
	synch_data()
	
