# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 09:24:21 2018

@author: abhij
"""

from nltk.classify import NaiveBayesClassifier
from sklearn.utils import shuffle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

with open("names.txt",'r') as f:
    names =[]
    feature_set = []
    for name_result in f:
        names.append(tuple(name_result.strip().split(',')))
        
    names = shuffle(names)
    
    for i in range(0,len(names)-1):
        last_letter = names[i][0][-1]
        gender = names[i][1]
        feature_set.append((last_letter,gender))
        
    from sklearn.cross_validation import train_test_split
    train_data_set, test_data_set = train_test_split(feature_set, test_size = 0.2, random_state = 0)    
    
    
    print(train_data_set)
    
















