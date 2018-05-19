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




def main():
    
<<<<<<< Updated upstream
    
    #This is the name of the trained model
    model = "M144-YpR0-DuAL-MAE:0.070-MSE:0.008-F3"
    
    #Defines whether the output is polar or not
=======
    model = "M89-CaRT-MAE:0.067-MSE:0.010-F2"
>>>>>>> Stashed changes
    polar = False
    #Defines whether it has one neural network or two
    dual_nets = False
    
    #Extract information from the name of the model
    if(model.find('PoLR') > 0):
        polar = True
    if(model.find('DuAL') > 0):
        dual_nets = True
    input_format = model.split('-')[-1]
    
    
    MODEL_DIR = ("../Models/" + model + "/")
    if(not dual_nets): 
        #Import the deep learning model
        deep_model = load_model(MODEL_DIR + model + '.h5py')
        deep_model._make_predict_function()
        out_scaler = joblib.load(MODEL_DIR + model + '.scl')
        
        #initialize the amount of timesteps
        time_steps = deep_model.input_shape[1]
        features = deep_model.input_shape[2]
        output_timesteps = deep_model.output_shape[1]
    else:
        #Import the deep learning model
        deep_model_x = load_model(MODEL_DIR + model.split(input_format)[0] + 
                        'X-' + input_format + '.h5py')
        deep_model_x._make_predict_function()
        deep_model_y = load_model(MODEL_DIR + model.split(input_format)[0] + 
                        'Y-' + input_format + '.h5py')
        deep_model_y._make_predict_function()
        out_scaler = joblib.load(MODEL_DIR + model + '.scl')
        
        #initialize the amount of timesteps
        time_steps = deep_model_x.input_shape[1]
        features = deep_model_x.input_shape[2]
        output_timesteps = deep_model_x.output_shape[1]
    
    #Verify if the scaler was initialized to be used
    out_scaling = False
    try:
        out_scaler.data_max_
        out_scaling = True
    except AttributeError:
        pass
    
    
    
    out_return_sequences = False
    if(output_timesteps > 2):
        out_return_sequences  = True
    
    rnn_model_input = np.zeros((time_steps, features))
    
    print("Initializing ROS")
    pose_pub = rospy.Publisher("neural_pose", PoseStamped, queue_size = 10)
    #data_sub = rospy.Subscriber("sensor_data", SensorData, sensor_data_callback)
    rospy.init_node("neural_network") 
    #rospy.spin()
    
    
    print("ROS Initialized")
    while not rospy.is_shutdown():
        data = rospy.wait_for_message("sensor_data", SensorData)
        if(input_format == "F2" or input_format == 'F3'):
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
        """
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(rnn_model_input)
        scaled_data = scaled_data.reshape(1, scaled_data.shape[0],
                                          scaled_data.shape[1])
        """
        scaled_data = rnn_model_input.reshape(1, rnn_model_input.shape[0],
                                          rnn_model_input.shape[1])
        
        if(not dual_nets):
            if(not out_return_sequences):
                output = deep_model.predict(x=scaled_data)
            else:
                output = deep_model.predict(x=scaled_data)
                output = output[:,-1,:].reshape(-1,2)
        if(dual_nets):
            if(not out_return_sequences):
                output = deep_model_x.predict(x=scaled_data)
                output = np.append(output, deep_model_y.predict(x=scaled_data), axis = 1)
            else:
                output = deep_model_x.predict(x=scaled_data)
                output = np.append(output, deep_model_y.predict(x=scaled_data), axis = 1)
                output = output[:,-1,:].reshape(-1,2)
        
        if(out_scaling):
            output = out_scaler.inverse_transform(output)
        
        
        message = PoseStamped()
        message.header.stamp = rospy.Time.now()
        message.header.frame_id = 'map'
        message.pose.orientation = data.pose.pose.orientation
        x , y = 0, 0
        if(polar):
            magnitud = output[0][0]
            angle = output[0][1]
            x = cos(angle)*magnitud
            y = sin(angle)*magnitud
            message.pose.position.x = x
            message.pose.position.y = y
        if(not polar):
            x = output[0][0]
            y = output[0][1]
            message.pose.position.x = x
            message.pose.position.y = y
        print("x in meters = " + str(x) + " y in meters = " + str(y))
       
        pose_pub.publish(message)
        

if __name__ == '__main__':
    main()

