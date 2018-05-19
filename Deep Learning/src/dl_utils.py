#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 16:03:50 2018

@author: rathk
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt
from sklearn.externals import joblib
import shutil


def to_polar(data):
    if(len(data.shape) == 2):
        x = data[:,0]
        y = data[:,1]
        r = np.sqrt(np.power(x,2) + np.power(y,2))
        t = np.arctan2(y, x)
        data[:,0] = r 
        data[:,1] = t
    if(len(data.shape) == 1):
        x = data[0]
        y = data[1]
        r = np.sqrt(np.power(x,2) + np.power(y,2))
        t = np.arctan2(y, x)
        data[0] = r 
        data[1] = t



def to_cartesian(data):
    if(len(data.shape) == 2):
        magnitude = data[:,0]
        angle = data[:,1]
        x = np.cos(angle)*magnitude
        y = np.sin(angle)*magnitude
        data[:,0] = x
        data[:,1] = y
    if(len(data.shape) == 1):
        magnitude = data[0]
        angle = data[1]
        x = np.cos(angle)*magnitude
        y = np.sin(angle)*magnitude
        data[0] = x
        data[1] = y

def to_cartesian_scalar (magnitude, angle):
    arr = to_cartesian(np.array([magnitude, angle]))
    x = arr[0]
    y = arr[1]
    return x, y

def setup_data(time_step, dataset, scale_output=True, scale_input=True,
               polar_output = False, zero_pad = True):
    #Create a copy so you dont alter the original
    dataset_copy = list(dataset)                                             #Make a copy of the list so you do not alter it
    #Pop the first item in the list
    dataset_total = pd.read_csv("../Datasets/"+dataset_copy.pop(0))            #Pop the first element out
    #If desired, add zero pad
    if(zero_pad):
        zeros_df = pd.DataFrame(0, index=range(time_step-1), 
                                columns= dataset_total.columns)
        dataset_total = pd.concat((zeros_df, dataset_total), axis = 0)
    
    #Iterate through the list appending each dataset
    for element in dataset_copy:                                               #If you have additional datasets, keep adding them 
        if(zero_pad):
            dataset_total = pd.concat((dataset_total, zeros_df), axis = 0)
        dataset_total = pd.concat((dataset_total,
        pd.read_csv("../Datasets/"+element)), axis=0)
    
    #Convert to numpy array
    dataset_total = dataset_total.as_matrix()    
    #Extract the output of the neural network
    y_set = dataset_total[0:-1*time_step,0:2]
    x_set = dataset_total[0:,2:]
    
    in_sc = StandardScaler()
    if(scale_input):
        x_set = in_sc.fit_transform(x_set)
    
    
    #Reshappe the inpputt so it fits the recurrent neural network
    x = []
    for i in range(0,int(dataset_total.shape[0]-time_step)):
        x.append(x_set[i : i+time_step , :])
    x = np.array(x)
   
    if(polar_output):
        to_polar(y_set)
    #Feature Scaling
    out_sc = MinMaxScaler(feature_range = (-1,1))
    if(scale_output):
        y_set = out_sc.fit_transform(y_set)

    
    return x, y_set, out_sc



