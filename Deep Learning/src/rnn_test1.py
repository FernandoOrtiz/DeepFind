# -*- coding: utf-8 -*-
"""
Spyder Editor

Fernando Ortiz
RNN Implementation
"""
#general purpose imports
import pandas as pd 
from matplotlib import pyplot
import numpy as np
from sklearn.preprocessing import MinMaxScaler


#Neural Network Keras Imports
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

#Set Training & test Data 
training_set = pd.read_csv("Training_Data - Copy2.csv")
test_set = pd.read_csv("Test_Data - Copy3.csv")

#Merge both test and train to obtain initial values
dataset_total = pd.concat((training_set, test_set), axis = 0)
sc = MinMaxScaler(feature_range = (-1,1))
sc.fit(dataset_total.iloc[:,0:2].as_matrix())

#Extract the inputs to the neural nework
training_input_set = training_set.iloc[:,2:376]
training_input_set = training_input_set.as_matrix() 


#data structure
X=[]
Y=[]
for i in range(60, int(training_input_set.size/training_input_set.shape[1])):
    X.append(training_input_set[i-60 : i , 0:])
X= np.array(X)

# Reshaping
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

#Initialization and Creation of the RNN
network = Sequential()
network.add(LSTM(units = 30, return_sequences = True, input_shape = (X.shape[1], 1)))
network.add(Dropout(0.5))

# Adding a second LSTM layer and some Dropout regularisation
network.add(LSTM(units = 30, return_sequences = True))
network.add(Dropout(0.5))

# Adding a third LSTM layer and some Dropout regularisation
network.add(LSTM(units = 30, return_sequences = True))
network.add(Dropout(0.5))

# Adding a fourth LSTM layer and some Dropout regularisation
network.add(LSTM(units = 30))
network.add(Dropout(0.5))

# Adding the output layer
network.add(Dense(units = 1))


#verify the history of the training
network.compile(optimizer = 'adam', loss='logcosh', metrics=['accuracy'])
history = network.fit(X,Y, epochs = 100)
print(history.history['loss'])
print(history.history['acc'])

#Validate the neural net
network.compile(optimizer = 'adam', loss='logcosh', metrics=['accuracy'])
history = network.fit(X, Y, epochs=100, validation_split=0.4)
print(history.history['loss'])
print(history.history['acc'])
print(history.history['val_loss'])
print(history.history['val_acc'])

#diagnose the system
history = network.fit(X, Y, epochs=100, validation_data=(X, Y))
pyplot.plot(history.history['loss'])
pyplot.plot(history.history['val_loss'])
pyplot.title('model train vs validation loss')
pyplot.ylabel('loss')
pyplot.xlabel('epoch')
pyplot.legend(['train', 'validation'], loc='upper right')
pyplot.show()