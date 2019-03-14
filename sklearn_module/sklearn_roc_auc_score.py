#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:01:41 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import numpy as np
from sklearn.metrics import roc_auc_score

y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
print("test1 score: ", roc_auc_score(y_true, y_scores))

y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.3, 0.8])
print("test2 score: ", roc_auc_score(y_true, y_scores))

y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.55, 0.8])
print("test3 score: ", roc_auc_score(y_true, y_scores))

y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.7, 0.8])
print("test4 score: ", roc_auc_score(y_true, y_scores))

y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.4, 0.8])
print("test5 score: ", roc_auc_score(y_true, y_scores))