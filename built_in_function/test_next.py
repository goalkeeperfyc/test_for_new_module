#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:31:24 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

random = [5, 9, 'cat']

# converting list to iterator
randomIterator = iter(random)
print(randomIterator)

# Output: 5
print(next(randomIterator))

# Output: 9
print(next(randomIterator))

# Output: 'cat'
print(next(randomIterator))

# This will raise Error
# iterator is exhausted
print(next(randomIterator, "the iterator is over"))

# 
try:
    print(next(random))
except TypeError as error_mess:
    print("TypeError: " + str(error_mess))
    

# What is the purpose of next
# What is iter in Python