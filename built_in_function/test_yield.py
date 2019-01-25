# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 09:17:31 2018

@author: fangyucheng
"""



def test1(num):
    for line in  range(1,5):
        m = num*line
        print (str(num))
        yield m
        
mmm = test1(4)
for ccc in mmm:
    print('this is %s' % ccc)