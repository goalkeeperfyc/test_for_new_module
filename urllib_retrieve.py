#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 12:46:00 2018

@author: fangyucheng
"""

import urllib

url = 'http://courses.csail.mit.edu/18.337/2015/docs/50YearsDataScience.pdf'

opener = urllib.request.build_opener()

urllib.request.install_opener(opener)

urllib.request.urlretrieve(url, '50YearsDataScience.pdf')