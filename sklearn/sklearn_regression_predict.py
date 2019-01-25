#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 13:30:18 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


"""
Write a function that fits a polynomial LinearRegression model on the training data 
X_train for degrees 1, 3, 6, and 9. (Use PolynomialFeatures in sklearn.preprocessing 
to create the polynomial features and then fit a linear regression model) For each model, 
find 100 predicted values over the interval x = 0 to 10 (e.g. np.linspace(0,10,100)) 
and store this in a numpy array. 
The first row of this array should correspond to 
the output from the model trained on degree 1, 
the second row degree 3, 
the third row degree 6, 
and the fourth row degree 9.
"""


np.random.seed(0)
n = 15
x = np.linspace(0,10,n) + np.random.randn(n)/5
y = np.sin(x)+x/6 + np.random.randn(n)/10

X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)

test_data = np.linspace(0,10,100)
test_data_2D = test_data.reshape(len(test_data), 1)

X_train_2D = X_train.reshape(len(X_train), 1)
y_train_2D = y_train.reshape(len(y_train), 1)


first_regression = LinearRegression().fit(X_train_2D, y_train_2D)
#first_regression.score(X_train_2D, y_train_2D)

degree1 = first_regression.predict(test_data_2D)

"""
this is for degree=1
"""
poly1 = PolynomialFeatures(degree=1)
X_train1 = poly1.fit_transform(X_train_2D)
regression1 = LinearRegression().fit(X_train1, y_train_2D)
test_data1 = poly1.fit_transform(test_data_2D)
degree_1 = regression1.predict(test_data1)


"""
this is for degree=3
"""
poly3 = PolynomialFeatures(degree=3)
X_train3 = poly3.fit_transform(X_train_2D)
regression3 = LinearRegression().fit(X_train3, y_train_2D)
test_data3 = poly3.fit_transform(test_data_2D)
degree3 = regression3.predict(test_data3)


"""
this is for degree=6
"""
poly6 = PolynomialFeatures(degree=6)
X_train6 = poly6.fit_transform(X_train_2D)
regression6 = LinearRegression().fit(X_train6, y_train_2D)
test_data6 = poly6.fit_transform(test_data_2D)
degree6 = regression6.predict(test_data6)


"""
this is for degree=9
"""
poly9 = PolynomialFeatures(degree=9)
X_train9 = poly9.fit_transform(X_train_2D)
regression9 = LinearRegression().fit(X_train9, y_train_2D)
test_data9 = poly9.fit_transform(test_data_2D)
degree9 = regression9.predict(test_data9)

degree_1 = degree1.reshape(1, len(degree1))
degree_3 = degree3.reshape(1, len(degree3))
degree_6 = degree6.reshape(1, len(degree6))
degree_9 = degree9.reshape(1, len(degree9))

degree = np.concatenate((degree_1, degree_3, degree_6, degree_9), axis=0)

#there is not difference between two methods to get the prediction when degree=1
