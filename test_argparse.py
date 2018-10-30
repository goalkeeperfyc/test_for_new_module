# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:23:37 2018

@author: fangyucheng
"""


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")