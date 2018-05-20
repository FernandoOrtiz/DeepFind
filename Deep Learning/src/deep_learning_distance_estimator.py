#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 15:27:51 2018

@author: rathk
"""
#%%
import rospy


from geometry_msgs.msg import PoseStamped
from deepfind_package.msg import SensorData
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
import numpy as np
from keras.models import load_model
import dl_utils as dl
import sys



#%%

def main():
    
#%%
    if(sys.argv != 2):
        print('invalid number of arguments: ' + len(sys.argv) + '. Expected two')
        exit()
    else:
        model = sys.argv[1]
    
    #Defines whether it has one neural network or two
    #dual_nets = False

    
    #Extract information from the name of the model
    
    #Defines whether the output is polar or not
    if(model.find('PoLR') > 0):
        polar_output = True
    else:
        polar_output = False
    
    if(model.find('LiN') > 0):
        recurrent = False
    else:
        recurrent = True
    #Extract whether or not to scale input
    if(model.find('IT') > 0):
        scale_input = True
    else:
        scale_input = False
    
    
    #Extract whether or not to scale output
    if(model.find('OT') > 0):
        scale_output = True
    else:
        scale_output = False
    
    #Extract output type from name
    input_format = model.split('-')[-1]
    
    
    MODEL_DIR = ("../Models/" + model + "/")
    #if(not dual_nets): 
    #Import the deep learning model
    deep_model = load_model(MODEL_DIR + model + '.h5py')
    deep_model._make_predict_function()
    out_scaler = joblib.load(MODEL_DIR + model + '.scl')
    
    #initialize the amount of timesteps and features
    if(recurrent):
        time_steps = deep_model.input_shape[1]
    features = deep_model.input_shape[2]
   
  
    if(recurrent):
        rnn_model_input = np.zeros((time_steps, features))
    else:
        rnn_model_input = np.zeros(features))
    
    print("Initializing ROS")
    pose_pub = rospy.Publisher("neural_pose", PoseStamped, queue_size = 10)
    rospy.init_node("neural_network") 
    
    if(scale_input):
        input_scaler = StandardScaler()
        
    print("ROS Initialized")
#%%
    while not rospy.is_shutdown():
#%%
        data = rospy.wait_for_message("sensor_data", SensorData)
        if(input_format == "F2" or input_format == 'F3'):
            sensor_data = np.array([data.imu.orientation.x, data.imu.orientation.y, 
                data.imu.orientation.z, data.imu.orientation.w,
                data.imu.angular_velocity.x, data.imu.angular_velocity.y,
                data.imu.angular_velocity.z, data.imu.linear_acceleration.x,
                data.imu.linear_acceleration.y, data.imu.linear_acceleration.z])
            sensor_data = np.append(sensor_data, data.lidar.ranges)
            sensor_data[sensor_data == np.inf] = 0
            
        else:
            raise TypeError('no valid format for data found')
        
        if(recurent):
            np.put(rnn_model_input,range(0, rnn_model_input.shape[1]), sensor_data, mode = 'raise')
            rnn_model_input = np.roll(rnn_model_input, -1, axis=0)
        else:
            rnn_model_input = sensor_data
        
        
        if(scale_input):
            scaled_data = input_scaler.fit_transform(rnn_model_input)
        else:
            scaled_data = rnn_model_input
        
        
        if(recurrent):
            scaled_data = scaled_data.reshape(1, scaled_data.shape[0],
                                          rnn_model_input.shape[1])
        else:
            scaled_data = scaled_data.reshape(1, scaled_data.shape[0])
            
        output = deep_model.predict(x=scaled_data)
   
        if(scale_output):
            output = out_scaler.inverse_transform(output)
        
        
        message = PoseStamped()
        message.header.stamp = rospy.Time.now()
        message.header.frame_id = 'map'
        message.pose.orientation = data.pose.orientation
        x , y = 0, 0
        if(polar_output):
            magnitude = output[0][0]
            #angle = output[0][1]
            angle = np.arctan2(sensor_data.pose.pose.y, sensor_data.pose.pose.x)
            print("magnitud in meters = " + str(magnitude) + " angle in radians = " + str(angle*180/3.1415))
            x, y = dl.to_cartesian_scalar(magnitude, angle)
            message.pose.position.x = x
            message.pose.position.y = y
        if(not polar_output):
            x = output[0][0]
            y = output[0][1]
            message.pose.position.x = x
            message.pose.position.y = y
        print("x in meters = " + str(x) + " y in meters = " + str(y))
       
        pose_pub.publish(message)
#%%        

if __name__ == '__main__':
    main()

