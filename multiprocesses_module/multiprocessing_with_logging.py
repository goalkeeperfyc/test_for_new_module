# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:38:48 2018

@author: fangyucheng
"""

import os
import time
import logging
from multiprocessing import Pool


class TestPool():
    
    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)4s: %(filename)s %(funcName)s %(levelname)8s: %(message)s',
                            handlers=[logging.FileHandler("test.log", "a"), logging.StreamHandler()])

    def func1(self, a, b=5):
        pid = os.getpid()
        c = a + b
        # print(c)
        logging.info('this is process %s with %s' % (pid, c))
        time.sleep(5)
        # print("this is process %s" % pid)
        logging.info('this is process %s' % pid)
        
    def func2(self, c, d):
        pid = os.getpid()
        logging.info('this is process %s, with input number %s %s' % (pid, c, d))


if __name__ == '__main__':
    test = TestPool()
    test.func1(a=5)
    pool = Pool(5)
    for num in range(5):
        pool.apply_async(func=test.func1, args=(num,))
        pool.apply_async(func=test.func2, args=(num, num))
    pool.close()
    pool.join()