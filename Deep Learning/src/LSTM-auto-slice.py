# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 17:26:34 2018

@author: Rathk
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 13:56:18 2018

@author: Rathk
"""

# Jose's Recurrent Neural Network
#Pre-process the data
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.layers import CuDNNLSTM
from keras.layers import Dropout
from keras.optimizers import Adam
from sklearn.model_selection import KFold


#The amount of time-steps the LSTM will look back at
time_step = 30


#Import the training set
train_dataset = pd.read_csv("Training_Data - Copy2.csv")
#Obtain the test Data
test_dataset = pd.read_csv("Test_Data - Copy3.csv")
#Merge both test and train to obtain initial values
dataset_total = pd.concat((train_dataset, test_dataset), axis = 0)


#Reshappe the inpputt so it fits the neural network
x = []
for i in range(time_step-1, int(dataset_total.size/dataset_total.shape[1])):
    x.append(dataset_total.as_matrix()[i-time_step+1 : i+1 , 2:])
x = np.array(x)


#Extract the output of the neural network
y = dataset_total.iloc[time_step-1:,0:2]
y = y.as_matrix()
#Feature Scaling
sc = MinMaxScaler(feature_range = (-1,1))
y = sc.fit_transform(y)




# Part 2 - Building the RNN
################################################################################
units = 50
dropout = 0.3
#Build rnn
regresor = Sequential()

#First Layer -- LSTM layer with dropout regularization -- dunno what that means
#Note that this is the only layer with input_shape
regresor.add(CuDNNLSTM(units = units, return_sequences = True, 
                   input_shape=(x.shape[1], x.shape[2])))
regresor.add(Dropout(dropout))


#Second layers with dropout regularization
regresor.add(CuDNNLSTM(units = units, return_sequences = True))
regresor.add(Dropout(dropout))

#Third layers with dropout regularization
regresor.add(CuDNNLSTM(units = units   , return_sequences = True)) 
regresor.add(Dropout(dropout))


#Fourth layers with dropout regularization
regresor.add(CuDNNLSTM(units = units))
regresor.add(Dropout(dropout))

#Output Layer
regresor.add(Dense(units = 2, activation = 'tanh'))

#Compile this network
regresor.compile(optimizer = Adam(lr=0.007), loss='logcosh', metrics=['accuracy'])
#Fit the data
regresor.fit(x, y, validation_split=0.2, epochs=100, batch_size = 64) 
#regresor.save('LSTM-51.28%accuracy.h5py')
   
