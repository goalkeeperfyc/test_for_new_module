# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:38:48 2018

@author: fangyucheng
"""

import os

class Test_Pool():
    
    def func1(self, a, b=5):
        pid = os.getpid()
        c = a + b
        print(c)
        print("this is process %s" % pid)
        
    def func2(self):
        pass