#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 14:07:06 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import pandas as pd

df = pd.DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], columns=["State", "RegionName"]  )

df2 = df[["RegionName", "State"]]