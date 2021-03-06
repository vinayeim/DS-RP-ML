# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 11:50:00 2017

@author: vinay
"""

'Automatic predictor removal'
'---------------------------'

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