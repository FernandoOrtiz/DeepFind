# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 10:26:01 2018

@author: Fernando Ortiz
"""
#general purpose imports
import pandas as pd 
from matplotlib import pyplot
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.callbacks import TensorBoard


#Neural Network Keras Imports
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.optimizers import Adam
from keras import regularizers
from sklearn.preprocessing import StandardScaler



#The amount of time-steps the LSTM will look back at
step = 20
val_dat = 0.2    

train_set = ["D1-30MinuteRun-M2.csv"]
test_set = ["D2-35MinuteRun-M2.csv"]

def to_polar(data):
    for i in range(0, data.shape[0]):
        r = np.sqrt((data[i,0]**2) + (data[i,1]**2))
        t = np.arctan2(data[i,0], data[i,1])
        data[i,0] = r 
        data[i,1] = t
  
      


def setup_data(time_step, dataset):
    global X
    global Y
    global sc
    dataset_copy = list(train_set)                                               #Make a copy of the list so you do not alter it
    dataset_total = pd.read_csv("../Datasets/"+dataset_copy.pop(0))            #Pop the first element out
    for element in dataset_copy:                                               #If you have additional datasets, keep adding them 
        dataset_total = pd.concat((dataset_total,
                                  pd.read_csv("../Datasets/"+element)),
                                  axis=0)
    dataset_total = dataset_total.as_matrix()                                
    
    scaler = StandardScaler(copy=True, with_mean=True, with_std=True )
    dataset_total[:,2:] = scaler.fit_transform(dataset_total[:,2:])
    
    #Reshappe the inpputt so it fits the neural network
    X = []
    for i in range(1, time_step):
        X.append(np.concatenate((np.zeros((time_step-i, dataset_total.shape[1]-2)), dataset_total[0:i, 2:]), axis = 0))
    
    
    for i in range(time_step-1, int(dataset_total.size/dataset_total.shape[1])):
        X.append(dataset_total[i-time_step+1 : i+1 , 2:])
    X = np.array(X)
    
    
    #Extract the output of the neural network
    #y = dataset_total.iloc[time_step-1:,0:2]
    Y = dataset_total[0:,0:2]
    to_polar(Y)
    #Feature Scaling
    sc = MinMaxScaler(feature_range = (-1,1))
    Y = sc.fit_transform(Y)

def setup_Val_data(time_step, dataset):
   global X
   global Y
   global sc
   dataset_copy = list(train_set)                                               #Make a copy of the list so you do not alter it
   dataset_total = pd.read_csv("../Datasets/"+dataset_copy.pop(0))            #Pop the first element out
   for element in dataset_copy:                                               #If you have additional datasets, keep adding them 
       dataset_total = pd.concat((dataset_total,
                                 pd.read_csv("../Datasets/"+element)),
                                 axis=0)
   dataset_total = dataset_total.as_matrix()                                

   scaler = StandardScaler(copy=True, with_mean=True, with_std=True )
   dataset_total[:,2:] = scaler.fit_transform(dataset_total[:,2:])

   #Reshappe the inpputt so it fits the neural network
   X = []
   for i in range(1, time_step):
       X.append(np.concatenate((np.zeros((time_step-i, dataset_total.shape[1]-2)), dataset_total[0:i, 2:]), axis = 0))


   for i in range(time_step-1, int(dataset_total.size/dataset_total.shape[1])):
       X.append(dataset_total[i-time_step+1 : i+1 , 2:])
   X = np.array(X)


   #Extract the output of the neural network
   #y = dataset_total.iloc[time_step-1:,0:2]
   Y = dataset_total[0:,0:2]
   to_polar(Y)
   #Feature Scaling
   sc = MinMaxScaler(feature_range = (-1,1))
   Y = sc.fit_transform(Y)

setup_data(step, train_set)




#Initialization and Creation of the RNN

network = Sequential()
network.add(LSTM(units = 80, return_sequences = True, input_shape = (X.shape[1], X.shape[2]),dropout= 0.002,recurrent_dropout=0.002, activation = 'relu', recurrent_regularizer = regularizers.l2(0.01)))
#network.add(Dropout(0.2))
#network.add(Dense(units = 30, activation = 'tanh'))

# Adding a second LSTM layer and some Dropout regularisation
#network.add(LSTM(units = 40, return_sequences = True,dropout= 0.02,recurrent_dropout=0.02, activation = 'relu', recurrent_regularizer = regularizers.l2(0.01)))
#network.add(Dropout(0.2))
#network.add(Dense(units = 20, activation = 'tanh'))

# Adding a second LSTM layer and some Dropout regularisation
#network.add(LSTM(units = 40, return_sequences = True,dropout= 0.02,recurrent_dropout=0.02, activation = 'relu', recurrent_regularizer = regularizers.l2(0.01)))
#network.add(Dropout(0.2))
#network.add(Dense(units = 20, activation = 'tanh'))

# Adding a third LSTM layer and some Dropout regularisation
#network.add(LSTM(units = 40, return_sequences = True,dropout= 0.02,recurrent_dropout=0.02, activation = 'relu', recurrent_regularizer = regularizers.l2(0.01)))
#network.add(Dropout(0.2))
#network.add(Dense(units = 20, activation = 'tanh'))

# Adding a fourth LSTM layer and some Dropout regularisation
network.add(LSTM(units = 80,dropout= 0.002,recurrent_dropout=0.002, activation = 'relu', recurrent_regularizer = regularizers.l2(0.01)))
#network.add(Dropout(0.2))

#network.add(Dense(units = 10, activation = 'tanh'))

# Adding the output layer
network.add(Dense(units = 2, activation = 'linear',kernel_regularizer = regularizers.l2(0.000001)))


#Validate the neural net
network.compile(optimizer = Adam(lr=0.0015), loss='logcosh', metrics=['accuracy','mae'])
#call_back = TensorBoard(log_dir='../',write_graph=True)
history = network.fit(X, Y, validation_split=val_dat, epochs=150, batch_size = 64) 
#print(history.history['loss'])
#print(history.history['acc'])
#print(history.history['val_loss'])
#print(history.history['val_acc'])

setup_Val_data(step, test_set)
scores = network.evaluate(X,Y)
print("\n%s: %.2f%%" %(network.metrics_names[1],scores[1]*100))
#%%Evaluate the model

#Plot this data

pyplot.plot(history.history['loss'])
pyplot.plot(history.history['val_loss'])
pyplot.title('model train vs validation loss')
pyplot.ylabel('loss')
pyplot.xlabel('epoch')
pyplot.legend(['train', 'validation'], loc='upper right')
pyplot.show()

pyplot.plot(history.history['acc'])
pyplot.plot(history.history['val_acc'])
pyplot.title('model train vs validation acc')
pyplot.ylabel('loss')
pyplot.xlabel('epoch')
pyplot.legend(['train', 'validation'], loc='upper right')
pyplot.show()

max(history.history['val_acc'])


#regresor = load_model('2LSTM-3ANN-100weights.81-0.8876.hdf5')

if(network.input_shape[1] != step):
    setup_data(network.input_shape[1])

slice_index = int(X.shape[0]*(1-val_dat))
prediction = network.predict(x=X[slice_index:,0:,0:])
prediction = sc.inverse_transform(prediction)
expected_outcome = sc.inverse_transform(Y[slice_index:,:])

   

pyplot.plot(expected_outcome[0:, 0:1])
pyplot.plot(prediction[0:,0:1])
pyplot.title('predictions vs expected outcome')
pyplot.ylabel('measurement')
pyplot.xlabel('meters')
pyplot.legend(['prediction', 'expected outcome'], loc='upper right')
pyplot.show()


pyplot.plot(expected_outcome[0:, 1:2])
pyplot.plot(prediction[0:,1:2])
pyplot.title('predictions vs expected outcome')
pyplot.ylabel('measurement')
pyplot.xlabel('meters')
pyplot.legend(['prediction', 'expected outcome'], loc='upper right')
pyplot.show()
setup_data(step)

#%%


#Save the trained model
#network.save('LSTM-70%accuracy-Good-Predictions-Fer.h5py')