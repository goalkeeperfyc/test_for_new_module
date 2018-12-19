# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:29:47 2018

output different level message to different file

@author: fangyucheng
"""

import logging

class MultiFileHandler(logging.FileHandler):

    def __init__(self, filename, mode='a', encoding='utf-8', delay=0):
        