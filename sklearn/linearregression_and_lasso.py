#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:11:54 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

"""
Training models on high degree polynomial features can result in overly complex models that overfit, 
so we often use regularized versions of the model to constrain model complexity, 
as we saw with Ridge and Lasso linear regression.

For this question, train two models: a non-regularized LinearRegression model (default parameters) 
and a regularized Lasso Regression model (with parameters  alpha=0.01, max_iter=10000) 
both on polynomial features of degree 12. Return the  R^2 score for both the LinearRegression 
and Lasso model's test sets.

This function should return one tuple (LinearRegression_R2_test_score, Lasso_R2_test_score)
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Lasso, LinearRegression
from sklearn.metrics.regression import r2_score

np.random.seed(0)
n = 15
x = np.linspace(0,10,n) + np.random.randn(n)/5
y = np.sin(x)+x/6 + np.random.randn(n)/10


X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)

#reshape dataset
X_train_reshape = X_train.reshape(len(X_train), 1)
y_train_reshape = y_train.reshape(len(y_train), 1)

X_test_reshape = X_test.reshape(len(X_test), 1)
y_test_reshape = y_test.reshape(len(y_test), 1)

#a non-regularized LinearRegression model
poly = PolynomialFeatures(degree=12)
X_train = poly.fit_transform(X_train_reshape)
X_test = poly.fit_transform(X_test_reshape)

linear = LinearRegression.fit(X_train, y_train)

