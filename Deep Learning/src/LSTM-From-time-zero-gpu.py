"""
Created on Sun Apr 15 13:56:18 2018

@author: Rathk
"""

#model_number = 0


#%%
# Jose's Recurrent Neural Network
#Pre-process the data
import numpy as np
from matplotlib import pyplot
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.layers import CuDNNLSTM
from keras.layers import CuDNNGRU
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import Activation
from keras.optimizers import Nadam
from keras.optimizers import Adam
from keras.regularizers import l1
from keras.regularizers import l2
from keras.callbacks import ModelCheckpoint
from keras.callbacks import TensorBoard


#Fix for kernel starting error. Provided by:
#https://stackoverflow.com/questions/47068709/your-cpu-supports-instructions-
#that-this-tensorflow-binary-was-not-compiled-to-u?utm_medium=organic&utm_
#source=google_rich_qa&utm_campaign=google_rich_qa
# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#os.environ["CUDA_VISIBLE_DEVICES"]="0"


 

#Fix to limit gpu memory usage. Provided by:
#https://michaelblogscode.wordpress.com/2017/10/10/
#reducing-and-profiling-gpu-memory-usage-in-keras-with-tensorflow-backend/
## extra imports to set GPU options
import tensorflow as tf
from keras import backend as k
###################################
# TensorFlow wizardry
config = tf.ConfigProto()
 
# Don't pre-allocate memory; allocate as-needed
config.gpu_options.allow_growth = True
 
# Only allow a total of half the GPU memory to be allocated
config.gpu_options.per_process_gpu_memory_fraction = 0.5
 
# Create a session with the above options specified.
k.tensorflow_backend.set_session(tf.Session(config=config))
###################################



#%%
#The amount of time-steps the LSTM will look back at
time_step = 39
val_split = 0.2    

train_set = ["20MinuteRun-M2.csv", "30MinuteRun-M2.csv"]
test_set = ["30MinuteRun-M2.csv"]
                           
def to_polar(data):
    for i in range(0, data.shape[0]):
        r = np.sqrt((data[i,0]**2) + (data[i,1]**2))
        t = np.arctan2(data[i,0], data[i,1])
        data[i,0] = r 
        data[i,1] = t

def setup_data(time_step, dataset):
    global x
    global y
    global out_sc
    dataset_copy = list(train_set)                                               #Make a copy of the list so you do not alter it
    dataset_total = pd.read_csv("../Datasets/"+dataset_copy.pop(0))            #Pop the first element out
    for element in dataset_copy:                                               #If you have additional datasets, keep adding them 
        dataset_total = pd.concat((dataset_total,
                                  pd.read_csv("../Datasets/"+element)),
                                  axis=0)
    dataset_total = dataset_total.as_matrix()                                  #Convert into numpy array 
    #Reshappe the inpputt so it fits the recurrent neural network
    x = []
    for i in range(1, time_step):                                              #Pad initial values with zeros 
        x.append(np.concatenate((np.zeros((time_step-i, 
                 dataset_total.shape[1]-2)), dataset_total[0:i, 2:]), 
                 axis = 0))
    
    
    for i in range(time_step-1,int(dataset_total.size/dataset_total.shape[1])):
        x.append(dataset_total[i-time_step+1 : i+1 , 2:])
    x = np.array(x)
    in_sc = StandardScaler()
    x = 
    
    #Extract the output of the neural network
    y = dataset_total[0:,0:2]
    #y = np.subtract(y, np.array([y[0,0], y[0,1]]))
    to_polar(y)
    #Feature Scaling
    out_sc = MinMaxScaler(feature_range = (-1,1))
    y = out_sc.fit_transform(y)

setup_data(time_step, train_set)


#%% Part 2 - Building the RNN
###############################################################################
units = 41
dropout = 0.2
regularizer_k = 0.00001
regularizer_r = 0.0001

#Initialize the model
regresor = Sequential()

#First Layer  -----------------------------------------------------------------
#Note that this is the only layer with input_shape
#Should only use one of these

