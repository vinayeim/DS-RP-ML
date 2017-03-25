# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:34:24 2017

@author: VM00463601
"""

'Simple linear regression'

# Import the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Set the working directory

import os
os.getcwd()
os.chdir(r'C:\Users\vm00463601\Documents\Machine Learning A-Z\Part 2 - Regression\Section 4 - Simple Linear Regression')
# Import the dataset

slr_data = pd.read_csv('Salary_Data.csv')
sal_ip = slr_data.iloc[:, :-1].values
sal_dp = slr_data.iloc[:, 1].values

# Spliting the dataset into the training and test dataset

from sklearn.cross_validation import train_test_split
sal_ip_train, sal_ip_test, sal_dp_train, sal_dp_test = train_test_split(sal_ip, sal_dp, test_size = 1/3, random_state = 0)

# Fitting simple Linear Regression to the Training set

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(sal_ip_train, sal_dp_train) # Train the model

# Predicting the Test set results

y_pred = regressor.predict(sal_ip_test)

# Visualising the Training set results

plt.scatter(sal_ip_train, sal_dp_train, color = 'red')
plt.plot(sal_ip_train, regressor.predict(sal_ip_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results

plt.scatter(sal_ip_test, sal_dp_test, color = 'red')
plt.plot(sal_ip_train, regressor.predict(sal_ip_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
