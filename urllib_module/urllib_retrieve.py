#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 12:46:00 2018

@author: fangyucheng
"""


import os
import urllib

url = 'https://i0.wp.com/cdnssl.ubergizmo.com/wp-content/uploads/2019/06/google-pixel-4-render-640x364.png?resize=640%2C364&ssl=1'

opener = urllib.request.build_opener()

urllib.request.install_opener(opener)

path = os.getcwd()

urllib.request.urlretrieve(url, path + '/test.jpg')
