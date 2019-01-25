#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 14:30:22 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

X = [[0.44, 0.68], [0.99, 0.23]]
vector = [109.85, 155.72]
predict= [0.49, 0.18]

poly = PolynomialFeatures(degree=2)
X_ = poly.fit_transform(X)
#predict_ = poly.fit_transform(predict)
#
#clf = linear_model.LinearRegression()
#clf.fit(X_, vector)
#print (clf.predict(predict_))