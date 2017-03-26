# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:45:33 2017

@author: vinay
"""

# Polynomial Regression

# importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import the datasets

import os
os.getcwd()
os.chdir(r'C:\Users\vinay\Documents\GitHub\DS-RP-ML\Machine Learning A-Z\Part 2 - Regression\Section 6 - Polynomial Regression\Polynomial_Regression')

prsal = pd.read_csv('Position_Salaries.csv')
ipprsal = prsal.iloc[:, 1:2].values
dpprsal = prsal.iloc[:, 2].values

'''Not Required because we dont have much information
# Splitting the dataset into the Training set and  Test set
from sklearn.cross_validation import train_test_split
ipprsal_train, ipprsal_test,dpprsal_train, dpprsal_test = train_test_split(ipprsal ,dpprsal, test_size = 0.2, random_state = 0)
'''

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(ipprsal,dpprsal)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
ipprsal_poly = poly_reg.fit_transform(ipprsal)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(ipprsal_poly, dpprsal)

# Visualising the Linear Regression results

plt.scatter(ipprsal, dpprsal, color = 'red')
plt.plot(ipprsal, lin_reg.predict(ipprsal), color = 'blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression results
ipprsal_grid = np.arange(min(ipprsal), max(ipprsal), 0.1)
ipprsal_grid= ipprsal_grid.reshape((len(ipprsal_grid),1))
plt.scatter(ipprsal, dpprsal, color = 'red')
plt.plot(ipprsal_grid, lin_reg_2.predict(poly_reg.fit_transform(ipprsal_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Predicting a new result with Linear Regression
lin_reg.predict(6.5)

# Predicting a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform(6.5))

