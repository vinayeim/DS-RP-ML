# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:21:18 2017

@author: VM00463601
"""

'Data Preprocessing'
'-------------------'
'Importing the libraries'
import numpy as np 
# The 'numpy' library contains mathametical tools we will use this in any mathametical code.
import matplotlib.pyplot as plt 
# The 'matplotlib' library contains different tools and the sublibrary 'pyplot' contains the graphical tools.
import pandas as pd
# The 'pandas' library to use import and manage datasets.

import os
os.getcwd()
os.chdir(r'C:\Users\vm00463601\Documents\Machine Learning A-Z\Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------')

'Importing the dataset'
'---------------------'
dataset = pd.read_csv('Data.csv')
dataset
# we can change the salary column formate from '%.3g' to '%.0f' for regular formate.

# Create a independent variable vector.
X = dataset.iloc[:, :-1].values
X
# first dataset from the dataset read the data using the 'iloc'[:'Rows', :'Columns'].values 

# Create a dependent variable vector.
y = dataset.iloc[:, 3].values
y

'Taking care of missing data'
'---------------------------'
'''
'sikat learn preprocessing' library from this we will import 'Imputer' class.
we use 'sikat learn' library to make machinery models.
'''

# Replacing the missing data with 'mean' value.
from sklearn.preprocessing import Imputer # importing the imputer library.
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0) # Creating an object
imputer = imputer.fit(X[:, 1:3]) # fitting the 'imputer' object to the dataset 'x'
X[:, 1:3] = imputer.transform(X[:, 1:3]) # Replacing the data with mean value.
np.set_printoptions(threshold = np.nan)
X

# Replacing the missing data with 'median' value.
dataset1 = pd.read_csv('.\Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------\Data.csv')
dataset1

ip1 = dataset1.iloc[:, :-1].values
ip1

dp1 = dataset1.iloc[:, 3].values
dp1

from sklearn.preprocessing import Imputer
ds1_median = Imputer(missing_values = 'NaN', strategy = 'median', axis = 0)
ds1_median = ds1_median.fit(ip1[:, 1:3])
ip1[:, 1:3] = ds1_median.transform(ip1[:, 1:3])
ip1

# Replacing the missing data with 'mode'(most_frequent) value.
dataset2 = pd.read_csv('.\Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------\Data.csv')
dataset2

ip2 = dataset2.iloc[:, :-1].values
ip2

dp2 = dataset2.iloc[:, 3].values
dp2

from sklearn.preprocessing import Imputer
ds2_mode = Imputer(missing_values = 'NaN', strategy = 'median', axis = 0)
ds2_mode = ds2_mode.fit(ip1[:, 1:3])
ip2[:, 1:3] = ds2_mode.transform(ip1[:, 1:3])
ip2

'Encoding categorical data'
'-------------------------'

from sklearn.preprocessing import LabelEncoder # label encoder
lablencoder_X = LabelEncoder()
X[:, 0] = lablencoder_X.fit_transform(X[:, 0]) # transform the data
X

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
X

lablencoder_y = LabelEncoder()
y = lablencoder_y.fit_transform(y)
y

'Splitting the dataset into the Training set and Test set'
'---------------------------------------------------------'

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

'Feature Scaling'
'---------------'

from sklearn.cross_validation import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_tain)
X_test = sc_X.transform(X_test)

