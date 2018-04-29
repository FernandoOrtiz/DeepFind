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



#The amount of time-steps the LSTM will look back at
step = 20
val_dat = 1

def setup_data(time_step):
    global X
    global Y
    global sc
    #Import the training set
    #train_dataset = pd.read_csv("../Datasets/Training_Data - Copy2.csv")
    #Obtain the test Data
    #test_dataset = pd.read_csv("../Datasets/Test_Data - Copy3.csv")
    #Merge both test and train to obtain initial values
    #dataset_total = pd.concat((train_dataset, test_dataset), axis = 0)
    dataset_total = pd.read_csv("../Datasets/30MinuteRun-M1.csv")
    dataset_total = dataset_total.as_matrix()
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
    #Feature Scaling
    sc = MinMaxScaler(feature_range = (-1,1))
    Y = sc.fit_transform(Y)


setup_data(step)





#Initialization and Creation of the RNN

network = Sequential()
network.add(LSTM(units = 30, return_sequences = True, input_shape = (X.shape[1], X.shape[2]),dropout= 0,recurrent_dropout=0))
#network.add(Dropout(0.2))
#network.add(Dense(units = 30, activation = 'tanh'))

# Adding a second LSTM layer and some Dropout regularisation
#network.add(LSTM(units = 30, return_sequences = True,dropout= 0,recurrent_dropout=0))
#network.add(Dropout(0.2))
#network.add(Dense(units = 20, activation = 'tanh'))

# Adding a second LSTM layer and some Dropout regularisation
#network.add(LSTM(units = 20, return_sequences = True,dropout= 0.2,recurrent_dropout=0.2))
#network.add(Dropout(0.2))
#network.add(Dense(units = 20, activation = 'tanh'))

# Adding a third LSTM layer and some Dropout regularisation
#network.add(LSTM(units = 20, return_sequences = True,dropout= 0.2,recurrent_dropout=0.2))
#network.add(Dropout(0.2))
#network.add(Dense(units = 20, activation = 'tanh'))

# Adding a fourth LSTM layer and some Dropout regularisation
network.add(LSTM(units = 30,dropout= 0,recurrent_dropout=0))
#network.add(Dropout(0.2))

#network.add(Dense(units = 10, activation = 'tanh'))

# Adding the output layer
network.add(Dense(units = 2, activation = 'tanh'))


#Validate the neural net
network.compile(optimizer = Adam(lr=0.002), loss='logcosh', metrics=['accuracy'])
#call_back = TensorBoard(log_dir='../',write_graph=True)
history = network.fit(X, Y, validation_split=1, epochs=50, batch_size = 64) 
#print(history.history['loss'])
#print(history.history['acc'])
#print(history.history['val_loss'])
#print(history.history['val_acc'])
scores = network.evaluate(X,Y)
print("\n%s: %.2f%%" %(network.metrics_names[1],scores[1]*100))
#%%Evaluate the model

#Plot this data

#pyplot.plot(history.history['loss'])
#pyplot.plot(history.history['val_loss'])
#pyplot.title('model train vs validation loss')
#pyplot.ylabel('loss')
#pyplot.xlabel('epoch')
#pyplot.legend(['train', 'validation'], loc='upper right')
#pyplot.show()
#
#pyplot.plot(history.history['acc'])
#pyplot.plot(history.history['val_acc'])
#pyplot.title('model train vs validation acc')
#pyplot.ylabel('loss')
#pyplot.xlabel('epoch')
#pyplot.legend(['train', 'validation'], loc='upper right')
#pyplot.show()
#
#max(history.history['val_acc'])


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