#LSTM First layer
regresor.add(CuDNNLSTM(units = units, unit_forget_bias=False,
                       recurrent_regularizer = l2(regularizer_r),
                       return_sequences = True, 
                       input_shape=(x.shape[1], x.shape[2])))

#ANN First Layer
#regresor.add(Dense(units = units, activation = 'tanh', 
#                   input_shape=(x.shape[1], x.shape[2])))
#------------------------------------------------------------------------------


#Middle layers-----------------------------------------------------------------
#They are connected in sequence, ordered in tuples of LSTM, ANN


#Second Layer----------------------------------#
#LSTM
regresor.add(CuDNNLSTM(units = units, unit_forget_bias=False,
                       recurrent_regularizer = l2(regularizer_r),
                       return_sequences = True))
regresor.add(Activation('tanh'))
#ANN
#regresor.add(Dense(units = units, activation = None))
#regresor.add(Dropout(dropout))
#----------------------------------------------#


#Third Layer----------------------------------#
#LSTM
#regresor.add(CuDNNLSTM(units = units, unit_forget_bias=False,
#                       recurrent_regularizer = l2(regularizer_r),
#                       return_sequences = True))
#ANN
#regresor.add(Dense(units = units, activation = 'tanh'))
#regresor.add(Dropout(dropout))
#----------------------------------------------#


#Fourth Layer----------------------------------#
#LSTM
#regresor.add(CuDNNLSTM(units = units,  
#                  return_sequences = True))
#ANN
#regresor.add(Dense(units = units, activation = 'tanh'))
#regresor.add(Dropout(dropout))
#----------------------------------------------#


#Fifth Layer----------------------------------#
#LSTM
#regresor.add(CuDNNLSTM(units = units, unit_forget_bias=False,
#                       recurrent_regularizer = l2(regularizer_r),
#                       return_sequences = True))
#ANN
#regresor.add(Dense(units = units, activation = 'tanh'))
#regresor.add(Dropout(dropout))
#----------------------------------------------#


#Sixth Layer----------------------------------#
#LSTM
#regresor.add(CuDNNLSTM(units = units, unit_forget_bias=False,
#                       recurrent_regularizer = l2(regularizer_r),
#                       return_sequences = True))
#ANN
#regresor.add(Dense(units = units, kernel_regularizer=l2(regularizer_c),
#                   use_bias=False, activation = 'tanh'))
#regresor.add(Dropout(dropout))
#----------------------------------------------#


#Additional ANN Layers----------------------------------#
#ANN
#regresor.add(Dense(units = units, activation = 'relu'))
#regresor.add(Dropout(dropout))
#ANN
#regresor.add(Dense(units = int(units/2), activation = 'sigmoid'))
#ANN
#regresor.add(Dense(units = units, activation = 'tanh'))
#ANN
regresor.add(Dense(units = units, kernel_regularizer=l2(regularizer_k),
                   activation = 'tanh'))
#regresor.add(Dense(units = units*2, kernel_regularizer=l2(regularizer_k),
#                   activation = 'tanh'))
#----------------------------------------------#


#------------------------------------------------------------------------------


#Output Layer------------------------------------------------------------------
#LSTM last layer
regresor.add(CuDNNLSTM(units = 2, unit_forget_bias=False,
                       recurrent_regularizer = l2(regularizer_r)))
regresor.add(Activation('tanh'))

#ANN Last Layer
#regresor.add(Dense(units = 2, kernel_regularizer=l2(regularizer_c),
#                   activation = 'tanh', use_bias = False))
#------------------------------------------------------------------------------


#Compile this network----------------------------------------------------------
regresor.compile(optimizer = Adam(lr=0.003), loss='mse', 
                 metrics=['mae', 'acc', 'mse'])
#------------------------------------------------------------------------------


#Callback Declarations---------------------------------------------------------
#Calbacks are used to alter the behaviour of the training. Descriptions of each
#function is provided bellow

#ModelCheckpoint - saves the data when a specific value is a its best
save_data = ModelCheckpoint('../Models/BigData_GPU_5LSTM_3ANN.\
{epoch:02d}-{val_acc:.4f}.hdf5', 
          monitor='val_acc',save_best_only=True)

