# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:38:48 2018

@author: fangyucheng
"""

import os
import time
from multiprocessing import Pool
import test_for_new_module



class Test_Pool():
    
    def __init__(self):
        self.loggerii = test_for_new_module.logging.getLogger('test_purpose')
#        logging.basicConfig(level=logging.DEBUG,  
#                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
#                            datefmt='%Y-%m-%d %H:%M:%S',
#                            filename='/home/fangyucheng/python_code/test_for_new_module/test_log',
#                            #filename='/users/fangyucheng/Documents/code/python_code/test_for_new_module/test_log',
#                            filemode='a') 
#        console = logging.StreamHandler()
#        console.setLevel(logging.DEBUG)
#        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
#        console.setFormatter(formatter)
#        logging.getLogger('').addHandler(console)

    def func1(self, a, b=5):
        pid = os.getpid()
        c = a + b
        self.loggerii.info('this is process %s with %s' % (pid, c))
        time.sleep(5)
        self.loggerii.logging.info('this is process %s' % pid)
        
    def func2(self, c, d):
        pid = os.getpid()
        self.loggerii.logging.info('this is process %s, with input number %s %s' % (pid, c, d))

if __name__ == '__main__':
    test = Test_Pool()
    pool = Pool(5)
    for num in range(5):
        pool.apply_async(func=test.func1, args=(num,))
    pool.close()
    pool.join()