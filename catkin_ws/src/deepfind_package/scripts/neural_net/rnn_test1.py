# -*- coding: utf-8 -*-
"""
Spyder Editor

Fernando Ortiz
RNN Implementation
"""
#general purpose imports
import pandas as pd 
from matplotlib import pyplot

#Neural Network Keras Imports
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

#Set Training Data 
data_set = pd.read_csv('')
training_set = dataset_train.iloc[:, 1:2].values

#data structure
X=[]
Y=[]
for i in range(60, 1258):
    X.append(training_set_scaled[i-60:i, 0])
    Y.append(training_set_scaled[i, 0])
X, Y = np.array(X), np.array(Y)

# Reshaping
X = np.reshape(X, (X.shape[0], X.shape[1], 1))


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
history = network.fit(X, Y, epochs=100, validation_split=0)
print(history.history['loss'])
print(history.history['acc'])
print(history.history['val_loss'])
print(history.history['val_acc'])

#diagnose the system
history = network.fit(X, Y, epochs=100, validation_data=(valX, valY))
pyplot.plot(history.history['loss'])
pyplot.plot(history.history['val_loss'])
pyplot.title('model train vs validation loss')
pyplot.ylabel('loss')
pyplot.xlabel('epoch')
pyplot.legend(['train', 'validation'], loc='upper right')
pyplot.show()