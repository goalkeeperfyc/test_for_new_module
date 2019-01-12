#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:19:24 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import pandas as pd

energy = pd.read_excel('Energy Indicators.xls', skiprows=17)
del energy['Unnamed: 0']
del energy['Unnamed: 1']
rename_dict = {'Unnamed: 2': 'Country',
               'Petajoules': 'Energy Supply',
               'Gigajoules': 'Energy Supply per Capita',
               '%': '% Renewable'}
energy = energy.rename(columns=rename_dict)

energy = energy[:227]

energy.set_value('Country', "Republic of Korea"， "South Korea")