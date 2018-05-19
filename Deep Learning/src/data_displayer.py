#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 20:07:28 2018

@author: rathk
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tf.transformations import euler_from_quaternion 

view = False
zero_pad=False
time_step = 3
train_dataset = ["D1-30MinuteRun-F2.csv",
           "D2-35MinuteRun-F2.csv",
           "D3-30MinuteStillRun-F2.csv",
           #"D4-18MinuteRun-F2.csv",
           #"D5-7MinuteRun-F2.csv",
           #"D6-27MinuteRun-F2.csv",
           "D7-60MinuteRun-F2.csv",
           "D8-60MinuteRun-F2.csv",
           "D9-60-MinuteRun-F2.csv",
           "D10-30MinuteRun-F2.csv",
           "D11-30MinuteRun-F2.csv",         
           "D12-25MinuteRun-F2.csv",
           "D13-60MinuteStillRun-F2.csv",
         ]

test_dataset = ["D4-18MinuteRun-F2.csv"]

def to_ypr(data):
    for i in range(0, data.shape[0]):
        quat = [data[i,2], data[i,3], data[i,4], data[i,5]]
        (roll, pitch, yaw) = euler_from_quaternion(quat)
        data[i,2] = yaw
        data[i,3] = pitch
        data[i,4] = roll
        data[i,5] = 0        
        


if __name__ == '__main__':        
    i = 0    
    if(view):        
        for element in dataset:
            i += 1
            data = pd.read_csv('../Datasets/' + element)
            data = data.as_matrix()
            plt.figure(figsize=(15,15))
            plt.subplot(211)
            plt.plot(data[:,0:1])
            plt.subplot(212)
            plt.plot(data[:,1:2])
            plt.title('Dataset number ' + element.split('-')[0].split('D')[-1])
            plt.ylabel('Meters')
            plt.xlabel('sample')
            plt.show()
    else: 
        #Create a copy so you dont alter the original
        dataset_copy = list(train_dataset)                                             #Make a copy of the list so you do not alter it
        #Pop the first item in the list
        dataset_total = pd.read_csv("../Datasets/"+dataset_copy.pop(0))            #Pop the first element out
        #If desired, add zero pad
        if(zero_pad):
            zeros_df = pd.DataFrame(0, index=range(time_step-1), 
                                    columns= dataset_total.columns)
            dataset_total = pd.concat((zeros_df, dataset_total), axis = 0)
        
        #Iterate through the list appending each dataset
        for element in dataset_copy:                                               #If you have additional datasets, keep adding them 
            if(zero_pad):
                dataset_total = pd.concat((dataset_total, zeros_df), axis = 0)
            dataset_total = pd.concat((dataset_total,
            pd.read_csv("../Datasets/"+element)), axis=0)
        
        #Convert to numpy array
        dataset_total = dataset_total.as_matrix()    
        #Extract the output of the neural network
        to_ypr(dataset_total)
        np.savetxt("../Datasets/D1-MegaSet-F3.csv", dataset_total,
                              delimiter = ",")
            
        #Create a copy so you dont alter the original
        dataset_copy = list(test_dataset)                                             #Make a copy of the list so you do not alter it
        #Pop the first item in the list
        dataset_total = pd.read_csv("../Datasets/"+dataset_copy.pop(0))            #Pop the first element out
        #If desired, add zero pad
        if(zero_pad):
            zeros_df = pd.DataFrame(0, index=range(time_step-1), 
                                    columns= dataset_total.columns)
            dataset_total = pd.concat((zeros_df, dataset_total), axis = 0)
        
        #Iterate through the list appending each dataset
        for element in dataset_copy:                                               #If you have additional datasets, keep adding them 
            if(zero_pad):
                dataset_total = pd.concat((dataset_total, zeros_df), axis = 0)
            dataset_total = pd.concat((dataset_total,
            pd.read_csv("../Datasets/"+element)), axis=0)
        
        #Convert to numpy array
        dataset_total = dataset_total.as_matrix()    
        #Extract the output of the neural network
        to_ypr(dataset_total)
        np.savetxt("../Datasets/D2-TestSet-F3.csv", dataset_total,
                              delimiter = ",")
            
      
