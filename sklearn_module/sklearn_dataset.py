#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:39:13 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

#import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


from sklearn.datasets import make_classification

X, y = make_classification()


cancer = load_breast_cancer()

def answer_one():
    data = cancer.data
    column_data = cancer.feature_names
    df_data = pd.DataFrame(data=data, index=range(0,569), columns=column_data)
    target = cancer.target
    df_target = pd.DataFrame(data=target, index=range(0,569), columns=["target"])
    df = pd.merge(df_data, df_target, how='inner', right_index=True, left_index=True)
    return df

df = answer_one()

target_series = df['target'].value_counts()

def answer_three():
    data = cancer.data
    column_data = cancer.feature_names
    X = pd.DataFrame(data=data, index=range(0,569), columns=column_data)
    target = cancer.target
    y = pd.Series(data=target, index=range(0,569))
    return X, y

X, y = answer_three()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

#means = df.mean()[:-1].values.reshape(1, -1)
#result = knn.predict(means)

test_result = knn.predict(X_test)

y_test = y_test.values.reshape(1, -1)
#test_result = test_result.values.reshape(1, -1)

#score = knn.score(y_test, test_result)

score = accuracy_score(y_test, test_result)