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

#Neural Network Keras Imports
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

#Set Training Data 
data_set = pd.read_csv('')
training_set = data_set.iloc[:, 1:2].values

#data structure
X=[]
Y=[]
for i in range(60, 1258):
    X.append(training_set[i-60:i, 0])
    Y.append(training_set[i, 0])
X, Y = np.array(X), np.array(Y)

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