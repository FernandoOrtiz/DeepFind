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

DIR = '../Models/'

#%%
#The amount of time-steps the LSTM will look back at
time_step = 20
val_split = 0.3    
polar = True
model_output = 'CaRT'
if(polar):
    model_output = 'PoLR'

train_set = ["D3-30MinuteStillRun-F2.csv", "D1-30MinuteRun-F2.csv",
             "D4-18MinuteRun-F2.csv", "D5-7MinuteRun-F2.csv"]
test_set = ["D2-35MinuteRun-F2.csv"]
input_format = train_set[0].split('-')[-1].split('.')[0]
                           
def to_polar(data):
    for i in range(0, data.shape[0]):
        r = np.sqrt((data[i,0]**2) + (data[i,1]**2))
        t = np.arctan2(data[i,0], data[i,1])
        data[i,0] = r 
        data[i,1] = t

def setup_data(time_step, dataset):
    dataset_copy = list(dataset)                                             #Make a copy of the list so you do not alter it
    dataset_total = pd.read_csv("../Datasets/"+dataset_copy.pop(0))            #Pop the first element out
    for element in dataset_copy:                                               #If you have additional datasets, keep adding them 
        dataset_total = pd.concat((dataset_total,
                                  pd.read_csv("../Datasets/"+element)), axis=0)
    #Convert into numpy array
    dataset_total = dataset_total.as_matrix()    
    in_sc = StandardScaler()
    dataset_total[:,2:] = in_sc.fit_transform(dataset_total[:,2:])
    
    
    #Reshappe the inpputt so it fits the recurrent neural network
    x = []
    for i in range(1, time_step):                                              #Pad initial values with zeros 
        x.append(np.concatenate((np.zeros((time_step-i, 
                 dataset_total.shape[1]-2)), dataset_total[0:i, 2:]), 
                 axis = 0))
    
    
    for i in range(time_step-1,int(dataset_total.size/dataset_total.shape[1])):
        x.append(dataset_total[i-time_step+1 : i+1 , 2:])
    x = np.array(x)
    
    #Extract the output of the neural network
    y = dataset_total[0:,0:2]
    #y = np.subtract(y, np.array([y[0,0], y[0,1]]))
    #to_polar(y)
    #Feature Scaling
    out_sc = MinMaxScaler(feature_range = (-1,1))
    y = out_sc.fit_transform(y)
    
    return x, y, out_sc

x, y, out_sc = setup_data(time_step, train_set)


#%% Part 2 - Building the RNN
###############################################################################
#Setup TODO -

units = 1
dropout = 0.0
regularizer_k = 0.1
regularizer_r = 0.1
optimizer = 'adam'
epochs = 150
batch_size = 64
loss = 'logcosh'
metrics = ['mae','mse', 'logcosh','acc']

###############################################################################

#Initialize the model
regresor = Sequential()

#First Layer  -----------------------------------------------------------------
#Note that this is the only layer with input_shape
#Should only use one of these

