# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:00:38 2018

@author: fangyucheng
"""

import urllib

url = 'http://www.baidu.com'
get_page = urllib.request.urlopen(url)
page = get_page.read()

