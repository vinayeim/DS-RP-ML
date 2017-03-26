# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:20:18 2017

@author: vinay
"""

# Multiple Lineat Regression

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

import os
os.getcwd()
os.chdir(r'C:\Users\vinay\Documents\GitHub\DS-RP-ML\Machine Learning A-Z\Part 2 - Regression\Section 5 - Multiple Linear Regression')

datamlr = pd.read_csv('50_Startups.csv')
datamlr
ipmlr = datamlr.iloc[:, :-1].values
dpmlr = datamlr.iloc[:, 4].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_ipmlr = LabelEncoder()
ipmlr[:, 3] = labelencoder_ipmlr.fit_transform(ipmlr[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
ipmlr = onehotencoder.fit_transform(ipmlr).toarray()

# Avoiding the Dummy Variable Trap
ipmlr = ipmlr[:, 1:]
# Splitting the dataset into the Training set and test set

from sklearn.cross_validation import train_test_split
ipmlr_train, ipmlr_test, dpmlr_train, dpmlr_test = train_test_split(ipmlr, dpmlr, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set

from sklearn.linear_model import LinearRegression
mlrreg = LinearRegression()
mlrreg.fit(ipmlr_train, dpmlr_train)

# Predicting the Test set results

mlr_pred = mlrreg.predict(ipmlr_test)

# Predicting the Training set results
mlr_pred_train = mlrreg.predict(ipmlr_train)

# Buulding the optimal model using Backward Elimination

import statsmodels.formula.api as sm
ipmlr = np.append(arr = np.ones((50, 1)).astype(int), values = ipmlr, axis = 1)
ipmlr_opt = ipmlr[:, [0,1,2,3,4,5]]
mlrreg_OLS = sm.OLS(endog = dpmlr, exog = ipmlr_opt).fit()
mlrreg_OLS.summary()

ipmlr_opt = ipmlr[:, [0,1,3,4,5]]
mlrreg_OLS = sm.OLS(endog = dpmlr, exog = ipmlr_opt).fit()
mlrreg_OLS.summary()

ipmlr_opt = ipmlr[:, [0,3,4,5]]
mlrreg_OLS = sm.OLS(endog = dpmlr, exog = ipmlr_opt).fit()
mlrreg_OLS.summary()

ipmlr_opt = ipmlr[:, [0,3,5]]
mlrreg_OLS = sm.OLS(endog = dpmlr, exog = ipmlr_opt).fit()
mlrreg_OLS.summary()

ipmlr_opt = ipmlr[:, [0,3]]
mlrreg_OLS = sm.OLS(endog = dpmlr, exog = ipmlr_opt).fit()
mlrreg_OLS.summary()



'Automatic predictor removal?'
'----------------------------'
def backwardElimination(x, sl):
    numVars = len(x[0])
    # The loop fits the model and checks for the max p-value
    # If p-value is higher than significance level, it is removed
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        # Inner loop is run numVars - 1 because we don't want to remove the y intercept
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    regressor_OLS.summary()
    return x
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)