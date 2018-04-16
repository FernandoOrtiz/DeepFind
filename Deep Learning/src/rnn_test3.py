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
from keras.optimizers import Adam
from sklearn.model_selection import KFold


#Import the training set
training_set = pd.read_csv("../Datasets/Training_Data - Copy2.csv")
#Obtain the test Data
test_set = pd.read_csv("../Datasets/Test_Data - Copy3.csv")
#Merge both test and train to obtain initial values
dataset_total = pd.concat((training_set, test_set), axis = 0)

#Reshappe the inpputt so it fits the neural network
step = 60

X = []
for i in range(step-1, int(dataset_total.size/dataset_total.shape[1])):
    X.append(dataset_total.as_matrix()[i-step+1 : i+1 , 2:])
X = np.array(X)


#Extract the output of the neural network
Y = dataset_total.iloc[step-1:,0:2]
Y = Y.as_matrix()
#Feature Scaling
sc = MinMaxScaler(feature_range = (-1,1))
Y = sc.fit_transform(Y)


#Initialization and Creation of the RNN

network = Sequential()
network.add(LSTM(units = 40, return_sequences = True, input_shape = (X.shape[1], X.shape[2])))
#network.add(Dropout(0.2))
#network.add(Dense(units = 40, activation = 'tanh'))

# Adding a second LSTM layer and some Dropout regularisation
#network.add(LSTM(units = 20, return_sequences = True))
#network.add(Dropout(0.2))
#network.add(Dense(units = 20, activation = 'tanh'))

# Adding a second LSTM layer and some Dropout regularisation
#network.add(LSTM(units = 20, return_sequences = True))
#network.add(Dropout(0.2))
#network.add(Dense(units = 20, activation = 'tanh'))

# Adding a third LSTM layer and some Dropout regularisation
#network.add(LSTM(units = 20, return_sequences = True))
#network.add(Dropout(0.2))
#network.add(Dense(units = 20, activation = 'tanh'))

# Adding a fourth LSTM layer and some Dropout regularisation
network.add(LSTM(units = 40))
#network.add(Dropout(0.2))

#network.add(Dense(units = 20, activation = 'tanh'))

# Adding the output layer
network.add(Dense(units = 2, activation = 'tanh'))


#Validate the neural net
network.compile(optimizer = Adam(lr=0.0002), loss='logcosh', metrics=['accuracy'])
history = network.fit(X, Y, validation_split=0.2, epochs=150, batch_size = 64) 
#print(history.history['loss'])
#print(history.history['acc'])
#print(history.history['val_loss'])
#print(history.history['val_acc'])

#diagnose the system 
pyplot.plot(history.history['loss'])
pyplot.plot(history.history['val_loss'])
pyplot.title('model train vs validation loss')
pyplot.ylabel('loss')
pyplot.xlabel('epoch')
pyplot.legend(['train', 'validation'], loc='upper right')
pyplot.show()

#Save the trained model
#regresor.save('LSTM-51.28%accuracy.h5py')