def setup_data_generator(dataset, batch_size=1500, time_step=50, shuffle = True,
                         scale_output=True, scale_input=True, 
                         polar_output=False, zero_pad = True):
    #Create a copy so you dont alter the original
    dataset_copy = list(dataset)                                             #Make a copy of the list so you do not alter it
    #Pop the first item in the list
    dataset_total = pd.read_csv("../Datasets/"+dataset_copy.pop(0))            #Pop the first element out
    #If desired, add zero pad
    if(zero_pad):
        zeros_df = pd.DataFrame(0, index=range(time_step-1), 
                                columns= dataset_total.columns)
        dataset_total = pd.concat((zeros_df, dataset_total), axis = 0)
    
    #Iterate through the list appending each dataset
    for element in dataset_copy:                                               #If you have additional datasets, keep adding them 
        if(zero_pad):
            dataset_total = pd.concat((dataset_total, zeros_df), axis = 0)
        dataset_total = pd.concat((dataset_total,
        pd.read_csv("../Datasets/"+element)), axis=0)
    
    #Convert to numpy array
    dataset_total = dataset_total.as_matrix()    
    
    #If desired, scale the input
    if(scale_input):
        in_sc = StandardScaler()
        dataset_total[:,2:] = in_sc.fit_transform(dataset_total[:,2:])   
    
    
    #If desired, convert the position to polar coordinates
    if(polar_output):
        to_polar(dataset_total)
    
    #If desired, scale the output
    out_sc = MinMaxScaler(feature_range = (-1,1))
    
    if(scale_output):
        dataset_total[:,0:2] = out_sc.fit_transform(dataset_total[:,0:2])
        print('out_sc data range' + str(out_sc.data_range_[0]))
        print('out_sc data min' + str(out_sc.data_min_[0]))
        
    if(time_step > batch_size):
        r_max = time_step
    else:
        r_max = batch_size
        
    n = dataset_total.shape[0]
    while True:
        inputs, outputs =[], []
        for i in np.random.permutation(range(0, batch_size, int(n/batch_size))):
            inputs, outputs =[], []
            
            for j in np.random.permutation(range(i, i+batch_size)):
                inputs.append(dataset_total[j:j+time_step,2:])
                outputs.append(dataset_total[j+time_step-1,0:2])
                # split your inputs, and outputs as you wish
                               
            yield np.array(inputs), np.array(outputs)
            
            
        inputs, outputs =[], []
        for k in np.random.permutation(range(0, batch_size, int(n/batch_size))):
            inputs, outputs =[], []
            i = np.random.randint(n - r_max - 1)
            for j in np.random.permutation(range(i, i+batch_size)):
                inputs.append(dataset_total[j:j+time_step,2:])
                outputs.append(dataset_total[j+time_step-1,0:2])
                # split your inputs, and outputs as you wish
                               
            yield np.array(inputs), np.array(outputs)

def get_out_sc(dataset, polar_output, zero_pad, time_step):
    #Create a copy so you dont alter the original
    dataset_copy = list(dataset)                                             #Make a copy of the list so you do not alter it
    #Pop the first item in the list
    dataset_total = pd.read_csv("../Datasets/"+dataset_copy.pop(0))            #Pop the first element out
    #If desired, add zero pad
    if(zero_pad):
        zeros_df = pd.DataFrame(0, index=range(time_step-1), 
                                columns= dataset_total.columns)
        dataset_total = pd.concat((zeros_df, dataset_total), axis = 0)
    
    #Iterate through the list appending each dataset
    for element in dataset_copy:                                               #If you have additional datasets, keep adding them 
        if(zero_pad):
            dataset_total = pd.concat((dataset_total, zeros_df), axis = 0)
        dataset_total = pd.concat((dataset_total,
        pd.read_csv("../Datasets/"+element)), axis=0)
    
    #Convert to numpy array
    dataset_total = dataset_total.as_matrix()    
    y_set = dataset_total[0:,0:2]
    if(polar_output):
        to_polar(y_set)
    out_sc = MinMaxScaler(feature_range = (-1,1))
    #out_sc = StandardScaler()
    y_set = out_sc.fit(y_set)
    return out_sc, dataset_total.shape[0]



def plot_history(history, directory, save_name, loss):
    plt.figure(figsize=(15,15))
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model train loss vs validation loss')
    plt.ylabel('loss: ' + loss)
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper right')
    plt.savefig(directory + 'Loss - ' + save_name + '.png')
    plt.show()


