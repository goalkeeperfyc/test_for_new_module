# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:27:27 2018

@author: fangyucheng
"""

import configparser

config = configparser.RawConfigParser()
config.sections()
config.read('D:/python_code/crawler/crawler_sys/framework/config/list_page_urls.ini', encoding='utf-8')

value_lst = []

for key, value in config['iqiyi'].items():
    value_lst.append(value)