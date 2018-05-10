#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 23:27:49 2018

@author: rathk
"""

import rospy
from geometry_msgs.msg import Path, PoseStamped


message = Path()


def np_callback(pose_stamped):
    global message
    global path_pub 
    message.header.stamp = rospy.Time.now()
    message.header.frame_id = 'base_link'
    message.pose = message.pose + [pose_stamped]
    path_pub.Publish(message)

pose_sub = rospy.Subscriber("neural_pose", PoseStamped, np_callback)
path_pub = rospy.Publisher("neural_path", Path)

sav = False
inp = input("Do you want to save this model? (yes/no): ")
print(inp.lower())
print(str(inp.lower() == 'yes'))
while((inp.lower() == 'yes' or inp.lower() == 'y' or inp.lower() == 'no' or inp.lower() == 'n')):
    print(inp.lower())
    print(str(inp.lower() == 'yes'))
    if(inp.lower() == 'yes' or inp.lower() == 'y' ):
        global sav
        sav = True
        print('BITCHHHH')
    elif (inp.lower() == 'no' or inp.lower() == 'n'):
        print("this")
    else:
        print('Invalid input')
        inp = input("Do you want to save this model? (yes/no): ")
        
if(sav):
    print("Saved to file")
else:
    print("Did not save to file")