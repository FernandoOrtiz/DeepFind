# -*- coding: utf-8 -*-
"""
Spyder Editor

Fernando Ortiz
RNN Implementation
"""
#general purpose imports
import pandas as pd 

#Neural Network Keras Imports
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

#Set Training Data 
data_set = pd.read_csv('')
training_set = dataset_train.iloc[:].values


#Initialization and Creation of the RNN
network = Sequential()
network.add()

#verify the history of the training
network.compile(optimizer = 'adam', loss='logcosh', metrics=['accuracy'])
history = network.fit(X,Y, epochs = 100)
print(history.history['loss'])
print(history.history['acc'])

#Validate the neural net
network.compile(optimizer = 'adam', loss='logcosh', metrics=['accuracy'])
history = network.fit(X, Y, epochs=100, validation_split=0.33)
print(history.history['loss'])
print(history.history['acc'])
print(history.history['val_loss'])
print(history.history['val_acc'])
