#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 13:05:13 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import pandas as pd

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3],
                  index=['Store 1', 'Store 1', 'Store 2'])

new_df = df[df['Cost'] > 3]['Name']
new_df2 = df['Name'][df['Cost'] > 3]

df = df.set_index([df.index, 'Name'])

df.index.names = ['Location', 'Name']

df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'},
                         name=('Store 2', 'Kevyn')))

#how to merge two data frame with same column and index
#how to add new data to data frame


