#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 12:46:00 2018

@author: fangyucheng
"""


import os
import urllib

url = 'https://d18ky98rnyall9.cloudfront.net/99DDF5ePEeaK1Q4gRyvE8A.processed/full/360p/index.mp4?Expires=1547078400&Signature=IiUK6ZcO6NUbnZHEFya54bwBET2010x4pELOml~83zY87h4ah31RGadtmzY7mZFHyfkQs8i8LxHT1f614L9Co4TeUm2QgSUJPO0onf4gPBmxY8fmBG0QHPv0mGWvcPf1gKfyLdD~FvRvKokh3m5JHJ5JgCoZSebrTmZ~30jf0q0_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'

opener = urllib.request.build_opener()

urllib.request.install_opener(opener)

path = os.getcwd()

urllib.request.urlretrieve(url, path + '/dataframe3.mp4')