#Tensoroard - Saves the output of the training so it can be visualized in
#tensorboard
#tensorboard_cb = TensorBoard(log_dir='../tensorboard_logs/{}'
#.format(model_number), histogram_freq=0, batch_size=32, write_graph=True,
# write_grads=True, write_images=False, embeddings_freq=0, 
# embeddings_layer_names=None, embeddings_metadata=None)
#model_number += 1 

#ReduceLROnPlateau - lowers the 
#plateau_cb = ReduceLROnPlateau(monitor='loss', factor=0.5, patience=10, 
#verbose=0, mode='auto', cooldown=0, min_lr=0)   
#------------------------------------------------------------------------------


#Train the model---------------------------------------------------------------
#Fit the data
history = regresor.fit(x, y, epochs = 400, validation_split = val_split,
          callbacks= [], batch_size = 10000) 


#Save the network if it is good------------------------------------------------
#regresor.save('Big_Data_LSTM-no-out-dense.h5py')


#%%Evaluate the model

#Plot this data

pyplot.plot(history.history['loss'])
pyplot.plot(history.history['val_loss'])
pyplot.title('model train vs validation loss')
pyplot.ylabel('loss')
pyplot.xlabel('epoch')
pyplot.legend(['train', 'validation'], loc='upper right')
pyplot.show()

"""
pyplot.plot(history.history['mean_absolute_error'])
pyplot.plot(history.history['val_mean_absolute_error'])
pyplot.title('model train vs validation acc')
pyplot.ylabel('loss')
pyplot.xlabel('epoch')
pyplot.legend(['train', 'validation'], loc='upper right')
pyplot.show()
"""

max(history.history['val_acc'])

#%%
#regresor = load_model('../Models/BigData_GPU_5LSTM_3ANN.16-0.8915.hdf5')

if(regresor.input_shape[1] != time_step):
    setup_data(regresor.input_shape[1], train_set)

slice_index = int(x.shape[0]*(1-val_split))
prediction = regresor.predict(x=x[slice_index:,0:,0:])
prediction = out_sc.inverse_transform(prediction)
expected_outcome = out_sc.inverse_transform(y[slice_index:,:])
#expected_outcome = y[slice_index:,:]

pyplot.plot(expected_outcome[0:, 0:1])
pyplot.plot(prediction[0:,0:1])
pyplot.title('Validation: Magnitud')
pyplot.ylabel('meters')
pyplot.xlabel('measurement')
pyplot.legend(['expected outcome', 'prediction'], loc='upper right')
pyplot.show()

pyplot.plot(expected_outcome[0:, 1:2])
pyplot.plot(prediction[0:,1:2])
pyplot.title('Validation: Angle')
pyplot.ylabel('radians')
pyplot.xlabel('measurement')
pyplot.legend(['expected outcome', 'prediction'], loc='upper right')
pyplot.show()

#%%
#Test neural networks performance with entirely new dataset

#Verify that the data is configures to the appropriate amount of timesteps
if(regresor.input_shape[1] != time_step):
    setup_data(regresor.input_shape[1], test_set)
else:
    setup_data(time_step, test_set)

slice_index = int(x.shape[0]*(1-val_split))
prediction = regresor.predict(x=x[slice_index:slice_index+1,0:,0:])
prediction = out_sc.inverse_transform(prediction)
expected_outcome = out_sc.inverse_transform(y[slice_index:,:])
#expected_outcome = y[slice_index:,:]


pyplot.plot(expected_outcome[0:, 0:1])
pyplot.plot(prediction[0:,0:1])
pyplot.title('Test X')
pyplot.ylabel('meters')
pyplot.xlabel('measurement')
pyplot.legend(['expected outcome', 'prediction'], loc='upper right')
pyplot.show()

pyplot.plot(expected_outcome[0:, 1:2])
pyplot.plot(prediction[0:,1:2])
pyplot.title('Test Dataset: Angle')
pyplot.ylabel('radians')
pyplot.xlabel('measurement')
pyplot.legend(['expected outcome', 'prediction'], loc='upper right')
pyplot.show()
#setup_data(time_step, train_set)


