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



#The amount of time-steps the LSTM will look back at
time_step = 100


#Import the training set
train_dataset = pd.read_csv("Training_Data - Copy2.csv")
#Obtain the test Data
test_dataset = pd.read_csv("Test_Data - Copy3.csv")
#Merge both test and train to obtain initial values
dataset_total = pd.concat((train_dataset, test_dataset), axis = 0)
sc = MinMaxScaler(feature_range = (-1,1))
sc.fit(dataset_total.iloc[:,0:2].as_matrix())

#Extract the inputs to the neural nework
training_input_set = train_dataset.iloc[:,2:376]
training_input_set = training_input_set.as_matrix()  
#Reshappe the inpputt so it fits the neural network
x_train = []
for i in range(time_step-1, int(training_input_set.size/training_input_set.shape[1])):
    x_train.append(training_input_set[i-time_step+1 : i+1 , 0:])
x_train= np.array(x_train)



#Extract the output of the neural network
y_train = train_dataset.iloc[time_step-1:,0:2]
y_train = y_train.as_matrix()
#Feature Scaling

y_train = sc.transform(y_train)



test_inputs_set = dataset_total.iloc[
        len(dataset_total) - len(test_dataset) - time_step:, 2:].values 
x_test = []
for i in range(time_step-1, int(test_inputs_set.size/test_inputs_set.shape[1])):
    x_test.append(test_inputs_set[i-time_step+1:i+1, :])
x_test= np.array(x_test)
y_test = dataset_total.iloc[len(dataset_total) - len(test_dataset)-1:, 0:2].values
y_test = sc.transform(y_test)


# Part 2 - Building the RNN
################################################################################
units = 200
dropout = 0.3
#Build rnn
regresor = Sequential()

#First Layer -- LSTM layer with dropout regularization -- dunno what that means
#Note that this is the only layer with input_shape
regresor.add(CuDNNLSTM(units = units, return_sequences = True, 
                   input_shape=(x_train.shape[1], x_train.shape[2])))
regresor.add(Dropout(dropout))


#Second layers with dropout regularization
#regresor.add(CuDNNLSTM(units = units, return_sequences = True))
#regresor.add(Dropout(dropout))

#Third layers with dropout regularization
#regresor.add(CuDNNLSTM(units = units   , return_sequences = True)) 
#regresor.add(Dropout(dropout))


#Fourth layers with dropout regularization
regresor.add(CuDNNLSTM(units = units))
regresor.add(Dropout(dropout))

#Output Layer
regresor.add(Dense(units = 2, activation = 'tanh'))

#Compile this network
regresor.compile(optimizer = 'adam', loss='logcosh', metrics=['accuracy'])
#Fit the data
regresor.fit(x_train, y_train, epochs=100)#batch_size = 32)#, shuffle=False) 
#Predict Values
predictions_logcosh = regresor.predict(x_test)
predictions_logcosh = sc.inverse_transform(predictions_logcosh)
scores = regresor.evaluate(x=x_test, y=y_test, verbose = 0)
print("%s: %.2f%%" % (regresor.metrics_names[1], scores[1]*100))
#regresor.save('LSTM-51.28%accuracy.h5py')




#Compile this network
regresor.compile(optimizer = 'adam', loss='mean_squared_error', metrics=['mse', 'accuracy'])
#Fit the data
regresor.fit(x_train, y_train, epochs=100, batch_size = 32)#, shuffle=False)
#Predict Values
predictions_mse = regresor.predict(x_test)
predictions_mse = sc.inverse_transform(predictions_mse)
regresor.evaluate(x=x_test, y=y_test)
#regresor.save('mse_ok_estimator.h5py')





