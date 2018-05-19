"""
Created on Sun Apr 15 13:56:18 2018

@author: Rathk
"""


#%% Impport and cofigure environment variables---------------------------------
###############################################################################

# Jose's Recurrent Neural Network
#Pre-process the data
import numpy as np
import os, os.path
import pandas as pd
import tensorflow as tf
import dl_utils
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
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
from keras import backend as k


#Fix for kernel starting error. Provided by:
#https://stackoverflow.com/questions/47068709/your-cpu-supports-instructions-
#that-this-tensorflow-binary-was-not-compiled-to-u?utm_medium=organic&utm_
#source=google_rich_qa&utm_campaign=google_rich_qa
# Just disables the warning, doesn't enable AVX/FMA
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#os.environ["CUDA_VISIBLE_DEVICES"]="0"
#------------------------------------------------------------------------------
#Fix to limit gpu memory usage. Provided by:
#https://michaelblogscode.wordpress.com/2017/10/10/
#reducing-and-profiling-gpu-memory-usage-in-keras-with-tensorflow-backend/
## extra imports to set GPU options
# TensorFlow wizardry
config = tf.ConfigProto()
# Don't pre-allocate memory; allocate as-needed
config.gpu_options.allow_growth = True
# Only allow a total of half the GPU memory to be allocated
config.gpu_options.per_process_gpu_memory_fraction = 0.5
# Create a session with the above options specified.
k.tensorflow_backend.set_session(tf.Session(config=config))


#%%Parameter configuration-----------------------------------------------------
###############################################################################

DIR = '../Models/'
time_step = 1
val_split = 0.2    
polar_output = True
scale_input = False
scale_output = True
units = 17
r_units = 100
dropout = 0.0
regularizer_k = 0.001
regularizer_r = 0.001
optimizer = 'adam'
epochs = 750
batch_size = 10000
loss = 'mae'
metrics = ['mae','mse']
input_format = "F3"
zero_pad = False

#%% Variable Setup colllection-------------------------------------------------
###############################################################################

#Next two help to define the save name of the model
#What the system outputs
model_output = 'CaRT'
if(polar_output):
    model_output = 'PoLR'
 
#Determine what is being scaled
if(scale_output):
    out_sc_name = 'OT'
else:
    out_sc_name = 'OF'
if(scale_input):
    in_sc_name = 'IT'
else:
    in_sc_name = 'IF'

#Choose dataset based on desired input format
if(input_format == "F3"):
    train_set = ["D1-MegaSet-F3.csv"]
    test_set = ["D2-TestSet-F3.csv"]

elif(input_format == "F2"):    
    train_set = ["D1-30MinuteRun-F2.csv", 
                 "D3-30MinuteStillRun-F2.csv",
                 "D13-60MinuteStillRun-F2.csv",
                 "D2-35MinuteRun-F2.csv",          
                 "D9-60-MinuteRun-F2.csv",
                 "D10-30MinuteRun-F2.csv",
                 "D11-30MinuteRun-F2.csv",
                 "D12-25MinuteRun-F2.csv",
                 "D8-60MinuteRun-F2.csv",
                 "D7-60MinuteRun-F2.csv"]  
    test_set = [#"D2-35MinuteRun-F2.csv"]
                "D4-18MinuteRun-F2.csv"]

else:
    raise ValueError("Invalid format: " + input_format)
    
#Prepare the validation dataset
val_data_x, val_data_y, val_out_sc = dl_utils.setup_data(time_step, test_set, 
                                     scale_output=scale_output,
                                     scale_input= scale_input,
                                     polar_output=polar_output,
                                     zero_pad=zero_pad)

#Prepare the generator of the training dataset
data_generator = dl_utils.setup_data_generator(train_set, batch_size=batch_size, 
                                 time_step=time_step,
                                 scale_output=scale_output,
                                 scale_input= scale_input,
                                 polar_output=polar_output,
                                 zero_pad=zero_pad)

#Retrieve scalers for data set, also retrieve train set sixe
if(scale_output):
    out_sc, train_dataset_size = dl_utils.get_out_sc(train_set, polar_output,
                                                     zero_pad, time_step)
else:
    out_sc = MinMaxScaler(feature_range=(-1,1))
    _, train_dataset_size = dl_utils.get_out_sc(train_set, polar_output,
                                                zero_pad, time_step)


#%% Configure the model--------------------------------------------------------
###############################################################################

#Initialize the model
regresor = Sequential()

#First Layer  ----------------------------------------------------------------
#Note that this is the only layer with input_shape
#LSTM First layer
regresor.add(CuDNNLSTM(units = r_units, 
                       recurrent_regularizer = l2(regularizer_r),
                       return_sequences = True, 
                       input_shape=(time_step, val_data_x.shape[2])))
