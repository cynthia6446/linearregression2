# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 17:32:55 2023

@author: be
ordinary leasst squares using OLS from statsmodels.apt 
predict point spread using line, and difference in days off the 
theory being more days off means a team is better rested
 and better prepared. 

y is the respone variable; actual spread (homescore-visitorscore)
x1 is the line 
x2 is the difference in days off 

y = b0 + b1*x1 + b2*x2


"""
import statsmodels.api as sm 
import pandas as pd 
import numpy as np

# reading data as pd 
data = pd.read_csv("NFl2022.csv")

#defining the cariables
 
y = (data["hScore"] - data["vScore"]).tolist()
x1 = data["line"]. tolist()
x2 = (data['hDoff'] - data["vDoff"]).tolist()

A = np.array([x1,x2]).T
A.shape
A = sm.add_constant(A)
A.shape

model = sm.OLS(y,A)
results = model.fit()

results.params
results.tvalues

print(results.t_test([1,0]))







