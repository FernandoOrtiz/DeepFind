#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 18:52:51 2018

@author: fernando
"""
#**********************variable declaration***********************************
import math

difference
average 
float64 neural_pose_x 
float64 neural_pose_y
float64 actual_pose_x
float64 actual_pose_y
n_values = 0
x_i = 0
y_i = 0
avg = 0
next_avg = 0
#**********************definition declaration*********************************

"""
calculates the difference between the actual pose and the predicted pose
 from the neural net 
 
calculate_difference(neural_x, neural_y, actual_x, actual_y)

float64 naural_x = Pose x component extracted from the neural net prediction pose
float64 naural_y = Pose y component extracted from the neural net prediction pose
float64 actual_x = Pose x component extracted from the navigation pose
float64 actual_y = Pose y component extracted from the navigation pose

return difference between the the given pose messages

"""
def calculate_difference(neural_x, neural_y, actual_x, actual_y):
    global difference
    global x_i
    global y_i
    difference_x = 0
    difference_y = 0
    
    #populate data with ros message 
    
    
    
    
    difference_x = (actual_x - neural_x)**2
    difference_y = (actual_y - neural_y)**2
    displacement_error = math.sqrt(difference_x + difference_y)
    
    return difference

def get_avg(average, xi)
    
    
    