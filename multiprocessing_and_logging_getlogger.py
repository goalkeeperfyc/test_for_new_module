# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:38:48 2018

@author: fangyucheng
"""

import os
import time
import datetime
import logging
from multiprocessing import Pool

class Test_Pool():
    
    def __init__(self):
        """
        logging.basicConfig(level=logging.DEBUG,  
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                            datefmt='%Y-%m-%d %H:%M:%S',  
                            filename='/users/fangyucheng/Documents/code//python_code/test_for_new_module/test_log',  
                            filemode='a') 
        logging.getLogger()        
        sh = logging.StreamHandler() 
        """
        logger = logging.getLogger()
        fh = logging.FileHandler('/users/fangyucheng/Documents/code/python_code/test_for_new_module/test_log2',encoding='utf-8')
        sh = logging.StreamHandler()                     
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s [line:%(lineno)d] : %(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter2)
        logger.addHandler(fh)
        logger.addHandler(sh)

    
    
    def func1(self, a, b=5):
        pid = os.getpid()
        c = a + b
        print(c)
        logging.info('this is process %s with %s' % (pid, c))
        time.sleep(5)
        print("this is process %s" % pid)
        logging.info('this is process %s' % pid)
        
    def func2(self, c, d):
        pid = os.getpid()
        logging.info('this is process %s, with input number %s %s' % (pid, c, d))

if __name__ == '__main__':
    test = Test_Pool()
    pool = Pool(5)
    for num in range(5):
        pool.apply_async(func=test.func1, args=(num,))
    pool.close()
    pool.join()