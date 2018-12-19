# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:38:48 2018

@author: fangyucheng
"""

import os
import time
import logging
from multiprocessing import Pool

class Test_Pool():
    
    def func1(self, a, b=5):
        pid = os.getpid()
        c = a + b
        print(c)
        time.sleep(5)
        print("this is process %s" % pid)
        
    def func2(self):
        pass