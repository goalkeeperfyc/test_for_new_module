# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:47:01 2018

@author: fangyucheng
"""

import logging

logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(name)-12s:%(filename)s %(funcName)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='/home/fangyucheng/python_code/test_for_new_module/test_log',
                    #filename='/users/fangyucheng/Documents/code/python_code/test_for_new_module/test_log',
                    filemode='a') 
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
