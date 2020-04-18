#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:03:41 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

print(times_tables() == [i*j for i in range(10) for j in range(10)])


"""
Here’s a harder question which brings a few things together.

Many organizations have user ids which are constrained in some way. Imagine you work at an internet service provider and the user ids are all two letters followed by two numbers (e.g. aa49). Your task at such an organization might be to hold a record on the billing activity for each possible user.

Write an initialization line as a single list comprehension which creates a list of all possible user ids. Assume the letters are all lower case.
"""




lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [a+b+str(c)+str(d) for a in list(lowercase) for b in list(lowercase) for c in list(digits) for d in list(digits)]
correct_answer == answer