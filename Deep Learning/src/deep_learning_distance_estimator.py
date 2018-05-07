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
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
import numpy as np
from keras.models import load_model
import time

#%%

def sensor_data_callback(data):
    global rnn_model_input
    global input_format
    global deep_model
    global pose_pub
    global out_scaler
    
    #data = rospy.wait_for_message("sensor_data", SensorData)
    #print(data)
    if(input_format == "M2"):
        sensor_data = np.array([data.imu.orientation.x, data.imu.orientation.y, 
            data.imu.orientation.z, data.imu.orientation.w,
            data.imu.angular_velocity.x, data.imu.angular_velocity.y,
            data.imu.angular_velocity.z, data.imu.linear_acceleration.x,
            data.imu.linear_acceleration.y, data.imu.linear_acceleration.z,
            data.pose.pose.orientation.z, data.pose.pose.orientation.w])
        sensor_data = np.append(sensor_data, data.lidar.ranges)
        sensor_data[sensor_data == np.inf] = 0
        
        np.put(rnn_model_input,range(0, rnn_model_input.shape[1]), sensor_data, mode = 'raise')
    else:
        raise TypeError('no valid format for data found')
    rnn_model_input = np.roll(rnn_model_input, -1, axis=0)

    #print("The values are: {}".format(rnn_model_input))
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(rnn_model_input)
    scaled_data = scaled_data.reshape(1, scaled_data.shape[0],
                                      scaled_data.shape[1])
    time.sleep(0.5)
    output = deep_model.predict(x=scaled_data)
    output = out_scaler.inverse_transform(output)
    magnitud = output[0][0]
    angle = output[0][1]
    
    message = PoseStamped()
    message.header.stamp = rospy.Time.now()
    message.header.frame_id = 'base_link'
    message.pose.orientation = data.pose.pose.orientation
    message.pose.position.x = cos(angle)*magnitud*3.3
    message.pose.position.y = sin(angle)*magnitud*3.3
    print("x = " + str(message.pose.position.x)
    + " y = " + str(message.pose.position.y))
    pose_pub.publish(message)



#%%
def main():
    global index
    global rnn_model_input
    global input_format
    global deep_model
    global pose_pub
    global out_scaler
    
    model = "M1-MAE:0.00-MSE:0.03"
    #Import the deep learning model
    deep_model = load_model("../Models/Models/"+model+'.h5py')
    deep_model._make_predict_function()
    out_scaler = joblib.load('../Models/Scalers/'+model+'.scl')
    #initialize the amount of timesteps
    time_steps = deep_model.input_shape[1]
    features = deep_model.input_shape[2]
    input_format = "M2"
    
    rnn_model_input = np.zeros((time_steps, features))
    
    print("Initializing ROS")
    pose_pub = rospy.Publisher("neural_pose", PoseStamped, queue_size = 10)
    #data_sub = rospy.Subscriber("sensor_data", SensorData, sensor_data_callback)
    rospy.init_node("neural_network") 
    #rospy.spin()
    
    
    print("ROS Initialized")
    while not rospy.is_shutdown():
        data = rospy.wait_for_message("sensor_data", SensorData)
        if(input_format == "M2"):
            sensor_data = np.array([data.imu.orientation.x, data.imu.orientation.y, 
                data.imu.orientation.z, data.imu.orientation.w,
                data.imu.angular_velocity.x, data.imu.angular_velocity.y,
                data.imu.angular_velocity.z, data.imu.linear_acceleration.x,
                data.imu.linear_acceleration.y, data.imu.linear_acceleration.z,
                data.pose.pose.orientation.z, data.pose.pose.orientation.w])
            sensor_data = np.append(sensor_data, data.lidar.ranges)
            sensor_data[sensor_data == np.inf] = 0
            
            np.put(rnn_model_input,range(0, rnn_model_input.shape[1]), sensor_data, mode = 'raise')
        else:
            raise TypeError('no valid format for data found')
        rnn_model_input = np.roll(rnn_model_input, -1, axis=0)
    
        #print("The values are: {}".format(rnn_model_input))
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(rnn_model_input)
        scaled_data = scaled_data.reshape(1, scaled_data.shape[0],
                                          scaled_data.shape[1])
        time.sleep(0.5)
        output = deep_model.predict(x=scaled_data)
        output = out_scaler.inverse_transform(output)
        magnitud = output[0][0]
        angle = output[0][1]
        
        message = PoseStamped()
        message.header.stamp = rospy.Time.now()
        message.header.frame_id = 'base_link'
        message.pose.orientation = data.pose.pose.orientation
        message.pose.position.x = cos(angle)*magnitud
        message.pose.position.y = sin(angle)*magnitud
        print("x in feet = " + str(magnitud) + " y in feet = " + str(angle))
        pose_pub.publish(message)
        

if __name__ == '__main__':
    main()

