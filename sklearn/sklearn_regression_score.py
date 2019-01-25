#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:14:46 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics.regression import r2_score

"""
Write a function that fits a polynomial LinearRegression model on the training 
data X_train for degrees 0 through 9. For each model compute the  R*R
(coefficient of determination) regression score on the training data 
as well as the the test data, and return both of these arrays in a tuple.

This function should return one tuple of numpy arrays (r2_train, r2_test). 
Both arrays should have shape (10,)
"""

np.random.seed(0)
n = 15
x = np.linspace(0,10,n) + np.random.randn(n)/5
y = np.sin(x)+x/6 + np.random.randn(n)/10

X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)

#train dataset
X_train_reshape = X_train.reshape(len(X_train), 1)
y_train_reshape = y_train.reshape(len(y_train), 1)

#test dataset
X_test_reshape = X_test.reshape(len(X_test), 1)
y_test_reshape = y_test.reshape(len(y_test), 1)

train_score_list = []
test_score_list = []


for degree in range(10):
    poly0 = PolynomialFeatures(degree=degree)
    X_train0 = poly0.fit_transform(X_train_reshape)
    y_train0 = poly0.fit_transform(y_train_reshape)
    X_test = poly0.fit_transform(X_test_reshape)
    y_test = poly0.fit_transform(y_test_reshape)
    regression0 = LinearRegression().fit(X_train0, y_train0)
    train_pred = regression0.predict(X_train0)
    train_score = r2_score(y_train0, train_pred)
    train_score_list.append(train_score)
    test_pred = regression0.predict(X_test)
    test_score = r2_score(y_test, test_pred)
    test_score_list.append(test_score)

r2_train = np.asarray(train_score_list)
r2_test = np.asarray(test_score_list)

final_tup = (r2_train, r2_test)

