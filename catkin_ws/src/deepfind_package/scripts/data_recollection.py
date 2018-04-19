#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from deepfind_package.msg import *
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry 
import message_filters


def callback(imu, lidar, encoders, pose):
	sensorData = sensor_data()
	sensorData.imu = imu;
	sensorData.lidar = lidar
	sensorData.encoder = encoders
	sensorData.pose = pose
	dataPub.publish(sensorData)
	
def synch_data():
	rospy.init_node('data_recollection')

	imu = message_filters.Subscriber('vn100_yaw', imu_data)
	lidar = message_filters.Subscriber('scan', LaserScan)
	encoders = message_filters.Subscriber('encoder', encoders_data)
	opose = message_filters.Subscriber('slam_out_pose', PoseStamped)
	#odom = message_filters.Subscriber('odom', Odometry) 

	ts = message_filters.ApproximateTimeSynchronizer([odom, imu, lidar, encoders, odom], 10, 0.1, allow_headerless=True)
	ts.registerCallback(callback)

	dataPub = rospy.Publisher('sensor_data', sensor_data, queue_size = 1000)
	rate = rospy.Rate(7.1)

	rospy.spin()


if __name__ == '__main__':
	synch_data()
	