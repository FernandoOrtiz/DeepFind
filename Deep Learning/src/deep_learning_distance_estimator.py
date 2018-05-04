#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 15:27:51 2018

@author: rathk
"""

import rospy

from math import cos, sin

from geometry_msgs.msg import PoseStamped
from deepfind_package.msg import SensorData

import numpy as np
from keras.models import load_model



def sensor_data_callback(data):
    global index
    global rnn_model_input
    global input_format
    global deep_model
    global pose_pub
    
    rnn_model_input = np.roll(rnn_model_input, 1, axis=0)
    if(input_format == "M2"):
        np.put(rnn_model_input,0,
           [data.imu.orientation.x, data.imu.orientation.y, 
            data.imu.orientation.z, data.imu.orientation.w,
            data.imu.angular_velocity.x, data.imu.angular_velocity.y,
            data.imu.angular_velocity.z, data.imu.linear_acceleration.x,
            data.imu.linear_acceleration.y, data.imu.linear_acceleration.z,
            data.pose.pose.orientation.z, data.pose.pose.orientation.w, 
            data.lidar.ranges], mode = 'raise')
    else:
        raise TypeError('no valid format for data found')
        
    magnitud, angle = deep_model.predict(rnn_model_input)
    
    
    message = PoseStamped()
    message.header.stamp = rospy.Time.now()
    message.header.frame_id = 'base_link'
    message.orientation = data.orientation
    message.position.x = cos(angle)*magnitud
    message.position.y = sin(angle)*magnitud
    pose_pub.Publish(message)

def main():
    global index
    global rnn_model_input
    global input_format
    global deep_model
    global pose_pub
    
    model = "Big_Data_LSTM-no-out-dense-lstm-regularizer.h5py"
    #Import the deep learning model
    deep_model = load_model("../Model"+model)
    #initialize the amount of timesteps
    time_steps = deep_model.input_shape[1]
    features = deep_model.input_shape[2]
    input_format = "M2"
    
    rnn_model_input = np.zeros(time_steps, features)
    index = 0
    
    
    pose_pub = rospy.Publisher("neural_pose", PoseStamped)
    data_sub = rospy.Subscriber("sensor_data", SensorData, sensor_data_callback)
    rospy.init_node("Neural Network")
    rospy.spin()
    

if __name__ == '__main__':
    main()