#LSTM First layer
regresor.add(LSTM(units = units, 
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
#regresor.add(LSTM(units = units, 
#                       recurrent_regularizer = l2(regularizer_r),
#                       return_sequences = True))
regresor.add(Activation('relu'))
#ANN
#regresor.add(Dense(units = units, activation = None))
#regresor.add(Dropout(dropout))
#----------------------------------------------#


#Third Layer----------------------------------#
#LSTM
#regresor.add(LSTM(units = units, 
#                       recurrent_regularizer = l2(regularizer_r),
#                       return_sequences = True))
#ANN
#regresor.add(Dense(units = units, activation = 'tanh'))
#regresor.add(Dropout(dropout))
#----------------------------------------------#


#Fourth Layer----------------------------------#
#LSTM
#regresor.add(LSTM(units = units,  
#                  return_sequences = True))
#ANN
#regresor.add(Dense(units = units, activation = 'tanh'))
#regresor.add(Dropout(dropout))
#----------------------------------------------#


#Fifth Layer----------------------------------#
#LSTM
#regresor.add(LSTM(units = units, 
#                       recurrent_regularizer = l2(regularizer_r),
#                       return_sequences = True))
#ANN
#regresor.add(Dense(units = units, activation = 'tanh'))
#regresor.add(Dropout(dropout))
#----------------------------------------------#


#Sixth Layer----------------------------------#
#LSTM
#regresor.add(LSTM(units = units, 
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
#regresor.add(Dense(units = units, kernel_regularizer=l2(regularizer_k),
#                   activation = 'relu'))
#regresor.add(Dense(units = units*2, kernel_regularizer=l2(regularizer_k),
#                   activation = 'tanh'))
#----------------------------------------------#


#------------------------------------------------------------------------------


#Output Layer------------------------------------------------------------------
#LSTM last layer
regresor.add(LSTM(units = 2, recurrent_regularizer = l2(regularizer_r)))
regresor.add(Activation('linear'))

#ANN Last Layer
#regresor.add(Dense(units = 2, kernel_regularizer=l2(regularizer_c),
#                   activation = 'tanh', use_bias = False))
#------------------------------------------------------------------------------


#Compile this network----------------------------------------------------------
regresor.compile(optimizer = optimizer , loss = loss, 
                 metrics = metrics)
#------------------------------------------------------------------------------


#Callback Declarations---------------------------------------------------------
#Calbacks are used to alter the behaviour of the training. Descriptions of each
#function is provided bellow

#ModelCheckpoint - saves the data when a specific value is a its best
#save_data = ModelCheckpoint(DIR + 'BigData_GPU_5LSTM_3ANN.\
#{epoch:02d}-{val_acc:.4f}.hdf5', 
#          monitor='val_acc',save_best_only=True)

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
#TODO - add handling of ctrl + c

history = regresor.fit(x, y, epochs = epochs, validation_split = val_split,
          callbacks= [], batch_size = batch_size)


#except KeyboardInterrupt:
#    print('Trying to save history from unecessarily long training')


#Save name for images and files
with open(DIR + 'Fernando_training_logs.txt','a+') as fh:
    fh.seek(0)
    run_count = fh.read().count('Training session #: ') + 1
save_name = 'F{}-{}-MAE:{:.2f}-MSE:{:.2f}-{}'.format(run_count, model_output,
              float(history.history['val_mean_absolute_error'][-1]), 
              float(history.history['val_mean_squared_error'][-1]),
              input_format)
SAVE_DIR = DIR + save_name + '/'
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)
else:
    while(not os.path.exists(SAVE_DIR)):
        dir_name = input("Model Directory already exists, input new name: ")    
        SAVE_DIR = DIR + dir_name + '/'
    os.makedirs(SAVE_DIR)
    
#%%Evaluate the model

#Plot this data

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model train loss vs validation loss')
plt.ylabel('loss: ' + loss)
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper right')
plt.savefig(SAVE_DIR + 'Loss - ' + save_name + '.png')
plt.show()


print('Lowest val loss = ' + str(min(history.history['val_loss'])))

#%%
####regresor = load_model(MODEL_DIR + 'BigData_GPU_5LSTM_3ANN.16-0.8915.hdf5')

if(regresor.input_shape[1] != time_step):
    x, y, out_sc = setup_data(regresor.input_shape[1], train_set)

slice_index = int(x.shape[0]*(1-val_split))
prediction = regresor.predict(x=x[slice_index:,0:,0:])
prediction = out_sc.inverse_transform(prediction)
expected_outcome = out_sc.inverse_transform(y[slice_index:,:])
#expected_outcome = y[slice_index:,:]

train_scores = regresor.evaluate(x,y)

plt.plot(expected_outcome[0:, 0:1])
plt.plot(prediction[0:,0:1])
if(polar):
    plt.title('Validation: Magnitud')
    plt.ylabel('meters')
else:
    plt.title('Validation: X')
    plt.ylabel('meters')
plt.xlabel('measurement')
plt.legend(['expected outcome', 'prediction'], loc='upper right')
if(polar):
    plt.savefig(SAVE_DIR + 'Validation - Magnitud' + save_name+ '.png')
else:
    plt.savefig(SAVE_DIR + 'Validation - X axis' + save_name+ '.png')
plt.show()

plt.plot(expected_outcome[0:, 1:2])
plt.plot(prediction[0:,1:2])
if(polar):
    plt.title('Validation: Angle')
    plt.ylabel('radians')
else:
    plt.title('Validation: X')
    plt.ylabel('meters')
plt.xlabel('measurement')
plt.legend(['expected outcome', 'prediction'], loc='upper right')
if(polar):
    plt.savefig(SAVE_DIR + 'Validation - Angles' + save_name + '.png')
else:
    plt.savefig(SAVE_DIR + 'Validation - Y axis' + save_name + '.png')
plt.show()

#%%
#Test neural networks performance with entirely new dataset

#Verify that the data is configures to the appropriate amount of timesteps
if(regresor.input_shape[1] != time_step):
    x, y, out_sc = setup_data(regresor.input_shape[1], test_set)
else:
    x, y, out_sc = setup_data(time_step, test_set)

slice_index = int(x.shape[0]*(1-val_split))
prediction = regresor.predict(x=x[slice_index:,0:,0:])
prediction = out_sc.inverse_transform(prediction)
expected_outcome = out_sc.inverse_transform(y[slice_index:,:])
#expected_outcome = y[slice_index:,:]

test_scores = regresor.evaluate(x,y)

plt.plot(expected_outcome[0:, 0:1])
plt.plot(prediction[0:,0:1])
if(polar):
    plt.title('Test: Magnitud')
    plt.ylabel('meters')
else:
    plt.title('Test: X')
    plt.ylabel('meters')
plt.xlabel('measurement')
plt.legend(['expected outcome', 'prediction'], loc='upper right')
if(polar):
    plt.savefig(SAVE_DIR + 'Test - Magnitud' + save_name + '.png')
else:
    plt.savefig(SAVE_DIR + 'Test - X axis' + save_name + '.png')
plt.show()

plt.plot(expected_outcome[0:, 1:2])
plt.plot(prediction[0:,1:2])
if(polar):
    plt.title('Test: Angle')
    plt.ylabel('radians')
else:
    plt.title('Test: X')
    plt.ylabel('meters')
plt.xlabel('measurement')
plt.legend(['expected outcome', 'prediction'], loc='upper right')
if(polar):
    plt.savefig(SAVE_DIR + 'Test - Angles' + save_name + '.png')
else:
    plt.savefig(SAVE_DIR + 'Test - Y axis' + save_name + '.png')
plt.show()
#x, y, out_sc = setup_data(time_step, train_set)



#%%Save the network if it is good----------------------------------------------

save_to_file = False
inp = input("Do you want to save this model? (yes/no): ")
if(inp.lower() == 'yes' or inp.lower() == 'y'):
    
    joblib.dump(out_sc,SAVE_DIR + save_name + '.scl')
    regresor.save(SAVE_DIR  + save_name + '.h5py')
    save_to_file = True

else:
    shutil.rmtree(SAVE_DIR)
    
    
#Append to logfile inconditionally
# Open the file
with open(DIR + 'Fernando_training_logs.txt','a+') as fh:
    fh.write('_________________________________________________________________\\\\\n')
    fh.write('Training session #: ' + str(run_count) + '\n')
    fh.write('Model Architecture:\n')
    # Pass the file handle in as a lambda function to make it callable
    regresor.summary(print_fn=lambda x: fh.write(x + '\n'))
    #validation parameters
    for element in history.history.keys():
        fh.write(element + ': ' + str(history.history[element][-1]) + '\n')
    fh.write('_______\n')
    fh.write('_______\n')
    for i in range(0,len(metrics)):
        fh.write('Test ' + metrics[i] + ': ' + str(test_scores[i]) + '\n')
    
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
    fh.write('_______\n')
    fh.write('Saved to file: ')
    if(save_to_file):
        fh.write(save_name + '.h5py')
    else:
        fh.write('N/A')
    fh.write('\n_________________________________________________________________//\n')
print("DONE")