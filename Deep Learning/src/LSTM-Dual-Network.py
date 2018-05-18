"""
Created on Sun Apr 15 13:56:18 2018

@author: Rathk
"""

#model_number = 0


#%%
# Jose's Recurrent Neural Network
#Pre-process the data
import numpy as np
import os, os.path
import pandas as pd
import tensorflow as tf
import shutil
import matplotlib.pyplot as plt
import gc
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


 

#Fix to limit gpu memory usage. Provided by:
#https://michaelblogscode.wordpress.com/2017/10/10/
#reducing-and-profiling-gpu-memory-usage-in-keras-with-tensorflow-backend/
## extra imports to set GPU options
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

###############################################################################
#%%

DIR = '../Models/'
time_step = 12
val_split = 0.2
ypr = False    
polar = False
in_return_sequence = True
out_return_sequence = False
scale_output = True
units = 10
r_units = 8
dropout = 0.2
regularizer_k = 0.0001
regularizer_r = 0.0001
optimizer = 'adam'
epochs = 150
batch_size = 16536
loss = 'mse'
metrics = ['mae','mse']

train_set = ["D1-MegaSet-F3.csv"]
test_set = ["D2-TestSet-F3.csv"]

"""
train_set = ["D8-60MinuteRun-F2.csv",
             "D3-30MinuteStillRun-F2.csv",
             "D2-35MinuteRun-F2.csv",
             "D9-60-MinuteRun-F2.csv",
             "D13-60MinuteStillRun-F2.csv",
             "D10-30MinuteRun-F2.csv",
             "D11-30MinuteRun-F2.csv",
             "D1-30MinuteRun-F2.csv",
             "D12-25MinuteRun-F2.csv",
             "D7-60MinuteRun-F2.csv"]

test_set = ["D4-18MinuteRun-F2.csv"]
"""


###############################################################################
#%%
#The amount of time-steps the LSTM will look back at

model_output = 'CaRT'
if(polar):
    model_output = 'PoLR'
    if(ypr):
        model_output = 'YpR0'


input_format = train_set[0].split('-')[-1].split('.')[0]
                           
def to_polar(data):
    for i in range(0, data.shape[0]):
        r = np.sqrt((data[i,0]**2) + (data[i,1]**2))
        t = np.arctan2(data[i,0], data[i,1])
        data[i,0] = r 
        data[i,1] = t

def setup_data(time_step, dataset, scale_output):
    dataset_copy = list(dataset)                                             #Make a copy of the list so you do not alter it
    dataset_total = pd.read_csv("../Datasets/"+dataset_copy.pop(0))            #Pop the first element out
    for element in dataset_copy:                                               #If you have additional datasets, keep adding them 
        dataset_total = pd.concat((dataset_total,
                                  pd.read_csv("../Datasets/"+element)), axis=0)
    #Convert into numpy array
    dataset_total = dataset_total.as_matrix()    
    #Extract the output of the neural network
    y_set = dataset_total[0:,0:2]
    x_set = dataset_total[0:,2:]
    
    #in_sc = StandardScaler()
    #x_set = in_sc.fit_transform(x_set)
    
    
    #Reshappe the inpputt so it fits the recurrent neural network
    x = []
    if(in_return_sequence):
        for i in range(1, time_step):                                              #Pad initial values with zeros 
            x.append(np.concatenate((np.zeros((time_step-i, 
                     x_set.shape[1])), x_set[0:i, :]), 
                     axis = 0))
        
        
        for i in range(time_step-1,int(dataset_total.size/dataset_total.shape[1])):
            x.append(x_set[i-time_step+1 : i+1 , :])
        x = np.array(x)
    else:
        x = x_set 
    #y = np.subtract(y, np.array([y[0,0], y[0,1]]))
    if(polar):
        to_polar(y_set)
    #Feature Scaling
    out_sc = MinMaxScaler(feature_range = (-1,1))
    if(scale_output):
        y_set = out_sc.fit_transform(y_set)
    
    if(out_return_sequence):
        y = []
        for i in range(1, time_step):                                              #Pad initial values with zeros 
            y.append(np.concatenate((np.zeros((time_step-i, 
                 y_set.shape[1])), y_set[0:i, :]), 
                 axis = 0))
    
    
        for i in range(time_step-1, int(y_set.size/y_set.shape[1])):
            y.append(y_set[i-time_step+1 : i+1 , :])
        y = np.array(y)
    else:
        y = y_set
    
    
    return x, y, out_sc

x, y, out_sc = setup_data(time_step, train_set, scale_output)

###############################################################################
#%% Part 2 - Building the RNN
###############################################################################
#Setup TODO -



#Initialize the model
regresor_x = Sequential()
regresor_y = Sequential()

#First Layer  ----------------------------------------------------------------
#Note that this is the only layer with input_shape
#Should only use one of these

