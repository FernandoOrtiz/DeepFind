"""
Created on Sun Apr 15 13:56:18 2018

@author: Rathk
"""

# Jose's Recurrent Neural Network
#Pre-process the data
import numpy as np
from matplotlib import pyplot
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.layers import CuDNNLSTM
from keras.layers import Dropout
from keras.optimizers import Nadam
from keras.callbacks import ModelCheckpoint
from sklearn.model_selection import KFold


#The amount of time-steps the LSTM will look back at
time_step = 15


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
units =100
dropout = 0.2
val_split = 0.15


#Build rnn
regresor = Sequential()

#First Layer -- LSTM layer with dropout regularization -- dunno what that means
#Note that this is the only layer with input_shape
regresor.add(CuDNNLSTM(units = units, return_sequences = True, 
                   input_shape=(x.shape[1], x.shape[2])))
regresor.add(Dropout(dropout))


#Second layers with dropout regularization
#regresor.add(CuDNNLSTM(units = units, return_sequences = False))
#regresor.add(Dropout(dropout))

#Third layers with dropout regularization
#regresor.add(CuDNNLSTM(units = units   , return_sequences = True)) 
#regresor.add(Dropout(dropout))

#Fourth layers with dropout regularization
#regresor.add(CuDNNLSTM(units = units   , return_sequences = True)) 
#regresor.add(Dropout(dropout))



#Fifth layers with dropout regularization
regresor.add(CuDNNLSTM(units = units))
regresor.add(Dropout(dropout))


#Output Layer
regresor.add(Dense(units = units, activation = 'relu'))


#Output Layer
regresor.add(Dense(units = units, activation = 'tanh'))



#Output Layer
regresor.add(Dense(units = 2, activation = 'tanh'))

#Compile this network
regresor.compile(optimizer = Nadam(lr=0.0025), loss='logcosh', metrics=['accuracy'])

#Fit the data
history = regresor.fit(x, y, validation_split=val_split, epochs=400, callbacks=
          [ModelCheckpoint('2LSTM-3ANN-100weights.{epoch:02d}-{val_acc:.4f}.hdf5', 
          monitor='val_acc',save_best_only=True)], batch_size = 32) 
#regresor.save('LSTM-2stack-2ANN-adam-74.51%accuracy.h5py')
 

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


#regresor = load_model('2LSTM-3ANN-weights.179-0.89.hdf5')

slice_index = int(x.shape[0]*(1-val_split))
regresor.evaluate(x=x[slice_index:,0:,0:], y=y[slice_index:,0:])
prediction = regresor.predict(x=x[slice_index:,0:,0:])
prediction = sc.inverse_transform(prediction)
expected_outcome = sc.inverse_transform(y[slice_index:,:])

   
