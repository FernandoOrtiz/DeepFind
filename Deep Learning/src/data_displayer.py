#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 20:07:28 2018

@author: rathk
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



data_sets = ["D1-30MinuteRun-F2.csv",
             "D2-35MinuteRun-F2.csv",
             "D3-30MinuteStillRun-F2.csv",
             "D4-18MinuteRun-F2.csv",
             "D5-7MinuteRun-F2.csv", 
             "D6-27MinuteRun-F2.csv",
             "D7-60MinuteRun-F2.csv",
             "D8-60MinuteRun-F2.csv"]


i = 0

for element in data_sets:
    i += 1
    data = pd.read_csv('../Datasets/' + element)
    data = data.as_matrix()
    plt.figure(figsize=(15,15))
    plt.subplot(211)
    plt.plot(data[:,0:1])
    plt.subplot(212)
    plt.plot(data[:,1:2])
    plt.title('Dataset number ' + str(i))
    plt.ylabel('Meters')
    plt.xlabel('sample')
    plt.show()