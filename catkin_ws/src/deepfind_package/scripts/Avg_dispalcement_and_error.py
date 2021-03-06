#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 18:52:51 2018

@author: fernando
"""
import math
import rospy
import message_filters
from geometry_msgs.msg import PoseStamped
#**********************variable declaration***********************************
n_values = 1
x_i = 0
avg = 0
next_avg = 0
#**********************definition declaration*********************************

"""
calculates the difference between the actual pose and the predicted pose
 from the neural net 
 
float64 naural_x = Pose x component extracted from the neural net prediction pose
float64 naural_y = Pose y component extracted from the neural net prediction pose
float64 actual_x = Pose x component extracted from the navigation pose
float64 actual_y = Pose y component extracted from the navigation pose

return difference between the the given pose messages

"""

def calculate_difference(neural_x, neural_y, actual_x, actual_y):

    difference_x = 0
    difference_y = 0
    
    
    
    difference_x = (actual_x - neural_x)**2
    difference_y = (actual_y - neural_y)**2
    displacement_error = math.sqrt(difference_x + difference_y)
    
    return displacement_error


"""
calculates the average error of the displacement 
 
prev_average = the previously calculated average for value followup
xi = the calculated difference from calculate_difference()
n_values = number of data values extracted from the system

return average error of displacement

"""
def get_avg(xi):
    global avg
    global n_values
    n_values += 1
    avg = ((avg*(n_values-1)) + xi)/n_values
    
    return avg



def callback(neural, slam):
 
    try:
        x_i = calculate_difference(neural.pose.position.x, neural.pose.position.y, slam.pose.position.x, slam.pose.position.y)
        avg = get_avg(x_i)
        print("The immediate error is: " + str(x_i*3.3) + "The average error is " + str(avg*3.3))
       
    except:
        print("Done")
        
    

"""
main definition that displays the average error

"""
def get_error_values():
    
    rospy.init_node('pose_error')
    
    neural_pose = message_filters.Subscriber('neural_pose', PoseStamped)
    slam_pose = message_filters.Subscriber('slam_out_pose',PoseStamped)
    
    ts = message_filters.ApproximateTimeSynchronizer([neural_pose, slam_pose], 10, 0.1, allow_headerless=True)
    ts.registerCallback(callback)
    rospy.spin() 

if __name__ == '__main__':
   get_error_values()
    
    
    
