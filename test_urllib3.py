# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:44:41 2018

@author: fangyucheng
"""

import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')