#regresor.add(Activation('tanh'))
#ANN First Layer
#regresor.add(Dense(units = 50, activation = 'tanh', 
#                   input_shape=(x.shape[1], )))
#------------------------------------------------------------------------------
#Middle layers-----------------------------------------------------------------
#They are connected in sequence, ordered in tuples of LSTM, ANN
#Second Layer----------------------------------#
#LSTM
#regresor.add(CuDNNLSTM(units = r_units*5, 
#                       recurrent_regularizer = l2(regularizer_r),
#                       return_sequences = True))
#regresor.add(Activation('tanh'))
#ANN
#regresor.add(Dense(units = units, activation = None))
#regresor.add(Dropout(dropout))
#----------------------------------------------#
#Third Layer----------------------------------#
#LSTM
#regresor.add(CuDNNLSTM(units = r_units*5, 
#                       recurrent_regularizer = l2(regularizer_r),
#                       return_sequences = True))
#ANN
#regresor.add(Dense(units = units, activation = 'tanh'))
#regresor.add(Dropout(dropout))
#----------------------------------------------#
#Fourth Layer---------------------------------#
#LSTM
regresor.add(CuDNNLSTM(units = r_units,  
                  return_sequences = False))
regresor.add(Activation('relu'))
#ANN
#regresor.add(Dense(units = units, activation = 'tanh'))
#regresor.add(Dropout(dropout))
#----------------------------------------------#
#Fifth Layer----------------------------------#
#LSTM
#regresor.add(CuDNNLSTM(units = units, 
#                       recurrent_regularizer = l2(regularizer_r),
#                       return_sequences = True))
#regresor.add(Activation('tanh'))
#ANN
#regresor.add(Dense(units = units, activation = 'tanh'))
#regresor.add(Dropout(dropout))
#----------------------------------------------#
#Sixth Layer----------------------------------#
#LSTM
#regresor.add(CuDNNLSTM(units = units, 
#                       recurrent_regularizer = l2(regularizer_r),
#                       return_sequences = True))
#ANN
#regresor.add(Dense(units = units, kernel_regularizer=l2(regularizer_c),
#                   use_bias=False, activation = 'tanh'))
#regresor.add(Dropout(dropout))
#----------------------------------------------#
#Additional ANN Layers------------------------#
#ANN
#regresor.add(Dense(units = units, activation = None, 
#                   kernel_regularizer=l2(regularizer_k)))
#regresor.add(Dropout(dropout))
#ANN
#regresor.add(Dense(units = int(units), activation = 'tanh'))
#ANN
#regresor.add(Dense(units = units, activation = None, 
#                   kernel_regularizer=l2(regularizer_k)))
#ANN
regresor.add(Dense(units = units, kernel_regularizer=l2(regularizer_k),
                  activation = 'linear'))
#regresor.add(Dense(units = units*2, kernel_regularizer=l2(regularizer_k),
#                   activation = 'tanh'))
#------------------------------------------------------------------------------
#Output Layer------------------------------------------------------------------
#LSTM last layer
#egresor.add(CuDNNLSTM(units = 2, recurrent_regularizer = l2(regularizer_r),
#                      return_sequences = False))
#regresor.add(Activation('tanh'))

#ANN Last Layer
regresor.add(Dense(units = 2, kernel_regularizer=l2(regularizer_k),
                   activation = 'linear'))



#Compile this network
regresor.compile(optimizer = optimizer , loss = loss, 
                 metrics = metrics)

#%%Train the model-------------------------------------------------------------
###############################################################################

#Fit the data
finished_training = False
try:
    history = regresor.fit_generator(data_generator, epochs = epochs, 
          validation_data = (val_data_x, val_data_y),
          steps_per_epoch = int(train_dataset_size/batch_size),
          callbacks=None)
    finished_training = True
except KeyboardInterrupt:
    print('Stopped training')
    finished_training = False
#%%Create directories for it---------------------------------------------------
###############################################################################
#Get run count
with open(DIR + 'training_logs.txt','a+') as fh:
    fh.seek(0)
    run_count = fh.read().count('Training session #: ') + 1

#Set save name
try:
    save_name = 'M{}-{}-{}-MAE:{:.3f}-MSE:{:.3f}-{}'.format(run_count,
              model_output, out_sc_name+in_sc_name,
              float(history.history['val_mean_absolute_error'][-1]), 
              float(history.history['val_mean_squared_error'][-1]),
              input_format)
except (NameError, KeyError) as e:
    save_name = 'M{}-{}-{}-MAE:{}-MSE:{}-{}'.format(run_count, 
              model_output, out_sc_name+in_sc_name,
              'x','x',input_format)
SAVE_DIR = DIR + save_name + '/'
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)
else:
    dir_name = input("Model Directory already exists: {} \nInput new name: ".format(save_name))    
    SAVE_DIR = DIR + dir_name + '/'
    while(os.path.exists(SAVE_DIR)):
        dir_name = input("Model Directory already exists, input new name: ")    
        SAVE_DIR = DIR + dir_name + '/'
    os.makedirs(SAVE_DIR)

#%%

if(finished_training):
    dl_utils.plot_history(history, SAVE_DIR, save_name, loss)

test_scores = dl_utils.plot_validation(regresor, validation_x=val_data_x, 
                         validation_y=val_data_y, directory=SAVE_DIR,
                         save_name=save_name, polar_output=polar_output,
                         out_sc=out_sc, out_scaler=scale_output)
save_to_file = dl_utils.save_model_to_file(regresor, out_sc, SAVE_DIR, 
                                           save_name)
dl_utils.save_log(DIR, regresor, run_count, optimizer, metrics, test_scores,
                  time_step, batch_size, dropout, regularizer_k, regularizer_r,
                  loss, epochs, val_split, train_set, test_set, False,
                  scale_input, scale_output, save_name, save_to_file, 
                  finished_training, history=None)