#LSTM First layer
regresor_x.add(CuDNNLSTM(units = r_units, 
                       recurrent_regularizer = l2(regularizer_r),
                       return_sequences = True, 
                       input_shape=(x.shape[1], x.shape[2])))
regresor_x.add(Activation('tanh'))
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

#Additional ANN Layers----------------------------------#
#ANN
#regresor_x.add(Dense(units = units, activation = 'relu', 
#                   kernel_regularizer=l2(regularizer_k)))
#regresor_x.add(Dropout(dropout))
#ANN
#regresor_x.add(Dense(units = units, activation = 'relu', 
#                   kernel_regularizer=l2(regularizer_k)))
#regresor_x.add(Dropout(dropout))
#ANN
#regresor_x.add(Dense(units = units, activation = 'tanh', 
#                   kernel_regularizer=l2(regularizer_k)))
#regresor_x.add(Dropout(dropout))

#------------------------------------------------------------------------------

#Output Layer------------------------------------------------------------------
#LSTM last layer
regresor_x.add(CuDNNLSTM(units = r_units, recurrent_regularizer = l2(regularizer_r),
                       return_sequences = out_return_sequence))
#regresor.add(Activation('tanh'))

#ANN Last Layer
regresor_x.add(Dense(units = 1, kernel_regularizer=l2(regularizer_k),
                   activation = 'linear'))
#------------------------------------------------------------------------------


#Compile this network---------------------------------------------------------
regresor_x.compile(optimizer = optimizer , loss = loss, 
                 metrics = metrics)

#------------------------------------------------------------------------------

#####################################$$$$######################################

#First Layer  ----------------------------------------------------------------
#Note that this is the only layer with input_shape
#Should only use one of these

#LSTM First layer
regresor_y.add(CuDNNLSTM(units = r_units, 
                       recurrent_regularizer = l2(regularizer_r),
                       return_sequences = True, 
                       input_shape=(x.shape[1], x.shape[2])))
regresor_y.add(Activation('tanh'))
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

#Additional ANN Layers----------------------------------#
#ANN
regresor_y.add(Dense(units = units, activation = None, 
                   kernel_regularizer=l2(regularizer_k)))
#regresor_y.add(Dropout(dropout))
#ANN
#regresor_y.add(Dense(units = units, activation = 'tanh', 
#                   kernel_regularizer=l2(regularizer_k)))
#regresor_y.add(Dropout(dropout))
#ANN
#regresor_y.add(Dense(units = units, activation = 'tanh', 
#                   kernel_regularizer=l2(regularizer_k)))
#regresor_y.add(Dropout(dropout))
#------------------------------------------------------------------------------

#Output Layer------------------------------------------------------------------
#LSTM last layer
regresor_y.add(CuDNNLSTM(units = 5, recurrent_regularizer = l2(regularizer_r),
                       return_sequences = out_return_sequence))
#regresor.add(Activation('tanh'))

#ANN Last Layer
regresor_y.add(Dense(units = 1, kernel_regularizer=l2(regularizer_k),
                   activation = 'tanh'))
#------------------------------------------------------------------------------


#Compile this network---------------------------------------------------------
regresor_y.compile(optimizer = optimizer , loss = loss, 
                 metrics = metrics)

#------------------------------------------------------------------------------

#Train the model---------------------------------------------------------------
#Fit the data

finished_training = False
x_finished = False
try:
    history_y = regresor_y.fit(x, y[:,1:2], epochs = epochs, validation_split = val_split,
          callbacks=None, batch_size = batch_size)
    x_finished = True
except KeyboardInterrupt:
    print('Stopped training')
    if(x_finished):
        finished_training = False
try:
    history_x = regresor_x.fit(x, y[:,0:1], epochs = epochs, validation_split = val_split,
          callbacks=None, batch_size = batch_size)
    finished_training = True
except KeyboardInterrupt:
    print('Stopped training')
    finished_training = False

#Save name for images and files
with open(DIR + 'training_logs.txt','a+') as fh:
    fh.seek(0)
    run_count = fh.read().count('Training session #: ') + 1
try:
    save_name = 'M{}-{}-DuAL-MAE:{:.3f}-MSE:{:.3f}-{}'.format(run_count, model_output,
              float(history_x.history['val_mean_absolute_error'][-1]), 
              float(history_x.history['val_mean_squared_error'][-1]),
              input_format)
