#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist



rospy.init_node('keyboard_to_car')


pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)


speed_booost = 1

def callback(data):
	data.linear.x *= speed_booost
	data.linear.y *= speed_booost
	data.linear.z *= speed_booost
	data.angular.x *= speed_booost
	data.angular.y *= speed_booost
	data.angular.z *= speed_booost
	pub.publish(data)

rospy.Subscriber('turtle1/cmd_vel', Twist, callback)

rate = rospy.Rate(10) # 10hz

rospy.spin()

