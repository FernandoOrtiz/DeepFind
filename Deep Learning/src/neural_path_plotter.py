#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 23:27:49 2018

@author: rathk
"""

import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path

message = Path()
message.poses = []

def np_callback(pose_stamped):
    global message
    global path_pub 
    message.header.stamp = rospy.Time.now()
    message.header.frame_id = 'base_link'
    message.poses = message.poses + [pose_stamped]
    print("publishing: " + str(message.poses.__len__))
    path_pub.publish(message)

rospy.init_node("neural_path_plotter")
pose_sub = rospy.Subscriber("neural_pose", PoseStamped, np_callback)
path_pub = rospy.Publisher("neural_path", Path)

rospy.spin()