except NameError:
    save_name = 'M{}-{}-DuAL-MAE:{}-MSE:{}-{}'.format(run_count+1, model_output,
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
###############################################################################    
#%%Evaluate the model
###############################################################################
#Plot this data
if(finished_training):
    plt.figure(figsize=(15,15))
    plt.plot(history_x.history['loss'])
    plt.plot(history_x.history['val_loss'])
    if(polar):
        plt.title('Magnitude model train loss vs validation loss')
    else:
        plt.title('X model train loss vs validation loss')
    plt.ylabel('loss: ' + loss)
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper right')
    plt.savefig(SAVE_DIR + 'Loss - ' + save_name + '.png')
    plt.show()
    
    plt.figure(figsize=(15,15))
    plt.plot(history_y.history['loss'])
    plt.plot(history_y.history['val_loss'])
    if(polar):
        plt.title('Angle model train loss vs validation loss')
    else:
        plt.title('Y model train loss vs validation loss')
    plt.ylabel('loss: ' + loss)
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper right')
    plt.savefig(SAVE_DIR + 'Loss - ' + save_name + '.png')
    plt.show()
    
    
    #print('Lowest val loss = ' + str(min(history.history['val_loss'])))
    
###############################################################################
#%%
####regresor = load_model(MODEL_DIR + 'BigData_GPU_5LSTM_3ANN.16-0.8915.hdf5')
try:
    if(regresor_x.input_shape[1] != time_step):
        x, y = setup_data(regresor_x.input_shape[1], train_set, scale_output)
    
    slice_index = int(x.shape[0]*(1-val_split))
    prediction = regresor_x.predict(x=x[slice_index:,0:,0:])
    prediction = np.concatenate((prediction, regresor_y.predict(x=x[slice_index:,0:,0:])),
                                                      axis = 1)
    if(not out_return_sequence):
        if(scale_output):
            expected_outcome = out_sc.inverse_transform(y[slice_index:,:])
        else:
            expected_outcome = y[slice_index:,:]
    else:
        expected_outcome = y[slice_index:,-1,:].reshape(prediction.shape[0], 2)
        if(scale_output):
             expected_outcome = out_sc.inverse_transform(expected_outcome)
        prediction = prediction[:,-1,:].reshape(prediction.shape[0], 2)
    if(scale_output):    
        prediction = out_sc.inverse_transform(prediction)
    
    
    train_scores_x = regresor_x.evaluate(x,y[:,0])
    train_scores_y = regresor_y.evaluate(x,y[:,1])
    
    plt.figure(figsize=(15,15))
    plt.plot(prediction[0:,0:1])
    plt.plot(expected_outcome[0:,0:1])
    if(polar):
        plt.title('Validation: Magnitud')
        plt.ylabel('meters')
    else:
        plt.title('Validation: X')
        plt.ylabel('meters')
    plt.xlabel('measurement')
    plt.legend(['prediction', 'expected outcome'], loc='upper right')
    if(polar):
        plt.savefig(SAVE_DIR + 'Validation - Magnitud' + save_name+ '.png')
    else:
        plt.savefig(SAVE_DIR + 'Validation - X axis' + save_name+ '.png')
    plt.show()
    
    plt.figure(figsize=(15,15))
    plt.plot(prediction[0:,1:2])
    plt.plot(expected_outcome[0:,1:2])
    if(polar):
        plt.title('Validation: Angle')
        plt.ylabel('radians')
    else:
        plt.title('Validation: Y')
        plt.ylabel('meters')
    plt.xlabel('measurement')
    plt.legend(['prediction', 'expected outcome'], loc='upper right')
    if(polar):
        plt.savefig(SAVE_DIR + 'Validation - Angles' + save_name + '.png')
    else:
        plt.savefig(SAVE_DIR + 'Validation - Y axis' + save_name + '.png')
    plt.show()
except MemoryError:
    print("Memory error")
###############################################################################
#%%
###############################################################################
#Test neural networks performance with entirely new dataset

#Verify that the data is configures to the appropriate amount of timesteps
try:  
    if(regresor_x.input_shape[1] != time_step):
        x, y, _ = setup_data(regresor_x.input_shape[1], test_set, scale_output)
    else:
        x, y, _ = setup_data(time_step, test_set, scale_output)
    slice_index = int(x.shape[0]*(1-val_split))
    prediction = regresor_x.predict(x=x[:,:,:])
    prediction = np.concatenate((prediction, regresor_y.predict(x=x[:,:,:])),
                                                      axis = 1)
    if(not out_return_sequence):
        if(scale_output):
            expected_outcome = out_sc.inverse_transform(y[:,:])
        else:
            expected_outcome = y
    else:
        expected_outcome = y[:,-1,:].reshape(prediction.shape[0], 2)
        if(scale_output):
            expected_outcome = out_sc.inverse_transform(expected_outcome)
        prediction = prediction[:,-1,:].reshape(prediction.shape[0], 2)
    
    if(scale_output):
        prediction = out_sc.inverse_transform(prediction)
    
    test_scores_x = regresor_x.evaluate(x,y[:,0])
    test_scores_y = regresor_y.evaluate(x,y[:,1])
    
    ######### PLOT X or Magnitud
    plt.figure(figsize=(15,15))
    plt.plot(prediction[0:,0:1])
    plt.plot(expected_outcome[0:,0:1])
    if(polar):
        plt.title('Test: Magnitud')
        plt.ylabel('meters')
    else:
        plt.title('Test: X')
        plt.ylabel('meters')
    plt.xlabel('measurement')
    plt.legend([ 'prediction', 'expected outcome'], loc='upper right')
    if(polar):
        plt.savefig(SAVE_DIR + 'Test - Magnitud' + save_name + '.png')
    else:
        plt.savefig(SAVE_DIR + 'Test - X axis' + save_name + '.png')
    plt.show()
    
    
    ######### PLOT Y or ANGLE
    plt.figure(figsize=(15,15))
    plt.plot(prediction[0:,1:2])
    plt.plot(expected_outcome[0:,1:2])
   
    if(polar):
        plt.title('Test: Angle')
        plt.ylabel('radians')
    else:
        plt.title('Test: Y')
        plt.ylabel('meters')
    plt.xlabel('measurement')
    plt.legend([ 'prediction', 'expected outcome'], loc='upper right')
    if(polar):
        plt.savefig(SAVE_DIR + 'Test - Angles' + save_name + '-X-F2.png')
    else:
        plt.savefig(SAVE_DIR + 'Test - Y axis' + save_name + '-Y-F2.png')
    plt.show()
    #x, y, out_sc = setup_data(time_step, train_set, scale_output)
except MemoryError:
    del x
    del y
    
    
###############################################################################
#%%Save the network if it is good----------------------------------------------
###############################################################################
save_to_file = False
valid_input = False
inp = input("Do you want to save this model? (yes/no): ")
while(not valid_input):
    if(inp.lower() == 'yes' or inp.lower() == 'y' ):
        joblib.dump(out_sc,SAVE_DIR + save_name + '.scl')
        regresor_x.save(SAVE_DIR  + save_name.split(input_format)[0] + 
                        'X-' + input_format + '.h5py')
        regresor_y.save(SAVE_DIR  + save_name.split(input_format)[0] + 
                        'Y-' + input_format + '.h5py')
        save_to_file = True
        valid_input = True
        print("Saved to file")
    elif (inp.lower() == 'no' or inp.lower() == 'n'):
        shutil.rmtree(SAVE_DIR)
        print("Did not save to file")
        valid_input = True
    else:
        print('Invalid input')
        inp = input("Do you want to save this model? (yes/no): ")

    
#Append to logfile inconditionally
# Open the file
with open(DIR + 'training_logs.txt','a+') as fh:
    fh.write('_________________________________________________________________\\\\\n')
    fh.write('Training session #: ' + str(run_count) + '\n')
    fh.write('Model Architecture:\n')
    # Pass the file handle in as a lambda function to make it callable
    regresor_x.summary(print_fn=lambda x: fh.write(x + '\n'))
    #validation parameters
    if(finished_training):
        for element in history_x.history.keys():
            fh.write(element + ': ' + str(history_x.history[element][-1]) + '\n')
            fh.write(element + ': ' + str(history_y.history[element][-1]) + '\n')
    fh.write('_______\n')
    fh.write('_______\n')
    try:
        for i in range(0,len(metrics)):
            fh.write('Test X ' + metrics[i] + ': ' + str(test_scores_x[i]) + '\n')
            fh.write('Test Y ' + metrics[i] + ': ' + str(test_scores_y[i]) + '\n')
    except NameError:
        pass
    
    fh.write('_______\n')
    fh.write('Hyperparameters:\n\n')
    fh.write('Loss: ' + str(loss) + '\n')
    fh.write('Optimizer: ' + str(optimizer) + '\n')
    fh.write('Timesetps: ' + str(time_step) + '\n')
    fh.write('Batch size: ' + str(batch_size) + '\n')
    fh.write('Dropout: ' + str(dropout) + '\n')
    fh.write('Regularizer: ' + str(regularizer_k) + '\n')
    fh.write('Recurrent Regularizer: ' + str(regularizer_r) + '\n')
    fh.write('Epochs: ' + str(epochs) + '\n')
    fh.write('Validation Split: ' + str(val_split) + '\n')
    fh.write('_______\n')
    fh.write('Training Sets: ' + str(train_set) + '\n')
    fh.write('Test Sets: ' + str(test_set) + '\n')
    fh.write('Finished Training: ' + str(finished_training) + '\n')
    fh.write('_______\n')
    fh.write('Saved to file: ')
    if(save_to_file):
        fh.write(save_name + '.h5py')
    else:
        fh.write('N/A')
    fh.write('\n_________________________________________________________________//\n')
print("DONE")
###############################################################################