def plot_validation(deep_model, validation_x, validation_y, 
                    directory, save_name, polar_output,
                    out_sc=None, out_scaler = False):
    
    prediction = deep_model.predict(validation_x)
    expected_outcome = validation_y.copy()
    if(out_scaler): 
        prediction = out_sc.inverse_transform(prediction)
        expected_outcome = out_sc.inverse_transform(expected_outcome)
 
    
    train_scores = deep_model.evaluate(validation_x,validation_y)
    
    plt.figure(figsize=(15,15))
    plt.plot(prediction[0:,0:1])
    plt.plot(expected_outcome[0:,0:1])
    if(polar_output):
        plt.title('Validation: Magnitude')
        plt.ylabel('meters')
    else:
        plt.title('Validation: X')
        plt.ylabel('meters')
    plt.xlabel('measurement')
    plt.legend(['prediction', 'expected outcome'], loc='upper right')
    if(polar_output):
        plt.savefig(directory + 'Validation - Magnitud' + save_name+ '.png')
    else:
        plt.savefig(directory + 'Validation - X axis' + save_name+ '.png')
    plt.show()
    
    plt.figure(figsize=(15,15))
    plt.plot(prediction[0:,1:2])
    plt.plot(expected_outcome[0:,1:2])
    if(polar_output):
        plt.title('Validation: Angle')
        plt.ylabel('radians')
    else:
        plt.title('Validation: Y')
        plt.ylabel('meters')
    plt.xlabel('measurement')
    plt.legend([ 'prediction','expected outcome'], loc='upper right')
    if(polar_output):
        plt.savefig(directory + 'Validation - Angles' + save_name + '.png')
    else:
        plt.savefig(directory + 'Validation - Y axis' + save_name + '.png')
    plt.show()
    
    return train_scores




def save_log(directory, deep_model, run_count,  optimizer,  metrics, test_scores, 
             time_step, batch_size, dropout, regularizer_k, regularizer_r, loss,
             epochs, val_split, train_set, test_set, yaw_pitch_roll_input,
             scale_input, scale_output, save_name, save_to_file, finished_training,
             history = None):
    
    with open(directory + 'training_logs.txt','a+') as fh:
        fh.write('_________________________________________________________________\\\\\n')
        fh.write('Training session #: ' + str(run_count) + '\n')
        fh.write('Model Architecture:\n')
        # Pass the file handle in as a lambda function to make it callable
        deep_model.summary(print_fn=lambda x: fh.write(x + '\n'))
        #validation parameters
        if(history != None):
            for element in history.history.keys():
                fh.write(element + ': ' + str(history.history[element][-1]) + '\n')
        fh.write('_______\n')
        fh.write('_______\n')
        try:
            for i in range(0,len(metrics)):
                fh.write('Test ' + metrics[i] + ': ' + str(test_scores[i]) + '\n')
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
        fh.write('YPR Input: ' + str(yaw_pitch_roll_input) + '\n')
        fh.write('In scaler: ' + str(scale_input) + '\n')
        fh.write('scale_output: ' + str(scale_output) + '\n')
        fh.write('Saved to file: ')
        if(save_to_file):
            fh.write(save_name + '.h5py')
        else:
            fh.write('N/A')
        fh.write('\n_________________________________________________________________//\n')


def save_model_to_file(deep_model, out_sc, directory, save_name):
    save_to_file = False
    valid_input = False
    inp = input("Do you want to save this model? (yes/no): ")
    while(not valid_input):
        if(inp.lower() == 'yes' or inp.lower() == 'y' ):
            joblib.dump(out_sc,directory + save_name + '.scl')
            deep_model.save(directory  + save_name + '.h5py')
            save_to_file = True
            valid_input = True
            print("Saved to file")
        elif (inp.lower() == 'no' or inp.lower() == 'n'):
            shutil.rmtree(directory)
            print("Did not save to file")
            valid_input = True
        else:
            print('Invalid input')
            inp = input("Do you want to save this model? (yes/no): ")
    return save_to_file